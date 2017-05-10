# -*- coding: utf-8 -*-
def words(string):
	word_count = {}
	for word in string.split():
		word = int(word) if word.isdigit() else word
		if word in word_count:
			word_count[word] +=1
		else:
			word_count[word] = 1
	return word_count
print (words("hello  world"))