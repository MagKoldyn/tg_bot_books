import telebot
from sqlalchemy import select
from telebot.types import User as tgUser
from message_controller import MessageController
from models.user import User
bot = telebot.TeleBot('6715917523:AAEqJ6qZiD5ZyXGBRFsLbUi-Rrd0VbS4sgE')
from user_controller import UserController

@bot.message_handler(commands=['start'])
def get_start(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    horrors = telebot.types.KeyboardButton('Ужасы')
    detectives = telebot.types.KeyboardButton('Детективы')
    markup.add(horrors, detectives)

    bot.send_message(message.chat.id, 'Привет друг!', reply_markup=markup)


@bot.message_handler(commands=['menu'])
def get_menu(message):
    markup2 = telebot.types.InlineKeyboardMarkup()
    horrors = telebot.types.InlineKeyboardButton('Ужасы', url='https://dzen.ru')
    detectives = telebot.types.InlineKeyboardButton('Детективы', callback_data='Садовник')
    markup2.add(horrors, detectives)

    bot.send_message(message.chat.id, 'Привет друг!', reply_markup=markup2)

@bot.message_handler(commands=['test'])
def send_message(message):
    # bot.send_message(message.chat.id, message)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!')
@bot.message_handler(commands=['test1'])
def get_user(message):
    user_controller = UserController()
    user = user_controller.get_user_controller(message.from_user)
    bot.send_message(message.chat.id, f'Добрый день, {user}')

# @bot.message_handler(content_types=['text'])
# def text_handler(message):
#     if message.text.lower() == 'счастье':
#         bot.send_message(message.chat.id, 'Там, где нас нет')
#     else:
#         bot.send_message(message.chat.id, 'Не знаю такого')

@bot.message_handler(content_types=['text'])
def send_books_by_category(message):
    books = MessageController.get_book_by_categories(message.text)
    if len(books) == 0:
        bot.send_message(message.chat.id, 'В категории нет книг')
    else:
        bot.send_message(message.chat.id, f'В категории {message.text} книга {", ".join(books)}')


bot.infinity_polling()
