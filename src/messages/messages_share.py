from linebot.models import (
    TemplateSendMessage,
    URIAction,
    ButtonsTemplate,
    ImageSendMessage,
)

from src.commonclass.constants import Constants


class Message:
    @staticmethod
    def create_message(__event, __obj=None):
        share_url = Constants.DOMAIN_URL + "resources/img/share.png"

        # 画像
        image_message = ImageSendMessage(
            preview_image_url=share_url,
            original_content_url=share_url,
        )

        buttons_template_message = TemplateSendMessage(
            alt_text="よろしければ画像を使用してシェアお願いします！",
            template=ButtonsTemplate(
                thumbnail_image_url=Constants.DOMAIN_URL
                + "resources/img/btn_share.png",
                text="よろしければシェアお願いします！",
                default_action=URIAction(label="ツイートする", uri=Constants.LINK_URL),
                actions=[URIAction(label="ツイートする", uri=Constants.LINK_URL)],
            ),
        )

        return [image_message, buttons_template_message]
