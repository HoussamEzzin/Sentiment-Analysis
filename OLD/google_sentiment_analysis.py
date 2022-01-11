from numpy import mod
import pandas as pd
from sklearn.model_selection import train_test_split
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

data = pd.read_csv('google_train.csv')

#show what's the data looks like
print(data.head())

def preprocess_data(data):
    
    data = data.drop('package_name', axis=1)
    
    data['review'] = data['review'].str.strip().str.lower()
    return data

data = preprocess_data(data)

# split data into training and testing data

x = data['review']
y = data['polarity']
x , x_test, y, y_test = train_test_split(x, y, stratify=y, test_size=0.25,random_state=42)
# train_test_split split arrays into random train and test subsets
# test_size represent the proportion of data to include in test
# random_state controls the shuffling applied to data

#now e need to vectorize text reviews to numbers:
vec = CountVectorizer(stop_words='english')
x = vec.fit_transform(x).toarray()
x_test = vec.transform(x_test).toarray()

model = MultinomialNB()
model.fit(x,y)

print(model.score(x_test,y_test))
