from linebot.models import ImageSendMessage, TemplateSendMessage,ButtonsTemplate,URIAction

from src.services.twitter_api_service import TwitterApiService


class Message :
	@staticmethod
	def create_message(__message) :		
		tweet = TwitterApiService.get_one_tweet()

		# 画像
		image_message = ImageSendMessage(
        	preview_image_url=tweet["img_url"],
        	original_content_url=tweet["img_url"],
    	)
		print(image_message.as_json_dict())

		# 補足
		message_template = TemplateSendMessage(
			alt_text="元ネタ情報",
			template=ButtonsTemplate(
				text=f"作者様 {tweet['user_name']}様",
				actions=[
					URIAction(
						uri=tweet["url"],
						label="元ツイート"
					),
						URIAction(
						uri=f"https://twitter.com/{tweet['user_id']}",
						label="作者様"
					)
				]
			)
    	)
		print(message_template.as_json_dict())
		return [image_message,message_template]