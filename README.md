# Redis database server

ちょくちょくベクトルデータに数値じゃなくてエラーコード入っています。ごめんなさい・・

## 実行方法
` docker run -d  -p 6379:6379 -v {full path to dump.rdb}/dump.rdb:/data/dump.rdb redis:latest `

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
