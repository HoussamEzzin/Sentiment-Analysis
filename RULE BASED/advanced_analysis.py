
import pandas as pd
import re

dataset = pd.read_excel('dataset/tweets_vectors.xlsx')
dataset.dropna(subset=["tweet"],inplace=True)
tweets = dataset['tweet'].values.tolist()
polarity_list = dataset['emotion'].values.tolist()


high_neg = open('sentiment_files/tiers/high_neg.txt',"r")

lines_tokens = []
for line in high_neg:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    lines_tokens.append(line.strip())
high_neg.close()

progress =0

dirty_words = []
for i in range(len(tweets)):
    progress += 1
    print("Progress : "+str((progress*100)/len(tweets))+"%")

    if polarity_list[i] == 'NE':
        tweet = tweets[i].split(' ')
        for word in tweet:
            if word in lines_tokens:
                dirty_words.append(word)

high_neg1 = open('sentiment_files/tiers/high_neg1.txt','w')
for l in lines_tokens:
    if l not in dirty_words:
        high_neg1.write(l+"\n")
high_neg1.close()
