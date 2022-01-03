from os import write
import nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core import frame
from scipy.sparse import csc

from sklearn.linear_model import Perceptron,LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn import datasets
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from datasets import load_dataset
import csv


# nltk.download('punkt')


# we have 3 classes :
# P : for positive comments
# N : Negative ones
# NE : Neutral

# corpus = load_dataset("ar_res_reviews") #first test








# corpus = load_dataset("ajgt_twitter_ar") #second test


def main():
    # output_tweets_file = open("output_tweets.txt",'a')


   
    tweets = pd.read_excel("final.xlsx")

    # print(tweets.head())
    # print("*******")

    X = tweets.drop('emotion', axis=1)
   

    y = tweets['emotion']

    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20)
    svclassifier = SVC(kernel='linear')
    svclassifier.fit(X_train, y_train)
    y_pred = svclassifier.predict(X_test)
    print(y_pred)



    # the comment column hopefully will be stored in the x variable
    # except fot the emotion column which will be stored in y


    # y = df['emotion']
    # # x = df.drop('emotion', axis=1)





    # x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.20)

    # svcclassifier = SVC(kernel='linear')
    # svcclassifier.fit(x_train, y_train)
    # y_pred = svcclassifier.predict(x_test)
    # print(confusion_matrix(y_test,y_pred))
    # print(classification_report(y_test,y_pred))

    print("done")

    # for tweet in tweets:
    #     print("Emotion :", tweet)
    #testing *******************
    # print(neg_eng_tokens)

    # ***********************


#     precision = 0
#     pts = 0
#    #for in range(len(corpus['train']))
#     for i in range(len(corpus['train'])):
#         score = 0
#         polarity = 2 #neutral
#         words = corpus['train'][i]['text'].split(' ')
#         success = False # just for testing
#         for word in words:
#             if word in pos_eng_tokens or word in pos_ar_tokens and word not in ['',' ']:
#                 score += 1

#             elif word in neg_eng_tokens or word in neg_ar_tokens and word not in ['',' ']:
#                 score -= 1


#         if score < 0:
#             polarity = 0
#         elif score == 0:
#             polarity = 2
#         else:
#             polarity = 1

#         if polarity == corpus['train'][i]['polarity']:
#             pts += 1
#             success = True

#         progress = (i/len(corpus['train'])) *100
#         print('Progress : ', progress, '% || SCORE OF  COMMENT n',i,' : ',score,' ||  Success : ',success, '|| USER id :', corpus['train'][i]['user_id'])



    # precision = (pts/len(corpus['train'])) * 100
    # print('Precision is :', precision, '%')




if __name__ == '__main__':

    main()


