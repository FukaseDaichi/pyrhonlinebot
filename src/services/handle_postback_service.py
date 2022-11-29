import json
from linebot.models import TextSendMessage
import re
import importlib


class HandlePostbackService:

    # クラスリスト
    __postback_classList = json.load(
        open(file="./const/postbackClassList.json", mode="r", encoding="utf-8")
    )

    @staticmethod
    def generate_reply_message(event):

        print(event.postback.data)
        # クラスリスト一致検索
        for key in HandlePostbackService.__postback_classList:
            if re.compile(key).fullmatch(event.postback.data):
                message_module = importlib.import_module(
                    HandlePostbackService.__postback_classList[key]
                )
                return message_module.Message.create_message(
                    event, HandlePostbackService.__postback_classList[key]
                )

        # なかった場合
        return TextSendMessage(text="例外が発生しました。")
