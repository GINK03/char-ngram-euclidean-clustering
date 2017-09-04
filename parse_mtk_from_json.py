import json
import gzip

link_freq = json.loads( open('./株式会社エニグモ_result.json').read() )

words = set()
for link, freq in link_freq.items():
  terms = [term for term in link.split('/') if 'mtk=' in term]
  for term in terms:
    words.add( term )

print( words )

with gzip.open('words.gz', 'wt') as f:
  for word in words:
    f.write( word + '\n' )
