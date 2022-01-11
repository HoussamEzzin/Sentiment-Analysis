'''
*** input ***
- Dataset : vector of tweets already processed with their polarity
- Sentiment Files : positive and negative words classified by their points, plus a file which contain negation words

*** process ***
- Calculate the score of each tweet and determine if it's positive , neutral or negative.
- Compare our results with the datatset and determine the precision

'''

from re import sub

from load_files import *
import pandas as pd


dataset = pd.read_excel('dataset/tweets_vectors.xlsx')

'''
Call df.dropna(subset, inplace=True) with inplace set to True 
and subset set to a list of column names 
to drop all rows that contain NaN under those columns. 

'''

print('old : '+str(dataset.size))

dataset.dropna(subset=["tweet"],inplace=True)
print('old : '+str(dataset.size))
tweets = dataset['tweet'].values.tolist()
polarity_list = dataset['emotion'].values.tolist()

dataset_size = len(tweets)
count = 0
progress = 0
for i in range(dataset_size):
    found = False
    score = 0
    progress +=1
    print("Tweet number  : "+str(i))
    negation = False
    tokens = tweets[i].split(' ')
    for j in range(len(tokens)):
     
        if tokens[j] in get_high_pos():
            score +=3
        elif tokens[j] in get_medium_pos():
            score += 2
        elif tokens[j] in get_low_pos():
            score += 1
        
        elif tokens[j] in get_high_neg():
            score -=3
        elif tokens[j] in get_medium_neg():
            score -= 2
        elif tokens[j] in get_low_neg():
            score -= 1
        
       
    

    # print('SCORE : '+str(score))
       
        
    if score > 0 and polarity_list[i] == "PO":
        found = True
        count += 1
    elif score < 0 and polarity_list[i] == "NG":
        found = True
        count += 1
    elif score ==0 and  polarity_list[i] == "NE":
        found =True
        count += 1
    
    if found == False:
        print("wrong in number : "+str(i))
        
    
print("PRECISION :", (count/dataset_size)*100)
  
        
    