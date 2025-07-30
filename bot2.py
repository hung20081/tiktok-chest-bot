from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import GiftEvent
import requests

client = TikTokLiveClient(unique_id="tên_tài_khoản_live")

TELEGRAM_TOKEN = "your_telegram_token"
TELEGRAM_CHAT_ID = "your_chat_id"

def send_telegram_message(message):
    requests.get(f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage?chat_id={TELEGRAM_CHAT_ID}&text={message}")

@client.on("gift")
async def on_gift(event: GiftEvent):
    if event.gift.info.name in ["Rương kho báu", "Treasure Box"]:
        send_telegram_message(f"🎁 Có rương trong live @{event.user.unique_id}!")

client.run()
