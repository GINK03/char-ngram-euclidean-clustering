# treasuredata metkeywod clustering

## fasttextとkmeansでクラスタリング

### 方法
- 直近、一年のユーザの時系列で触れたメタキーワードのデータを全てダンプ
- metakeywordを一つの単語として位置付ける
- fasttextで256次元でベクトル化(そのたデフォルト値)
- 200クラスタにkmeans

## 実行
fasttextで学習
```cosnole
$ fasttext -input metakeyword.txt -ouput model -dim 256 -thread 16
```
dictionaryの作成
```console
$ python3 process.py --make_dic
```
clustering
```console
$ python3 process.py --fit
```
predict(クラスタリングしたファイルを出力)
```console
$ python3 process.py --predict
```
