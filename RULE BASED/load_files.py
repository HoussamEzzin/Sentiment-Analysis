import re



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


    