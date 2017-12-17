
# coding: utf-8

# In[11]:


def genderclf(*args, model='genderclf.pkl', vec='gendervec.pkl'):
    '''Takes an array of names and determines gender.
    Format for names should be ['Matt'] or ['Matt','Elizabeth','etc.']
    Model name and vectorizer will default to included model unless
    otherwise specified.
    '''
    import pickle
    import numpy as np
    from sklearn.externals import joblib
    loaded_model = joblib.load(model)
    loaded_vec = joblib.load(vec)
    for x in args:
        name_vec = loaded_vec.transform(x)
        prediction = loaded_model.predict(name_vec)
    return np.concatenate((np.array(x)[:, np.newaxis], np.array(prediction).T[:, np.newaxis]), axis=1)

def updatedmodel(begindate=1960, enddate=2016, modelname='newmodel'):
    '''Takes a beginning and end date and creates new pickled models and
    vectorizers.  If no input is given this will create a model similar
    to the included model with a name of newmodel'''
    
    from zipfile import ZipFile
    import requests
    import pandas as pd
    import glob
    import os
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn import metrics
    import numpy as np
    import string
    import pickle
    from sklearn.externals import joblib
    
    #Runs error checking to make sure that dates are appropriate
    if begindate < 1880:
        raise ValueError('Begindate must be between 1880 & 2016')
    elif enddate > 2016:
        raise ValueError('Enddate must be between 1880 & 2016')
    elif begindate > enddate:
        raise ValueError('Begindate must be before enddate')
    
    #Downloads the files from the SSA
    print('Downloading files')
    url = 'https://www.ssa.gov/oact/babynames/names.zip'
    r = requests.get(url)
    open('names.zip', 'wb').write(r.content)
    with ZipFile('names.zip', 'r') as zip_ref:
        zip_ref.extractall('Names')
    
    #Creates a glob of all the files from the census database
    globbed_files = glob.glob('./Names/*.txt')
    
    #Creates data to hold the list of files
    data = [] 

    #Reads each file in the glob and appeads it to the dataframe
    for txt in globbed_files:
        frame = pd.read_table(txt, delimiter=',', header=None)
        #Adds the file name to the dataframe
        frame['filename'] = os.path.basename(txt)
        data.append(frame)

    #Don't want pandas to try an align row indexes    
    allfiles = pd.concat(data, ignore_index=True)
    
    #Updates the names 
    allfiles.columns = ['Name', 'Gender', 'Count', 'Source']
    
    #Cleaning up the Source column
    allfiles['Source'] = allfiles['Source'].str.replace('yob', '')
    allfiles['Source'] = allfiles['Source'].str.replace('.txt', '')
    
    #Changing the source to a number value
    allfiles['Source'] = pd.to_numeric(allfiles['Source'], errors='coerce')
    
    print('Preparing to update the model, this may take several minutes')
    
    #Stores a subset of the model
    updatedmodel = allfiles[(allfiles['Source']>=begindate) & (allfiles['Source']<=enddate)]
    del updatedmodel['Source']
    
    #changes all the F to 0 and M to 1
    updatedmodel['Gender'] = updatedmodel['Gender'].replace(['F', 'M'], [0, 1])
    
    #Sets the gender column to Y for modeling
    y = updatedmodel['Gender']
    
    #Drops the target column from the dataframe
    updatedmodel.drop('Gender', axis=1)
    
    #Creates a train test split of the data frame
    X_train, X_test, y_train, y_test = train_test_split(updatedmodel['Name'], y, test_size=0.2, random_state=42)
    
    #Does a split of the count column so that it can be used in the 
    #sample weight
    X_train_weight, X_test_weight, y_train_weight, y_test_weight = train_test_split(updatedmodel['Count'], y, test_size=0.2, random_state=42)

    #Instaniates the count vectorize to create a character bi grame
    count_vectorizer = CountVectorizer(analyzer='char', ngram_range=(2,2))
    #Fits the vectorizer to the X train data set
    count_train = count_vectorizer.fit_transform(X_train)
    #Vectorizers the X test data set
    count_test = count_vectorizer.transform(X_test)
    
    #Instantiates the Random Forect Classifer
    clf = RandomForestClassifier()
    
    #Fits the data to the model and prints up a prediction
    clf.fit(count_train, y_train, sample_weight=X_train_weight)
    pred = clf.predict(count_test)
    score = metrics.accuracy_score(y_test, pred)
    print('accuracy: %0.3f' % score)
    
    #pickles the model and vectorizer
    joblib.dump(clf, modelname+'.pkl')
    joblib.dump(count_vectorizer, modelname+'vec.pkl')
    
    
    #Outputs the name of the model and vectorizer
    print('New model name is ' + modelname +'.pkl')
    print('New vectorizer name is ' + modelname +'vec.pkl')
    
    return
    

