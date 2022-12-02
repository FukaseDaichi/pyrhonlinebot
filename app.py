from flask import Flask, request, abort, render_template

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    StickerMessage,
    ImageMessage,
    JoinEvent,
    PostbackEvent,
)
import os
from src.services.handle_postback_service import HandlePostbackService
from src.messages.messages_get_randomquiz import Message as DefoltMessage
from src.commonclass.dict_not_notetion import DictDotNotation
from src.services.handle_message_service import *

from src.services.schedule import *


# Flaskを準備
app = Flask(__name__, static_folder="resources")

# 環境変数からLINE Access Tokenを設定
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
# 環境変数からLINE Channel Secretを設定
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

# LineBotApiのインスタンスを生成
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

# WebhookHandlerのインスタンスを生成
handler = WebhookHandler(LINE_CHANNEL_SECRET)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/share")
def share():
    return render_template("share.html")


@app.route("/callback", methods=["POST"])
def callback():
    # HTTPリクエストヘッダからX-Line-Signatureを取り出す
    signature = request.headers["X-Line-Signature"]
    # テキストでpostされたデータを取得
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


# 動作確認用
@app.route("/test//<text>", methods=["GET"])
def test(text):
    event = DictDotNotation({"message": DictDotNotation({"text": text})})
    messages = HandleMessageService.generate_reply_message(event)
    if type(messages) == list:
        return {"messages": [message.as_json_dict() for message in messages]}

    return {"messages": [message.as_json_dict() for message in [messages]]}


# MessageEvent
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # テキストでの返信を行う
    try:
        messages = HandleMessageService.generate_reply_message(event)

        line_bot_api.reply_message(event.reply_token, messages)
    except Exception as e:
        error_handler(event.reply_token, e)


# スタンプハンドラー
@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker(event):
    defolt_handler(event)


# 画像ハンドラー
@handler.add(MessageEvent, message=ImageMessage)
def handle_image(event):
    defolt_handler(event)


# グループ参加
@handler.add(JoinEvent)
def handle_join(event):
    defolt_handler(event)


# PostBackEvent
@handler.add(PostbackEvent)
def handle_postback(event):
    # テキストでの返信を行う
    try:
        messages = HandlePostbackService.generate_reply_message(event)

        line_bot_api.reply_message(event.reply_token, messages)
    except Exception as e:
        error_handler(event.reply_token, e)


# デフォルトハンドラー
def defolt_handler(event):
    # テキストでの返信を行う
    try:
        messages = DefoltMessage.create_message(event)
        line_bot_api.reply_message(event.reply_token, messages)
    except Exception as e:
        error_handler(event.reply_token, e)


# エラーハンドラー
def error_handler(reply_token, e):
    print(e)
    line_bot_api.reply_message(reply_token, TextSendMessage(text="例外が発生しました。"))


if __name__ == "__main__":
    app.run()
