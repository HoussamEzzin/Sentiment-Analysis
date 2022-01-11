
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB


tweets = pd.read_excel('SAFAR_TWEETS_VECTORS.xlsx')

print(tweets.head())


x=tweets['tweet']
y=tweets['emotion']
# tweets.dropna(subset = ["tweet"], inplace=True)
# print(x.size)
x, x_test, y , y_test = train_test_split(x,y,stratify=y,test_size=0.3,random_state=50)


vec = CountVectorizer()

x = vec.fit_transform(x.astype('U')).toarray()

    
x_test = vec.transform(x_test.astype('U')).toarray()

model = MultinomialNB()
model.fit(x,y)


precision = model.score(x_test,y_test)
print("PRECISION :",precision*100," %")