import requests
import datetime
import time

tokens = ["YOUR_TOKEN_1", "YOUR_TOKEN_2", "YOUR_TOKEN_3"]

def update_status(token, status):
    url = 'https://discord.com/api/v9/users/@me/settings'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    data = {'status': status}
    response = requests.patch(url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"Status updated to {status} for token ending in ...{token[-4:]}")
    else:
        print(f"Failed to update status for token ending in ...{token[-4:]}. Response: {response.status_code}")

while True:
    now = datetime.datetime.now()
    hour = now.hour

    if 21 <= hour or hour < 5:
        status = "idle"  
    elif 5 <= hour < 12:
        status = "dnd"  
    else:
        status = "online"

    for token in tokens:
        update_status(token, status)
        
    time.sleep(300)
