from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize # non-library functions

text = open("dorian_gray.txt", encoding='utf-8').read().lower()

word_tokenized_text = word_sentence_tokenize(text)

pos_tagged_text = list()

for sentence in word_tokenized_text:
  pos_tagged_text.append(pos_tag(sentence))

# single_pos_sentence = pos_tagged_text[50]
# print(single_pos_sentence)



