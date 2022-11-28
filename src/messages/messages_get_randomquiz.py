from linebot.models import ImageSendMessage, TemplateSendMessage,ButtonsTemplate,URIAction,PostbackAction

from src.services.twitter_api_service import TwitterApiService


class Message :
	@staticmethod
	def create_message(event) :		
		tweet = TwitterApiService.get_one_tweet()

		# 画像
		image_message = ImageSendMessage(
        	preview_image_url=tweet.img_url,
        	original_content_url=tweet.img_url,
    	)
		print(image_message.as_json_dict())

		actions = [
					URIAction(
						uri=tweet.url,
						label="元ツイート"
					),
					URIAction(
						uri=f"https://twitter.com/{tweet.user_id}",
						label="作者様"
					)
				]

		if event.source.type == "group":
			actions.append(PostbackAction(
                label='再取得',
                display_text='ランダム謎取得',
                data='id=0'
            ),)

		# 補足
		message_template = TemplateSendMessage(
			alt_text="元ネタ情報",
			template=ButtonsTemplate(
				text=f"作者様 {tweet.user_name}様",
				actions=actions
			)
    	)
		print(message_template.as_json_dict())
		return [image_message,message_template]