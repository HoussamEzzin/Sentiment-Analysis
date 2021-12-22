from re import S
from load_dataset_files import get_negatives_ar, get_negatives_eng, get_positives_ar, get_positives_eng



with open('Tweets.txt') as tweets_file:
    progress = 0
    N = 10006
    pts =0
    for line in tweets_file:
        progress +=1
        print("Progress : "+str((progress*100)/N)+"%")
        line = line.split()
        emotion = line[len(line)-1]
        line.pop()
        score = 0
        
        for word in line:
            if word in get_positives_ar():
                score +=1
            elif word in get_negatives_ar():
                score -=1
        
        if score == 0 and (emotion == 'OBJ' or emotion == 'NEUTRAL'):
            print("NEUTRAL FOUND")
            pts +=1
        elif score < 0 and emotion == 'NEG':
            print("NEG FOUND")
            pts +=1
        elif score > 0 and emotion == 'POS':
            print("POS FOUND")
            pts+=1
    
    print("PRECISION :", (pts/N)*100)
        
        
