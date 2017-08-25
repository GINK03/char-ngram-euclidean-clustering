import glob
import os
import sys
import math
import pickle
import random
import numpy as np

def make_dic():
  word_vec = {}
  with open('../model.vec') as f:
    head = next(f)
    for line in f:
      line = line.strip()
      ents = line.split(' ')
      word = ents.pop(0)
      vec  = list(map(float, ents))
      word_vec[word] = vec
  print('dump to pickle')
  open('word_vec.pkl', 'wb').write( pickle.dumps(word_vec) )
  print('finish to pickle')

def _clustering(word_vec, word_clus):
  C = 3
  cset = {}
  for c in range(C):
    cset[c] = list()
  # initial 
  for word, clus in word_clus.items():
    cset[clus].append(word_vec[word])
  # calc each mean
  LEN = 256

  b_base = {}
  for c, ss in cset.items():
    base = np.zeros( (LEN) )
    arr = [s for s in ss] 
    for s in arr:
      base += np.array( s )
    base = base / len(ss)
    b_base[c] = base
 
  word_clus = {}
  for word, vec in word_vec.items():
    if len(vec) != LEN:
      continue
    clus_sim = {}
    for clus, base in b_base.items():
      clus 
      head = np.dot(np.array(base),np.array(vec)) 
      tail = np.linalg.norm(base)*np.linalg.norm(vec)
      clus_sim[clus] = head/tail
    va = list( clus_sim.values() )
    #print( clus_sim )
    alloc = np.argmax(va)
    word_clus[word] = alloc
  return word_clus

def clustering():
  word_vec = pickle.loads( open('word_vec.pkl', 'rb').read() ) 
  word_vec = {word:vec for word, vec in list(word_vec.items())[:10]}
  ns = {}
  LEN = 256
  if os.path.exists('word_clus.pkl') is not None:
    for word, vec in list(word_vec.items()):
      print( word, vec )
      if len(vec) == LEN:
        ns[word] = vec 
    print( ns )

    C = 3
    cset = {}
    for c in range(C):
      cset[c] = list()
    # initial 
    for en, vec in enumerate(ns.values()):
      init = en%C
      cset[init].append(vec)
    # calc each mean

    b_base = {}
    for c, ss in cset.items():
      base = np.zeros( (LEN) )
      arr = [s for s in ss] 
      for s in arr:
        base += np.array( s )
      base = base / len(ss)
      # print( base )
      b_base[c] = base
   
    word_clus = {}
    for word, vec in word_vec.items():
      if len(vec) != LEN:
        continue
      clus_sim = {}
      for clus, base in b_base.items():
        clus 
        head = np.dot(np.array(base),np.array(vec)) 
        tail = np.linalg.norm(base)*np.linalg.norm(vec)
        clus_sim[clus] = head/tail
      va = list( clus_sim.values() )
      #print( clus_sim )
      alloc = np.argmax(va)
      word_clus[word] = alloc
    
    for i in range(100):
      print( i )
      word_clus = _clustering(word_vec, word_clus) 
      open('word_clus.pkl', 'wb').write( pickle.dumps(word_clus) )
  else:
      word_clus = pickle.loads( open('word_clus.pkl', 'rb').read() )
      for i in range(100):
        print( i )
        word_clus = _clustering(word_vec, word_clus) 
        open('word_clus.pkl', 'wb').write( pickle.dumps(word_clus) )
    
   

if '--make_dic' in sys.argv:
  make_dic()

if '--clustering' in sys.argv:
  clustering()
