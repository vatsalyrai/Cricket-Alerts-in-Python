import requests
import json
api_key="use your api key"
url = "https://cricapi.com/api/matches?apikey="+api_key


response = requests.get(url)

data = response.json()

uid = str(data["matches"][3]["unique_id"])



url ="https://cricapi.com/api/cricketScore?apikey="+api_key"&unique_id="+uid
response = requests.get(url)

data = response.json()

score = data["score"]

print(score)  # if score key not found means the match hasn't started

      

# importing all required libraries
import telebot
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events


# get your api_id, api_hash, token
# from telegram 
api_id = 'use your api id'
api_hash = 'use your api hash'
token = 'use your acess token'

# your phone number
phone = 'use your phone number'

# creating a telegram session and assigning
# it to a variable client
client = TelegramClient('session', api_id, api_hash)

# connecting and building the session
client.connect()
participants=[]

# in case of script ran first time it will
# ask either to input token or otp sent to
# number or sent or your telegram id
if not client.is_user_authorized():

	client.send_code_request(phone)
	
	# signing in the client
	client.sign_in(phone, input('Enter the code: '))


try:
	# receiver user_id and access_hash, use
	# my user_id and access_hash for reference
	participants = client.get_participants('enter user name of reciever in here')
	print(participants)
	#a_hash = participants.access_hash
	receiver = InputPeerUser(1xx3x02x28,3x1xxx9x6xx5x2x1x)

	# sending message using telegram client
	client.send_message(receiver, score, parse_mode='html')
except Exception as e:
	
	# there may be many error coming in while like peer
	# error, wwrong access_hash, flood_error, etc
	print(e);

# disconnecting the telegram session
client.disconnect()

