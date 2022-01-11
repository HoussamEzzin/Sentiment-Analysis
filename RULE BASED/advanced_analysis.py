'''
a_file = open("sample.txt", "r")
get list of lines
lines = a_file.readlines()
a_file.close()
new_file = open("sample.txt", "w")
for line in lines:
    if line.strip("\n") != "line2":
Delete "line2" from new_file

        new_file.write(line)
new_file.close()
'''
import pandas as pd

dataset = pd.read_excel('dataset/tweets_vectors.xlsx')
dataset.dropna(subset=["tweet"],inplace=True)
tweets = dataset['tweet'].values.tolist()
polarity_list = dataset['emotion'].values.tolist()


high_pos = open('sentiment_files/tiers/high_pos.txt',"r")
lines = high_pos.readlines()
high_pos.close()
high_pos1 = open('sentiment_files/tiers/high_pos1.txt','w')

for i in range(len(tweets)):
    print("Tweet number  : "+str(i))
    if polarity_list[i] == 'NE':
        tweet = tweets[i].split(' ')
        
        for word in tweet:
            for line in lines:
                line = line.strip("\n")
                if line != word:
                    high_pos1.write(line+"\n")

high_pos1.close()
