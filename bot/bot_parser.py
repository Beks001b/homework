import telebot
from bs4 import BeautifulSoup as bs
import requests

bot = telebot.TeleBot('7548138178:AAGT5yKSRmMc_mS8cAYejxioFbYwGnAoJsU')

keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
button1 = telebot.types.KeyboardButton('Ноутбуки')
button2 = telebot.types.KeyboardButton('Телефоны')
keyboard.add(button1, button2)

@bot.message_handler(commands=['start'])
def start_message(message):
    message2 = bot.send_message(message.chat.id, 'Привет могу спарсить', reply_markup=keyboard)
    bot.register_next_step_handler(message2, handler)
    
@bot.message_handler(content_types=['text'])
def handler(message):
    if message.text.lower() == 'телефоны':
        parsing('https://www.kivano.kg/mobilnye-telefony', message)
    elif message.text.lower() == 'ноутбуки':
        parsing('https://www.kivano.kg/noutbuki-i-kompyutery', message) 
    else:
        bot.send_message(message.chat.id, 'Нажми на кнопку', reply_markup=keyboard)
        
        
def parsing(url, message):
    html = requests.get(url).text
    soup = bs(html, 'lxml')
    print(soup, '+++++++++++++')
    telephones = soup.find_all('div', class_='item product_listbox oh' )
    coint = 1
    for telephone in telephones:
        link = 'https://www.kivano.kg' + telephone.find('a').get('href')
        title = telephone.find('img').get('alt')
        price = telephone.find('div', class_="listbox_price text-center").text
        bot.send_message(message.chat.id, f'ноутбуки - {title}\nСсылка - {link}\nЦена - {price}')
        count += 1
    
    
    
   
bot.polling(non_stop=True, interval=0)