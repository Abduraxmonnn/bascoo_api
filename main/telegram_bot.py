import requests
import os
import pytz
import telegram
from dotenv import load_dotenv

# Django
import django

# Project
from main.models import EmailMessage

load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

TOKEN = os.getenv('TELEGRAM_TOKEN')
request_url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"


def get_group_chat_ids() -> list:
    data = []
    response = requests.get(request_url).json()
    for item in response['result']:
        chat_members = item.get('my_chat_member', None)
        if chat_members is not None:
            data.append(chat_members['chat']['id'])
    return data


async def send_msg_to_group(data: dict, obj: EmailMessage):
    try:
        tashkent_tz = pytz.timezone('Asia/Tashkent')
        tashkent_time = obj.created_date.astimezone(tashkent_tz)
        formatted_date = tashkent_time.strftime("%d:%m:%Y %H:%M:%S")
        msg = (f"✅Статус: Успешно\n\n "
               f"📩№ Сообщения: {obj.id}\n"
               f"⏱Время: {formatted_date}\n\n"
               f"📌Названия: {data['name']}\n\n"
               f"👤Отправитель:  {data['sender']}\n\n"
               f"💌Тема: {data['subject']}\n\n"
               f"📄Сообщения: {data['message']}\n\n")

        bot = telegram.Bot(token=TOKEN)
        chat_ids = get_group_chat_ids()

        for chat_id in chat_ids:
            try:
                await bot.sendMessage(chat_id=chat_id, text=msg)
            except Exception as e:
                print(f"Error sending message to chat_id {chat_id}: {e}")

    except Exception as e:
        print(f"General error sending message: {e}")
