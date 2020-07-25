# Redis database server

ちょくちょくベクトルデータに数値じゃなくてエラーコード入っています。ごめんなさい・・

## 実行方法
1. ビルドと起動 
    ```bash
    docker build ./ -t bba_redis_server
    docker run --name bba_redis_server -d -p 6379:6379 bba_redis_server
    ```
    コンテナ起動時に`init.sh`が実行され、初期データ`init.rdb`が全てデータベースに登録されます。通信は6379番ポートを利用しています。


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
