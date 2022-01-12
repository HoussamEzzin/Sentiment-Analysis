
import pandas as pd
import re

dataset = pd.read_excel('dataset/tweets_vectors.xlsx')
dataset.dropna(subset=["tweet"],inplace=True)
tweets = dataset['tweet'].values.tolist()
polarity_list = dataset['emotion'].values.tolist()


high_pos2 = open('sentiment_files/tiers/high_pos2.txt',"r")

lines_tokens = []
for line in high_pos2:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    lines_tokens.append(line.strip())
high_pos2.close()

progress =0

dirty_words = []
for i in range(len(tweets)):
    progress += 1
    print("Progress : "+str((progress*100)/len(tweets))+"%")

    if polarity_list[i] == 'NE':
        tweet = tweets[i].split(' ')
        for word in tweet:
            if word in lines_tokens:
                print("****************************************")
                dirty_words.append(word)

high_pos3 = open('sentiment_files/tiers/high_pos3.txt','w')
for l in lines_tokens:
    if l not in dirty_words:
        high_pos3.write(l+"\n")
high_pos3.close()
