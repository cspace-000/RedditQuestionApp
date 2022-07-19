import json
import os


with open('../../keys.txt' , 'r') as f:
    keys = json.loads(f.read())


client_id = keys['client_id']
client_secret = keys['client_secret']
password = keys['password']
username = keys['username']
user_agent = keys['user_agent']