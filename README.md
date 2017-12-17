# GenderClassifier

This package is designed to take in an array of names and produce a gender represented by either a 0 (Female) or 1 (Male).  

## Package Prerequisites

The following is a list of all packages necessary to utilize this package

* sklearn
* numpy
* pickle

The following is a list of all packages necessary to create a new model

* zipfile
* requests
* pandas
* glob
* os
* sklearn
* numpy
* string
* pickle

## Getting Started

To get started you will need to download Gender_Classifier.py and GenderClfModelAndVec.zip to whatever folder you will be working from.  You will then need to unzip the GenderClfModelAndVec.zip into that same folder. 

Navigate your python installation to the file location

Import the Gender Classifier using the following code:

```
from Gender_Classifier import genderclf
```

Then you can imput names into the classifier as so:

```
genderclf(['Alexander'])
```

Which will return an array, where Alexander was classified as "1", indicating a male name.

```
array([['Alexander', '1']],
      dtype='<U21')
```

You can also submit multiple names at one time:

```
genderclf(['Alexander', 'Alexandria'])
```

Here Alexander was classified as male (1) and Alexandria was classified as a female (0)

```
array([['Alexander', '1'],
       ['Alexandria', '0']],
      dtype='<U21')
```

## Explanation of Model

The model is trained using a list of birth names from the Social Security Administration (SSA).  This data exists going back to 1880 and is publicly available at the following link (https://www.ssa.gov/oact/babynames/limits.html).  Due to more recent shifts in the usage of names (i.e. in 1900 Leslie was prodominantly a male name, now it is prodominantly a female name), the default model was trained using data from 1960 to 2016.   A variety of models were experimented with on with different features and combinations of features including:

* Word vectorization
* Word vectorization using first 3 characters
* Word vectorization using last 3 characters
* Final letter of name
* Ratio of individual letters compared to name length
* Count of letters
* Unigram character vectorization
* Bigram character vectorization
* Trigram character vectorization

Additionally a variety of Sci Kit Learn's classification techniques were used, including:

* MultinomialNB
* BernoulliNB
* SGDClassifier
* Perceptron
* GaussianProcessClassifier
* GaussianNB
* LinearSVC
* RandomForestClassifier
* SVM

Ultimately the final model used Bigram Character Vectorization and a Random Forest Classifier.  This combination had a good balance of time to create when building new models, as well as generalizing well to unseen names.  

### Notes about the model and dataset

The model was built using lists of names in the US.  Although the US is very representative of many nations and cultures some names may have unique combinations of characters that are representative of different genders and be classified incorrectly.  Additionally, the SSA dataset removes any cases where there were less than 5 names in a given year.  Finally, the model is likely to classify names based on the prodominant representation in the population. 

## Using the Package

This package has two main pieces:

* The Gender Classifier function (genderclf)
* The Gender Model Creator function (updatemodel)

The models can be called using the following lines of code: 

```
from Gender_Classifier import genderclf
```

```
from Gender_Classifier import updatemodel
```

### Gender Classifier

```
genderclf(*args, model='genderclf.pkl', vec='gendervec.pkl')
```

This is the main package and is used for inputting names and generating a list of genders.  The package takes up to three inputs:  

* An array of names
* A model name
* A vector model name

The final output will be an array with the name and gender classification for that name, either a 0 (Female) or 1 (Male).

The array of names takes names in the following format:

Single - ['Matt']

Multiple Names - ['Elizabeth', 'Barbara'] (There is no limit on length)

The model name and vector model names are option variables.  If left blank the model will default to the pickled models named genderclf.pkl and gendervec.pkl. These models are trained on data from 1960 - 2016 and have an approximate 90% accuracy on that data set.  If you create a new model using the Gender_Model_Refresh package new names will be provided that can be used for the model and vectorization.

### Gender Model Creator

```
updatedmodel(begindate=1960, enddate=2016, modelname='newmodel')
```

This package is used to create a new model using specfic year ranges.  This package takes up to three inputs 

* A begin year
* An end year
* A new model name

** Please notes that all values have a default and if this is run without setting values a model will be created using dates from 1960 - 2016.  This will be the same model as the default model that comes with the package.
** Also this package will download files and create a new model which will take up approximately 100mb of space

Begindate must be between 1880-2015 and Enddate must be between 1881-2016.  The Begindate must also be before the Enddate.

Once started the model will do the following:

* Download and unzip the SSA names files from the SSA
* Remove unused years from the training process
* Build a Bigram character vectorizer based on the data set
* Train the model
* Produce an accuracy rating based on the trained dataset
* Pickle the vectorizer and model
* Provide file names for vectorizer and model for use in the classifier

** Please note that based on your internet connection, processing speed, the number of years selected this process can take between 5-30 minutes to complete.  

## Version

0.1 - 12/17/2017

## Author

Matthew Weirath

