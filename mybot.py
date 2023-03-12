import requests
from bs4 import BeautifulSoup as BS
import csv
import telebot
import telebot
from datetime import datetime
today = datetime.today()

token = '6074708790:AAHkgqO7GVMwtuT-51g8zzeKHNR2BPGglEY'
bot = telebot.TeleBot(token)


def get_news():
    url = 'https://kaktus.media/?lable=8&date='
    date = today.date()
    order = '&order=time'
    html = requests.get(url+str(date)+order)
    soup = BS(html.text, 'html.parser')
    news = soup.find('div',class_= 'Tag').find_all('div',class_='Tag--article')
    return news

@bot.message_handler(commands=['start'])
def send_news(message):
    news_list = get_news()
    for index, item in enumerate(news_list[:20], 1):
        image = item.find('a',class_='ArticleItem--image').find('img').get('data-src')
        p = item.find('a',class_='ArticleItem--name').text
        bot.send_message(message.chat.id, f"{index}. {p} - {image} ")
    bot.send_message(message.chat.id, 'some title news you can see Description of this news and Photo')
        
@bot.message_handler(commands=['quit'])
def send_goodbye(message):
    bot.send_message(message.chat.id, "До свидания")


@bot.message_handler(func=lambda message: True)
def send_news_description(message):
    try:
        news_id = int(message.text)
        print(f"news_id: {news_id}")
        news_list = get_news()
        if news_id <= 0 or news_id > 20:
            raise ValueError
        news = news_list[news_id - 1]
        title = news.find('a',class_='ArticleItem--name')
        photo = news.find('a',class_='ArticleItem--image').find('img').get('data-src')
        bot.send_message(message.chat.id, f"{title.text}\n\n{photo}\n\n")
    except ValueError:
        bot.send_message(message.chat.id, "Некорректный номер новости или id")

bot.polling()
