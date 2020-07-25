# Redis database server

ちょくちょくベクトルデータに数値じゃなくてエラーコード入っています。ごめんなさい・・

## 実行方法
1. ビルドと起動 
Dockerのredisイメージ撮ってきて.rdbファイルをデータベースに読み込んでください。


## データベースの内容
 |key |value type|
 |------ |------ |
 |user:{Id}:name|string|
 |user:{Id}:pref|string|
 |user:{Id}:vec|string [300]|
 |hotel:{Id}:vec|string [300]|

- 総キー数11604
- ~~ホテル数29475~~
- 初期ユーザ数5人
