from load_files import *

def check_for_pos(token):
    score = 0
    if token in get_high_pos():
        score +=3
    elif token in get_medium_pos():
        score += 2
    elif token in get_low_pos():
        score += 1
    return score

def check_for_neg(token):
    score =0
    if token in get_high_neg():
            score -=3
    elif token in get_medium_neg():
            score -= 2
    elif token in get_low_neg():
            score -= 1
    return score

def negation_word_checker(token,next_token):
    score =0
    if check_for_pos(next_token) != 0 :
        score -= 1
    elif check_for_neg(next_token) !=0:
        score += 1
    else:
        score -=1 
    return score

def analyze(tokens):
    score = 0
    for j in range(len(tokens)):
        if tokens[j] in get_negation_words():
            score += negation_word_checker(tokens[j],tokens[j+1])
        score +=check_for_pos(tokens[j])
        score += check_for_neg(tokens[j])
        
    return score

def update_count(score,polarity):
    count = 0
    if score > 0 and polarity == "PO":
        count += 1
    elif score < 0 and polarity == "NG":
        count += 1
    elif score == 0 and polarity == "NE":
        count += 1  
    return count