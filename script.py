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
    output_tweets_file = open("output_tweets.txt",'a')



    tweets = []
   

    with open("Tweets.txt") as tweets_file:
        max = 0
        lines =[]
       
        for line in tweets_file:
            words = line.split()
            tweet_line = []
    
            comment = []
            for word in words:
                comment.append(word)
            lines.append(comment)
           
            # for i in range(len(line)-1):
            #     tweet_line.append(line[i])
                
            # for i in range(len(words)-1):
            #     if(len(words[i]) < len(words[i+1])):
            #         max = len(words[i+1])
            
            
            # str_to_write += line[len(line)-1] +"\n"
            # output_tweets_file.write(str_to_write)  
            # tweets.append(tweet_line)
        
        for i in range(len(lines)-1):
            if(len(lines[i])< len(lines[i+1])):
                max = len(lines[i+1])
        
        for i in range(max):
            output_tweets_file.write("comment"+i+"gg")
            
            for comment_array in lines:
                word_to_write = ''
                if comment_array[i] is None:
                    word_to_write = 'none'
                else:
                    word_to_write = comment_array[i]
                output_tweets_file.write(word_to_write+"gg")
            output_tweets_file.write("/n")
        
        
            

    output_tweets_file.close()
    
    # plt.plot([1,2,3,4])
    # plt.ylabel('some numbers')
    # plt.show()
    
    df = pd.read_csv("output_tweets.txt", sep="gg", encoding='windows-1256')
    
    print(df.head())
    
    # the comment column hopefully will be stored in the x variable
    # except fot the emotion column which will be stored in y
    # x = df['comment'].values
    # x = LabelEncoder().fit_transform(x)
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


