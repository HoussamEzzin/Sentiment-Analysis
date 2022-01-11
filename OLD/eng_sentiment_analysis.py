

with open('Tweets.txt') as tweets_file:
    for line in tweets_file:
        line = line.split()
        line.pop()
        print(line)