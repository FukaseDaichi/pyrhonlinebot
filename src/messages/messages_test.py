from linebot.models import (
    TextSendMessage
)

class Message :
	@staticmethod
	def create_message(__message) :		
		return TextSendMessage(text='テスト')