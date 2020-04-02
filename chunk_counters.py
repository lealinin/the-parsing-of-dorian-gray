from collections import Counter

def np_chunk_counter(chunked_sentences):
  chunks = list()

  for sentence in chunked_sentences:
    for subtree in sentence.subtrees(filter=lambda t:t.label() == 'NP'):
      chunks.append(tuple(subtree))

  chunk_counter = Counter()

  for chunk in chunks:
    chunk_counter[chunk] += 1