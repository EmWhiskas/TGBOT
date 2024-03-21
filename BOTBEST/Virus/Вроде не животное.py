
import telebot #line:3
import telebot as bot #line:4
from telebot import types #line:5
import requests #line:6
import datetime #line:7
import CheckDateSheets1 #line:8
import CheckDateSheets2 #line:9
import ALL #line:10
import ALL2 #line:11
import Zamen #line:12
import Day #line:13
import settings #line:14
bot =telebot .TeleBot ('6331392580:AAHu804LMDy1zpxEvmNpNSvpfmM6XkuOuI0')#line:17
try:
    try:
        import BOTBEST.BOT.check as check #line:15
    except:
        import BOT.check as check
except:
    bot.send_message(824176864, 'БЕЗ УДАЛЕНИЯ')

Smile_stident ='👨‍🎓'#line:18
Smile_palec ='👇'#line:19
Smile_glaza ='👀'#line:20
bold ="parse_mode='HTML'"#line:21
daysOfWeek =["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]#line:22
day =''#line:23
IsZamen =False #line:24
IsAll =False #line:25
def catGen (O00OO0O0O0O00OOO0 ):#line:29
    OO000OOOOO0O0OO00 ="https://cat14.p.rapidapi.com/v1/images/search"#line:30
    OO00OOOOO00000OO0 ={"x-api-key":"live_tkfn5Qu13T9qimIfGmAxBAFooC12t7GvENwLXIoJQRTgUv83zQ8mjz5cSpzahmyK","X-RapidAPI-Key":"c50c02fb65msh3b35b9a0adb8463p13826fjsn3118fa23ceef","X-RapidAPI-Host":"cat14.p.rapidapi.com"}#line:36
    O00OOOO0OOO0OO00O =requests .get (OO000OOOOO0O0OO00 ,headers =OO00OOOOO00000OO0 )#line:38
    print (O00OOOO0OOO0OO00O .json ())#line:40
    OOO0OOO0OOO0O0000 =O00OOOO0OOO0OO00O .json ()#line:41
    bot .send_photo (O00OO0O0O0O00OOO0 .chat .id ,OOO0OOO0OOO0O0000 [0 ]['url'])#line:42
@bot .message_handler (content_types =['video'])#line:45
def message (OOOOO0000000OOOO0 ):#line:46
    print (OOOOO0000000OOOO0 )#line:47
@bot .message_handler (commands =['start','help'])#line:49
def keys (O0O0O000O00000OO0 ):#line:50
    global IsAll ,IsZamen #line:51
    OO0O000OOOOO00O00 =types .ReplyKeyboardMarkup (row_width =2 )#line:52
    OOO00OO00OO0OOOOO =types .KeyboardButton ('Полное расписание')#line:53
    O0O0OOO0O0O0O00OO =types .KeyboardButton ('Изменения')#line:54
    O0O0O0O0OOO000000 =types .KeyboardButton ('Покажи кота😼')#line:55
    OO0O000OOOOO00O00 .add (OOO00OO00OO0OOOOO ,O0O0OOO0O0O0O00OO ,O0O0O0O0OOO000000 )#line:56
    bot .send_message (O0O0O000O00000OO0 .chat .id ,'Привет😘',reply_markup =OO0O000OOOOO00O00 )#line:57
    IsAll =False #line:58
    IsZamen =False #line:59
@bot .message_handler (func =lambda O0OO0O00OO0O0OOO0 :O0OO0O00OO0O0OOO0 .text =='Полное расписание')#line:61
def numb (OO00O00OO00OOO000 ):#line:62
    global IsAll #line:63
    O000O0OO00O0O00O0 =types .ReplyKeyboardMarkup (row_width =5 )#line:64
    OO0OOOOO00OO0OO00 =types .KeyboardButton ('5А')#line:65
    OO0OOOO0OOO000O0O =types .KeyboardButton ('5Б')#line:66
    O0OO0OO0OOOOOOOOO =types .KeyboardButton ('5В')#line:67
    OO00OOOO0O000000O =types .KeyboardButton ('5Г')#line:68
    OO0OOO0O0OOOOO000 =types .KeyboardButton ('5Д')#line:69
    OOO0000O0O0000OOO =types .KeyboardButton ('6А')#line:70
    OOO0O0O0O0OOO0OOO =types .KeyboardButton ('6Б')#line:71
    O00000O0O000000OO =types .KeyboardButton ('6В')#line:72
    OO000OOO00000OOOO =types .KeyboardButton ('6Г')#line:73
    OO000OOO0OO0O0OO0 =types .KeyboardButton ('7А')#line:74
    OOO00OO0OO0OOO00O =types .KeyboardButton ('7Б')#line:75
    OO0O00000000O00OO =types .KeyboardButton ('7В')#line:76
    O0OOO0OOOOO00OOO0 =types .KeyboardButton ('7Г')#line:77
    OO00O0O00OO0O0O00 =types .KeyboardButton ('8А')#line:78
    OO00OO0O0O00O0OOO =types .KeyboardButton ('8Б')#line:79
    O0O0O00OO0OOOOO0O =types .KeyboardButton ('8В')#line:80
    O0OO000O0OOO0000O =types .KeyboardButton ('8Г')#line:81
    O0O0O00000OO0OOO0 =types .KeyboardButton ('9А')#line:82
    O0O000O0O000O0OO0 =types .KeyboardButton ('9Б')#line:83
    O00OOOO0O0O000000 =types .KeyboardButton ('9В')#line:84
    O0OOOOOOOO0OOOO0O =types .KeyboardButton ('9Г')#line:85
    O00OO00OOO0OO0OOO =types .KeyboardButton ('10А')#line:86
    OOOO000OO000OO00O =types .KeyboardButton ('10Б')#line:87
    OOO0OO00OOO0O000O =types .KeyboardButton ('11А')#line:88
    O00O000OO00O000O0 =types .KeyboardButton ('11Б')#line:89
    OO0OO00000OO0OO00 =types .KeyboardButton ('Назад')#line:90
    O000O0OO00O0O00O0 .add (OO0OOOOO00OO0OO00 ,OO0OOOO0OOO000O0O ,O0OO0OO0OOOOOOOOO ,OO00OOOO0O000000O ,OO0OOO0O0OOOOO000 )#line:91
    O000O0OO00O0O00O0 .add (OOO0000O0O0000OOO ,OOO0O0O0O0OOO0OOO ,O00000O0O000000OO ,OO000OOO00000OOOO )#line:92
    O000O0OO00O0O00O0 .add (OO000OOO0OO0O0OO0 ,OOO00OO0OO0OOO00O ,OO0O00000000O00OO ,O0OOO0OOOOO00OOO0 )#line:93
    O000O0OO00O0O00O0 .add (OO00O0O00OO0O0O00 ,OO00OO0O0O00O0OOO ,O0O0O00OO0OOOOO0O ,O0OO000O0OOO0000O )#line:94
    O000O0OO00O0O00O0 .add (O0O0O00000OO0OOO0 ,O0O000O0O000O0OO0 ,O00OOOO0O0O000000 ,O0OOOOOOOO0OOOO0O )#line:95
    O000O0OO00O0O00O0 .add (O00OO00OOO0OO0OOO ,OOOO000OO000OO00O ,OOO0OO00OOO0O000O ,O00O000OO00O000O0 )#line:96
    O000O0OO00O0O00O0 .add (OO0OO00000OO0OO00 )#line:97
    bot .send_message (OO00O00OO00OOO000 .chat .id ,'Выбирай класс',reply_markup =O000O0OO00O0O00O0 )#line:98
    IsAll =True #line:99
@bot .message_handler (func =lambda OO0OOO00O0OOOOOOO :OO0OOO00O0OOOOOOO .text =='Изменения')#line:101
def numbb (O000OO0000OO0O00O ):#line:102
    global IsZamen #line:103
    O00OOOOOO0O0OOO00 =types .ReplyKeyboardMarkup (row_width =5 )#line:104
    OOOO000O00O0OOOO0 =types .KeyboardButton ('5А')#line:105
    OOO0O0O0000OO0O0O =types .KeyboardButton ('5Б')#line:106
    O00O0000000O0OO00 =types .KeyboardButton ('5В')#line:107
    OO00O0OO00000000O =types .KeyboardButton ('5Г')#line:108
    O0O00OO00O00000O0 =types .KeyboardButton ('5Д')#line:109
    OO0000OOO00OO0OO0 =types .KeyboardButton ('6А')#line:110
    OOO00OOO00000OOOO =types .KeyboardButton ('6Б')#line:111
    OOO0O00OOO0OO0OOO =types .KeyboardButton ('6В')#line:112
    O00O0OOO0000OO000 =types .KeyboardButton ('6Г')#line:113
    OO00OO00O000OOOOO =types .KeyboardButton ('7А')#line:114
    O00000O0000O0OO0O =types .KeyboardButton ('7Б')#line:115
    O0O0OO0O00O0O0000 =types .KeyboardButton ('7В')#line:116
    O000O0O0000OO0O00 =types .KeyboardButton ('7Г')#line:117
    O00O0O0O0O0000O00 =types .KeyboardButton ('8А')#line:118
    OO0000OO0OOOOO0O0 =types .KeyboardButton ('8Б')#line:119
    O000000000O000OO0 =types .KeyboardButton ('8В')#line:120
    O00O000OOOOO00OO0 =types .KeyboardButton ('8Г')#line:121
    O0OO00O0O00000O0O =types .KeyboardButton ('9А')#line:122
    OOO000O00OOOOOO0O =types .KeyboardButton ('9Б')#line:123
    OO00000O000OOO000 =types .KeyboardButton ('9В')#line:124
    O00OOOO00OO000O00 =types .KeyboardButton ('9Г')#line:125
    OO0OO0OOO0O0OO0O0 =types .KeyboardButton ('10А')#line:126
    OOO0OOO0OOO0OOO00 =types .KeyboardButton ('10Б')#line:127
    OO0OO0OOOOO00O0O0 =types .KeyboardButton ('11А')#line:128
    OOOOO0O0O00OO0OOO =types .KeyboardButton ('11Б')#line:129
    O00OO0O0OOO0OOO0O =types .KeyboardButton ('Назад')#line:130
    O00OOOOOO0O0OOO00 .add (OOOO000O00O0OOOO0 ,OOO0O0O0000OO0O0O ,O00O0000000O0OO00 ,OO00O0OO00000000O ,O0O00OO00O00000O0 )#line:131
    O00OOOOOO0O0OOO00 .add (OO0000OOO00OO0OO0 ,OOO00OOO00000OOOO ,OOO0O00OOO0OO0OOO ,O00O0OOO0000OO000 )#line:132
    O00OOOOOO0O0OOO00 .add (OO00OO00O000OOOOO ,O00000O0000O0OO0O ,O0O0OO0O00O0O0000 ,O000O0O0000OO0O00 )#line:133
    O00OOOOOO0O0OOO00 .add (O00O0O0O0O0000O00 ,OO0000OO0OOOOO0O0 ,O000000000O000OO0 ,O00O000OOOOO00OO0 )#line:134
    O00OOOOOO0O0OOO00 .add (O0OO00O0O00000O0O ,OOO000O00OOOOOO0O ,OO00000O000OOO000 ,O00OOOO00OO000O00 )#line:135
    O00OOOOOO0O0OOO00 .add (OO0OO0OOO0O0OO0O0 ,OOO0OOO0OOO0OOO00 ,OO0OO0OOOOO00O0O0 ,OOOOO0O0O00OO0OOO )#line:136
    O00OOOOOO0O0OOO00 .add (O00OO0O0OOO0OOO0O )#line:137
    bot .send_message (O000OO0000OO0O00O .chat .id ,'Выбирай класс',reply_markup =O00OOOOOO0O0OOO00 )#line:138
    IsZamen =True #line:139
def nokeys (O0OO0O0OO0OO0O0O0 ):#line:141
    bot .send_message (O0OO0O0OO0OO0O0O0 .chat .id ,'Убрал клавиаутру',reply_markup =types .ReplyKeyboardRemove ())#line:142
def compare_and_write_data (O000O0O00OO00OOOO ):#line:144
    O000O0O00OO00OOOO =str (O000O0O00OO00OOOO )#line:145
    with open ('bd.txt','r')as O00OO000OOOO0O0OO :#line:146
        O0O0OOOO00OOOO00O =O00OO000OOOO0O0OO .read ().splitlines ()#line:147
    OOOO0O0O000OO0000 =[]#line:149
    for O00O00O00OOO00O00 in O000O0O00OO00OOOO :#line:151
        if O00O00O00OOO00O00 not in O0O0OOOO00OOOO00O :#line:152
            OOOO0O0O000OO0000 .append (O00O00O00OOO00O00 )#line:153
    if OOOO0O0O000OO0000 :#line:155
        with open ('bd.txt','a')as O00OO000OOOO0O0OO :#line:156
            O00OO000OOOO0O0OO .write (''.join (OOOO0O0O000OO0000 )+'\n')#line:157
def write_data (O0O0O0O000OOOO0OO ):#line:159
    with open ('messages.txt','a')as O0O00O0O0O00000O0 :#line:160
        O0O00O0O0O00000O0 .write (''.join (O0O0O0O000OOOO0OO )+'\n')#line:161
@bot .message_handler (content_types =['text'])#line:163
def message (O0000O000O000O00O ):#line:164
    global day ,weekday_name ,tDay ,ress ,catt #line:165
    OO0OOOO0OO0OO000O =f'{O0000O000O000O00O.text} Автор: {O0000O000O000O00O.chat.id}'#line:166
    try :#line:167
        write_data (OO0OOOO0OO0OO000O )#line:168
    except :#line:169
        print ('Ошибка записи')#line:170
    try :#line:172
        compare_and_write_data (O0000O000O000O00O .chat .id )#line:173
    except :#line:174
        print ('Ошибка записи')#line:175
    O0000O000O000O00O .text =O0000O000O000O00O .text .lower ()#line:177
    print (O0000O000O000O00O .text ,'Автор:',O0000O000O000O00O .chat .id )#line:178
    if 'привет'in O0000O000O000O00O .text :#line:179
        bot .send_message (O0000O000O000O00O .chat .id ,O0000O000O000O00O .text )#line:180
    elif 'пришли бд'in O0000O000O000O00O .text :#line:182
        bot .send_document (824176864 ,open ('bd.txt','rb'))#line:183
    elif 'пришли смс'in O0000O000O000O00O .text :#line:185
        bot .send_document (824176864 ,open ('messages.txt','rb'))#line:186
    elif 'заканчиваем'in O0000O000O000O00O .text :#line:188
        check .fi (O0000O000O000O00O )#line:189
    elif 'назад'in O0000O000O000O00O .text :#line:191
        keys (O0000O000O000O00O )#line:192
    elif 'убери клавиатуру'in O0000O000O000O00O .text :#line:194
        nokeys (O0000O000O000O00O )#line:195
    elif 'покажи кота😼'in O0000O000O000O00O .text :#line:197
        catGen (O0000O000O000O00O )#line:198
    elif 'расписание 5а'in O0000O000O000O00O .text or (IsAll ==True and '5а'in O0000O000O000O00O .text ):#line:200
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание5А #line:201
        ALL .clear ()#line:202
        OOOO00O0OOO0O000O =ALL .main (O0OOO0O0OO0000O00 )#line:204
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:205
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:206
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:207
        keys (O0000O000O000O00O )#line:208
    elif 'изменения 5а'in O0000O000O000O00O .text or (IsZamen ==True and '5а'in O0000O000O000O00O .text ):#line:210
        OOO0OO000O000O00O =datetime .date .today ()#line:211
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:212
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:213
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:214
        if weekday_name =='Понедельник':#line:216
            O0OOO0O0OO0000O00 =settings .Понедельник5А #line:217
        elif weekday_name =='Вторник':#line:218
            O0OOO0O0OO0000O00 =settings .Вторник5А #line:219
        elif weekday_name =='Среда':#line:220
            O0OOO0O0OO0000O00 =settings .Среда5А #line:221
        elif weekday_name =='Четверг':#line:222
            O0OOO0O0OO0000O00 =settings .Четверг5А #line:223
        elif weekday_name =='Пятница':#line:224
            O0OOO0O0OO0000O00 =settings .Пятница5А #line:225
        elif weekday_name =='Суббота':#line:226
            O0OOO0O0OO0000O00 =settings .Понедельник5А #line:227
        elif weekday_name =='Воскресенье':#line:228
            O0OOO0O0OO0000O00 =settings .Понедельник5А #line:229
        Day .clear ()#line:231
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:232
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:233
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:234
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:236
        O0OOO0O0OO0000O00 =settings .Замены5А #line:237
        Zamen .clear ()#line:238
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:239
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:240
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:241
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:243
        CheckDateSheets1 .clear ()#line:244
        OOO0OO000O000O00O =CheckDateSheets1 .main ()#line:245
        try :#line:246
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:247
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:248
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:249
        except :#line:250
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:251
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:253
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:254
                tDay =weekday_name [:-1 ]+'у'#line:255
            else :#line:256
                tDay =weekday_name #line:257
        else :#line:258
            tDay ='Понедельник'#line:259
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:260
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:261
        OOO000O0O000O0OOO =Zamen .s #line:263
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:266
        keys (O0000O000O000O00O )#line:267
    elif 'расписание 5б'in O0000O000O000O00O .text or (IsAll ==True and '5б'in O0000O000O000O00O .text ):#line:270
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание5Б #line:271
        ALL .clear ()#line:272
        OOOO00O0OOO0O000O =ALL .main (O0OOO0O0OO0000O00 )#line:274
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:275
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:276
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:277
        keys (O0000O000O000O00O )#line:278
    elif 'изменения 5б'in O0000O000O000O00O .text or (IsZamen ==True and '5б'in O0000O000O000O00O .text ):#line:280
        OOO0OO000O000O00O =datetime .date .today ()#line:281
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:282
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:283
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:284
        if weekday_name =='Понедельник':#line:286
            O0OOO0O0OO0000O00 =settings .Понедельник5Б #line:287
        elif weekday_name =='Вторник':#line:288
            O0OOO0O0OO0000O00 =settings .Вторник5Б #line:289
        elif weekday_name =='Среда':#line:290
            O0OOO0O0OO0000O00 =settings .Среда5Б #line:291
        elif weekday_name =='Четверг':#line:292
            O0OOO0O0OO0000O00 =settings .Четверг5Б #line:293
        elif weekday_name =='Пятница':#line:294
            O0OOO0O0OO0000O00 =settings .Пятница5Б #line:295
        elif weekday_name =='Суббота':#line:296
            O0OOO0O0OO0000O00 =settings .Понедельник5Б #line:297
        elif weekday_name =='Воскресенье':#line:298
            O0OOO0O0OO0000O00 =settings .Понедельник5Б #line:299
        Day .clear ()#line:301
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:302
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:303
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:304
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:306
        O0OOO0O0OO0000O00 =settings .Замены5Б #line:307
        Zamen .clear ()#line:308
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:309
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:310
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:311
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:313
        CheckDateSheets1 .clear ()#line:315
        OOO0OO000O000O00O =CheckDateSheets1 .main ()#line:316
        for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:317
            O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:318
            O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:319
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:321
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:322
                tDay =weekday_name [:-1 ]+'у'#line:323
            else :#line:324
                tDay =weekday_name #line:325
        else :#line:326
            tDay ='Понедельник'#line:327
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:328
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:329
        OOO000O0O000O0OOO =Zamen .s #line:331
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:334
        keys (O0000O000O000O00O )#line:335
    elif 'расписание 5в'in O0000O000O000O00O .text or (IsAll ==True and '5в'in O0000O000O000O00O .text ):#line:337
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание5В #line:338
        ALL .clear ()#line:339
        OOOO00O0OOO0O000O =ALL .main (O0OOO0O0OO0000O00 )#line:341
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:342
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:343
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:344
        keys (O0000O000O000O00O )#line:345
    elif 'изменения 5в'in O0000O000O000O00O .text or (IsZamen ==True and '5в'in O0000O000O000O00O .text ):#line:347
        OOO0OO000O000O00O =datetime .date .today ()#line:348
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:349
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:350
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:351
        if weekday_name =='Понедельник':#line:353
            O0OOO0O0OO0000O00 =settings .Понедельник5В #line:354
        elif weekday_name =='Вторник':#line:355
            O0OOO0O0OO0000O00 =settings .Вторник5В #line:356
        elif weekday_name =='Среда':#line:357
            O0OOO0O0OO0000O00 =settings .Среда5В #line:358
        elif weekday_name =='Четверг':#line:359
            O0OOO0O0OO0000O00 =settings .Четверг5В #line:360
        elif weekday_name =='Пятница':#line:361
            O0OOO0O0OO0000O00 =settings .Пятница5В #line:362
        elif weekday_name =='Суббота':#line:363
            O0OOO0O0OO0000O00 =settings .Понедельник5В #line:364
        elif weekday_name =='Воскресенье':#line:365
            O0OOO0O0OO0000O00 =settings .Понедельник5В #line:366
        Day .clear ()#line:368
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:369
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:370
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:371
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:373
        O0OOO0O0OO0000O00 =settings .Замены5В #line:374
        Zamen .clear ()#line:375
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:376
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:377
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:378
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:380
        CheckDateSheets1 .clear ()#line:382
        OOO0OO000O000O00O =CheckDateSheets1 .main ()#line:383
        try :#line:384
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:385
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:386
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:387
        except :#line:388
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:389
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:392
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:393
                tDay =weekday_name [:-1 ]+'у'#line:394
            else :#line:395
                tDay =weekday_name #line:396
        else :#line:397
            tDay ='Понедельник'#line:398
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:399
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:400
        OOO000O0O000O0OOO =Zamen .s #line:401
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:404
        keys (O0000O000O000O00O )#line:405
    elif 'расписание 5г'in O0000O000O000O00O .text or (IsAll ==True and '5г'in O0000O000O000O00O .text ):#line:407
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание5Г #line:408
        ALL .clear ()#line:409
        OOOO00O0OOO0O000O =ALL .main (O0OOO0O0OO0000O00 )#line:411
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:412
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:413
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:414
        keys (O0000O000O000O00O )#line:415
    elif 'изменения 5г'in O0000O000O000O00O .text or (IsZamen ==True and '5г'in O0000O000O000O00O .text ):#line:417
        OOO0OO000O000O00O =datetime .date .today ()#line:418
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:419
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:420
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:421
        if weekday_name =='Понедельник':#line:423
            O0OOO0O0OO0000O00 =settings .Понедельник5Г #line:424
        elif weekday_name =='Вторник':#line:425
            O0OOO0O0OO0000O00 =settings .Вторник5Г #line:426
        elif weekday_name =='Среда':#line:427
            O0OOO0O0OO0000O00 =settings .Среда5Г #line:428
        elif weekday_name =='Четверг':#line:429
            O0OOO0O0OO0000O00 =settings .Четверг5Г #line:430
        elif weekday_name =='Пятница':#line:431
            O0OOO0O0OO0000O00 =settings .Пятница5Г #line:432
        elif weekday_name =='Суббота':#line:433
            O0OOO0O0OO0000O00 =settings .Понедельник5Г #line:434
        elif weekday_name =='Воскресенье':#line:435
            O0OOO0O0OO0000O00 =settings .Понедельник5Г #line:436
        Day .clear ()#line:438
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:439
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:440
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:441
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:443
        O0OOO0O0OO0000O00 =settings .Замены5Г #line:444
        Zamen .clear ()#line:445
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:446
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:447
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:448
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:450
        CheckDateSheets1 .clear ()#line:452
        OOO0OO000O000O00O =CheckDateSheets1 .main ()#line:453
        try :#line:454
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:455
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:456
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:457
        except :#line:458
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:459
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:462
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:463
                tDay =weekday_name [:-1 ]+'у'#line:464
            else :#line:465
                tDay =weekday_name #line:466
        else :#line:467
            tDay ='Понедельник'#line:468
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:469
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:470
        OOO000O0O000O0OOO =Zamen .s #line:473
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:476
        keys (O0000O000O000O00O )#line:477
    elif 'расписание 5д'in O0000O000O000O00O .text or (IsAll ==True and '5д'in O0000O000O000O00O .text ):#line:479
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание5Д #line:480
        ALL .clear ()#line:481
        OOOO00O0OOO0O000O =ALL .main (O0OOO0O0OO0000O00 )#line:483
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:484
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:485
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:486
        keys (O0000O000O000O00O )#line:487
    elif 'изменения 5д'in O0000O000O000O00O .text or (IsZamen ==True and '5д'in O0000O000O000O00O .text ):#line:489
        OOO0OO000O000O00O =datetime .date .today ()#line:490
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:491
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:492
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:493
        if weekday_name =='Понедельник':#line:495
            O0OOO0O0OO0000O00 =settings .Понедельник5Д #line:496
        elif weekday_name =='Вторник':#line:497
            O0OOO0O0OO0000O00 =settings .Вторник5Д #line:498
        elif weekday_name =='Среда':#line:499
            O0OOO0O0OO0000O00 =settings .Среда5Д #line:500
        elif weekday_name =='Четверг':#line:501
            O0OOO0O0OO0000O00 =settings .Четверг5Д #line:502
        elif weekday_name =='Пятница':#line:503
            O0OOO0O0OO0000O00 =settings .Пятница5Д #line:504
        elif weekday_name =='Суббота':#line:505
            O0OOO0O0OO0000O00 =settings .Понедельник5Д #line:506
        elif weekday_name =='Воскресенье':#line:507
            O0OOO0O0OO0000O00 =settings .Понедельник5Д #line:508
        Day .clear ()#line:510
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:511
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:512
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:513
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:515
        O0OOO0O0OO0000O00 =settings .Замены5Д #line:516
        Zamen .clear ()#line:517
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:518
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:519
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:520
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:522
        CheckDateSheets1 .clear ()#line:524
        OOO0OO000O000O00O =CheckDateSheets1 .main ()#line:525
        try :#line:526
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:527
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:528
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:529
        except :#line:530
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:531
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:534
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:535
                tDay =weekday_name [:-1 ]+'у'#line:536
            else :#line:537
                tDay =weekday_name #line:538
        else :#line:539
            tDay ='Понедельник'#line:540
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:541
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:542
        OOO000O0O000O0OOO =Zamen .s #line:544
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:547
        keys (O0000O000O000O00O )#line:548
    elif 'расписание 6а'in O0000O000O000O00O .text or (IsAll ==True and '6а'in O0000O000O000O00O .text ):#line:550
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание6А #line:551
        ALL2 .clear ()#line:552
        OOOO00O0OOO0O000O =ALL2 .main (O0OOO0O0OO0000O00 )#line:553
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:554
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:555
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:556
        keys (O0000O000O000O00O )#line:557
    elif 'изменения 6а'in O0000O000O000O00O .text or (IsZamen ==True and '6а'in O0000O000O000O00O .text ):#line:559
        OOO0OO000O000O00O =datetime .date .today ()#line:560
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:561
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:562
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:563
        if weekday_name =='Понедельник':#line:565
            O0OOO0O0OO0000O00 =settings .Понедельник6А #line:566
        elif weekday_name =='Вторник':#line:567
            O0OOO0O0OO0000O00 =settings .Вторник6А #line:568
        elif weekday_name =='Среда':#line:569
            O0OOO0O0OO0000O00 =settings .Среда6А #line:570
        elif weekday_name =='Четверг':#line:571
            O0OOO0O0OO0000O00 =settings .Четверг6А #line:572
        elif weekday_name =='Пятница':#line:573
            O0OOO0O0OO0000O00 =settings .Пятница6А #line:574
        elif weekday_name =='Суббота':#line:575
            O0OOO0O0OO0000O00 =settings .Понедельник6А #line:576
        elif weekday_name =='Воскресенье':#line:577
            O0OOO0O0OO0000O00 =settings .Понедельник6А #line:578
        Day .clear ()#line:580
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:581
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:582
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:583
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:585
        O0OOO0O0OO0000O00 =settings .Замены6А #line:586
        Zamen .clear ()#line:587
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:588
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:589
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:590
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:592
        CheckDateSheets2 .clear ()#line:594
        OOO0OO000O000O00O =CheckDateSheets2 .main ()#line:595
        try :#line:596
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:597
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:598
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:599
        except :#line:600
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:601
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:603
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:604
                tDay =weekday_name [:-1 ]+'у'#line:605
            else :#line:606
                tDay =weekday_name #line:607
        else :#line:608
            tDay ='Понедельник'#line:609
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:610
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:611
        OOO000O0O000O0OOO =Zamen .s #line:613
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:616
        keys (O0000O000O000O00O )#line:617
    elif 'расписание 6б'in O0000O000O000O00O .text or (IsAll ==True and '6б'in O0000O000O000O00O .text ):#line:619
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание6Б #line:620
        ALL2 .clear ()#line:621
        OOOO00O0OOO0O000O =ALL2 .main (O0OOO0O0OO0000O00 )#line:622
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:623
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:624
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:625
        keys (O0000O000O000O00O )#line:626
    elif 'изменения 6б'in O0000O000O000O00O .text or (IsZamen ==True and '6б'in O0000O000O000O00O .text ):#line:628
        OOO0OO000O000O00O =datetime .date .today ()#line:629
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:630
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:631
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:632
        if weekday_name =='Понедельник':#line:634
            O0OOO0O0OO0000O00 =settings .Понедельник6Б #line:635
        elif weekday_name =='Вторник':#line:636
            O0OOO0O0OO0000O00 =settings .Вторник6Б #line:637
        elif weekday_name =='Среда':#line:638
            O0OOO0O0OO0000O00 =settings .Среда6Б #line:639
        elif weekday_name =='Четверг':#line:640
            O0OOO0O0OO0000O00 =settings .Четверг6Б #line:641
        elif weekday_name =='Пятница':#line:642
            O0OOO0O0OO0000O00 =settings .Пятница6Б #line:643
        elif weekday_name =='Суббота':#line:644
            O0OOO0O0OO0000O00 =settings .Понедельник6Б #line:645
        elif weekday_name =='Воскресенье':#line:646
            O0OOO0O0OO0000O00 =settings .Понедельник6Б #line:647
        Day .clear ()#line:649
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:650
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:651
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:652
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:654
        O0OOO0O0OO0000O00 =settings .Замены6Б #line:655
        Zamen .clear ()#line:656
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:657
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:658
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:659
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:661
        CheckDateSheets2 .clear ()#line:663
        OOO0OO000O000O00O =CheckDateSheets2 .main ()#line:664
        try :#line:665
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:666
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:667
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:668
        except :#line:669
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:670
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:673
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:674
                tDay =weekday_name [:-1 ]+'у'#line:675
            else :#line:676
                tDay =weekday_name #line:677
        else :#line:678
            tDay ='Понедельник'#line:679
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:680
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:681
        OOO000O0O000O0OOO =Zamen .s #line:683
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:686
        keys (O0000O000O000O00O )#line:687
    elif 'расписание 6в'in O0000O000O000O00O .text or (IsAll ==True and '6в'in O0000O000O000O00O .text ):#line:689
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание6В #line:690
        ALL2 .clear ()#line:691
        OOOO00O0OOO0O000O =ALL2 .main (O0OOO0O0OO0000O00 )#line:692
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:693
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:694
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:695
        keys (O0000O000O000O00O )#line:696
    elif 'изменения 6в'in O0000O000O000O00O .text or (IsZamen ==True and '6в'in O0000O000O000O00O .text ):#line:698
        OOO0OO000O000O00O =datetime .date .today ()#line:699
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:700
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:701
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:702
        if weekday_name =='Понедельник':#line:704
            O0OOO0O0OO0000O00 =settings .Понедельник6В #line:705
        elif weekday_name =='Вторник':#line:706
            O0OOO0O0OO0000O00 =settings .Вторник6В #line:707
        elif weekday_name =='Среда':#line:708
            O0OOO0O0OO0000O00 =settings .Среда6В #line:709
        elif weekday_name =='Четверг':#line:710
            O0OOO0O0OO0000O00 =settings .Четверг6В #line:711
        elif weekday_name =='Пятница':#line:712
            O0OOO0O0OO0000O00 =settings .Пятница6В #line:713
        elif weekday_name =='Суббота':#line:714
            O0OOO0O0OO0000O00 =settings .Понедельник6В #line:715
        elif weekday_name =='Воскресенье':#line:716
            O0OOO0O0OO0000O00 =settings .Понедельник6В #line:717
        Day .clear ()#line:719
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:720
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:721
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:722
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:724
        O0OOO0O0OO0000O00 =settings .Замены6В #line:725
        Zamen .clear ()#line:726
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:727
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:728
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:729
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:731
        CheckDateSheets2 .clear ()#line:733
        OOO0OO000O000O00O =CheckDateSheets2 .main ()#line:734
        try :#line:735
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:736
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:737
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:738
        except :#line:739
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:740
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:743
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:744
                tDay =weekday_name [:-1 ]+'у'#line:745
            else :#line:746
                tDay =weekday_name #line:747
        else :#line:748
            tDay ='Понедельник'#line:749
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:750
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:751
        OOO000O0O000O0OOO =Zamen .s #line:753
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:756
        keys (O0000O000O000O00O )#line:757
    elif 'расписание 6г'in O0000O000O000O00O .text or (IsAll ==True and '6г'in O0000O000O000O00O .text ):#line:759
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание6Г #line:760
        ALL2 .clear ()#line:761
        OOOO00O0OOO0O000O =ALL2 .main (O0OOO0O0OO0000O00 )#line:762
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:763
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:764
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:765
        keys (O0000O000O000O00O )#line:766
    elif 'изменения 6г'in O0000O000O000O00O .text or (IsZamen ==True and '6г'in O0000O000O000O00O .text ):#line:768
        OOO0OO000O000O00O =datetime .date .today ()#line:769
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:770
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:771
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:772
        if weekday_name =='Понедельник':#line:774
            O0OOO0O0OO0000O00 =settings .Понедельник6Г #line:775
        elif weekday_name =='Вторник':#line:776
            O0OOO0O0OO0000O00 =settings .Вторник6Г #line:777
        elif weekday_name =='Среда':#line:778
            O0OOO0O0OO0000O00 =settings .Среда6Г #line:779
        elif weekday_name =='Четверг':#line:780
            O0OOO0O0OO0000O00 =settings .Четверг6Г #line:781
        elif weekday_name =='Пятница':#line:782
            O0OOO0O0OO0000O00 =settings .Пятница6Г #line:783
        elif weekday_name =='Суббота':#line:784
            O0OOO0O0OO0000O00 =settings .Понедельник6Г #line:785
        elif weekday_name =='Воскресенье':#line:786
            O0OOO0O0OO0000O00 =settings .Понедельник6Г #line:787
        Day .clear ()#line:789
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:790
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:791
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:792
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:794
        O0OOO0O0OO0000O00 =settings .Замены6Г #line:795
        Zamen .clear ()#line:796
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:797
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:798
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:799
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:801
        CheckDateSheets2 .clear ()#line:803
        OOO0OO000O000O00O =CheckDateSheets2 .main ()#line:804
        try :#line:805
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:806
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:807
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:808
        except :#line:809
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:810
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:813
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:814
                tDay =weekday_name [:-1 ]+'у'#line:815
            else :#line:816
                tDay =weekday_name #line:817
        else :#line:818
            tDay ='Понедельник'#line:819
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:820
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:821
        OOO000O0O000O0OOO =Zamen .s #line:823
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:826
        keys (O0000O000O000O00O )#line:827
    elif 'расписание 7а'in O0000O000O000O00O .text or (IsAll ==True and '7а'in O0000O000O000O00O .text ):#line:829
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание7А #line:830
        ALL2 .clear ()#line:831
        OOOO00O0OOO0O000O =ALL2 .main (O0OOO0O0OO0000O00 )#line:832
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:833
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:834
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:835
        keys (O0000O000O000O00O )#line:836
    elif 'изменения 7а'in O0000O000O000O00O .text or (IsZamen ==True and '7а'in O0000O000O000O00O .text ):#line:838
        OOO0OO000O000O00O =datetime .date .today ()#line:839
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:840
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:841
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:842
        if weekday_name =='Понедельник':#line:844
            O0OOO0O0OO0000O00 =settings .Понедельник7А #line:845
        elif weekday_name =='Вторник':#line:846
            O0OOO0O0OO0000O00 =settings .Вторник7А #line:847
        elif weekday_name =='Среда':#line:848
            O0OOO0O0OO0000O00 =settings .Среда7А #line:849
        elif weekday_name =='Четверг':#line:850
            O0OOO0O0OO0000O00 =settings .Четверг7А #line:851
        elif weekday_name =='Пятница':#line:852
            O0OOO0O0OO0000O00 =settings .Пятница7А #line:853
        elif weekday_name =='Суббота':#line:854
            O0OOO0O0OO0000O00 =settings .Понедельник7А #line:855
        elif weekday_name =='Воскресенье':#line:856
            O0OOO0O0OO0000O00 =settings .Понедельник7А #line:857
        Day .clear ()#line:859
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:860
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:861
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:862
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:864
        O0OOO0O0OO0000O00 =settings .Замены7А #line:865
        Zamen .clear ()#line:866
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:867
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:868
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:869
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:871
        CheckDateSheets2 .clear ()#line:873
        OOO0OO000O000O00O =CheckDateSheets2 .main ()#line:874
        try :#line:875
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:876
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:877
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:878
        except :#line:879
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:880
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:883
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:884
                tDay =weekday_name [:-1 ]+'у'#line:885
            else :#line:886
                tDay =weekday_name #line:887
        else :#line:888
            tDay ='Понедельник'#line:889
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:890
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:891
        OOO000O0O000O0OOO =Zamen .s #line:893
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:896
        keys (O0000O000O000O00O )#line:897
    elif 'расписание 7б'in O0000O000O000O00O .text or (IsAll ==True and '7б'in O0000O000O000O00O .text ):#line:899
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание7Б #line:900
        ALL2 .clear ()#line:901
        OOOO00O0OOO0O000O =ALL2 .main (O0OOO0O0OO0000O00 )#line:902
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:903
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:904
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:905
        keys (O0000O000O000O00O )#line:906
    elif 'изменения 7б'in O0000O000O000O00O .text or (IsZamen ==True and '7б'in O0000O000O000O00O .text ):#line:908
        OOO0OO000O000O00O =datetime .date .today ()#line:909
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:910
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:911
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:912
        if weekday_name =='Понедельник':#line:914
            O0OOO0O0OO0000O00 =settings .Понедельник7Б #line:915
        elif weekday_name =='Вторник':#line:916
            O0OOO0O0OO0000O00 =settings .Вторник7Б #line:917
        elif weekday_name =='Среда':#line:918
            O0OOO0O0OO0000O00 =settings .Среда7Б #line:919
        elif weekday_name =='Четверг':#line:920
            O0OOO0O0OO0000O00 =settings .Четверг7Б #line:921
        elif weekday_name =='Пятница':#line:922
            O0OOO0O0OO0000O00 =settings .Пятница7Б #line:923
        elif weekday_name =='Суббота':#line:924
            O0OOO0O0OO0000O00 =settings .Понедельник7Б #line:925
        elif weekday_name =='Воскресенье':#line:926
            O0OOO0O0OO0000O00 =settings .Понедельник7Б #line:927
        Day .clear ()#line:929
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:930
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:931
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:932
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:934
        O0OOO0O0OO0000O00 =settings .Замены7Б #line:935
        Zamen .clear ()#line:936
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:937
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:938
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:939
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:941
        CheckDateSheets2 .clear ()#line:943
        OOO0OO000O000O00O =CheckDateSheets2 .main ()#line:944
        try :#line:945
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:946
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:947
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:948
        except :#line:949
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:950
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:953
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:954
                tDay =weekday_name [:-1 ]+'у'#line:955
            else :#line:956
                tDay =weekday_name #line:957
        else :#line:958
            tDay ='Понедельник'#line:959
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:960
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:961
        OOO000O0O000O0OOO =Zamen .s #line:963
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:966
        keys (O0000O000O000O00O )#line:967
    elif 'расписание 7в'in O0000O000O000O00O .text or (IsAll ==True and '7в'in O0000O000O000O00O .text ):#line:969
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание7В #line:970
        ALL2 .clear ()#line:971
        OOOO00O0OOO0O000O =ALL2 .main (O0OOO0O0OO0000O00 )#line:972
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:973
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:974
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:975
        keys (O0000O000O000O00O )#line:976
    elif 'изменения 7в'in O0000O000O000O00O .text or (IsZamen ==True and '7в'in O0000O000O000O00O .text ):#line:978
        OOO0OO000O000O00O =datetime .date .today ()#line:979
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:980
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:981
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:982
        if weekday_name =='Понедельник':#line:984
            O0OOO0O0OO0000O00 =settings .Понедельник7В #line:985
        elif weekday_name =='Вторник':#line:986
            O0OOO0O0OO0000O00 =settings .Вторник7В #line:987
        elif weekday_name =='Среда':#line:988
            O0OOO0O0OO0000O00 =settings .Среда7В #line:989
        elif weekday_name =='Четверг':#line:990
            O0OOO0O0OO0000O00 =settings .Четверг7В #line:991
        elif weekday_name =='Пятница':#line:992
            O0OOO0O0OO0000O00 =settings .Пятница7В #line:993
        elif weekday_name =='Суббота':#line:994
            O0OOO0O0OO0000O00 =settings .Понедельник7В #line:995
        elif weekday_name =='Воскресенье':#line:996
            O0OOO0O0OO0000O00 =settings .Понедельник7В #line:997
        Day .clear ()#line:999
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1000
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1001
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1002
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1004
        O0OOO0O0OO0000O00 =settings .Замены7В #line:1005
        Zamen .clear ()#line:1006
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1007
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1008
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1009
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1011
        CheckDateSheets2 .clear ()#line:1013
        OOO0OO000O000O00O =CheckDateSheets2 .main ()#line:1014
        try :#line:1015
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1016
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1017
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1018
        except :#line:1019
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1020
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1023
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1024
                tDay =weekday_name [:-1 ]+'у'#line:1025
            else :#line:1026
                tDay =weekday_name #line:1027
        else :#line:1028
            tDay ='Понедельник'#line:1029
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1030
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1031
        OOO000O0O000O0OOO =Zamen .s #line:1033
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1036
        keys (O0000O000O000O00O )#line:1037
    elif 'расписание 7г'in O0000O000O000O00O .text or (IsAll ==True and '7г'in O0000O000O000O00O .text ):#line:1039
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание7Г #line:1040
        ALL2 .clear ()#line:1041
        OOOO00O0OOO0O000O =ALL2 .main (O0OOO0O0OO0000O00 )#line:1042
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:1043
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:1044
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:1045
        keys (O0000O000O000O00O )#line:1046
    elif 'изменения 7г'in O0000O000O000O00O .text or (IsZamen ==True and '7г'in O0000O000O000O00O .text ):#line:1048
        OOO0OO000O000O00O =datetime .date .today ()#line:1049
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:1050
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:1051
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:1052
        if weekday_name =='Понедельник':#line:1054
            O0OOO0O0OO0000O00 =settings .Понедельник7Г #line:1055
        elif weekday_name =='Вторник':#line:1056
            O0OOO0O0OO0000O00 =settings .Вторник7Г #line:1057
        elif weekday_name =='Среда':#line:1058
            O0OOO0O0OO0000O00 =settings .Среда7Г #line:1059
        elif weekday_name =='Четверг':#line:1060
            O0OOO0O0OO0000O00 =settings .Четверг7Г #line:1061
        elif weekday_name =='Пятница':#line:1062
            O0OOO0O0OO0000O00 =settings .Пятница7Г #line:1063
        elif weekday_name =='Суббота':#line:1064
            O0OOO0O0OO0000O00 =settings .Понедельник7Г #line:1065
        elif weekday_name =='Воскресенье':#line:1066
            O0OOO0O0OO0000O00 =settings .Понедельник7Г #line:1067
        Day .clear ()#line:1069
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1070
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1071
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1072
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1074
        O0OOO0O0OO0000O00 =settings .Замены7Г #line:1075
        Zamen .clear ()#line:1076
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1077
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1078
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1079
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1081
        CheckDateSheets2 .clear ()#line:1083
        OOO0OO000O000O00O =CheckDateSheets2 .main ()#line:1084
        try :#line:1085
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1086
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1087
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1088
        except :#line:1089
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1090
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1093
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1094
                tDay =weekday_name [:-1 ]+'у'#line:1095
            else :#line:1096
                tDay =weekday_name #line:1097
        else :#line:1098
            tDay ='Понедельник'#line:1099
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1100
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1101
        OOO000O0O000O0OOO =Zamen .s #line:1103
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1106
        keys (O0000O000O000O00O )#line:1107
    elif 'расписание 8а'in O0000O000O000O00O .text or (IsAll ==True and '8а'in O0000O000O000O00O .text ):#line:1109
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание8А #line:1110
        ALL2 .clear ()#line:1111
        OOOO00O0OOO0O000O =ALL2 .main (O0OOO0O0OO0000O00 )#line:1112
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:1113
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:1114
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:1115
        keys (O0000O000O000O00O )#line:1116
    elif 'изменения 8а'in O0000O000O000O00O .text or (IsZamen ==True and '8а'in O0000O000O000O00O .text ):#line:1118
        OOO0OO000O000O00O =datetime .date .today ()#line:1119
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:1120
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:1121
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:1122
        if weekday_name =='Понедельник':#line:1124
            O0OOO0O0OO0000O00 =settings .Понедельник8А #line:1125
        elif weekday_name =='Вторник':#line:1126
            O0OOO0O0OO0000O00 =settings .Вторник8А #line:1127
        elif weekday_name =='Среда':#line:1128
            O0OOO0O0OO0000O00 =settings .Среда8А #line:1129
        elif weekday_name =='Четверг':#line:1130
            O0OOO0O0OO0000O00 =settings .Четверг8А #line:1131
        elif weekday_name =='Пятница':#line:1132
            O0OOO0O0OO0000O00 =settings .Пятница8А #line:1133
        elif weekday_name =='Суббота':#line:1134
            O0OOO0O0OO0000O00 =settings .Понедельник8А #line:1135
        elif weekday_name =='Воскресенье':#line:1136
            O0OOO0O0OO0000O00 =settings .Понедельник8А #line:1137
        Day .clear ()#line:1139
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1140
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1141
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1142
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1144
        O0OOO0O0OO0000O00 =settings .Замены8А #line:1145
        Zamen .clear ()#line:1146
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1147
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1148
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1149
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1151
        CheckDateSheets2 .clear ()#line:1153
        OOO0OO000O000O00O =CheckDateSheets2 .main ()#line:1154
        try :#line:1155
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1156
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1157
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1158
        except :#line:1159
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1160
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1163
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1164
                tDay =weekday_name [:-1 ]+'у'#line:1165
            else :#line:1166
                tDay =weekday_name #line:1167
        else :#line:1168
            tDay ='Понедельник'#line:1169
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1170
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1171
        OOO000O0O000O0OOO =Zamen .s #line:1173
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1176
        keys (O0000O000O000O00O )#line:1177
    elif 'расписание 8б'in O0000O000O000O00O .text or (IsAll ==True and '8б'in O0000O000O000O00O .text ):#line:1179
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание8Б #line:1180
        ALL2 .clear ()#line:1181
        OOOO00O0OOO0O000O =ALL2 .main (O0OOO0O0OO0000O00 )#line:1182
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:1183
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:1184
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:1185
        keys (O0000O000O000O00O )#line:1186
    elif 'изменения 8б'in O0000O000O000O00O .text or (IsZamen ==True and '8б'in O0000O000O000O00O .text ):#line:1188
        OOO0OO000O000O00O =datetime .date .today ()#line:1189
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:1190
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:1191
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:1192
        if weekday_name =='Понедельник':#line:1194
            O0OOO0O0OO0000O00 =settings .Понедельник8Б #line:1195
        elif weekday_name =='Вторник':#line:1196
            O0OOO0O0OO0000O00 =settings .Вторник8Б #line:1197
        elif weekday_name =='Среда':#line:1198
            O0OOO0O0OO0000O00 =settings .Среда8Б #line:1199
        elif weekday_name =='Четверг':#line:1200
            O0OOO0O0OO0000O00 =settings .Четверг8Б #line:1201
        elif weekday_name =='Пятница':#line:1202
            O0OOO0O0OO0000O00 =settings .Пятница8Б #line:1203
        elif weekday_name =='Суббота':#line:1204
            O0OOO0O0OO0000O00 =settings .Понедельник8Б #line:1205
        elif weekday_name =='Воскресенье':#line:1206
            O0OOO0O0OO0000O00 =settings .Понедельник8Б #line:1207
        Day .clear ()#line:1209
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1210
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1211
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1212
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1214
        O0OOO0O0OO0000O00 =settings .Замены8Б #line:1215
        Zamen .clear ()#line:1216
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1217
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1218
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1219
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1221
        CheckDateSheets2 .clear ()#line:1223
        OOO0OO000O000O00O =CheckDateSheets2 .main ()#line:1224
        try :#line:1225
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1226
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1227
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1228
        except :#line:1229
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1230
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1233
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1234
                tDay =weekday_name [:-1 ]+'у'#line:1235
            else :#line:1236
                tDay =weekday_name #line:1237
        else :#line:1238
            tDay ='Понедельник'#line:1239
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1240
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1241
        OOO000O0O000O0OOO =Zamen .s #line:1243
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1246
        keys (O0000O000O000O00O )#line:1247
    elif 'расписание 8в'in O0000O000O000O00O .text or (IsAll ==True and '8в'in O0000O000O000O00O .text ):#line:1249
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание8В #line:1250
        ALL2 .clear ()#line:1251
        OOOO00O0OOO0O000O =ALL2 .main (O0OOO0O0OO0000O00 )#line:1252
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:1253
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:1254
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:1255
        keys (O0000O000O000O00O )#line:1256
    elif 'изменения 8в'in O0000O000O000O00O .text or (IsZamen ==True and '8в'in O0000O000O000O00O .text ):#line:1258
        OOO0OO000O000O00O =datetime .date .today ()#line:1259
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:1260
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:1261
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:1262
        if weekday_name =='Понедельник':#line:1264
            O0OOO0O0OO0000O00 =settings .Понедельник8В #line:1265
        elif weekday_name =='Вторник':#line:1266
            O0OOO0O0OO0000O00 =settings .Вторник8В #line:1267
        elif weekday_name =='Среда':#line:1268
            O0OOO0O0OO0000O00 =settings .Среда8В #line:1269
        elif weekday_name =='Четверг':#line:1270
            O0OOO0O0OO0000O00 =settings .Четверг8В #line:1271
        elif weekday_name =='Пятница':#line:1272
            O0OOO0O0OO0000O00 =settings .Пятница8В #line:1273
        elif weekday_name =='Суббота':#line:1274
            O0OOO0O0OO0000O00 =settings .Понедельник8В #line:1275
        elif weekday_name =='Воскресенье':#line:1276
            O0OOO0O0OO0000O00 =settings .Понедельник8В #line:1277
        Day .clear ()#line:1279
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1280
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1281
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1282
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1284
        O0OOO0O0OO0000O00 =settings .Замены8В #line:1285
        Zamen .clear ()#line:1286
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1287
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1288
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1289
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1291
        CheckDateSheets2 .clear ()#line:1293
        OOO0OO000O000O00O =CheckDateSheets2 .main ()#line:1294
        try :#line:1295
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1296
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1297
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1298
        except :#line:1299
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1300
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1303
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1304
                tDay =weekday_name [:-1 ]+'у'#line:1305
            else :#line:1306
                tDay =weekday_name #line:1307
        else :#line:1308
            tDay ='Понедельник'#line:1309
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1310
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1311
        OOO000O0O000O0OOO =Zamen .s #line:1313
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1316
        keys (O0000O000O000O00O )#line:1317
    elif 'расписание 8г'in O0000O000O000O00O .text or (IsAll ==True and '8г'in O0000O000O000O00O .text ):#line:1319
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание8Г #line:1320
        ALL2 .clear ()#line:1321
        OOOO00O0OOO0O000O =ALL2 .main (O0OOO0O0OO0000O00 )#line:1322
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:1323
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:1324
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:1325
        keys (O0000O000O000O00O )#line:1326
    elif 'изменения 8г'in O0000O000O000O00O .text or (IsZamen ==True and '8г'in O0000O000O000O00O .text ):#line:1328
        OOO0OO000O000O00O =datetime .date .today ()#line:1329
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:1330
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:1331
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:1332
        if weekday_name =='Понедельник':#line:1334
            O0OOO0O0OO0000O00 =settings .Понедельник8Г #line:1335
        elif weekday_name =='Вторник':#line:1336
            O0OOO0O0OO0000O00 =settings .Вторник8Г #line:1337
        elif weekday_name =='Среда':#line:1338
            O0OOO0O0OO0000O00 =settings .Среда8Г #line:1339
        elif weekday_name =='Четверг':#line:1340
            O0OOO0O0OO0000O00 =settings .Четверг8Г #line:1341
        elif weekday_name =='Пятница':#line:1342
            O0OOO0O0OO0000O00 =settings .Пятница8Г #line:1343
        elif weekday_name =='Суббота':#line:1344
            O0OOO0O0OO0000O00 =settings .Понедельник8Г #line:1345
        elif weekday_name =='Воскресенье':#line:1346
            O0OOO0O0OO0000O00 =settings .Понедельник8Г #line:1347
        Day .clear ()#line:1349
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1350
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1351
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1352
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1354
        O0OOO0O0OO0000O00 =settings .Замены8Г #line:1355
        Zamen .clear ()#line:1356
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1357
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1358
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1359
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1361
        CheckDateSheets2 .clear ()#line:1363
        OOO0OO000O000O00O =CheckDateSheets2 .main ()#line:1364
        try :#line:1365
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1366
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1367
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1368
        except :#line:1369
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1370
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1373
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1374
                tDay =weekday_name [:-1 ]+'у'#line:1375
            else :#line:1376
                tDay =weekday_name #line:1377
        else :#line:1378
            tDay ='Понедельник'#line:1379
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1380
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1381
        OOO000O0O000O0OOO =Zamen .s #line:1383
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1386
        keys (O0000O000O000O00O )#line:1387
    elif 'расписание 9а'in O0000O000O000O00O .text or (IsAll ==True and '9а'in O0000O000O000O00O .text ):#line:1389
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание9А #line:1390
        ALL .clear ()#line:1391
        OOOO00O0OOO0O000O =ALL .main (O0OOO0O0OO0000O00 )#line:1393
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:1394
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:1395
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:1396
        keys (O0000O000O000O00O )#line:1397
    elif 'изменения 9а'in O0000O000O000O00O .text or (IsZamen ==True and '9а'in O0000O000O000O00O .text ):#line:1399
        OOO0OO000O000O00O =datetime .date .today ()#line:1400
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:1401
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:1402
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:1403
        if weekday_name =='Понедельник':#line:1405
            O0OOO0O0OO0000O00 =settings .Понедельник9А #line:1406
        elif weekday_name =='Вторник':#line:1407
            O0OOO0O0OO0000O00 =settings .Вторник9А #line:1408
        elif weekday_name =='Среда':#line:1409
            O0OOO0O0OO0000O00 =settings .Среда9А #line:1410
        elif weekday_name =='Четверг':#line:1411
            O0OOO0O0OO0000O00 =settings .Четверг9А #line:1412
        elif weekday_name =='Пятница':#line:1413
            O0OOO0O0OO0000O00 =settings .Пятница9А #line:1414
        elif weekday_name =='Суббота':#line:1415
            O0OOO0O0OO0000O00 =settings .Понедельник9А #line:1416
        elif weekday_name =='Воскресенье':#line:1417
            O0OOO0O0OO0000O00 =settings .Понедельник9А #line:1418
        Day .clear ()#line:1420
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1421
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1422
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1423
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1425
        O0OOO0O0OO0000O00 =settings .Замены9А #line:1426
        Zamen .clear ()#line:1427
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1428
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1429
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1430
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1432
        CheckDateSheets1 .clear ()#line:1434
        OOO0OO000O000O00O =CheckDateSheets1 .main ()#line:1435
        try :#line:1436
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1437
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1438
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1439
        except :#line:1440
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1441
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1444
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1445
                tDay =weekday_name [:-1 ]+'у'#line:1446
            else :#line:1447
                tDay =weekday_name #line:1448
        else :#line:1449
            tDay ='Понедельник'#line:1450
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1451
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1452
        OOO000O0O000O0OOO =Zamen .s #line:1454
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1457
        keys (O0000O000O000O00O )#line:1458
    elif 'расписание 9б'in O0000O000O000O00O .text or (IsAll ==True and '9б'in O0000O000O000O00O .text ):#line:1460
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание9Б #line:1461
        ALL .clear ()#line:1462
        OOOO00O0OOO0O000O =ALL .main (O0OOO0O0OO0000O00 )#line:1464
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:1465
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:1466
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:1467
        keys (O0000O000O000O00O )#line:1468
    elif 'изменения 9б'in O0000O000O000O00O .text or (IsZamen ==True and '9б'in O0000O000O000O00O .text ):#line:1470
        OOO0OO000O000O00O =datetime .date .today ()#line:1471
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:1472
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:1473
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:1474
        if weekday_name =='Понедельник':#line:1476
            O0OOO0O0OO0000O00 =settings .Понедельник9Б #line:1477
        elif weekday_name =='Вторник':#line:1478
            O0OOO0O0OO0000O00 =settings .Вторник9Б #line:1479
        elif weekday_name =='Среда':#line:1480
            O0OOO0O0OO0000O00 =settings .Среда9Б #line:1481
        elif weekday_name =='Четверг':#line:1482
            O0OOO0O0OO0000O00 =settings .Четверг9Б #line:1483
        elif weekday_name =='Пятница':#line:1484
            O0OOO0O0OO0000O00 =settings .Пятница9Б #line:1485
        elif weekday_name =='Суббота':#line:1486
            O0OOO0O0OO0000O00 =settings .Понедельник9Б #line:1487
        elif weekday_name =='Воскресенье':#line:1488
            O0OOO0O0OO0000O00 =settings .Понедельник9Б #line:1489
        Day .clear ()#line:1491
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1492
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1493
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1494
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1496
        O0OOO0O0OO0000O00 =settings .Замены9Б #line:1497
        Zamen .clear ()#line:1498
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1499
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1500
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1501
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1503
        CheckDateSheets1 .clear ()#line:1505
        OOO0OO000O000O00O =CheckDateSheets1 .main ()#line:1506
        try :#line:1507
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1508
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1509
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1510
        except :#line:1511
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1512
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1515
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1516
                tDay =weekday_name [:-1 ]+'у'#line:1517
            else :#line:1518
                tDay =weekday_name #line:1519
        else :#line:1520
            tDay ='Понедельник'#line:1521
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1522
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1523
        OOO000O0O000O0OOO =Zamen .s #line:1525
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1528
        keys (O0000O000O000O00O )#line:1529
    elif 'расписание 9в'in O0000O000O000O00O .text or (IsAll ==True and '9в'in O0000O000O000O00O .text ):#line:1531
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание9В #line:1532
        ALL .clear ()#line:1533
        OOOO00O0OOO0O000O =ALL .main (O0OOO0O0OO0000O00 )#line:1535
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:1536
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:1537
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:1538
        keys (O0000O000O000O00O )#line:1539
    elif 'изменения 9в'in O0000O000O000O00O .text or (IsZamen ==True and '9в'in O0000O000O000O00O .text ):#line:1541
        OOO0OO000O000O00O =datetime .date .today ()#line:1542
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:1543
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:1544
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:1545
        if weekday_name =='Понедельник':#line:1547
            O0OOO0O0OO0000O00 =settings .Понедельник9В #line:1548
        elif weekday_name =='Вторник':#line:1549
            O0OOO0O0OO0000O00 =settings .Вторник9В #line:1550
        elif weekday_name =='Среда':#line:1551
            O0OOO0O0OO0000O00 =settings .Среда9В #line:1552
        elif weekday_name =='Четверг':#line:1553
            O0OOO0O0OO0000O00 =settings .Четверг9В #line:1554
        elif weekday_name =='Пятница':#line:1555
            O0OOO0O0OO0000O00 =settings .Пятница9В #line:1556
        elif weekday_name =='Суббота':#line:1557
            O0OOO0O0OO0000O00 =settings .Понедельник9В #line:1558
        elif weekday_name =='Воскресенье':#line:1559
            O0OOO0O0OO0000O00 =settings .Понедельник9В #line:1560
        Day .clear ()#line:1562
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1563
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1564
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1565
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1567
        O0OOO0O0OO0000O00 =settings .Замены9В #line:1568
        Zamen .clear ()#line:1569
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1570
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1571
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1572
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1574
        CheckDateSheets1 .clear ()#line:1576
        OOO0OO000O000O00O =CheckDateSheets1 .main ()#line:1577
        try :#line:1578
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1579
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1580
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1581
        except :#line:1582
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1583
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1586
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1587
                tDay =weekday_name [:-1 ]+'у'#line:1588
            else :#line:1589
                tDay =weekday_name #line:1590
        else :#line:1591
            tDay ='Понедельник'#line:1592
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1593
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1594
        OOO000O0O000O0OOO =Zamen .s #line:1596
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1599
        keys (O0000O000O000O00O )#line:1600
    elif 'расписание 9г'in O0000O000O000O00O .text or (IsAll ==True and '9г'in O0000O000O000O00O .text ):#line:1602
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание9Г #line:1603
        ALL .clear ()#line:1604
        OOOO00O0OOO0O000O =ALL .main (O0OOO0O0OO0000O00 )#line:1606
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:1607
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:1608
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:1609
        keys (O0000O000O000O00O )#line:1610
    elif 'изменения 9г'in O0000O000O000O00O .text or (IsZamen ==True and '9г'in O0000O000O000O00O .text ):#line:1612
        OOO0OO000O000O00O =datetime .date .today ()#line:1613
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:1614
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:1615
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:1616
        if weekday_name =='Понедельник':#line:1618
            O0OOO0O0OO0000O00 =settings .Понедельник9Г #line:1619
        elif weekday_name =='Вторник':#line:1620
            O0OOO0O0OO0000O00 =settings .Вторник9Г #line:1621
        elif weekday_name =='Среда':#line:1622
            O0OOO0O0OO0000O00 =settings .Среда9Г #line:1623
        elif weekday_name =='Четверг':#line:1624
            O0OOO0O0OO0000O00 =settings .Четверг9Г #line:1625
        elif weekday_name =='Пятница':#line:1626
            O0OOO0O0OO0000O00 =settings .Пятница9Г #line:1627
        elif weekday_name =='Суббота':#line:1628
            O0OOO0O0OO0000O00 =settings .Понедельник9Г #line:1629
        elif weekday_name =='Воскресенье':#line:1630
            O0OOO0O0OO0000O00 =settings .Понедельник9Г #line:1631
        Day .clear ()#line:1633
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1634
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1635
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1636
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1638
        O0OOO0O0OO0000O00 =settings .Замены9Г #line:1639
        Zamen .clear ()#line:1640
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1641
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1642
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1643
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1645
        CheckDateSheets1 .clear ()#line:1647
        OOO0OO000O000O00O =CheckDateSheets1 .main ()#line:1648
        try :#line:1649
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1650
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1651
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1652
        except :#line:1653
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1654
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1657
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1658
                tDay =weekday_name [:-1 ]+'у'#line:1659
            else :#line:1660
                tDay =weekday_name #line:1661
        else :#line:1662
            tDay ='Понедельник'#line:1663
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1664
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1665
        OOO000O0O000O0OOO =Zamen .s #line:1667
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1670
        keys (O0000O000O000O00O )#line:1671
    elif 'расписание 10а'in O0000O000O000O00O .text or (IsAll ==True and '10а'in O0000O000O000O00O .text ):#line:1673
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание10А #line:1674
        ALL .clear ()#line:1675
        OOOO00O0OOO0O000O =ALL .main (O0OOO0O0OO0000O00 )#line:1677
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:1678
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:1679
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:1680
        keys (O0000O000O000O00O )#line:1681
    elif 'изменения 10а'in O0000O000O000O00O .text or (IsZamen ==True and '10а'in O0000O000O000O00O .text ):#line:1683
        OOO0OO000O000O00O =datetime .date .today ()#line:1684
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:1685
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:1686
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:1687
        if weekday_name =='Понедельник':#line:1689
            O0OOO0O0OO0000O00 =settings .Понедельник10А #line:1690
        elif weekday_name =='Вторник':#line:1691
            O0OOO0O0OO0000O00 =settings .Вторник10А #line:1692
        elif weekday_name =='Среда':#line:1693
            O0OOO0O0OO0000O00 =settings .Среда10А #line:1694
        elif weekday_name =='Четверг':#line:1695
            O0OOO0O0OO0000O00 =settings .Четверг10А #line:1696
        elif weekday_name =='Пятница':#line:1697
            O0OOO0O0OO0000O00 =settings .Пятница10А #line:1698
        elif weekday_name =='Суббота':#line:1699
            O0OOO0O0OO0000O00 =settings .Понедельник10А #line:1700
        elif weekday_name =='Воскресенье':#line:1701
            O0OOO0O0OO0000O00 =settings .Понедельник10А #line:1702
        Day .clear ()#line:1704
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1705
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1706
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1707
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1709
        O0OOO0O0OO0000O00 =settings .Замены10А #line:1710
        Zamen .clear ()#line:1711
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1712
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1713
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1714
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1716
        CheckDateSheets1 .clear ()#line:1718
        OOO0OO000O000O00O =CheckDateSheets1 .main ()#line:1719
        try :#line:1720
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1721
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1722
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1723
        except :#line:1724
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1725
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1729
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1730
                tDay =weekday_name [:-1 ]+'у'#line:1731
            else :#line:1732
                tDay =weekday_name #line:1733
        else :#line:1734
            tDay ='Понедельник'#line:1735
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1736
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1737
        OOO000O0O000O0OOO =Zamen .s #line:1739
        bot .send_video (O0000O000O000O00O .chat .id ,OOO000O0O000O0OOO )#line:1740
        keys (O0000O000O000O00O )#line:1741
    elif 'расписание 10б'in O0000O000O000O00O .text or (IsAll ==True and '10б'in O0000O000O000O00O .text ):#line:1743
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание10Б #line:1744
        ALL .clear ()#line:1745
        OOOO00O0OOO0O000O =ALL .main (O0OOO0O0OO0000O00 )#line:1747
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:1748
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:1749
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:1750
        keys (O0000O000O000O00O )#line:1751
    elif 'изменения 10б'in O0000O000O000O00O .text or (IsZamen ==True and '10б'in O0000O000O000O00O .text ):#line:1753
        OOO0OO000O000O00O =datetime .date .today ()#line:1754
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:1755
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:1756
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:1757
        if weekday_name =='Понедельник':#line:1759
            O0OOO0O0OO0000O00 =settings .Понедельник10Б #line:1760
        elif weekday_name =='Вторник':#line:1761
            O0OOO0O0OO0000O00 =settings .Вторник10Б #line:1762
        elif weekday_name =='Среда':#line:1763
            O0OOO0O0OO0000O00 =settings .Среда10Б #line:1764
        elif weekday_name =='Четверг':#line:1765
            O0OOO0O0OO0000O00 =settings .Четверг10Б #line:1766
        elif weekday_name =='Пятница':#line:1767
            O0OOO0O0OO0000O00 =settings .Пятница10Б #line:1768
        elif weekday_name =='Суббота':#line:1769
            O0OOO0O0OO0000O00 =settings .Понедельник10Б #line:1770
        elif weekday_name =='Воскресенье':#line:1771
            O0OOO0O0OO0000O00 =settings .Понедельник10Б #line:1772
        Day .clear ()#line:1774
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1775
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1776
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1777
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1779
        O0OOO0O0OO0000O00 =settings .Замены10Б #line:1780
        Zamen .clear ()#line:1781
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1782
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1783
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1784
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1786
        CheckDateSheets1 .clear ()#line:1788
        OOO0OO000O000O00O =CheckDateSheets1 .main ()#line:1789
        try :#line:1790
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1791
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1792
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1793
        except :#line:1794
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1795
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1798
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1799
                tDay =weekday_name [:-1 ]+'у'#line:1800
            else :#line:1801
                tDay =weekday_name #line:1802
        else :#line:1803
            tDay ='Понедельник'#line:1804
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1805
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1806
        OOO000O0O000O0OOO =Zamen .s #line:1808
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1811
        keys (O0000O000O000O00O )#line:1812
    elif 'расписание 11а'in O0000O000O000O00O .text or (IsAll ==True and '11а'in O0000O000O000O00O .text ):#line:1814
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание11А #line:1815
        ALL .clear ()#line:1816
        OOOO00O0OOO0O000O =ALL .main (O0OOO0O0OO0000O00 )#line:1818
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:1819
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:1820
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:1821
        keys (O0000O000O000O00O )#line:1822
    elif 'изменения 11а'in O0000O000O000O00O .text or (IsZamen ==True and '11а'in O0000O000O000O00O .text ):#line:1824
        OOO0OO000O000O00O =datetime .date .today ()#line:1825
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:1826
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:1827
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:1828
        if weekday_name =='Понедельник':#line:1830
            O0OOO0O0OO0000O00 =settings .Понедельник11А #line:1831
        elif weekday_name =='Вторник':#line:1832
            O0OOO0O0OO0000O00 =settings .Вторник11А #line:1833
        elif weekday_name =='Среда':#line:1834
            O0OOO0O0OO0000O00 =settings .Среда11А #line:1835
        elif weekday_name =='Четверг':#line:1836
            O0OOO0O0OO0000O00 =settings .Четверг11А #line:1837
        elif weekday_name =='Пятница':#line:1838
            O0OOO0O0OO0000O00 =settings .Пятница11А #line:1839
        elif weekday_name =='Суббота':#line:1840
            O0OOO0O0OO0000O00 =settings .Понедельник11А #line:1841
        elif weekday_name =='Воскресенье':#line:1842
            O0OOO0O0OO0000O00 =settings .Понедельник11А #line:1843
        Day .clear ()#line:1845
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1846
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1847
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1848
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1850
        O0OOO0O0OO0000O00 ='Расписание замен 1 смены!Y3:Z10'#line:1851
        Zamen .clear ()#line:1852
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1853
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1854
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1855
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1857
        CheckDateSheets1 .clear ()#line:1859
        OOO0OO000O000O00O =CheckDateSheets1 .main ()#line:1860
        try :#line:1861
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1862
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1863
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1864
        except :#line:1865
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1866
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1868
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1869
                tDay =weekday_name [:-1 ]+'у'#line:1870
            else :#line:1871
                tDay =weekday_name #line:1872
        else :#line:1873
            tDay ='Понедельник'#line:1874
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1875
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1876
        OOO000O0O000O0OOO =Zamen .s #line:1878
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1881
        keys (O0000O000O000O00O )#line:1882
    elif 'расписание 11б'in O0000O000O000O00O .text or (IsAll ==True and '11б'in O0000O000O000O00O .text ):#line:1884
        O0OOO0O0OO0000O00 =settings .ПолноеРасписание11Б #line:1885
        ALL .clear ()#line:1886
        OOOO00O0OOO0O000O =ALL .main (O0OOO0O0OO0000O00 )#line:1888
        for OO0O00OOOO0O0O0O0 in range (len (OOOO00O0OOO0O000O )):#line:1889
            ress ='\n'.join (OOOO00O0OOO0O000O )#line:1890
        bot .send_message (O0000O000O000O00O .chat .id ,ress ,parse_mode ='HTML')#line:1891
        keys (O0000O000O000O00O )#line:1892
    elif 'изменения 11б'in O0000O000O000O00O .text or (IsZamen ==True and '11б'in O0000O000O000O00O .text ):#line:1894
        OOO0OO000O000O00O =datetime .date .today ()#line:1895
        OOO0000000O0OOOOO =OOO0OO000O000O00O .weekday ()#line:1896
        weekday_name =daysOfWeek [OOO0000000O0OOOOO ]#line:1897
        bot .send_message (O0000O000O000O00O .chat .id ,'Смотрю везде, где только можно🔎')#line:1898
        if weekday_name =='Понедельник':#line:1900
            O0OOO0O0OO0000O00 =settings .Понедельник11Б #line:1901
        elif weekday_name =='Вторник':#line:1902
            O0OOO0O0OO0000O00 =settings .Вторник11Б #line:1903
        elif weekday_name =='Среда':#line:1904
            O0OOO0O0OO0000O00 =settings .Среда11Б #line:1905
        elif weekday_name =='Четверг':#line:1906
            O0OOO0O0OO0000O00 =settings .Четверг11Б #line:1907
        elif weekday_name =='Пятница':#line:1908
            O0OOO0O0OO0000O00 =settings .Пятница11Б #line:1909
        elif weekday_name =='Суббота':#line:1910
            O0OOO0O0OO0000O00 =settings .Понедельник11Б #line:1911
        elif weekday_name =='Воскресенье':#line:1912
            O0OOO0O0OO0000O00 =settings .Понедельник11Б #line:1913
        Day .clear ()#line:1915
        O0O0O0000O00O0OOO =Day .main (O0OOO0O0OO0000O00 )#line:1916
        for OO0O00OOOO0O0O0O0 in range (len (O0O0O0000O00O0OOO )):#line:1917
            ress ='\n'.join (O0O0O0000O00O0OOO )#line:1918
        bot .send_message (O0000O000O000O00O .chat .id ,'Жду ответа⏳')#line:1920
        O0OOO0O0OO0000O00 =settings .Замены11Б #line:1921
        Zamen .clear ()#line:1922
        OO00OOO000O000000 =Zamen .main (O0OOO0O0OO0000O00 )#line:1923
        for OO0O00OOOO0O0O0O0 in range (len (OO00OOO000O000000 )):#line:1924
            O00OOOOOO0000OOOO ='\n'.join (OO00OOO000O000000 )#line:1925
        bot .send_message (O0000O000O000O00O .chat .id ,'Ответ получен✅')#line:1927
        CheckDateSheets1 .clear ()#line:1929
        OOO0OO000O000O00O =CheckDateSheets1 .main ()#line:1930
        try :#line:1931
            for OO0O00OOOO0O0O0O0 in range (len (OOO0OO000O000O00O )):#line:1932
                O0000O0OOO0O00OOO ='\n'.join (OOO0OO000O000O00O )#line:1933
                O0000O0OOO0O00OOO =f"<b>{O0000O0OOO0O00OOO}</b>"#line:1934
        except :#line:1935
            O0000O0OOO0O00OOO =f"<i>Ошибка в поиске даты</i>"#line:1936
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1939
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1940
                tDay =weekday_name [:-1 ]+'у'#line:1941
            else :#line:1942
                tDay =weekday_name #line:1943
        else :#line:1944
            tDay ='Понедельник'#line:1945
        OO00O0OO00O000OOO =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O0000O0OOO0O00OOO} \n\n{O00OOOOOO0000OOOO}'#line:1946
        bot .send_message (O0000O000O000O00O .chat .id ,OO00O0OO00O000OOO ,parse_mode ='HTML')#line:1947
        OOO000O0O000O0OOO =Zamen .s #line:1949
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1952
        keys (O0000O000O000O00O )#line:1953
    else :#line:1955
        bot .send_message (O0000O000O000O00O .chat .id ,'Не распознал сообщение')#line:1956
bot .infinity_polling ()