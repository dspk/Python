#. Derive the sentiment score of new terms(terms not in afinn-111.txt)
#. Author: @dspk

import sys
import string

def lines(fp):
    print str(len(fp.readlines()))

#. Create a dictionary named scores from AFINN-111.txt file
def create_dictionary(afinn):
	scores = {}
	for line in afinn:
		term, score = line.split("\t")
		scores[term] = int(score)
	return scores    

#. Derive the total sentiment score of tweets using terms which show up in afinn-111
def get_sentiment_score(tweet, scores):
	tot_score = 0
	for key in scores:
		if key in tweet:
			tot_score += scores[key] 
	return tot_score

#. Find length of words in each tweet corresponding with sent_file(afinn-111.txt)
def len_words(tweet, scores):
	count = 0
	for key in scores:
		if key in tweet:
			count += 1
	return count

#. Calculate average for every tweet
def tot_average(tweet, scores):
	if len_words(tweet, scores) != 0:
		tot_avg = get_sentiment_score(tweet, scores)/len_words(tweet, scores)
	else:
		tot_avg = 0
	return tot_avg

#. Derive the sentiment score for terms which do not show up in afinn-111
def get_sentiment_noshow(tweet, scores):
	new_sent_dictionary = {}
	words = string.split(tweet)
	for word in words:
		if word not in scores:
			sent_noshow = tot_average(tweet, scores)
			new_sent_dictionary[word] = sent_noshow
	return new_sent_dictionary

#. Print each term-sentiment pair and tweet score
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = create_dictionary(sent_file)
    
    for i in range(0, 20):
	x = tweet_file.readline()
    	print x
	score =  get_sentiment_score(x, scores)
	print score
	new_score = get_sentiment_noshow(x, scores)
	print new_score

if __name__ == '__main__':
    main()
