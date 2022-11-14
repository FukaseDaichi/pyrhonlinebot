from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
import os

from src.services.handle_message_service import *

#Flaskを準備
app = Flask(__name__)

#環境変数からLINE Access Tokenを設定
LINE_CHANNEL_ACCESS_TOKEN = os.environ["LINE_CHANNEL_ACCESS_TOKEN"]
#環境変数からLINE Channel Secretを設定
LINE_CHANNEL_SECRET = os.environ["LINE_CHANNEL_SECRET"]

#LineBotApiのインスタンスを生成
line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

#WebhookHandlerのインスタンスを生成
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # HTTPリクエストヘッダからX-Line-Signatureを取り出す
    signature = request.headers['X-Line-Signature']
    #テキストでpostされたデータを取得
    body = request.get_data(as_text=True)

    app.logger.info("Request body: " + body)
    # webhookのbodyを解析する
    # この結果はadd関数で受け取る
    # なお、Signatureが一致していない時はInvalidSignatureError例外が発生する

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# MessageEvent
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # テキストでの返信を行う
    reply = handle_message_service.generate_reply_message(event.message.text)

    # line_bot_api.reply_message(
    #     event.reply_token,
    #     TextSendMessage(text=event.message.text )
    # )

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply )
    )

if __name__ == "__main__":
    app.run()