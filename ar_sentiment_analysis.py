from re import M
from numpy import mod
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


tweets = pd.read_excel('TESTFINAL.xlsx')

print(tweets.head())


x=tweets['tweet']
y=tweets['emotion']
print(x.size)
x, x_test, y , y_test = train_test_split(x,y,stratify=y,test_size=0.25,random_state=42)


vec = CountVectorizer()
x = vec.fit_transform(x).toarray()
x_test = vec.transform(x_test).toarray()

model = MultinomialNB()
model.fit(x,y)


precision = model.score(x_test,y_test)
print("PRECISION :",precision*100," %")