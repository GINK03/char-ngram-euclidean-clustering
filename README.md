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
（言葉のcharactorの並びで判断しているので、うまくいかないものはうまくいかない）
```console
  "4": [
    "mtk=iPhone７",
    "mtk=Pinkhouse",
    "mtk=iPhone6S",
    "mtk=iPhoneSE",
    "mtk=IPhone",
    "mtk=iPhonese",
    "mtk=iPhone5",
    "mtk=iPhone",
    "mtk=iPhone5手帳型",
    "mtk=iPhone7",
    "mtk=whitehole",
    "mtk=Rosenheim",
    "mtk=iPhone6",
    "mtk=iPhone7プラス",
    "mtk=ihone",
    "mtk=Chickenson",
    "mtk=iPhone 6",
    "mtk=iPhone 7",
    "mtk=iPhone SE",
    "mtk=iPhone５",
    "mtk=iPhone7手帳型",
    "mtk=iPhone 5",
    "mtk=iPhoneカバー"
  ],
    "29": [
    "mtk=レザーパンツ",
    "mtk=スパンコール",
    "mtk=ヨガパンツ",
    "mtk=カジュアルパンツ",
    "mtk=ワイドパンツ",
    "mtk=桃色パンサー",
    "mtk=パスザバトン",
    "mtk=ロンパース",
    "mtk=靴下、タイツ、スパッツ類",
    "mtk=スウェットパンツ",
    "mtk=バギーパンツ",
    "mtk=パックマン",
    "mtk=スキニーパンツ",
    "mtk=アッパマン",
    "mtk=パンプス・ミュール",
    "mtk=ZNEパンツ",
```
