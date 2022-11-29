from linebot.models import TextSendMessage


class Message:
    @staticmethod
    def create_message(__event, __obj=None):
        return TextSendMessage(text="テスト")
