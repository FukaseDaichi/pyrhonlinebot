# ライブラリのインポート
import os
import random
import tweepy
from datetime import datetime, timezone
import pytz
import pandas as pd

from src.commonclass.dict_not_notetion import DictDotNotation


class TwitterApiService:
    # Twitter情報。
    CONSUMER_KEY = os.environ["CONSUMER_KEY"]
    CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
    ACCESS_TOKEN = os.environ["ACCESS_TOKEN"]
    ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

    # 検索条件の設定
    # リツイート除外
    SEARCH_WORD = "(#解けたらRT OR #kotae謎解き) -filter:retweets"
    # 何件のツイートを取得するか
    ITEM_NUMBER = 1000

    # Twitterの認証
    __auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    __auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    __api = tweepy.API(__auth)
    # 　”wait_on_rate_limit = True”　利用制限にひっかかた時に必要時間待機する
    __api = tweepy.API(__auth, wait_on_rate_limit=True)

    __tw_data = []

    @staticmethod
    def change_time_JST(u_time):
        # イギリスのtimezoneを設定するために再定義する
        utc_time = datetime(
            u_time.year,
            u_time.month,
            u_time.day,
            u_time.hour,
            u_time.minute,
            u_time.second,
            tzinfo=timezone.utc,
        )
        # タイムゾーンを日本時刻に変換
        jst_time = utc_time.astimezone(pytz.timezone("Asia/Tokyo"))
        # 文字列で返す
        str_time = jst_time.strftime("%Y-%m-%d_%H:%M:%S")
        return str_time

    # 検索条件を元にツイートを抽出
    @staticmethod
    def get_tweets():

        print("◆定期実行：ツイート取得")
        # 初期化
        TwitterApiService.__tw_data = []
        count = 0

        for tweet in tweepy.Cursor(
            TwitterApiService.__api.search_tweets,
            q=TwitterApiService.SEARCH_WORD,
            tweet_mode="extended",
            result_type="mixed",
            lang="ja",
            include_entities=True,
            count=200,
        ).items(TwitterApiService.ITEM_NUMBER):
            count = count + 1
            # 以下デバッグ用
            # print(tweet._json)
            try:
                # 画像取得
                tweet_url = tweet.extended_entities["media"][0]["url"]
                tweet_img_url = tweet.extended_entities["media"][0]["media_url_https"]

                # ツイート時刻とユーザのアカウント作成時刻を日本時刻にする
                tweet_time = TwitterApiService.change_time_JST(tweet.created_at)

                # tweet_dataの配列に取得したい情報を入れていく
                TwitterApiService.__tw_data.append(
                    DictDotNotation(
                        {
                            "url": tweet_url,
                            "img_url": tweet_img_url,
                            "time": tweet_time,
                            "user_id": tweet.user.screen_name,
                            "user_name": tweet.user.name,
                        }
                    )
                )

            except Exception as e:
                continue

        print(f"{count}件検索")

    @staticmethod
    def get_one_tweet():
        return random.choice(TwitterApiService.__tw_data)

    @staticmethod
    def output_csv():
        # 取り出したデータをpandasのDataFrameに変換
        # CSVファイルに出力するときの列の名前を定義
        labels = [
            "URL",
            "画像",
            "ツイート時間",
            "ユーザー名",
            "アカウント名",
        ]

        # tw_dataのリストをpandasのDataFrameに変換
        datas = [list(tw.values()) for tw in TwitterApiService.__tw_data]
        df = pd.DataFrame(datas, columns=labels)

        # CSVファイルに出力する
        # CSVファイルの名前を決める
        file_name = "./const.tw_data.csv"

        # CSVファイルを出力する
        df.to_csv(file_name, encoding="utf-8-sig", index=False)
