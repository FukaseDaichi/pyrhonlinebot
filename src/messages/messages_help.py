from linebot.models import (
    TextSendMessage
)

class Message :
	@staticmethod
	def create_message(message) :		
		return TextSendMessage(text=message)