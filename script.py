from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize # non-library functions

text = open("dorian_gray.txt", encoding='utf-8').read().lower()

word_tokenized_text = word_sentence_tokenize(text)

pos_tagged_text = list()

for sentence in word_tokenized_text:
  pos_tagged_text.append(pos_tag(sentence))

np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

np_chunk_parser = RegexpParser(np_chunk_grammar)

