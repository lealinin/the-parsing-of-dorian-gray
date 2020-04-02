from nltk.tokenize import PunktSentenceTokenizer, word_tokenize

def word_sentence_tokenize(text):

  sentence_tokenizer = PunktSentenceTokenizer(text)

  sentence_tokenized = sentence_tokenizer.tokenize(text)

  word_tokenized = list()

  for sentence in sentence_tokenized:
    word_tokenized.append(word_tokenize(sentence))
    return word_tokenized
