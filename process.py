import os
import sys
import glob
import pickle
import json
from gensim.models import KeyedVectors
import numpy as np
def make_dic():
  word_vec = {}
  with open('model.vec') as f:
    next(f)
    for line in f:
      line = line.strip()
      ents = line.split(' ')
      word = ents.pop(0)
      # print( line )
      vec = list(map(float, ents) )
      # print( word, vec)
      word_vec[word] = vec
  open('word_vec.pkl', 'wb').write( pickle.dumps(word_vec) )
  model = KeyedVectors.load_word2vec_format('model.vec', binary=False)
  open('model.pkl', 'wb').write( pickle.dumps(model) )

def calc():
  model = pickle.loads( open('model.pkl', 'rb').read() ) 
  words = [w for w in pickle.loads( open('word_vec.pkl','rb').read() ).keys()]
  for word in words:
    try:
      scores = model.most_similar(positive=[ word ])
    except KeyError as e:
      continue
    print( word )
    print( json.dumps(scores, ensure_ascii=False, indent=2) )

# clustering
from sklearn.cluster import KMeans
def fit():
  model = KMeans(n_clusters=200, random_state=0)
  print('load to numpy array') 
  xs = np.array( [np.array(w) for w in pickle.loads( open('word_vec.pkl','rb').read() ).values() if len(w) == 256 ][:1024*100] )
  print('finished to numpy array') 
  print('start to fit') 
  model.fit(xs)
  print('finish to fit') 

  open('kmean-model.pkl', 'wb').write( pickle.dumps(model) )
# predict
def predict():
  km = pickle.loads( open('kmean-model.pkl', 'rb').read() )
  word_vec = pickle.loads( open('word_vec.pkl','rb').read() )

  cluster_words = {}
  for word, vec in word_vec.items():
    if len(vec) != 256:
      continue
    p = km.predict( [vec] )
    cluster = int(p[0])
    #print(cluster, word)
    if cluster_words.get(cluster) is None:
      cluster_words[cluster] = list()

    cluster_words[cluster].append( str(word) )
  open('cluter_words.json', 'w').write( json.dumps( cluster_words, indent=2, ensure_ascii=False ) )

if '--make_dic' in sys.argv:
  make_dic()

if '--calc' in sys.argv:
  calc()

if '--fit' in sys.argv:
  fit()

if '--predict' in sys.argv:
  predict()
