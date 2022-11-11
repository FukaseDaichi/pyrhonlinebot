import json

class handle_message_service :
	def generate_reply_message(receivedMessage) :
		json_file = open(file='./src/dict/mydict.json', mode='r', encoding="utf-8")
		mydict = json.load(json_file)
		
		for key in mydict :
			if (receivedMessage == key) :
				return mydict[key]
		return mydict['except']