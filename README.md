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

The model is trained using a list of names from the Social Security Administration (SSA).  This data exists going back to 1880 and is publicly available at the following link (https://www.ssa.gov/oact/babynames/limits.html).  Due to more recent shifts in the usage of names (i.e. in 1900 Leslie was prodominantly a male name, now it is prodominantly a female name), the default model was trained using data from 1960 to 2016.   A variety of models were experimented with on with different features and combinations of features including:

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

## Using the Package

## Version

## Author

