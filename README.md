# char ngram eclidean clustering

### 方法
- 集計粒度をまず固定する
- この方法では、kmeansでユークリッド距離を距離関数として、char-ngramでクラスタリングする
- 5000単語で200クラスタで60秒ほど

## 実行
可視化ソフトなどに代入する、データのjsonから、単語一覧を抜き出す
```console
$ python3 parse_mtk_from_json.py
```
単語をvector化する
```console
$ python3 make_char_ngram.py --make1
```
KMeansでクラスタリングを行い、モデルを学習
```console
$ python3 make_char_ngram.py --make2
```
全ての単語にクラスタを割り当てて、jsonで保存
```console
$ python3 make_char_ngram.py --make3
```

## 実行例
総合通販サイトからクラスタリングを行い、結果を確認すると、うまくいくものはうまくいくことがわかる
```console

```
