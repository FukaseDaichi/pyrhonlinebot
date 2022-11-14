import json
from linebot.models import (
    TextSendMessage
)

class handle_message_service :
	__mydict = json.load(open(file='./const/dict/mydict.json', mode='r', encoding="utf-8"))

	@staticmethod
	def generate_reply_message(receivedMessage) :
		for key in handle_message_service.__mydict :
			if (receivedMessage == key) :
				return TextSendMessage(text=handle_message_service.__mydict[key])

		# なかった場合
		return TextSendMessage(text=handle_message_service.__mydict["except"])