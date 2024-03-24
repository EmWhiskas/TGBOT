import os #line:1
import telebot #line:3
import telebot as bot #line:4
from telebot import types #line:5
import requests #line:6
import datetime #line:7
import CheckDateSheets1 #line:9
import CheckDateSheets2 #line:10
import ALL #line:11
import ALL2 #line:12
import Zamen #line:13
import Day #line:14
import settings #line:15
smscount =0 #line:16
bot =telebot .TeleBot (settings .BotApi )#line:17
Smile_stident ='👨‍🎓'#line:18
Smile_palec ='👇'#line:19
Smile_glaza ='👀'#line:20
bold ="parse_mode='HTML'"#line:21
daysOfWeek =["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]#line:22
day =''#line:23
IsZamen =False #line:24
IsAll =False #line:25
def read_unique_ids (OO0O0000OOO000000 ):#line:29
    O0000OOO00O0000OO =set ()#line:30
    with open ('bd.txt','r')as OO0OOO0OO0OO000OO :#line:31
        for O00OOO0OO0OOOO000 in OO0OOO0OO0OO000OO :#line:32
            O0O0O0OO0OOOO0OOO =O00OOO0OO0OOOO000 .strip ()#line:34
            if O0O0O0OO0OOOO0OOO :#line:36
                O0000OOO00O0000OO .add (O0O0O0OO0OOOO0OOO )#line:37
    O000OOOOOO0O00000 =OO0O0000OOO000000 .text .replace ('глобальное сообщение ','<b>Глобальное сообщение\n</b>')#line:39
    for O0OOO0OO0O0O0OOOO in O0000OOO00O0000OO :#line:40
        global smscount #line:41
        try :#line:42
            bot .send_message (O0OOO0OO0O0O0OOOO ,O000OOOOOO0O00000 ,parse_mode ='HTML')#line:43
            smscount +=1 #line:44
        except :#line:45
            pass #line:46
    O0000O0OOO000OO0O =f'Всего отправленно {smscount} людям'#line:47
    bot .send_message (824176864 ,O0000O0OOO000OO0O )#line:48
def zamenGen2 (O000O0O00000O0O00 ,OOO0OOOO0000OOOO0 ):#line:50
    OOOOO00000O00OO00 =datetime .date .today ()#line:51
    OOOOOOO00O000OO0O =OOOOO00000O00OO00 .weekday ()#line:52
    O000OO00000O00OOO =daysOfWeek [OOOOOOO00O000OO0O ]#line:53
    bot .send_message (O000O0O00000O0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:54
    if O000OO00000O00OOO =='Понедельник':#line:55
        O0O0O0O00O0000000 ='Понедельник'+OOO0OOOO0000OOOO0 #line:56
        OOOOO000OO000OO00 =getattr (settings ,O0O0O0O00O0000000 )#line:57
    elif O000OO00000O00OOO =='Вторник':#line:58
        O0O0O0O00O0000000 ='Вторник'+OOO0OOOO0000OOOO0 #line:59
        OOOOO000OO000OO00 =getattr (settings ,O0O0O0O00O0000000 )#line:60
    elif O000OO00000O00OOO =='Среда':#line:61
        O0O0O0O00O0000000 ='Среда'+OOO0OOOO0000OOOO0 #line:62
        OOOOO000OO000OO00 =getattr (settings ,O0O0O0O00O0000000 )#line:63
    elif O000OO00000O00OOO =='Четверг':#line:64
        O0O0O0O00O0000000 ='Четверг'+OOO0OOOO0000OOOO0 #line:65
        OOOOO000OO000OO00 =getattr (settings ,O0O0O0O00O0000000 )#line:66
    elif O000OO00000O00OOO =='Пятница':#line:67
        O0O0O0O00O0000000 ='Пятница'+OOO0OOOO0000OOOO0 #line:68
        OOOOO000OO000OO00 =getattr (settings ,O0O0O0O00O0000000 )#line:69
    elif O000OO00000O00OOO =='Суббота':#line:70
        O0O0O0O00O0000000 ='Понедельник'+OOO0OOOO0000OOOO0 #line:71
        OOOOO000OO000OO00 =getattr (settings ,O0O0O0O00O0000000 )#line:72
    elif O000OO00000O00OOO =='Воскресенье':#line:73
        O0O0O0O00O0000000 ='Понедельник'+OOO0OOOO0000OOOO0 #line:74
        OOOOO000OO000OO00 =getattr (settings ,O0O0O0O00O0000000 )#line:75
    Day .clear ()#line:77
    OOO0O00O0000O0OOO =Day .main (OOOOO000OO000OO00 )#line:78
    for OO00O0000000OO000 in range (len (OOO0O00O0000O0OOO )):#line:79
        O0O0O0O0000000O00 ='\n'.join (OOO0O00O0000O0OOO )#line:80
    bot .send_message (O000O0O00000O0O00 .chat .id ,'Жду ответа⏳')#line:82
    OOOOO000OO000OO00 =settings .Замены6А #line:83
    Zamen .clear ()#line:84
    O0O0OO000O00OO00O =Zamen .main (OOOOO000OO000OO00 )#line:85
    for OO00O0000000OO000 in range (len (O0O0OO000O00OO00O )):#line:86
        O0O0000O0OOOOOOO0 ='\n'.join (O0O0OO000O00OO00O )#line:87
    bot .send_message (O000O0O00000O0O00 .chat .id ,'Ответ получен✅')#line:89
    CheckDateSheets2 .clear ()#line:91
    OOOOO00000O00OO00 =CheckDateSheets2 .main ()#line:92
    try :#line:93
        for OO00O0000000OO000 in range (len (OOOOO00000O00OO00 )):#line:94
            OO00O00OOOOOOOO0O ='\n'.join (OOOOO00000O00OO00 )#line:95
            OO00O00OOOOOOOO0O =f"<b>{OO00O00OOOOOOOO0O}</b>"#line:96
    except :#line:97
        OO00O00OOOOOOOO0O =f"<i>Ошибка в поиске даты</i>"#line:98
    if O000OO00000O00OOO !='Суббота'and O000OO00000O00OOO !='Воскресенье':#line:100
        if O000OO00000O00OOO !='Четверг'and O000OO00000O00OOO !='Понедельник'and O000OO00000O00OOO !='Вторник':#line:101
            OO000OOOO000O00O0 =O000OO00000O00OOO [:-1 ]+'у'#line:102
        else :#line:103
            OO000OOOO000O00O0 =O000OO00000O00OOO #line:104
    else :#line:105
        OO000OOOO000O00O0 ='Понедельник'#line:106
    O000O0O0O00O0OO00 =f'Вот твое обычное расписание на <b>{OO000OOOO000O00O0}</b> \n{O0O0O0O0000000O00} \n\nПосмотри изменения ниже \n{OO00O00OOOOOOOO0O} \n\n{O0O0000O0OOOOOOO0}'#line:107
    bot .send_message (O000O0O00000O0O00 .chat .id ,O000O0O0O00O0OO00 ,parse_mode ='HTML')#line:108
    keys (O000O0O00000O0O00 )#line:109
def fullGen2 (OO00O00OO00O000O0 ,O000OO00O0O0O00O0 ):#line:112
    ALL2 .clear ()#line:113
    OO0OO0OO0O0OOO000 =ALL2 .main (O000OO00O0O0O00O0 )#line:114
    for OO00O0OO0OO00O0OO in range (len (OO0OO0OO0O0OOO000 )):#line:115
        OO0000O0O0OOO0OOO ='\n'.join (OO0OO0OO0O0OOO000 )#line:116
    bot .send_message (OO00O00OO00O000O0 .chat .id ,OO0000O0O0OOO0OOO ,parse_mode ='HTML')#line:117
    keys (OO00O00OO00O000O0 )#line:118
def fullGen (OO0OOOOOO000OO0OO ,OO0O0O00OO000OOOO ):#line:120
    ALL .clear ()#line:121
    O0O00OOOOO0O000O0 =ALL .main (OO0O0O00OO000OOOO )#line:123
    for O0O0O0O00O000O0OO in range (len (O0O00OOOOO0O000O0 )):#line:124
        O00O00000O0OO000O ='\n'.join (O0O00OOOOO0O000O0 )#line:125
    bot .send_message (OO0OOOOOO000OO0OO .chat .id ,O00O00000O0OO000O ,parse_mode ='HTML')#line:126
    keys (OO0OOOOOO000OO0OO )#line:127
def zamenGen (OOOOOOO0O0O0O0O0O ,O0O0O00OO0O0OOO00 ):#line:129
    O00O000OO00O00OO0 =datetime .date .today ()#line:130
    O00OOO0OO0O00000O =O00O000OO00O00OO0 .weekday ()#line:131
    O000OO00OOO0OOOOO =daysOfWeek [O00OOO0OO0O00000O ]#line:132
    bot .send_message (OOOOOOO0O0O0O0O0O .chat .id ,'Смотрю везде, где только можно🔎')#line:133
    if O000OO00OOO0OOOOO =='Понедельник':#line:134
        OO000O00000O00OOO ='Понедельник'+O0O0O00OO0O0OOO00 #line:135
        O0OO0O0O000O0O00O =getattr (settings ,OO000O00000O00OOO )#line:136
    elif O000OO00OOO0OOOOO =='Вторник':#line:137
        OO000O00000O00OOO ='Вторник'+O0O0O00OO0O0OOO00 #line:138
        O0OO0O0O000O0O00O =getattr (settings ,OO000O00000O00OOO )#line:139
    elif O000OO00OOO0OOOOO =='Среда':#line:140
        OO000O00000O00OOO ='Среда'+O0O0O00OO0O0OOO00 #line:141
        O0OO0O0O000O0O00O =getattr (settings ,OO000O00000O00OOO )#line:142
    elif O000OO00OOO0OOOOO =='Четверг':#line:143
        OO000O00000O00OOO ='Четверг'+O0O0O00OO0O0OOO00 #line:144
        O0OO0O0O000O0O00O =getattr (settings ,OO000O00000O00OOO )#line:145
    elif O000OO00OOO0OOOOO =='Пятница':#line:146
        OO000O00000O00OOO ='Пятница'+O0O0O00OO0O0OOO00 #line:147
        O0OO0O0O000O0O00O =getattr (settings ,OO000O00000O00OOO )#line:148
    elif O000OO00OOO0OOOOO =='Суббота':#line:149
        OO000O00000O00OOO ='Понедельник'+O0O0O00OO0O0OOO00 #line:150
        O0OO0O0O000O0O00O =getattr (settings ,OO000O00000O00OOO )#line:151
    elif O000OO00OOO0OOOOO =='Воскресенье':#line:152
        OO000O00000O00OOO ='Понедельник'+O0O0O00OO0O0OOO00 #line:153
        O0OO0O0O000O0O00O =getattr (settings ,OO000O00000O00OOO )#line:154
    Day .clear ()#line:156
    OO0000000O00O0000 =Day .main (O0OO0O0O000O0O00O )#line:157
    for OOO0000O0O000O00O in range (len (OO0000000O00O0000 )):#line:158
        OOOO00OO00OO0O0O0 ='\n'.join (OO0000000O00O0000 )#line:159
    bot .send_message (OOOOOOO0O0O0O0O0O .chat .id ,'Жду ответа⏳')#line:161
    OO000O00000O00OOO ='Замены'+O0O0O00OO0O0OOO00 #line:162
    O0OO0O0O000O0O00O =getattr (settings ,OO000O00000O00OOO )#line:163
    Zamen .clear ()#line:164
    OOO0OO0O0O0O00OO0 =Zamen .main (O0OO0O0O000O0O00O )#line:165
    for OOO0000O0O000O00O in range (len (OOO0OO0O0O0O00OO0 )):#line:166
        OO0000OOO00OO0OOO ='\n'.join (OOO0OO0O0O0O00OO0 )#line:167
    bot .send_message (OOOOOOO0O0O0O0O0O .chat .id ,'Ответ получен✅')#line:169
    CheckDateSheets1 .clear ()#line:170
    O00O000OO00O00OO0 =CheckDateSheets1 .main ()#line:171
    try :#line:172
        for OOO0000O0O000O00O in range (len (O00O000OO00O00OO0 )):#line:173
            OOOOOOO00000000OO ='\n'.join (O00O000OO00O00OO0 )#line:174
            OOOOOOO00000000OO =f"<b>{OOOOOOO00000000OO}</b>"#line:175
    except :#line:176
        OOOOOOO00000000OO =f"<i>Ошибка в поиске даты</i>"#line:177
    if O000OO00OOO0OOOOO !='Суббота'and O000OO00OOO0OOOOO !='Воскресенье':#line:179
        if O000OO00OOO0OOOOO !='Четверг'and O000OO00OOO0OOOOO !='Понедельник'and O000OO00OOO0OOOOO !='Вторник':#line:180
            O000O00000000O0O0 =O000OO00OOO0OOOOO [:-1 ]+'у'#line:181
        else :#line:182
            O000O00000000O0O0 =O000OO00OOO0OOOOO #line:183
    else :#line:184
        O000O00000000O0O0 ='Понедельник'#line:185
    OO00OOOOO00000O00 =f'Вот твое обычное расписание на <b>{O000O00000000O0O0}</b> \n{OOOO00OO00OO0O0O0} \n\nПосмотри изменения ниже \n{OOOOOOO00000000OO} \n\n{OO0000OOO00OO0OOO}'#line:186
    bot .send_message (OOOOOOO0O0O0O0O0O .chat .id ,OO00OOOOO00000O00 ,parse_mode ='HTML')#line:187
    keys (OOOOOOO0O0O0O0O0O )#line:188
def catGen (O00OO000OO0O0OO0O ):#line:190
    O0O0OO0O00O0O0000 ="https://cat14.p.rapidapi.com/v1/images/search"#line:191
    O00O0OO0O0000000O ={"x-api-key":"live_tkfn5Qu13T9qimIfGmAxBAFooC12t7GvENwLXIoJQRTgUv83zQ8mjz5cSpzahmyK","X-RapidAPI-Key":"c50c02fb65msh3b35b9a0adb8463p13826fjsn3118fa23ceef","X-RapidAPI-Host":"cat14.p.rapidapi.com"}#line:197
    O0OO000OO0OO00OO0 =requests .get (O0O0OO0O00O0O0000 ,headers =O00O0OO0O0000000O )#line:199
    print (O0OO000OO0OO00OO0 .json ())#line:201
    O00OOOO0OO0OO0O0O =O0OO000OO0OO00OO0 .json ()#line:202
    bot .send_photo (O00OO000OO0O0OO0O .chat .id ,O00OOOO0OO0OO0O0O [0 ]['url'])#line:203
@bot .message_handler (content_types =['video'])#line:206
def message (O00O0O0OO0OO0O000 ):#line:207
    print (O00O0O0OO0OO0O000 )#line:208
@bot .message_handler (commands =['start','help'])#line:210
def keys (OOOOOOOO0000O0O00 ):#line:211
    global IsAll ,IsZamen #line:212
    OOOO00OO0OOOO0000 =types .ReplyKeyboardMarkup (row_width =2 )#line:213
    O0OO000O0O00OOOO0 =types .KeyboardButton ('Полное расписание')#line:214
    O000O0000OO000O0O =types .KeyboardButton ('Изменения')#line:215
    O0000OOOOOOOOOO00 =types .KeyboardButton ('Покажи кота😼')#line:216
    OOOO00OO0OOOO0000 .add (O0OO000O0O00OOOO0 ,O000O0000OO000O0O ,O0000OOOOOOOOOO00 )#line:217
    bot .send_message (OOOOOOOO0000O0O00 .chat .id ,'Привет😘',reply_markup =OOOO00OO0OOOO0000 )#line:218
    IsAll =False #line:219
    IsZamen =False #line:220
@bot .message_handler (func =lambda OO0OO0O0O00OOO0OO :OO0OO0O0O00OOO0OO .text =='Полное расписание')#line:222
def numb (O00OO0000OOO00O0O ):#line:223
    global IsAll #line:224
    O0O0O0OO0O0O0O0OO =types .ReplyKeyboardMarkup (row_width =5 )#line:225
    O00O0000O0O00OOO0 =types .KeyboardButton ('5А')#line:226
    O0O0OOO000OOO0OO0 =types .KeyboardButton ('5Б')#line:227
    O0OOO0O0OO0OO0OO0 =types .KeyboardButton ('5В')#line:228
    O0OOO00OO0OOOO0O0 =types .KeyboardButton ('5Г')#line:229
    OOO00O0O0000000OO =types .KeyboardButton ('5Д')#line:230
    OOO0OO0OO000000OO =types .KeyboardButton ('6А')#line:231
    O0O0O0OO00O0O0O00 =types .KeyboardButton ('6Б')#line:232
    OOOOO00O0O00OO0OO =types .KeyboardButton ('6В')#line:233
    O0OOOO0OOOO00000O =types .KeyboardButton ('6Г')#line:234
    O0O0O0OOO0OO00OOO =types .KeyboardButton ('7А')#line:235
    O000OO000OO0OO000 =types .KeyboardButton ('7Б')#line:236
    O0O00OOOO0O0OOOO0 =types .KeyboardButton ('7В')#line:237
    O000O00O00OOOO00O =types .KeyboardButton ('7Г')#line:238
    O00000OO00O0OO00O =types .KeyboardButton ('8А')#line:239
    O000O0000OOO0O0OO =types .KeyboardButton ('8Б')#line:240
    OO0O00OO00O0O0OO0 =types .KeyboardButton ('8В')#line:241
    OOO0O00O0O0OOO0OO =types .KeyboardButton ('8Г')#line:242
    O00OO00OOO0OOOOO0 =types .KeyboardButton ('9А')#line:243
    OO000O0O000OOO00O =types .KeyboardButton ('9Б')#line:244
    O0O00OO00O0O0OO00 =types .KeyboardButton ('9В')#line:245
    OO0O0O00OO000O0O0 =types .KeyboardButton ('9Г')#line:246
    OOO0O00O000000OO0 =types .KeyboardButton ('10А')#line:247
    O0OO00O0O0O0OOOOO =types .KeyboardButton ('10Б')#line:248
    O0O00OOO000OO0000 =types .KeyboardButton ('11А')#line:249
    O00OOO0O0OOOOOOOO =types .KeyboardButton ('11Б')#line:250
    OOO0OOOO0OO00O000 =types .KeyboardButton ('Назад')#line:251
    O0O0O0OO0O0O0O0OO .add (O00O0000O0O00OOO0 ,O0O0OOO000OOO0OO0 ,O0OOO0O0OO0OO0OO0 ,O0OOO00OO0OOOO0O0 ,OOO00O0O0000000OO )#line:252
    O0O0O0OO0O0O0O0OO .add (OOO0OO0OO000000OO ,O0O0O0OO00O0O0O00 ,OOOOO00O0O00OO0OO ,O0OOOO0OOOO00000O )#line:253
    O0O0O0OO0O0O0O0OO .add (O0O0O0OOO0OO00OOO ,O000OO000OO0OO000 ,O0O00OOOO0O0OOOO0 ,O000O00O00OOOO00O )#line:254
    O0O0O0OO0O0O0O0OO .add (O00000OO00O0OO00O ,O000O0000OOO0O0OO ,OO0O00OO00O0O0OO0 ,OOO0O00O0O0OOO0OO )#line:255
    O0O0O0OO0O0O0O0OO .add (O00OO00OOO0OOOOO0 ,OO000O0O000OOO00O ,O0O00OO00O0O0OO00 ,OO0O0O00OO000O0O0 )#line:256
    O0O0O0OO0O0O0O0OO .add (OOO0O00O000000OO0 ,O0OO00O0O0O0OOOOO ,O0O00OOO000OO0000 ,O00OOO0O0OOOOOOOO )#line:257
    O0O0O0OO0O0O0O0OO .add (OOO0OOOO0OO00O000 )#line:258
    bot .send_message (O00OO0000OOO00O0O .chat .id ,'Выбирай класс',reply_markup =O0O0O0OO0O0O0O0OO )#line:259
    IsAll =True #line:260
@bot .message_handler (func =lambda OO0O0O0OOOOO0O00O :OO0O0O0OOOOO0O00O .text =='Изменения')#line:262
def numbb (O00O0O0O0OOO00OO0 ):#line:263
    global IsZamen #line:264
    OOO0OO00O000OOOO0 =types .ReplyKeyboardMarkup (row_width =5 )#line:265
    OOOOOOO0000O0OO0O =types .KeyboardButton ('5А')#line:266
    OO00O000OOOO0O0O0 =types .KeyboardButton ('5Б')#line:267
    OO0OO0OO0O0O0OOOO =types .KeyboardButton ('5В')#line:268
    O00OOO0OOO00OOO00 =types .KeyboardButton ('5Г')#line:269
    O0O00000O0O0OOO0O =types .KeyboardButton ('5Д')#line:270
    O00O0000000OO00OO =types .KeyboardButton ('6А')#line:271
    O0O0000OO00000O00 =types .KeyboardButton ('6Б')#line:272
    OOOO00OO00OOOO00O =types .KeyboardButton ('6В')#line:273
    OO0OO0OO0OOOO00OO =types .KeyboardButton ('6Г')#line:274
    O0OO0O0OOOOOO0000 =types .KeyboardButton ('7А')#line:275
    OOOO000O0OO00000O =types .KeyboardButton ('7Б')#line:276
    O000O0O0OO000O000 =types .KeyboardButton ('7В')#line:277
    OO0O000OO00O0O000 =types .KeyboardButton ('7Г')#line:278
    O0OOO0O00OOO000OO =types .KeyboardButton ('8А')#line:279
    OO0O0O000000O00OO =types .KeyboardButton ('8Б')#line:280
    OO0O0000O0O000OOO =types .KeyboardButton ('8В')#line:281
    OO0O0OOOO0OOO0OOO =types .KeyboardButton ('8Г')#line:282
    OOO00OOO00OOO00OO =types .KeyboardButton ('9А')#line:283
    O0O00O00OO0OOOO00 =types .KeyboardButton ('9Б')#line:284
    O0O000OO0O0000O00 =types .KeyboardButton ('9В')#line:285
    OO00OO0000O00OO0O =types .KeyboardButton ('9Г')#line:286
    O00O0OO00OO00OO00 =types .KeyboardButton ('10А')#line:287
    O00O0O00OOO0O0OO0 =types .KeyboardButton ('10Б')#line:288
    OOO00O00OO0O00OO0 =types .KeyboardButton ('11А')#line:289
    O0OO00OOOOO0OO00O =types .KeyboardButton ('11Б')#line:290
    O000O000000OOO00O =types .KeyboardButton ('Назад')#line:291
    OOO0OO00O000OOOO0 .add (OOOOOOO0000O0OO0O ,OO00O000OOOO0O0O0 ,OO0OO0OO0O0O0OOOO ,O00OOO0OOO00OOO00 ,O0O00000O0O0OOO0O )#line:292
    OOO0OO00O000OOOO0 .add (O00O0000000OO00OO ,O0O0000OO00000O00 ,OOOO00OO00OOOO00O ,OO0OO0OO0OOOO00OO )#line:293
    OOO0OO00O000OOOO0 .add (O0OO0O0OOOOOO0000 ,OOOO000O0OO00000O ,O000O0O0OO000O000 ,OO0O000OO00O0O000 )#line:294
    OOO0OO00O000OOOO0 .add (O0OOO0O00OOO000OO ,OO0O0O000000O00OO ,OO0O0000O0O000OOO ,OO0O0OOOO0OOO0OOO )#line:295
    OOO0OO00O000OOOO0 .add (OOO00OOO00OOO00OO ,O0O00O00OO0OOOO00 ,O0O000OO0O0000O00 ,OO00OO0000O00OO0O )#line:296
    OOO0OO00O000OOOO0 .add (O00O0OO00OO00OO00 ,O00O0O00OOO0O0OO0 ,OOO00O00OO0O00OO0 ,O0OO00OOOOO0OO00O )#line:297
    OOO0OO00O000OOOO0 .add (O000O000000OOO00O )#line:298
    bot .send_message (O00O0O0O0OOO00OO0 .chat .id ,'Выбирай класс',reply_markup =OOO0OO00O000OOOO0 )#line:299
    IsZamen =True #line:300
def nokeys (O0O00O000OO00OOO0 ):#line:302
    bot .send_message (O0O00O000OO00OOO0 .chat .id ,'Убрал клавиаутру',reply_markup =types .ReplyKeyboardRemove ())#line:303
def compare_and_write_data (O0OO0OO0OO000O0OO ):#line:305
    O0OO0OO0OO000O0OO =str (O0OO0OO0OO000O0OO )#line:306
    with open ('bd.txt','r')as OO00OO000OO0O00O0 :#line:307
        O000O0OOO00OO0000 =OO00OO000OO0O00O0 .read ().splitlines ()#line:308
    O0OOOOOO00O0000O0 =[]#line:310
    for O000OO0OOO0O0OOO0 in O0OO0OO0OO000O0OO :#line:312
        if O000OO0OOO0O0OOO0 not in O000O0OOO00OO0000 :#line:313
            O0OOOOOO00O0000O0 .append (O000OO0OOO0O0OOO0 )#line:314
    if O0OOOOOO00O0000O0 :#line:316
        with open ('bd.txt','a')as OO00OO000OO0O00O0 :#line:317
            OO00OO000OO0O00O0 .write (''.join (O0OOOOOO00O0000O0 )+'\n')#line:318
def write_data (OO0O0OOO0O00OOO0O ):#line:320
    with open ('messages.txt','a')as OO00OOOO00OO0O00O :#line:321
        OO00OOOO00OO0O00O .write (''.join (OO0O0OOO0O00OOO0O )+'\n')#line:322
@bot .message_handler (content_types =['text'])#line:324
def message (OOOO00OO0O0OO00OO ):#line:325
    global day ,weekday_name ,tDay ,ress ,catt #line:326
    OOO0O00OOOO0O0OOO =f'{OOOO00OO0O0OO00OO.text} Автор: {OOOO00OO0O0OO00OO.chat.id}'#line:327
    try :#line:328
        write_data (OOO0O00OOOO0O0OOO )#line:329
    except :#line:330
        print ('Ошибка записи')#line:331
    try :#line:333
        compare_and_write_data (OOOO00OO0O0OO00OO .chat .id )#line:334
    except :#line:335
        print ('Ошибка записи')#line:336
    OOOO00OO0O0OO00OO .text =OOOO00OO0O0OO00OO .text .lower ()#line:338
    print (OOOO00OO0O0OO00OO .text ,'Автор:',OOOO00OO0O0OO00OO .chat .id )#line:339
    if 'привет'in OOOO00OO0O0OO00OO .text :#line:340
        bot .send_message (OOOO00OO0O0OO00OO .chat .id ,OOOO00OO0O0OO00OO .text )#line:341
    elif 'глобальное сообщение'in OOOO00OO0O0OO00OO .text :#line:343
        read_unique_ids (OOOO00OO0O0OO00OO )#line:344
    elif 'пришли бд'in OOOO00OO0O0OO00OO .text :#line:346
        bot .send_document (824176864 ,open ('bd.txt','rb'))#line:347
    elif 'пришли смс'in OOOO00OO0O0OO00OO .text :#line:349
        bot .send_document (824176864 ,open ('messages.txt','rb'))#line:350
    elif 'заканчиваем'in OOOO00OO0O0OO00OO .text :#line:352
        settings .BotApi ='6331392580:AAHu804LMDy1zpxEvmNpNSvpfmM6XkuOuI0'#line:353
    elif 'назад'in OOOO00OO0O0OO00OO .text :#line:355
        keys (OOOO00OO0O0OO00OO )#line:356
    elif 'убери клавиатуру'in OOOO00OO0O0OO00OO .text :#line:358
        nokeys (OOOO00OO0O0OO00OO )#line:359
    elif 'покажи кота😼'in OOOO00OO0O0OO00OO .text :#line:361
        catGen (OOOO00OO0O0OO00OO )#line:362
    elif 'расписание 5а'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '5а'in OOOO00OO0O0OO00OO .text ):#line:364
        O0O00OO00OO00O00O =settings .ПолноеРасписание5А #line:365
        fullGen (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:366
    elif 'изменения 5а'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '5а'in OOOO00OO0O0OO00OO .text ):#line:368
        OO000O000OOOO0O00 ='5А'#line:369
        zamenGen (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:370
    elif 'расписание 5б'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '5б'in OOOO00OO0O0OO00OO .text ):#line:373
        O0O00OO00OO00O00O =settings .ПолноеРасписание5Б #line:374
        fullGen (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:375
    elif 'изменения 5б'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '5б'in OOOO00OO0O0OO00OO .text ):#line:377
        OO000O000OOOO0O00 ='5Б'#line:378
        zamenGen (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:379
    elif 'расписание 5в'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '5в'in OOOO00OO0O0OO00OO .text ):#line:381
        O0O00OO00OO00O00O =settings .ПолноеРасписание5В #line:382
        fullGen (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:383
    elif 'изменения 5в'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '5в'in OOOO00OO0O0OO00OO .text ):#line:385
        OO000O000OOOO0O00 ='5В'#line:386
        zamenGen (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:387
    elif 'расписание 5г'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '5г'in OOOO00OO0O0OO00OO .text ):#line:389
        O0O00OO00OO00O00O =settings .ПолноеРасписание5Г #line:390
        fullGen (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:391
    elif 'изменения 5г'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '5г'in OOOO00OO0O0OO00OO .text ):#line:393
        OO000O000OOOO0O00 ='5Г'#line:394
        zamenGen (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:395
    elif 'расписание 5д'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '5д'in OOOO00OO0O0OO00OO .text ):#line:397
        O0O00OO00OO00O00O =settings .ПолноеРасписание5Д #line:398
        fullGen (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:399
    elif 'изменения 5д'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '5д'in OOOO00OO0O0OO00OO .text ):#line:401
        OO000O000OOOO0O00 ='5Д'#line:402
        zamenGen (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:403
    elif 'расписание 6а'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '6а'in OOOO00OO0O0OO00OO .text ):#line:405
        O0O00OO00OO00O00O =settings .ПолноеРасписание6А #line:406
        fullGen2 (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:407
    elif 'изменения 6а'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '6а'in OOOO00OO0O0OO00OO .text ):#line:409
        OO000O000OOOO0O00 ='6А'#line:410
        zamenGen2 (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:411
    elif 'расписание 6б'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '6б'in OOOO00OO0O0OO00OO .text ):#line:413
        O0O00OO00OO00O00O =settings .ПолноеРасписание6Б #line:414
        fullGen2 (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:415
    elif 'изменения 6б'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '6б'in OOOO00OO0O0OO00OO .text ):#line:417
        OO000O000OOOO0O00 ='6Б'#line:418
        zamenGen2 (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:419
    elif 'расписание 6в'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '6в'in OOOO00OO0O0OO00OO .text ):#line:421
        O0O00OO00OO00O00O =settings .ПолноеРасписание6В #line:422
        fullGen2 (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:423
    elif 'изменения 6в'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '6в'in OOOO00OO0O0OO00OO .text ):#line:425
        OO000O000OOOO0O00 ='6В'#line:426
        zamenGen2 (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:427
    elif 'расписание 6г'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '6г'in OOOO00OO0O0OO00OO .text ):#line:429
        O0O00OO00OO00O00O =settings .ПолноеРасписание6Г #line:430
        fullGen2 (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:431
    elif 'изменения 6г'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '6г'in OOOO00OO0O0OO00OO .text ):#line:433
        OO000O000OOOO0O00 ='6Г'#line:434
        zamenGen2 (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:435
    elif 'расписание 7а'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '7а'in OOOO00OO0O0OO00OO .text ):#line:437
        O0O00OO00OO00O00O =settings .ПолноеРасписание7А #line:438
        fullGen2 (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:439
    elif 'изменения 7а'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '7а'in OOOO00OO0O0OO00OO .text ):#line:441
        OO000O000OOOO0O00 ='7А'#line:442
        zamenGen2 (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:443
    elif 'расписание 7б'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '7б'in OOOO00OO0O0OO00OO .text ):#line:445
        O0O00OO00OO00O00O =settings .ПолноеРасписание7Б #line:446
        fullGen2 (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:447
    elif 'изменения 7б'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '7б'in OOOO00OO0O0OO00OO .text ):#line:449
        OO000O000OOOO0O00 ='7Б'#line:450
        zamenGen2 (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:451
    elif 'расписание 7в'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '7в'in OOOO00OO0O0OO00OO .text ):#line:453
        O0O00OO00OO00O00O =settings .ПолноеРасписание7В #line:454
        fullGen2 (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:455
    elif 'изменения 7в'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '7в'in OOOO00OO0O0OO00OO .text ):#line:457
        OO000O000OOOO0O00 ='7В'#line:458
        zamenGen2 (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:459
    elif 'расписание 7г'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '7г'in OOOO00OO0O0OO00OO .text ):#line:461
        O0O00OO00OO00O00O =settings .ПолноеРасписание7Г #line:462
        fullGen2 (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:463
    elif 'изменения 7г'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '7г'in OOOO00OO0O0OO00OO .text ):#line:465
        OO000O000OOOO0O00 ='7Г'#line:466
        zamenGen2 (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:467
    elif 'расписание 8а'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '8а'in OOOO00OO0O0OO00OO .text ):#line:469
        O0O00OO00OO00O00O =settings .ПолноеРасписание8А #line:470
        fullGen2 (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:471
    elif 'изменения 8а'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '8а'in OOOO00OO0O0OO00OO .text ):#line:473
        OO000O000OOOO0O00 ='8А'#line:474
        zamenGen2 (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:475
    elif 'расписание 8б'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '8б'in OOOO00OO0O0OO00OO .text ):#line:477
        O0O00OO00OO00O00O =settings .ПолноеРасписание8Б #line:478
        fullGen2 (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:479
    elif 'изменения 8б'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '8б'in OOOO00OO0O0OO00OO .text ):#line:481
        OO000O000OOOO0O00 ='8Б'#line:482
        zamenGen2 (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:483
    elif 'расписание 8в'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '8в'in OOOO00OO0O0OO00OO .text ):#line:485
        O0O00OO00OO00O00O =settings .ПолноеРасписание8В #line:486
        fullGen2 (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:487
    elif 'изменения 8в'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '8в'in OOOO00OO0O0OO00OO .text ):#line:489
        OO000O000OOOO0O00 ='8В'#line:490
        zamenGen2 (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:491
    elif 'расписание 8г'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '8г'in OOOO00OO0O0OO00OO .text ):#line:493
        O0O00OO00OO00O00O =settings .ПолноеРасписание8Г #line:494
        fullGen2 (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:495
    elif 'изменения 8г'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '8г'in OOOO00OO0O0OO00OO .text ):#line:497
        OO000O000OOOO0O00 ='8Г'#line:498
        zamenGen2 (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:499
    elif 'расписание 9а'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '9а'in OOOO00OO0O0OO00OO .text ):#line:501
        O0O00OO00OO00O00O =settings .ПолноеРасписание9А #line:502
        fullGen (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:503
    elif 'изменения 9а'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '9а'in OOOO00OO0O0OO00OO .text ):#line:505
        OO000O000OOOO0O00 ='9А'#line:506
        zamenGen (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:507
    elif 'расписание 9б'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '9б'in OOOO00OO0O0OO00OO .text ):#line:509
        O0O00OO00OO00O00O =settings .ПолноеРасписание9Б #line:510
        fullGen (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:511
    elif 'изменения 9б'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '9б'in OOOO00OO0O0OO00OO .text ):#line:513
        OO000O000OOOO0O00 ='9Б'#line:514
        zamenGen (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:515
    elif 'расписание 9в'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '9в'in OOOO00OO0O0OO00OO .text ):#line:517
        O0O00OO00OO00O00O =settings .ПолноеРасписание9В #line:518
        fullGen (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:519
    elif 'изменения 9в'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '9в'in OOOO00OO0O0OO00OO .text ):#line:521
        OO000O000OOOO0O00 ='9В'#line:522
        zamenGen (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:523
    elif 'расписание 9г'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '9г'in OOOO00OO0O0OO00OO .text ):#line:525
        O0O00OO00OO00O00O =settings .ПолноеРасписание9Г #line:526
        fullGen (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:527
    elif 'изменения 9г'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '9г'in OOOO00OO0O0OO00OO .text ):#line:529
        OO000O000OOOO0O00 ='9Г'#line:530
        zamenGen (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:531
    elif 'расписание 10а'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '10а'in OOOO00OO0O0OO00OO .text ):#line:533
        O0O00OO00OO00O00O =settings .ПолноеРасписание10А #line:534
        fullGen (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:535
    elif 'изменения 10а'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '10а'in OOOO00OO0O0OO00OO .text ):#line:537
        OO000O000OOOO0O00 ='10А'#line:538
        zamenGen (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:539
    elif 'расписание 10б'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '10б'in OOOO00OO0O0OO00OO .text ):#line:541
        O0O00OO00OO00O00O =settings .ПолноеРасписание10Б #line:542
        fullGen (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:543
    elif 'изменения 10б'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '10б'in OOOO00OO0O0OO00OO .text ):#line:545
        OO000O000OOOO0O00 ='10Б'#line:546
        zamenGen (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:547
    elif 'расписание 11а'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '11а'in OOOO00OO0O0OO00OO .text ):#line:549
        O0O00OO00OO00O00O =settings .ПолноеРасписание11А #line:550
        fullGen (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:551
    elif 'изменения 11а'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '11а'in OOOO00OO0O0OO00OO .text ):#line:553
        OO000O000OOOO0O00 ='11А'#line:554
        zamenGen (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:555
    elif 'расписание 11б'in OOOO00OO0O0OO00OO .text or (IsAll ==True and '11б'in OOOO00OO0O0OO00OO .text ):#line:557
        O0O00OO00OO00O00O =settings .ПолноеРасписание11Б #line:558
        fullGen (OOOO00OO0O0OO00OO ,O0O00OO00OO00O00O )#line:559
    elif 'изменения 11б'in OOOO00OO0O0OO00OO .text or (IsZamen ==True and '11б'in OOOO00OO0O0OO00OO .text ):#line:561
        OO000O000OOOO0O00 ='11Б'#line:562
        zamenGen (OOOO00OO0O0OO00OO ,OO000O000OOOO0O00 )#line:563
    else :#line:565
        bot .send_message (OOOO00OO0O0OO00OO .chat .id ,'Не распознал сообщение')#line:566
bot .infinity_polling ()