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

* The Gender Classifier Package (Gender_Classifier.py)
* The Gender Model Creator Package (Gender_Model_Refresh.py)

### Gender Classifier

This is the main package and is used for inputting names and generating a list of genders.  The package takes up to three inputs:

* An array of names
* A model name
* A vector model name

The final output will be an array with the name and gender classification for that name, either a 0 (Female) or 1 (Male).

The array of names takes names in the following format:

Single - ['Matt']
Multiple Names - ['Elizabeth', 'Barbara'] (There is no limit on lenght)

## Version

## Author

