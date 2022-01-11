'''
*** input ***
- Dataset : vector of tweets already processed with their polarity
- Sentiment Files : positive and negative words classified by their points, plus a file which contain negation words

*** process ***
- Calculate the score of each tweet and determine if it's positive , neutral or negative.
- Compare our results with the datatset and determine the precision

'''

from re import sub
from numpy import NaN
from load_files import get_negatives_ar, get_positives_ar
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
    score = 0
    progress +=1
    print("Progress : "+str((progress*100)/dataset_size)+"%")
    for word in tweets[i]:
        if word in get_positives_ar():
            score += 1
        elif word in get_negatives_ar():
            score -= 1
        
    if score > 0 and polarity_list[i] == "PO":
       
        count += 1
    elif score < 0 and polarity_list[i] == "NG":
       
        count += 1
    elif score == 0 and polarity_list[i] == "NE":
        
        count += 1
    
print("PRECISION :", (count/dataset_size)*100)
  
        
    