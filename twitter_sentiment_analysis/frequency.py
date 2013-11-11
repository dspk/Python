#. Compute frequency of each term across all tweets
#. Author: @dspk

import sys
import string
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from collections import Counter

#. Create a dictionary named scores from AFINN-111.txt file
def create_dictionary(afinn):
	scores = {}
	for line in afinn:
		term, score = line.split("\t")
		scores[term] = int(score)
	return scores    

#. Find total number of words in all tweets using string.split
def total_words(tweet):
	words_total = len(string.split(tweet)) #words in every tweet
	return words_total

#. Find total number of words in all tweets using nltk tokenize
def words_total(tweet):
	words_t = word_tokenize(tweet)
	words_tot = len(words_t)
	return words_tot

#. Find number of occurences of each term in a tweet
def word_freq_dictionary(tweet, word_frequency):
	words_t = word_tokenize(tweet)
	for word in words_t:
		if word in word_frequency:
			word_frequency[word] += 1
		elif word not in word_frequency:
			word_frequency[word] = 1  #if word not in dict add it to the dict
	return word_frequency
			
#. Print each term-frequency pair
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = create_dictionary(sent_file)
    
    word_frequency = {}
    words_total_value = 0
    for i in range(0, 20):
 	x = tweet_file.readline()
	words_total_value += total_words(x)
	word_frequency = word_freq_dictionary(x, word_frequency)
	
    count_term = 0
    for key in word_frequency:
	count_term += 1
	print count_term, key, float(word_frequency[key])/words_total_value

if __name__ == '__main__':
    main()











