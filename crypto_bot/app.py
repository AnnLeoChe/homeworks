import telebot
from config import keys, TOKEN
from extensions import ConvertExaption, CryptoConverter


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def help(massage: telebot.types.Message):
    text = 'Привет!  Я Бот-Конвертер валют и я могу:  \n- Показать список доступных валют через команду /values \
    \n- Вывести конвертацию валюты через команду <имя валюты> <в какую валюту перевести> <количество переводимой валюты> '
    bot.reply_to(massage, text)


@bot.message_handler(commands=['help'])
def help(massage: telebot.types.Message):
    text = '- Показать список доступных валют через команду /values \
    \n- Вывести конвертацию валюты через команду <имя валюты> <в какую валюту перевести> <количество переводимой валюты> \
     \n Пример правильного ввода: \
      \n доллар рубль 100     '
    bot.reply_to(massage, text)


@bot.message_handler(content_types=['photo','document', 'audio', 'video' ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'я работаю только с текстом, список доступных команд /help')


@bot.message_handler(commands=['values'])
def values(massage: telebot.types.Message):
    text = 'доступные валюты:'
    for key in keys.keys():
        text='\n'.join((text, key, ))
    bot.reply_to(massage, text)

@bot.message_handler(content_types=['text',])
def convert(massage: telebot.types.Message):
    try:
        values = massage.text.split(' ')
        if len(values) != 3:
            raise ConvertExaption('неправильное количество введенных параметров, список доступных команд /help ')

        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertExaption as e:
        bot.reply_to(massage, f'ошибка пользователя \n{e}')
    except Exception as e:
        bot.reply_to(massage, f'Не удалось обработать команду \n{e}')
    else:
         text = f'Переводим {quote} в {base}\n{amount} {quote} = {total_base} {base}'
         bot.send_message(massage.chat.id, text)


bot.polling()