import gzip
import os
import math
import pickle
import sys
if '--make1' in sys.argv:
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

if '--make2' in sys.argv:
  word_vec = pickle.loads( open('pickles/word_vec.pkl', 'rb').read() )
  import numpy as np
  from sklearn.cluster import KMeans
  for word in word_vec.keys():
    #print( len(word_vec) )
    word_vec[word] = np.array(word_vec[word])
  print('make numpy array')
  X = np.array( list( word_vec.values() ) )

  print('start to fit kmeans')
  kmeans = KMeans(n_clusters=200, random_state=0).fit(X)
  print('finished to fit kmeans')
  open('pickles/kmeans.pkl', 'wb').write( pickle.dumps(kmeans) )
 
 # 実際にクラスタリングする
if '--make3' in sys.argv:
  import numpy as np
  kmeans = pickle.loads(open('pickles/kmeans.pkl', 'rb').read() )
  word_vec = pickle.loads( open('pickles/word_vec.pkl', 'rb').read() )

  cls_words = {}
  for en, (word, vec) in enumerate(word_vec.items()):
    if en%1000 == 0:
      print( en, word )
    word, x =  word, np.array([vec])
    y = kmeans.predict(x)
    y = y.tolist().pop()
    if cls_words.get(y) is None:
      cls_words[y] = []
    cls_words[y].append( word )

  for cls, words in cls_words.items():
    print( cls, sorted(words)[:20] )
