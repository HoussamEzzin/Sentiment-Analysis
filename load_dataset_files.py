import re


pos_eng_file = open('dataset/positive-words.txt','r')
pos_eng_tokens = []
for line in pos_eng_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    pos_eng_tokens.append(line.strip())

pos_ar_file = open('dataset/ar-positive-words.txt','r',encoding='utf-8')
pos_ar_tokens = []
for line in pos_ar_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    pos_ar_tokens.append(line.strip())

neg_eng_file = open('dataset/negative-words.txt','r')
neg_eng_tokens = []
for line in neg_eng_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    neg_eng_tokens.append(line.strip())

neg_ar_file = open('dataset/ar-negative-words.txt','r',encoding='utf-8')
neg_ar_tokens = []
for line in neg_ar_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    neg_ar_tokens.append(line.strip())
    
    
def get_positives_eng():
    return pos_eng_tokens
    
def get_negatives_eng():
    return pos_eng_tokens
    
def get_positives_ar():
    return pos_ar_tokens
    
def get_negatives_ar():
    return neg_ar_tokens
    