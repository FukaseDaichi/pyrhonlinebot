from linebot.models import TextSendMessage


class Message:
    @staticmethod
    def create_message(event):
        return TextSendMessage(text=event.message.text)
