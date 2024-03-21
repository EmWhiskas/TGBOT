import os

import telebot
import telebot as bot
from telebot import types
import requests
import datetime
import CheckDateSheets1
import CheckDateSheets2
import ALL
import ALL2
import Zamen
import Day
import settings
catt = 1
bot = telebot.TeleBot(settings.BotApi)
Smile_stident = '👨‍🎓'
Smile_palec = '👇'
Smile_glaza = '👀'
bold = "parse_mode='HTML'"
daysOfWeek = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
day = ''
IsZamen = False
IsAll = False



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
        ALL.clear()

        res = ALL.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 5а' in msg.text or (IsZamen == True and '5а' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник5А
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник5А
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда5А
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг5А
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница5А
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник5А
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник5А

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены5А
        Zamen.clear()
        zam = Zamen.main(SAMPLE_RANGE_NAME)
        for i in range(len(zam)):
            resss = '\n'.join(zam)

        bot.send_message(msg.chat.id, 'Ответ получен✅')
        CheckDateSheets1.clear()
        today = CheckDateSheets1.main()
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)


    elif 'расписание 5б' in msg.text or (IsAll == True and '5б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание5Б
        ALL.clear()

        res = ALL.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 5б' in msg.text or (IsZamen == True and '5б' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник5Б
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник5Б
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда5Б
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг5Б
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница5Б
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник5Б
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник5Б

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены5Б
        Zamen.clear()
        zam = Zamen.main(SAMPLE_RANGE_NAME)
        for i in range(len(zam)):
            resss = '\n'.join(zam)

        bot.send_message(msg.chat.id, 'Ответ получен✅')

        CheckDateSheets1.clear()
        today = CheckDateSheets1.main()
        for i in range(len(today)):
            ressss = '\n'.join(today)
            ressss = f"<b>{ressss}</b>"

        if weekday_name != 'Суббота' and weekday_name != 'Воскресенье':
            if weekday_name != 'Четверг' and weekday_name != 'Понедельник' and weekday_name != 'Вторник':
                tDay = weekday_name[:-1] + 'у'
            else:
                tDay = weekday_name
        else:
            tDay = 'Понедельник'
        zamen = f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{ressss} \n\n{resss}'
        bot.send_message(msg.chat.id, zamen, parse_mode='HTML')

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 5в' in msg.text or (IsAll == True and '5в' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание5В
        ALL.clear()

        res = ALL.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 5в' in msg.text or (IsZamen == True and '5в' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник5В
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник5В
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда5В
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг5В
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница5В
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник5В
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник5В

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены5В
        Zamen.clear()
        zam = Zamen.main(SAMPLE_RANGE_NAME)
        for i in range(len(zam)):
            resss = '\n'.join(zam)

        bot.send_message(msg.chat.id, 'Ответ получен✅')

        CheckDateSheets1.clear()
        today = CheckDateSheets1.main()
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
        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 5г' in msg.text or (IsAll == True and '5г' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание5Г
        ALL.clear()

        res = ALL.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 5г' in msg.text or (IsZamen == True and '5г' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник5Г
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник5Г
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда5Г
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг5Г
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница5Г
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник5Г
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник5Г

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены5Г
        Zamen.clear()
        zam = Zamen.main(SAMPLE_RANGE_NAME)
        for i in range(len(zam)):
            resss = '\n'.join(zam)

        bot.send_message(msg.chat.id, 'Ответ получен✅')

        CheckDateSheets1.clear()
        today = CheckDateSheets1.main()
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


        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 5д' in msg.text or (IsAll == True and '5д' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание5Д
        ALL.clear()

        res = ALL.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 5д' in msg.text or (IsZamen == True and '5д' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник5Д
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник5Д
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда5Д
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг5Д
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница5Д
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник5Д
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник5Д

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены5Д
        Zamen.clear()
        zam = Zamen.main(SAMPLE_RANGE_NAME)
        for i in range(len(zam)):
            resss = '\n'.join(zam)

        bot.send_message(msg.chat.id, 'Ответ получен✅')

        CheckDateSheets1.clear()
        today = CheckDateSheets1.main()
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 6а' in msg.text or (IsAll == True and '6а' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание6А
        ALL2.clear()
        res = ALL2.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 6а' in msg.text or (IsZamen == True and '6а' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник6А
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник6А
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда6А
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг6А
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница6А
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник6А
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник6А

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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 6б' in msg.text or (IsAll == True and '6б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание6Б
        ALL2.clear()
        res = ALL2.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 6б' in msg.text or (IsZamen == True and '6б' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник6Б
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник6Б
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда6Б
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг6Б
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница6Б
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник6Б
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник6Б

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены6Б
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 6в' in msg.text or (IsAll == True and '6в' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание6В
        ALL2.clear()
        res = ALL2.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 6в' in msg.text or (IsZamen == True and '6в' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник6В
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник6В
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда6В
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг6В
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница6В
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник6В
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник6В

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены6В
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 6г' in msg.text or (IsAll == True and '6г' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание6Г
        ALL2.clear()
        res = ALL2.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 6г' in msg.text or (IsZamen == True and '6г' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник6Г
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник6Г
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда6Г
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг6Г
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница6Г
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник6Г
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник6Г

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены6Г
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 7а' in msg.text or (IsAll == True and '7а' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание7А
        ALL2.clear()
        res = ALL2.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 7а' in msg.text or (IsZamen == True and '7а' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник7А
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник7А
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда7А
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг7А
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница7А
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник7А
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник7А

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены7А
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 7б' in msg.text or (IsAll == True and '7б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание7Б
        ALL2.clear()
        res = ALL2.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 7б' in msg.text or (IsZamen == True and '7б' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник7Б
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник7Б
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда7Б
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг7Б
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница7Б
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник7Б
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник7Б

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены7Б
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 7в' in msg.text or (IsAll == True and '7в' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание7В
        ALL2.clear()
        res = ALL2.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 7в' in msg.text or (IsZamen == True and '7в' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник7В
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник7В
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда7В
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг7В
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница7В
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник7В
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник7В

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены7В
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 7г' in msg.text or (IsAll == True and '7г' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание7Г
        ALL2.clear()
        res = ALL2.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 7г' in msg.text or (IsZamen == True and '7г' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник7Г
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник7Г
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда7Г
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг7Г
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница7Г
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник7Г
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник7Г

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены7Г
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 8а' in msg.text or (IsAll == True and '8а' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание8А
        ALL2.clear()
        res = ALL2.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 8а' in msg.text or (IsZamen == True and '8а' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник8А
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник8А
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда8А
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг8А
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница8А
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник8А
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник8А

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены8А
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 8б' in msg.text or (IsAll == True and '8б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание8Б
        ALL2.clear()
        res = ALL2.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 8б' in msg.text or (IsZamen == True and '8б' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник8Б
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник8Б
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда8Б
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг8Б
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница8Б
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник8Б
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник8Б

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены8Б
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 8в' in msg.text or (IsAll == True and '8в' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание8В
        ALL2.clear()
        res = ALL2.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 8в' in msg.text or (IsZamen == True and '8в' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник8В
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник8В
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда8В
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг8В
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница8В
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник8В
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник8В

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены8В
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 8г' in msg.text or (IsAll == True and '8г' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание8Г
        ALL2.clear()
        res = ALL2.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 8г' in msg.text or (IsZamen == True and '8г' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник8Г
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник8Г
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда8Г
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг8Г
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница8Г
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник8Г
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник8Г

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены8Г
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 9а' in msg.text or (IsAll == True and '9а' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание9А
        ALL.clear()

        res = ALL.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 9а' in msg.text or (IsZamen == True and '9а' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник9А
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник9А
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда9А
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг9А
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница9А
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник9А
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник9А

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены9А
        Zamen.clear()
        zam = Zamen.main(SAMPLE_RANGE_NAME)
        for i in range(len(zam)):
            resss = '\n'.join(zam)

        bot.send_message(msg.chat.id, 'Ответ получен✅')

        CheckDateSheets1.clear()
        today = CheckDateSheets1.main()
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 9б' in msg.text or (IsAll == True and '9б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание9Б
        ALL.clear()

        res = ALL.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 9б' in msg.text or (IsZamen == True and '9б' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник9Б
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник9Б
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда9Б
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг9Б
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница9Б
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник9Б
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник9Б

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены9Б
        Zamen.clear()
        zam = Zamen.main(SAMPLE_RANGE_NAME)
        for i in range(len(zam)):
            resss = '\n'.join(zam)

        bot.send_message(msg.chat.id, 'Ответ получен✅')

        CheckDateSheets1.clear()
        today = CheckDateSheets1.main()
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 9в' in msg.text or (IsAll == True and '9в' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание9В
        ALL.clear()

        res = ALL.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 9в' in msg.text or (IsZamen == True and '9в' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник9В
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник9В
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда9В
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг9В
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница9В
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник9В
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник9В

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены9В
        Zamen.clear()
        zam = Zamen.main(SAMPLE_RANGE_NAME)
        for i in range(len(zam)):
            resss = '\n'.join(zam)

        bot.send_message(msg.chat.id, 'Ответ получен✅')

        CheckDateSheets1.clear()
        today = CheckDateSheets1.main()
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 9г' in msg.text or (IsAll == True and '9г' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание9Г
        ALL.clear()

        res = ALL.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 9г' in msg.text or (IsZamen == True and '9г' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник9Г
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник9Г
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда9Г
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг9Г
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница9Г
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник9Г
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник9Г

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены9Г
        Zamen.clear()
        zam = Zamen.main(SAMPLE_RANGE_NAME)
        for i in range(len(zam)):
            resss = '\n'.join(zam)

        bot.send_message(msg.chat.id, 'Ответ получен✅')

        CheckDateSheets1.clear()
        today = CheckDateSheets1.main()
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 10а' in msg.text or (IsAll == True and '10а' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание10А
        ALL.clear()

        res = ALL.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 10а' in msg.text or (IsZamen == True and '10а' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник10А
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник10А
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда10А
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг10А
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница10А
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник10А
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник10А

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены10А
        Zamen.clear()
        zam = Zamen.main(SAMPLE_RANGE_NAME)
        for i in range(len(zam)):
            resss = '\n'.join(zam)

        bot.send_message(msg.chat.id, 'Ответ получен✅')

        CheckDateSheets1.clear()
        today = CheckDateSheets1.main()
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

        video = Zamen.s
        bot.send_video(msg.chat.id, video)
        keys(msg)

    elif 'расписание 10б' in msg.text or (IsAll == True and '10б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание10Б
        ALL.clear()

        res = ALL.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 10б' in msg.text or (IsZamen == True and '10б' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник10Б
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник10Б
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда10Б
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг10Б
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница10Б
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник10Б
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник10Б

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены10Б
        Zamen.clear()
        zam = Zamen.main(SAMPLE_RANGE_NAME)
        for i in range(len(zam)):
            resss = '\n'.join(zam)

        bot.send_message(msg.chat.id, 'Ответ получен✅')

        CheckDateSheets1.clear()
        today = CheckDateSheets1.main()
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 11а' in msg.text or (IsAll == True and '11а' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание11А
        ALL.clear()

        res = ALL.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 11а' in msg.text or (IsZamen == True and '11а' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник11А
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник11А
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда11А
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг11А
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница11А
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник11А
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник11А

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = 'Расписание замен 1 смены!Y3:Z10'
        Zamen.clear()
        zam = Zamen.main(SAMPLE_RANGE_NAME)
        for i in range(len(zam)):
            resss = '\n'.join(zam)

        bot.send_message(msg.chat.id, 'Ответ получен✅')

        CheckDateSheets1.clear()
        today = CheckDateSheets1.main()
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    elif 'расписание 11б' in msg.text or (IsAll == True and '11б' in msg.text):
        SAMPLE_RANGE_NAME = settings.ПолноеРасписание11Б
        ALL.clear()

        res = ALL.main(SAMPLE_RANGE_NAME)
        for i in range(len(res)):
            ress = '\n'.join(res)
        bot.send_message(msg.chat.id, ress, parse_mode='HTML')
        keys(msg)

    elif 'изменения 11б' in msg.text or (IsZamen == True and '11б' in msg.text):
        today = datetime.date.today()
        weekday = today.weekday()
        weekday_name = daysOfWeek[weekday]
        bot.send_message(msg.chat.id, 'Смотрю везде, где только можно🔎')

        if weekday_name == 'Понедельник':
            SAMPLE_RANGE_NAME = settings.Понедельник11Б
        elif weekday_name == 'Вторник':
            SAMPLE_RANGE_NAME = settings.Вторник11Б
        elif weekday_name == 'Среда':
            SAMPLE_RANGE_NAME = settings.Среда11Б
        elif weekday_name == 'Четверг':
            SAMPLE_RANGE_NAME = settings.Четверг11Б
        elif weekday_name == 'Пятница':
            SAMPLE_RANGE_NAME = settings.Пятница11Б
        elif weekday_name == 'Суббота':
            SAMPLE_RANGE_NAME = settings.Понедельник11Б
        elif weekday_name == 'Воскресенье':
            SAMPLE_RANGE_NAME = settings.Понедельник11Б

        Day.clear()
        pol = Day.main(SAMPLE_RANGE_NAME)
        for i in range(len(pol)):
            ress = '\n'.join(pol)

        bot.send_message(msg.chat.id, 'Жду ответа⏳')
        SAMPLE_RANGE_NAME = settings.Замены11Б
        Zamen.clear()
        zam = Zamen.main(SAMPLE_RANGE_NAME)
        for i in range(len(zam)):
            resss = '\n'.join(zam)

        bot.send_message(msg.chat.id, 'Ответ получен✅')

        CheckDateSheets1.clear()
        today = CheckDateSheets1.main()
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

        video = Zamen.s
        '''
        bot.send_video(msg.chat.id, video)
        '''
        keys(msg)

    else:
        bot.send_message(msg.chat.id, 'Не распознал сообщение')
bot.infinity_polling()