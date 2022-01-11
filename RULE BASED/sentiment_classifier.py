'''
each word in this dictionnary is either positive or negative
the goal is to classify this words per tiers ;
1: low
2: medium
3 : high
'''


import pandas as pd

high_pos = open('sentiment_files/tiers/high_pos.txt', 'a', encoding="windows-1256")
medium_pos = open('sentiment_files/tiers/medium_pos.txt', 'a', encoding="windows-1256")
low_pos = open('sentiment_files/tiers/low_pos.txt', 'a', encoding="windows-1256")
high_neg = open('sentiment_files/tiers/high_neg.txt', 'a', encoding="windows-1256")
medium_neg = open('sentiment_files/tiers/medium_neg.txt', 'a', encoding="windows-1256")
low_neg = open('sentiment_files/tiers/low_neg.txt', 'a', encoding="windows-1256")

dataset = pd.read_excel('sentiment_files/dict.xlsx')

dataset.dropna(subset=["word"],inplace=True)

words = dataset['word'].values.tolist()
score = dataset['score'].values.tolist()

for i in range(len(words)):
    if score[i] == 1:
        low_pos.write(words[i]+"\n")
    elif score[i] == 2:
        medium_pos.write(words[i]+"\n")
    elif score[i] == 3:
        high_pos.write(words[i]+"\n")
    elif score[i] == -1:
        low_neg.write(words[i]+"\n")
    elif score[i] == -2:
        medium_neg.write(words[i]+"\n")
    elif score[i] == -3:
        high_neg.write(words[i]+"\n")
    