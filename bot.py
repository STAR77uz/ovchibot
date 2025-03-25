import os
import time
import asyncio
from dotenv import load_dotenv
from telethon import TelegramClient, events

# .env faylidan ma'lumotlarni yuklash
load_dotenv()
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")

# Telegram Client yaratish
client = TelegramClient("ovchibot", API_ID, API_HASH)

print("Bot ishga tushdi! 🟢")

# Ovga chiqish va tugmani bosish
async def hunt():
    chat = "@JangUzBot"  # To‘g‘ri botga yozishi uchun yangilandi
    await client.send_message(chat, "Bo'rilarga ovga chiqish🐺")  # 1-qadam: Xabar yuborish
    await asyncio.sleep(5)  # Xabar yuborilgach, 5 soniya kutish

    async for message in client.iter_messages(chat, limit=10):  # Oxirgi 10ta xabarni tekshiramiz
        if message.buttons:  # Tugmalar borligini tekshirish
            for row in message.buttons:
                for button in row:
                    if button.text == "Bo'rilarni ovlashni boshlash💰":  # Tugma matni to‘g‘ri yozildi
                        await button.click()  # 2-qadam: Tugmani bosish
                        print("Tugma bosildi! ✅")
                        return  # Tugmani bosgandan keyin chiqish

    print("Tugma topilmadi! ❌")  # Agar tugma bo‘lmasa

# Har 13 daqiqada ov qilish
async def auto_hunt():
    while True:
        await hunt()
        print("13 daqiqa kutamiz... 🕒")
        await asyncio.sleep(780)  # 13 daqiqa = 780 soniya

# Botni ishga tushirish
with client:
    client.loop.run_until_complete(auto_hunt())
