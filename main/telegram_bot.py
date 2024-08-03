# Python
import os
import asyncio
import pytz
import telegram

# Django
import django
from django.conf import settings

# Project
from main.models import EmailMessage

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

TOKEN = settings.TELEGRAM_TOKEN
chat_id = settings.TELEGRAM_GROUPS_ID


def send_msg_to_group(data: dict, obj: EmailMessage) -> None:
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    tashkent_tz = pytz.timezone('Asia/Tashkent')
    tashkent_time = obj.created_date.astimezone(tashkent_tz)
    formatted_date = tashkent_time.strftime("%d:%m:%Y %H:%M:%S")
    msg = (f"✅Статус: Успешно\n\n "
           f"📩№ Сообщения: {obj.id}\n"
           f"⏱Время: {formatted_date}\n\n"
           f"📌Названия: {data['name']}\n\n"
           f"👤Отправитель:  {data['sender']}\n\n"
           f"💌Тема: {data['subject']}\n\n"
           f"📄Сообщения: {data['message']}\n\n")
    bot = telegram.Bot(token=TOKEN)
    sent_msg = bot.sendMessage(chat_id=chat_id, text=msg)
    asyncio.run(sent_msg)
