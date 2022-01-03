
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


tweets = pd.read_excel('final.xlsx')

print(tweets.head())


x=tweets.drop('emotion',axis=1)
y=tweets['emotion']
count = 0
for array in x.values:
    try:
        line = ' '.join(array)
        count +=1
    except TypeError:
        print('error')
        
        print('tweet : ', array)


print(count)