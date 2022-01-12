import pandas as pd


dataset = pd.read_excel('dataset/tweets_vectors.xlsx')

'''
Call df.dropna(subset, inplace=True) with inplace set to True 
and subset set to a list of column names 
to drop all rows that contain NaN under those columns. 

'''

import re

dataset.dropna(subset=["tweet"],inplace=True)

tweets = dataset['tweet'].values.tolist()
polarity_list = dataset['emotion'].values.tolist()

pos_file = open('pos_tokens.txt','r')
neg_file= open('neg_tokens.txt','r')
neutral_file = open('neutralComments.txt','r')

low_pos3 = open('sentiment_files/tiers/low_pos3.txt','a')
low_neg3 = open('sentiment_files/tiers/low_neg3.txt','a')

neutral_tokens = []
for line in neutral_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    neutral_tokens.append(line.strip())
    
pos_tokens = []
for line in pos_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    pos_tokens.append(line.strip())

neg_tokens = []
for line in neg_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    neg_tokens.append(line.strip())

for pos_word in pos_tokens:
    if pos_word not in neutral_tokens and pos_word not in neg_tokens:
        low_pos3.write(pos_word+"\n")
        
        
for neg_word in neg_tokens:
    if neg_word not in neutral_tokens and neg_word not in pos_tokens:
        low_neg3.write(neg_word+"\n")
