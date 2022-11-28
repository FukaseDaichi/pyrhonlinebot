from linebot.models import (
    TextSendMessage
)

class Message :
	@staticmethod
	def create_message(__event) :		
		return TextSendMessage(text='テスト')