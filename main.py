import requests
import telebot 
import json
import os

# TOKEN = os.environ['TOKEN']
# CID = os.environ['CID']


#bot = telebot.TeleBot(TOKEN)

http = requests.get("https://www.proxyscan.io/api/proxy?limit=15&type=http&format=txt")
https = requests.get("https://www.proxyscan.io/api/proxy?limit=15&type=https&format=txt")
socks4= requests.get("https://www.proxyscan.io/api/proxy?limit=15&type=socks4&format=txt")
socks5 = requests.get("https://www.proxyscan.io/api/proxy?limit=15&type=socks5&format=txt")

open('http.txt', 'wb').write(http.content)
open('https.txt', 'wb').write(https.content)
open('socks4.txt', 'wb').write(socks4.content)
open('socks5.txt', 'wb').write(socks5.content)

contador = 0

while contador != 3:
	http = requests.get("https://www.proxyscan.io/api/proxy?limit=15&type=http&format=txt")
	https = requests.get("https://www.proxyscan.io/api/proxy?limit=15&type=https&format=txt")
	socks4= requests.get("https://www.proxyscan.io/api/proxy?limit=15&type=socks4&format=txt")
	socks5 = requests.get("https://www.proxyscan.io/api/proxy?limit=15&type=socks5&format=txt")

	with open("http.txt", 'ab') as f:
	    f.write(http.content)
	with open("https.txt", 'ab') as f:
	    f.write(https.content)
	with open("socks4.txt", 'ab') as f:
	    f.write(socks4.content)
	with open("socks5.txt", 'ab') as f:
	    f.write(socks5.content)
	contador = contador +1 


# r = requests.post('https://api.telegram.org/bot'+TOKEN+'/sendMessage', data={'chat_id': CID, 'text': "Los proxys se actualizaran cada 5 minutos"}) 
# open('status.json', 'wb').write(r.content)
# f = open('status.json')
# json_file = json.load(f)
# json_str = json.dumps(json_file)
# resp = json.loads(json_str)

# last_message = resp['result']['message_id']



# file = open('http.txt', 'rb')
# bot.send_document(CID, file)

# file = open('https.txt', 'rb')
# bot.send_document(CID, file)

# file = open('socks5.txt', 'rb')
# bot.send_document(CID, file)

# file = open('socks4.txt', 'rb')
# bot.send_document(CID, file)

# try:
# 	bot.delete_message(CID, last_message -1)
# 	bot.delete_message(CID, last_message -2)
# 	bot.delete_message(CID, last_message -3)
# 	bot.delete_message(CID, last_message -4)
# 	bot.delete_message(CID, last_message -5)
# except:
# 	print("NO HAY NADA QUE BORRAR")

	
# print("FIN")
