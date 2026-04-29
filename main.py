
import telebot
import google.generativeai as genai
import os

# Kalitlar
TOKEN = "8724375286:AAGmkMhqOHRsf72avH0RZ0n__ij5Lg8DRGA"
GEMINI_KEY = "AIzaSyDxVkjW4Fl-7cBIjRksAgl3lhvVkPsq3YQ"

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
bot = telebot.TeleBot(TOKEN)
chat_sessions = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Assalomu alaykum! Men aqlli AI botman. Savolingizni bering.")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.chat.id
    if user_id not in chat_sessions:
        chat_sessions[user_id] = model.start_chat(history=[])
    try:
        response = chat_sessions[user_id].send_message(message.text)
        bot.reply_to(message, response.text)
    except:
        bot.reply_to(message, "Xatolik yuz berdi. Birozdan so'ng urinib ko'ring.")

bot.infinity_polling()
