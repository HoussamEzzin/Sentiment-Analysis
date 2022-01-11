import pandas as pd

dataset = pd.read_excel('dataset/tweets_vectors.xlsx')


new_pos = open('pos.txt','a',encoding="windows-1256")
new_neg = open('neg.txt','a',encoding="windows-1256")


dataset.dropna(subset=["tweet"],inplace=True)

tweets = dataset['tweet'].values.tolist()
polarity_list = dataset['emotion'].values.tolist()

for i in range(len(tweets)):
    tokens = tweets[i].split(' ')
    if polarity_list[i] == 'PO':
        for j in range(len(tokens)):
            if tokens[j] != '':
                new_pos.write(tokens[j]+"\n")
    elif polarity_list[i] == 'NG':
        for j in range(len(tokens)):
            if tokens[j] != '':
                new_neg.write(tokens[j]+"\n")
    

print('donec')