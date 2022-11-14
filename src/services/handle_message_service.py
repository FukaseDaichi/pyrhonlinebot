import json

class handle_message_service :
	mydict = json.load(open(file='./src/dict/mydict.json', mode='r', encoding="utf-8"))

	@staticmethod
	def generate_reply_message(receivedMessage) :
		for key in handle_message_service.mydict :
			if (receivedMessage == key) :
				return handle_message_service.mydict[key]
		return handle_message_service.mydict['except']