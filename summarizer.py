# importing libraries 
import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

# Input text - to summarize 
text = "Ce petit être est joyeux. Il ne mange pas tous les jours et il va au \
spectacle, si bon lui semble, tous les soirs. Il n’a pas de chemise sur le \
corps, pas de souliers aux pieds, pas de toit sur la tête; il est comme les \
mouches du ciel qui n’ont rien de tout cela. Il a de sept à treize ans, vit \
par bandes, bat le pavé, loge en plein air, porte un vieux pantalon de son \
père qui lui descend plus bas que les talons, un vieux chapeau de quelque \
autre père qui lui descend plus bas que les oreilles, une seule bretelle en \
lisière jaune, court, guette, quête, perd le temps, culotte des pipes, jure \
comme un damné, hante le cabaret, connaît des voleurs, tutoie des filles, \
parle argot, chante des chansons obscènes, et n’a rien de mauvais dans le \
cœur. C’est qu’il a dans l’âme une perle, l’innocence, et les perles ne se \
dissolvent pas dans la boue. Tant que l’homme est enfant, Dieu veut qu’il \
soit innocent."

# Tokenizing the text 
stopWords = set(stopwords.words("french")) 
words = word_tokenize(text) 

# Creating a frequency table to keep the 
# score of each word 

freqTable = dict() 
for word in words: 
	word = word.lower() 
	if word in stopWords: 
		continue
	if word in freqTable: 
		freqTable[word] += 1
	else: 
		freqTable[word] = 1

# Creating a dictionary to keep the score 
# of each sentence 
sentences = sent_tokenize(text) 
sentenceValue = dict() 

for sentence in sentences: 
	for word, freq in freqTable.items(): 
		if word in sentence.lower(): 
			if sentence in sentenceValue: 
				sentenceValue[sentence] += freq 
			else: 
				sentenceValue[sentence] = freq 

sumValues = 0
for sentence in sentenceValue: 
	sumValues += sentenceValue[sentence] 

# Average value of a sentence from the original text 

average = int(sumValues / len(sentenceValue)) 

# Storing sentences into our summary. 
summary = '' 
for sentence in sentences: 
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
		summary += " " + sentence 
print(summary) 