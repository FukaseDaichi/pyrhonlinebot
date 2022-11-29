import json
from linebot.models import TextSendMessage
import re
import importlib

from src.messages.messages_share import Message as ShareMessage


class HandleMessageService:

    # クラスリスト
    __classList = json.load(
        open(file="./const/classList.json", mode="r", encoding="utf-8")
    )

    # メッセージ辞書
    __messagedict = json.load(
        open(file="./const/messagedict.json", mode="r", encoding="utf-8")
    )

    @staticmethod
    def generate_reply_message(event):
        # クラスリスト一致検索
        for key in HandleMessageService.__classList:
            if re.compile(key).fullmatch(event.message.text):
                message_module = importlib.import_module(
                    HandleMessageService.__classList[key]
                )
                return message_module.Message.create_message(event)

        # メッセージ辞書一致
        for key in HandleMessageService.__messagedict:
            if re.compile(key).fullmatch(event.message.text):
                return TextSendMessage(text=HandleMessageService.__messagedict[key])

        # なかった場合
        return ShareMessage.create_message(event)
