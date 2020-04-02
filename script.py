from nltk import pos_tag, RegexpParser
from tokenize_words import word_sentence_tokenize # non-library functions
from np_chunk_counter import np_chunk_counter # non-library function
from vp_chunk_counter import vp_chunk_counter # non-library function

text = open("dorian_gray.txt", encoding='utf-8').read().lower()

word_tokenized_text = word_sentence_tokenize(text)

pos_tagged_text = list()

for sentence in word_tokenized_text:
  pos_tagged_text.append(pos_tag(sentence))

np_chunk_grammar = "NP: {<DT>?<JJ>*<NN>}"

np_chunk_parser = RegexpParser(np_chunk_grammar)

vp_chunk_grammar = "VP: {<DT>?<JJ>*<NN><VB.*><RB.?>?}"

vp_chunk_parser = RegexpParser(vp_chunk_grammar)

np_chunked_text = list()
vp_chunked_text = list()

for sentence in pos_tagged_text:
  np_chunked_text.append(np_chunk_parser.parse(sentence))
  vp_chunked_text.append(vp_chunk_parser.parse(sentence))

most_common_np_chunks = np_chunk_counter(np_chunked_text)
print(most_common_np_chunks)

most_common_vp_chunks = vp_chunk_counter(vp_chunked_text)
print(most_common_vp_chunks)
