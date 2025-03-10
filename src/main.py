import telebot
import os
import emoji
import requests
from dotenv import load_dotenv


load_dotenv()
API_TOKEN = os.getenv('APIKEY')
bot = telebot.TeleBot(API_TOKEN)


def load_phrases(file_path):
    phrases_1 = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                phrases_1[key.strip()] = value.strip()
    return phrases_1


phrases = load_phrases('X:/ALLPyCharmProjects/TelegramBot1/phrases.txt')
text_for_main_start = phrases.get('text_for_main_start')


@bot.message_handler(commands=['start'])
def main_start(message):
    bot.send_message(message.chat.id, emoji.emojize(text_for_main_start))


@bot.message_handler(commands=['help'])
def help_user(message):
    bot.send_message(message.chat.id,
    f"Хули тебе надо от меня на этот раз?! Я всё про тебя знаю {message.from_user.first_name}, "
    f"даже твой ID - {message.from_user.id}!!! Так что не выёбывайся и быстрее задавай свой вопрос!!!")


# бот реагирует на то что ввел юзер
# @bot.message_handler()
# def info(message):
#     if message.text.lower() == '':
#         pass

bot.polling(none_stop=True)
