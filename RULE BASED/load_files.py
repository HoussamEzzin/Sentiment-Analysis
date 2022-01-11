import re




pos_ar_file = open('sentiment_files/ar-positive-words.txt','r',encoding='utf-8')
pos_ar_tokens = []
for line in pos_ar_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    pos_ar_tokens.append(line.strip())



neg_ar_file = open('sentiment_files/ar-negative-words.txt','r',encoding='utf-8')
neg_ar_tokens = []
for line in neg_ar_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    neg_ar_tokens.append(line.strip())
    

tokens = []


def get_positives_ar():
    return pos_ar_tokens
    
def get_negatives_ar():
    return neg_ar_tokens
    