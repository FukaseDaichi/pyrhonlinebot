from linebot.models import (
    TemplateSendMessage,
    URIAction,
    ButtonsTemplate,
    ImageSendMessage,
)


class Message:
    @staticmethod
    def create_message(__event):

        SHARE_IMG_URL = "https://pythonlinebot.onrender.com/resources/img/share.png"
        LINK_URL = "https://twitter.com/intent/tweet?text=LINE%E8%AC%8E%E8%A7%A3%E3%81%8D%E3%80%8C%E3%83%A9%E3%83%B3%E3%83%80%E3%83%A0%E8%AC%8E%E3%80%8D%0ATwitter%E3%81%AE%E4%B8%80%E6%9E%9A%E8%AC%8E%E3%82%92%E3%83%A9%E3%83%B3%E3%83%80%E3%83%A0%E3%81%A7%E5%8F%96%E5%BE%97%E3%81%97%E3%81%BE%E3%81%99%E3%80%82%E6%96%B0%E3%81%97%E3%81%84%E4%BD%9C%E8%80%85%E3%81%A8%E3%81%AE%E5%87%BA%E4%BC%9A%E3%81%84%E3%82%92%E3%81%82%E3%81%AA%E3%81%9F%E3%81%AB%EF%BC%81%0Ahttps%3A%2F%2Flin.ee%2FZfNZsfI%0A%0&hashtags=Line%E8%AC%8E,%E8%AC%8E%E8%A7%A3%E3%81%8D"

        # 画像
        image_message = ImageSendMessage(
            preview_image_url=SHARE_IMG_URL,
            original_content_url=SHARE_IMG_URL,
        )

        buttons_template_message = TemplateSendMessage(
            alt_text="よろしければシェアお願いします！",
            template=ButtonsTemplate(
                thumbnail_image_url="https://pythonlinebot.onrender.com/resources/img/btn_share.png",
                text="よろしければシェアお願いします！",
                default_action=URIAction(label="ツイートする", uri=LINK_URL),
                actions=[URIAction(label="ツイートする", uri=LINK_URL)],
            ),
        )

        return [image_message, buttons_template_message]
