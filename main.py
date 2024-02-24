import requests
import datetime
import time

token = 'Your_Discord_Token'

def update_status(status):
    url = "https://discord.com/api/v9/users/@me/settings"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
    }
    json_data = {
        "custom_status": {"text": status}
    }
    response = requests.patch(url, headers=headers, json=json_data)
    print(f"Status updated to: {status}, Response: {response.status_code}")

while True:
    now = datetime.datetime.now()
    hour = now.hour
    
    if 21 <= hour or hour < 5:
        update_status("退席中")
    elif 5 <= hour < 12:
        update_status("取り込み中")
    else:
        update_status("オンライン")
    
    time.sleep(3600)
