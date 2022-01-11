import nltk
import re
from datasets import load_dataset


# nltk.download('punkt')

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


corpus = load_dataset("ar_res_reviews") #first test

# corpus = load_dataset("ajgt_twitter_ar") #second test


def main():
    #testing *******************
    # print(neg_eng_tokens)

    # ***********************

     
    precision = 0
    pts = 0
   #for in range(len(corpus['train']))
    for i in range(len(corpus['train'])):
        score = 0
        polarity = 2 #neutral
        words = corpus['train'][i]['text'].split(' ')
        success = False # just for testing
        for word in words:
            if word in pos_eng_tokens or word in pos_ar_tokens and word not in ['',' ']:
                score += 1
                
            elif word in neg_eng_tokens or word in neg_ar_tokens and word not in ['',' ']:
                score -= 1
                
        
        if score < 0:
            polarity = 0
        elif score == 0:
            polarity = 2
        else:
            polarity = 1
         
        if polarity == corpus['train'][i]['polarity']:
            pts += 1
            success = True
        
        progress = (i/len(corpus['train'])) *100
        print('Progress : ', progress, '% || SCORE OF  COMMENT n',i,' : ',score,' ||  Success : ',success, '|| USER id :', corpus['train'][i]['user_id'])
        
        
    
    precision = (pts/len(corpus['train'])) * 100 
    print('Precision is :', precision, '%')
        
    
    

if __name__ == '__main__':
    
    main()


