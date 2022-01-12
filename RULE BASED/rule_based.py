'''
*** input ***
- Dataset : vector of tweets already processed with their polarity
- Sentiment Files : positive and negative words classified by their points, plus a file which contain negation words

*** process ***
- Calculate the score of each tweet and determine if it's positive , neutral or negative.
- Compare our results with the datatset and determine the precision

'''

from load_files import *
import pandas as pd
from sentiment_analyzer import *

dataset = pd.read_excel('dataset/tweets_vectors.xlsx')

'''
Call df.dropna(subset, inplace=True) with inplace set to True 
and subset set to a list of column names 
to drop all rows that contain NaN under those columns. 

'''



dataset.dropna(subset=["tweet"],inplace=True)

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
    tokens = tweets[i].split(' ')
    score = analyze(tokens)
    count += update_count(score,polarity_list[i])

        

print("PRECISION :", (count/dataset_size)*100)
  
        
# 77.42
# 77.49
# 85.06