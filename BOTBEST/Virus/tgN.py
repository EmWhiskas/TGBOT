import os
# Импорт необходимых библиотек
import telebot
import telebot as bot
from telebot import types
import requests
import datetime
# Импорт необходимых зависимостей
import CheckDateSheets1
import CheckDateSheets2
import ALL
import ALL2
import Zamen
import Day
import settings
smscount = 0
bot = telebot.TeleBot(settings.BotApi)
Smile_stident = '👨‍🎓'
Smile_palec = '👇'
Smile_glaza = '👀'
bold = "parse_mode='HTML'"
daysOfWeek = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
day = ''
IsZamen = False # Для переключения кнопок
IsAll = False # Для переключения кнопок



def read_unique_ids(msg):
    unique_ids = set()
    with open('bd.txt', 'r') as file:
        for line in file:
            # Удаление пробельных символов и переносов строки
            id = line.strip()
            # Добавление id в множество, если строка не пустая
            if id:
                unique_ids.add(id)
    # Преобразование множества в список для возможного дальнейшего использования
    text = msg.text.replace('глобальное сообщение ', '<b>Глобальное сообщение\n</b>')
    for one in unique_ids:
        global smscount
        try:
            bot.send_message(one, text, parse_mode='HTML')
            smscount += 1
        except:
            pass
    globalsms = f'Всего отправленно {smscount} людям'
    bot.send_message(824176864, globalsms)

def zamenGen2(msg, liter):
    today = datetime.date.today()
    weekday = today.weekday()
    weekday_name = daysOfWeek[weekday]
    bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')
    if weekday_name == 'Понедельник':
        attribute_name = 'Понедельник' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)
    elif weekday_name == 'Вторник':
        attribute_name = 'Вторник' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)
    elif weekday_name == 'Среда':
        attribute_name = 'Среда' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)
    elif weekday_name == 'Четверг':
        attribute_name = 'Четверг' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)
    elif weekday_name == 'Пятница':
        attribute_name = 'Пятница' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)
    elif weekday_name == 'Суббота':
        attribute_name = 'Понедельник' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)
    elif weekday_name == 'Воскресенье':
        attribute_name = 'Понедельник' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)

    Day.clear()
    pol = Day.main(SAMPLE_RANGE_NAME)
    for i in range(len(pol)):
        ress = '\n'.join(pol)

    bot.send_message(msg.chat.id, 'Жду ответа⏳')
    SAMPLE_RANGE_NAME = settings.Замены6А
    Zamen.clear()
    zam = Zamen.main(SAMPLE_RANGE_NAME)
    for i in range(len(zam)):
        resss = '\n'.join(zam)

    bot.send_message(msg.chat.id, 'Ответ получен✅')

    CheckDateSheets2.clear()
    today = CheckDateSheets2.main()
    try:
        for i in range(len(today)):
            ressss = '\n'.join(today)
            ressss = f"<b>{ressss}</b>"
    except:
        ressss = f"<i>Ошибка в поиске даты</i>"

    if weekday_name != 'Суббота' and weekday_name != 'Воскресенье':
        if weekday_name != 'Четверг' and weekday_name != 'Понедельник' and weekday_name != 'Вторник':
            tDay = weekday_name[:-1] + 'у'
        else:
            tDay = weekday_name
    else:
        tDay = 'Понедельник'
    zamen = f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{ressss} \n\n{resss}'
    bot.send_message(msg.chat.id, zamen, parse_mode='HTML')
    keys(msg)


def fullGen2(msg, SAMPLE_RANGE_NAME):
    ALL2.clear()
    res = ALL2.main(SAMPLE_RANGE_NAME)
    for i in range(len(res)):
        ress = '\n'.join(res)
    bot.send_message(msg.chat.id, ress, parse_mode='HTML')
    keys(msg)

def fullGen(msg, SAMPLE_RANGE_NAME):
    ALL.clear()

    res = ALL.main(SAMPLE_RANGE_NAME)
    for i in range(len(res)):
        ress = '\n'.join(res)
    bot.send_message(msg.chat.id, ress, parse_mode='HTML')
    keys(msg)

def zamenGen(msg, liter):
    today = datetime.date.today()  # получает текущую дату
    weekday = today.weekday()  # Достает день недели
    weekday_name = daysOfWeek[weekday]  # Берет название дня недели
    bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')
    if weekday_name == 'Понедельник':
        attribute_name = 'Понедельник' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)
    elif weekday_name == 'Вторник':
        attribute_name = 'Вторник' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)
    elif weekday_name == 'Среда':
        attribute_name = 'Среда' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)
    elif weekday_name == 'Четверг':
        attribute_name = 'Четверг' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)
    elif weekday_name == 'Пятница':
        attribute_name = 'Пятница' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)
    elif weekday_name == 'Суббота':
        attribute_name = 'Понедельник' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)
    elif weekday_name == 'Воскресенье':
        attribute_name = 'Понедельник' + liter
        SAMPLE_RANGE_NAME = getattr(settings, attribute_name)

    Day.clear()
    pol = Day.main(SAMPLE_RANGE_NAME)  # Получает полное расписание на этот день недели
    for i in range(len(pol)):
        ress = '\n'.join(pol)

    bot.send_message(msg.chat.id, 'Жду ответа⏳')
    attribute_name = 'Замены' + liter
    SAMPLE_RANGE_NAME = getattr(settings, attribute_name)
    Zamen.clear()
    zam = Zamen.main(SAMPLE_RANGE_NAME)  # Получает измененное расписание на этот день недели
    for i in range(len(zam)):
        resss = '\n'.join(zam)

    bot.send_message(msg.chat.id, 'Ответ получен✅')
    CheckDateSheets1.clear()
    today = CheckDateSheets1.main()  # Чтобы не запутаться берет дату, на которое сделано изменение
    try:
        for i in range(len(today)):
            ressss = '\n'.join(today)
            ressss = f"<b>{ressss}</b>"
    except:
        ressss = f"<i>Ошибка в поиске даты</i>"  # Все мы люди и можем ошибаться и не написать дату, а это позволит избежать критической ошибки

    if weekday_name != 'Суббота' and weekday_name != 'Воскресенье':
        if weekday_name != 'Четверг' and weekday_name != 'Понедельник' and weekday_name != 'Вторник':
            tDay = weekday_name[:-1] + 'у'
        else:
            tDay = weekday_name
    else:
        tDay = 'Понедельник'
    zamen = f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{ressss} \n\n{resss}'
    bot.send_message(msg.chat.id, zamen, parse_mode='HTML')
    keys(msg)

def catGen(msg):
    url = "https://cat14.p.rapidapi.com/v1/images/search"

    headers = {
        "x-api-key": "live_tkfn5Qu13T9qimIfGmAxBAFooC12t7GvENwLXIoJQRTgUv83zQ8mjz5cSpzahmyK",
        "X-RapidAPI-Key": "c50c02fb65msh3b35b9a0adb8463p13826fjsn3118fa23ceef",
        "X-RapidAPI-Host": "cat14.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.json())
    catJs = response.json()
    bot.send_photo(msg.chat.id, catJs[0]['url'])


@bot.message_handler(content_types=['video'])
def message(info):
    print(info)

@bot.message_handler(commands=['start', 'help'])
def keys(info):
    global IsAll, IsZamen
    kb = types.ReplyKeyboardMarkup(row_width=2)
    but1 = types.KeyboardButton('Полное расписание')
    but2 = types.KeyboardButton('Изменения')
    but3 = types.KeyboardButton('Покажи кота😼')
    kb.add(but1, but2, but3)
    bot.send_message(info.chat.id, 'Привет😘', reply_markup = kb)
    IsAll = False
    IsZamen = False

@bot.message_handler(func=lambda msg: msg.text == 'Полное расписание')
def numb(info):
    global IsAll
    kb = types.ReplyKeyboardMarkup(row_width=5)
    but1 = types.KeyboardButton('5А')
    but2 = types.KeyboardButton('5Б')
    but3 = types.KeyboardButton('5В')
    but33 = types.KeyboardButton('5Г')
    but4 = types.KeyboardButton('5Д')
    but5 = types.KeyboardButton('6А')
    but6 = types.KeyboardButton('6Б')
    but7 = types.KeyboardButton('6В')
    but8 = types.KeyboardButton('6Г')
    but9 = types.KeyboardButton('7А')
    but10 = types.KeyboardButton('7Б')
    but11 = types.KeyboardButton('7В')
    but12 = types.KeyboardButton('7Г')
    but13 = types.KeyboardButton('8А')
    but14 = types.KeyboardButton('8Б')
    but15 = types.KeyboardButton('8В')
    but16 = types.KeyboardButton('8Г')
    but17 = types.KeyboardButton('9А')
    but18 = types.KeyboardButton('9Б')
    but19 = types.KeyboardButton('9В')
    but20 = types.KeyboardButton('9Г')
    but21 = types.KeyboardButton('10А')
    but22 = types.KeyboardButton('10Б')
    but23 = types.KeyboardButton('11А')
    but24 = types.KeyboardButton('11Б')
    but25 = types.KeyboardButton('Назад')
    kb.add(but1, but2, but3, but33, but4)  # Первая строка с 5 кнопками 5Д вы лучшие 😘😘😘😘😘😘😘😘😘😘😘😘😘
    kb.add(but5, but6, but7, but8)
    kb.add(but9, but10, but11, but12)
    kb.add(but13, but14, but15, but16)
    kb.add(but17, but18, but19, but20)
    kb.add(but21, but22, but23, but24)
    kb.add(but25)
    bot.send_message(info.chat.id, 'Выбирай класс', reply_markup = kb)
    IsAll = True

@bot.message_handler(func=lambda msg: msg.text == 'Изменения')
def numbb(info):
    global IsZamen
    kb = types.ReplyKeyboardMarkup(row_width=5)
    but1 = types.KeyboardButton('5А')
    but2 = types.KeyboardButton('5Б')
    but3 = types.KeyboardButton('5В')
    but33 = types.KeyboardButton('5Г')
    but4 = types.KeyboardButton('5Д')
    but5 = types.KeyboardButton('6А')
    but6 = types.KeyboardButton('6Б')
    but7 = types.KeyboardButton('6В')
    but8 = types.KeyboardButton('6Г')
    but9 = types.KeyboardButton('7А')
    but10 = types.KeyboardButton('7Б')
    but11 = types.KeyboardButton('7В')
    but12 = types.KeyboardButton('7Г')
    but13 = types.KeyboardButton('8А')
    but14 = types.KeyboardButton('8Б')
    but15 = types.KeyboardButton('8В')
    but16 = types.KeyboardButton('8Г')
    but17 = types.KeyboardButton('9А')
    but18 = types.KeyboardButton('9Б')
    but19 = types.KeyboardButton('9В')
    but20 = types.KeyboardButton('9Г')
    but21 = types.KeyboardButton('10А')
    but22 = types.KeyboardButton('10Б')
    but23 = types.KeyboardButton('11А')
    but24 = types.KeyboardButton('11Б')
    but25 = types.KeyboardButton('Назад')
    kb.add(but1, but2, but3, but33, but4)  # Первая строка с 5 кнопками 5Д вы лучшие 😘😘😘😘😘😘😘😘😘😘😘😘😘
    kb.add(but5, but6, but7, but8)
    kb.add(but9, but10, but11, but12)
    kb.add(but13, but14, but15, but16)
    kb.add(but17, but18, but19, but20)
    kb.add(but21, but22, but23, but24)
    kb.add(but25)
    bot.send_message(info.chat.id, 'Выбирай класс', reply_markup = kb)
    IsZamen = True

def nokeys(info):
    bot.send_message(info.chat.id, 'Убрал клавиаутру', reply_markup = types.ReplyKeyboardRemove())

def compare_and_write_data(data):
    data = str(data)
    with open('bd.txt', 'r') as file:
        existing_data = file.read().splitlines()

    new_data = []

    for value in data:
        if value not in existing_data:
            new_data.append(value)

    if new_data:
        with open('bd.txt', 'a') as file:
            file.write(''.join(new_data) + '\n')

def write_data(data):
    with open('messages.txt', 'a') as file:
        file.write(''.join(data) + '\n')

@bot.message_handler(content_types=['text'])
def message(msg):
    global day, weekday_name, tDay, ress, catt
    inf = f'{msg.text} Автор: {msg.chat.id}'
    try:
        write_data(inf)
    except:
        print('Ошибка записи')

    try:
        compare_and_write_data(msg.chat.id)
    except:
        print('Ошибка записи')

    msg.text = msg.text.lower()
    print(msg.text, 'Автор:', msg.chat.id)
    if 'привет' in msg.text:
        bot.send_message(msg.chat.id, msg.text)

    elif 'глобальное сообщение' in msg.text:
        read_unique_ids(msg)

    elif 'пришли бд' in msg.text:
        bot.send_document(824176864, open('bd.txt', 'rb'))

    elif 'пришли смс' in msg.text:
        bot.send_document(824176864, open('messages.txt', 'rb'))

    elif 'заканчиваем' in msg.text:
        settings.BotApi = '6331392580:AAHu804LMDy1zpxEvmNpNSvpfmM6XkuOuI0'

    elif 'назад' in msg.text:
        keys(msg)

    elif 'убери клавиатуру' in msg.text:
        nokeys(msg)

    elif 'покажи кота😼' in msg.text:
        catGen(msg)

    elif 'расписание 5а' in msg.text or (IsAll == True and '5а' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание5А
        fullGen(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 5а' in msg.text or (IsZamen == True and '5а' in msg.text):
        liter = '5А'
        zamenGen(msg, liter)


    elif 'расписание 5б' in msg.text or (IsAll == True and '5б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание5Б
        fullGen(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 5б' in msg.text or (IsZamen == True and '5б' in msg.text):
        liter = '5Б'
        zamenGen(msg, liter)

    elif 'расписание 5в' in msg.text or (IsAll == True and '5в' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание5В
        fullGen(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 5в' in msg.text or (IsZamen == True and '5в' in msg.text):
        liter = '5В'
        zamenGen(msg, liter)

    elif 'расписание 5г' in msg.text or (IsAll == True and '5г' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание5Г
        fullGen(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 5г' in msg.text or (IsZamen == True and '5г' in msg.text):
        liter = '5Г'
        zamenGen(msg, liter)

    elif 'расписание 5д' in msg.text or (IsAll == True and '5д' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание5Д
        fullGen(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 5д' in msg.text or (IsZamen == True and '5д' in msg.text):
        liter = '5Д'
        zamenGen(msg, liter)

    elif 'расписание 6а' in msg.text or (IsAll == True and '6а' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание6А
        fullGen2(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 6а' in msg.text or (IsZamen == True and '6а' in msg.text):
        liter = '6А'
        zamenGen2(msg, liter)

    elif 'расписание 6б' in msg.text or (IsAll == True and '6б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание6Б
        fullGen2(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 6б' in msg.text or (IsZamen == True and '6б' in msg.text):
        liter = '6Б'
        zamenGen2(msg, liter)

    elif 'расписание 6в' in msg.text or (IsAll == True and '6в' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание6В
        fullGen2(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 6в' in msg.text or (IsZamen == True and '6в' in msg.text):
        liter = '6В'
        zamenGen2(msg, liter)

    elif 'расписание 6г' in msg.text or (IsAll == True and '6г' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание6Г
        fullGen2(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 6г' in msg.text or (IsZamen == True and '6г' in msg.text):
        liter = '6Г'
        zamenGen2(msg, liter)

    elif 'расписание 7а' in msg.text or (IsAll == True and '7а' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание7А
        fullGen2(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 7а' in msg.text or (IsZamen == True and '7а' in msg.text):
        liter = '7А'
        zamenGen2(msg, liter)

    elif 'расписание 7б' in msg.text or (IsAll == True and '7б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание7Б
        fullGen2(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 7б' in msg.text or (IsZamen == True and '7б' in msg.text):
        liter = '7Б'
        zamenGen2(msg, liter)

    elif 'расписание 7в' in msg.text or (IsAll == True and '7в' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание7В
        fullGen2(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 7в' in msg.text or (IsZamen == True and '7в' in msg.text):
        liter = '7В'
        zamenGen2(msg, liter)

    elif 'расписание 7г' in msg.text or (IsAll == True and '7г' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание7Г
        fullGen2(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 7г' in msg.text or (IsZamen == True and '7г' in msg.text):
        liter = '7Г'
        zamenGen2(msg, liter)

    elif 'расписание 8а' in msg.text or (IsAll == True and '8а' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание8А
        fullGen2(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 8а' in msg.text or (IsZamen == True and '8а' in msg.text):
        liter = '8А'
        zamenGen2(msg, liter)

    elif 'расписание 8б' in msg.text or (IsAll == True and '8б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание8Б
        fullGen2(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 8б' in msg.text or (IsZamen == True and '8б' in msg.text):
        liter = '8Б'
        zamenGen2(msg, liter)

    elif 'расписание 8в' in msg.text or (IsAll == True and '8в' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание8В
        fullGen2(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 8в' in msg.text or (IsZamen == True and '8в' in msg.text):
        liter = '8В'
        zamenGen2(msg, liter)

    elif 'расписание 8г' in msg.text or (IsAll == True and '8г' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание8Г
        fullGen2(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 8г' in msg.text or (IsZamen == True and '8г' in msg.text):
        liter = '8Г'
        zamenGen2(msg, liter)

    elif 'расписание 9а' in msg.text or (IsAll == True and '9а' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание9А
        fullGen(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 9а' in msg.text or (IsZamen == True and '9а' in msg.text):
        liter = '9А'
        zamenGen(msg, liter)

    elif 'расписание 9б' in msg.text or (IsAll == True and '9б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание9Б
        fullGen(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 9б' in msg.text or (IsZamen == True and '9б' in msg.text):
        liter = '9Б'
        zamenGen(msg, liter)

    elif 'расписание 9в' in msg.text or (IsAll == True and '9в' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание9В
        fullGen(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 9в' in msg.text or (IsZamen == True and '9в' in msg.text):
        liter = '9В'
        zamenGen(msg, liter)

    elif 'расписание 9г' in msg.text or (IsAll == True and '9г' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание9Г
        fullGen(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 9г' in msg.text or (IsZamen == True and '9г' in msg.text):
        liter = '9Г'
        zamenGen(msg, liter)

    elif 'расписание 10а' in msg.text or (IsAll == True and '10а' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание10А
        fullGen(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 10а' in msg.text or (IsZamen == True and '10а' in msg.text):
        liter = '10А'
        zamenGen(msg, liter)

    elif 'расписание 10б' in msg.text or (IsAll == True and '10б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание10Б
        fullGen(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 10б' in msg.text or (IsZamen == True and '10б' in msg.text):
        liter = '10Б'
        zamenGen(msg, liter)

    elif 'расписание 11а' in msg.text or (IsAll == True and '11а' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание11А
        fullGen(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 11а' in msg.text or (IsZamen == True and '11а' in msg.text):
        liter = '11А'
        zamenGen(msg, liter)

    elif 'расписание 11б' in msg.text or (IsAll == True and '11б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание11Б
        fullGen(msg, SAMPLE_RANGE_NAME)

    elif 'изменения 11б' in msg.text or (IsZamen == True and '11б' in msg.text):
        liter = '11Б'
        zamenGen(msg, liter)

    else:
        bot.send_message(msg.chat.id, 'Не распознал сообщение')
bot.infinity_polling()