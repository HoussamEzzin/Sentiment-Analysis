import re


# -**/************* POSITIVES
high_pos_file = open('sentiment_files/tiers/high_pos.txt','r',encoding="windows-1256")
high_pos_tokens = []
for line in high_pos_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    high_pos_tokens.append(line.strip())
    
medium_pos_file = open('sentiment_files/tiers/medium_pos.txt','r',encoding="windows-1256")
medium_pos_tokens = []
for line in medium_pos_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    medium_pos_tokens.append(line.strip())

low_pos_file = open('sentiment_files/tiers/low_pos.txt','r',encoding="windows-1256")
low_pos_tokens = []
for line in low_pos_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    low_pos_tokens.append(line.strip())

# ****************** NEGATIVES
low_neg_file = open('sentiment_files/tiers/low_neg.txt','r',encoding="windows-1256")
low_neg_tokens = []
for line in low_neg_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    low_neg_tokens.append(line.strip())

medium_neg_file = open('sentiment_files/tiers/medium_neg.txt','r',encoding="windows-1256")
medium_neg_tokens = []
for line in medium_neg_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    medium_neg_tokens.append(line.strip())
    
high_neg_file = open('sentiment_files/tiers/high_neg.txt','r',encoding="windows-1256")
high_neg_tokens = []
for line in high_neg_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    high_neg_tokens.append(line.strip())




pos_ar_file = open('pos.txt','r',encoding="windows-1256")
pos_ar_tokens = []
for line in pos_ar_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    pos_ar_tokens.append(line.strip())
    
negation_words_file = open('sentiment_files/negationWords.txt','r',encoding="windows-1256")
negation_words_tokens = []
for line in negation_words_file:
    if re.search('\n$',line):
        line = line[0:len(line)-1]
    negation_words_tokens.append(line.strip())



neg_ar_file = open('neg.txt','r',encoding="windows-1256")
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

def get_negation_words():
    return negation_words_tokens

def get_high_pos():
    return high_pos_tokens

def get_medium_pos():
    return medium_pos_tokens

def get_low_pos():
    return low_pos_tokens

def get_high_neg():
    return high_neg_tokens

def get_medium_neg():
    return medium_neg_tokens

def get_low_neg():
    return low_neg_tokens


    