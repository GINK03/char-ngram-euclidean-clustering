import gzip
import os
import math
import pickle
char_index = {}
with gzip.open('./201708.neologd.gz', 'rt') as f:
  for line in f:
    line = line.strip()
    #print( line )
    for char in set(line):
      if char_index.get(char) is None:
        char_index[char] = len(char_index)

open('pickles/char_index.pkl', 'wb').write( pickle.dumps(char_index) )


word_vec = {}
vec_size = len(char_index)
with gzip.open('./201708.neologd.gz', 'rt') as f:
  for line in f:
    line = line.strip()
    vec = [0.0]*vec_size
    for char in list(line):
      index = char_index[char]
      vec[index] += 1.0
    word = line
    word_vec[word] = vec

open('pickles/word_vec.pkl', 'wb').write( pickle.dumps(word_vec) )
