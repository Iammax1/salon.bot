import os
import requests
import time

TOKEN = os.environ.get("BOT_TOKEN")
URL = f"https://api.telegram.org/bot{TOKEN}/"

def get_updates(offset=None):
    params = {"timeout": 30, "offset": offset}
    r = requests.get(URL + "getUpdates", params=params)
    return r.json()

def send_message(chat_id, text):
    requests.post(URL + "sendMessage", data={"chat_id": chat_id, "text": text})

print("Бот запущен!")
offset = None
while True:
    updates = get_updates(offset)
    for update in updates.get("result", []):
        offset = update["update_id"] + 1
        msg = update.get("message", {})
        if msg.get("text") == "/start":
            send_message(msg["chat"]["id"], "Привет! Добро пожаловать в салон! 💅")
    time.sleep(1)
