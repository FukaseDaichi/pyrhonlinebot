from linebot.models import (
    ImagemapSendMessage,BaseSize, URIImagemapAction,
    ImagemapArea,TemplateSendMessage,URIAction,ButtonsTemplate
)

class Message :
	@staticmethod
	def create_message(__event) :
		LINK_URL="https://twitter.com/intent/tweet?text=LINE%E8%AC%8E%E8%A7%A3%E3%81%8D%E3%80%8C%E3%83%A9%E3%83%B3%E3%83%80%E3%83%A0%E8%AC%8E%E3%80%8D%0ATwitter%E3%81%AE%E4%B8%80%E6%9E%9A%E8%AC%8E%E3%82%92%E3%83%A9%E3%83%B3%E3%83%80%E3%83%A0%E3%81%A7%E5%8F%96%E5%BE%97%E3%81%97%E3%81%BE%E3%81%99%E3%80%82%E6%96%B0%E3%81%97%E3%81%84%E4%BD%9C%E8%80%85%E3%81%A8%E3%81%AE%E5%87%BA%E4%BC%9A%E3%81%84%E3%82%92%E3%81%82%E3%81%AA%E3%81%9F%E3%81%AB%EF%BC%81%0Ahttps%3A%2F%2Flin.ee%2FZfNZsfI%0A%0Ahttps%3A%2F%2Ft.co%2Fe60uHIZo5W&hashtags=Line%E8%AC%8E,%E8%AC%8E%E8%A7%A3%E3%81%8D"
		
		imagemap_message = ImagemapSendMessage(
   			base_url="https://pythonlinebot.onrender.com/resources/img/imagemap",
    		alt_text="シェアツイート",
    		base_size=BaseSize(height=1040, width=1040),
    		actions=[
        		URIImagemapAction(
            		link_uri=LINK_URL,
            		area=ImagemapArea(
                		x=0, y=0, width=1040, height=1040
            		)
        		),
    		]
		)

		buttons_template_message = TemplateSendMessage(
    		alt_text="よろしければシェアお願いします！",
    		template=ButtonsTemplate(
        		thumbnail_image_url="https://pythonlinebot.onrender.com/resources/img/share.png",
				imageAspectRatio="square",
        		text="よろしければシェアお願いします！",
				default_action=URIAction(
                		label="ツイートする",
                		uri=LINK_URL),
        		actions=[
            		URIAction(
                		label="ツイートする",
                		uri=LINK_URL
            		)
        		]
    		)
	)

		return [imagemap_message,buttons_template_message]