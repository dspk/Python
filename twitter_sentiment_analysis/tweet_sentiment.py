#. Compute the sentiment of each tweet based on the sentiment scores of the terms in the tweet.
#. Author: @dspk

import sys

def lines(fp):
    print str(len(fp.readlines()))

def create_dictionary(afinn):
    scores = {}
    for line in afinn:
	term,score = line.split("\t") 
	scores[term] = int(score) 
    return scores

#. Calculate total sentiment score for terms that appear in the file containing the sentiment scores(afinn-111)
def get_sentiment_score(tweet, scores):
	tot_score = 0	
	for key in scores:
		if key in tweet:
			tot_score += scores[key]
	return tot_score

#. Print tweets and sentiment scores of each tweet 
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = create_dictionary(sent_file)

    for i in range(0,20):
    	x = tweet_file.readline()
    	print x
	score =  get_sentiment_score(x, scores)
	print score

if __name__ == '__main__':
    main()


