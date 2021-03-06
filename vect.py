'''importing the libraries'''
%matplotlib inline
import numpy as np
import pandas as pd
import os
import sklearn
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier

#sample text to be studied
phrases = ["The quick brown fox jumped over the lazy dog",
           "education is what you have left over after forgetting everything ever learnt"]
           
           
#implementation of the bag of words model
vect = CountVectorizer()
vect.fit(phrases)

print("vocabulary size: {}".format(len(vect.vocabulary_)))
print("vocabulary content:\n {}".format(vect.vocabulary_))

bag_of_words = vect.transform(phrases)

print(bag_of_words)


print("bag_of_words as an array:\n {}".format(bag_of_words.toarray()))


#list of all the unique words with their indices from bag_of_words
vect.get_feature_names()

