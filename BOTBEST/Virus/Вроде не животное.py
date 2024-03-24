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
catt =1 #line:16
bot =telebot .TeleBot (settings .BotApi )#line:17
Smile_stident ='👨‍🎓'#line:18
Smile_palec ='👇'#line:19
Smile_glaza ='👀'#line:20
bold ="parse_mode='HTML'"#line:21
daysOfWeek =["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]#line:22
day =''#line:23
IsZamen =False #line:24
IsAll =False #line:25
def zamenGen2 (O000O0000000OO00O ,OO0O0OO0O0000O000 ):#line:28
    OO0OOOOOO00O00O0O =datetime .date .today ()#line:29
    O0OO00000O0OOO0OO =OO0OOOOOO00O00O0O .weekday ()#line:30
    OOOOO0000000OOOO0 =daysOfWeek [O0OO00000O0OOO0OO ]#line:31
    bot .send_message (O000O0000000OO00O .chat .id ,'Смотрю везде, где только можно🔎')#line:32
    if OOOOO0000000OOOO0 =='Понедельник':#line:33
        OOO00OO0O00000O0O ='Понедельник'+OO0O0OO0O0000O000 #line:34
        O0OOOO00OOOO00OO0 =getattr (settings ,OOO00OO0O00000O0O )#line:35
    elif OOOOO0000000OOOO0 =='Вторник':#line:36
        OOO00OO0O00000O0O ='Вторник'+OO0O0OO0O0000O000 #line:37
        O0OOOO00OOOO00OO0 =getattr (settings ,OOO00OO0O00000O0O )#line:38
    elif OOOOO0000000OOOO0 =='Среда':#line:39
        OOO00OO0O00000O0O ='Среда'+OO0O0OO0O0000O000 #line:40
        O0OOOO00OOOO00OO0 =getattr (settings ,OOO00OO0O00000O0O )#line:41
    elif OOOOO0000000OOOO0 =='Четверг':#line:42
        OOO00OO0O00000O0O ='Четверг'+OO0O0OO0O0000O000 #line:43
        O0OOOO00OOOO00OO0 =getattr (settings ,OOO00OO0O00000O0O )#line:44
    elif OOOOO0000000OOOO0 =='Пятница':#line:45
        OOO00OO0O00000O0O ='Пятница'+OO0O0OO0O0000O000 #line:46
        O0OOOO00OOOO00OO0 =getattr (settings ,OOO00OO0O00000O0O )#line:47
    elif OOOOO0000000OOOO0 =='Суббота':#line:48
        OOO00OO0O00000O0O ='Понедельник'+OO0O0OO0O0000O000 #line:49
        O0OOOO00OOOO00OO0 =getattr (settings ,OOO00OO0O00000O0O )#line:50
    elif OOOOO0000000OOOO0 =='Воскресенье':#line:51
        OOO00OO0O00000O0O ='Понедельник'+OO0O0OO0O0000O000 #line:52
        O0OOOO00OOOO00OO0 =getattr (settings ,OOO00OO0O00000O0O )#line:53
    Day .clear ()#line:55
    O0OOOO0OOO00OO00O =Day .main (O0OOOO00OOOO00OO0 )#line:56
    for OO0O0O000O0O0OO00 in range (len (O0OOOO0OOO00OO00O )):#line:57
        OO000000O00OO0O0O ='\n'.join (O0OOOO0OOO00OO00O )#line:58
    bot .send_message (O000O0000000OO00O .chat .id ,'Жду ответа⏳')#line:60
    O0OOOO00OOOO00OO0 =settings .Замены6А #line:61
    Zamen .clear ()#line:62
    OO0OOO0O0OO0OO0O0 =Zamen .main (O0OOOO00OOOO00OO0 )#line:63
    for OO0O0O000O0O0OO00 in range (len (OO0OOO0O0OO0OO0O0 )):#line:64
        O0O0O0OO000O000O0 ='\n'.join (OO0OOO0O0OO0OO0O0 )#line:65
    bot .send_message (O000O0000000OO00O .chat .id ,'Ответ получен✅')#line:67
    CheckDateSheets2 .clear ()#line:69
    OO0OOOOOO00O00O0O =CheckDateSheets2 .main ()#line:70
    try :#line:71
        for OO0O0O000O0O0OO00 in range (len (OO0OOOOOO00O00O0O )):#line:72
            O000O0OO0O0OO0OO0 ='\n'.join (OO0OOOOOO00O00O0O )#line:73
            O000O0OO0O0OO0OO0 =f"<b>{O000O0OO0O0OO0OO0}</b>"#line:74
    except :#line:75
        O000O0OO0O0OO0OO0 =f"<i>Ошибка в поиске даты</i>"#line:76
    if OOOOO0000000OOOO0 !='Суббота'and OOOOO0000000OOOO0 !='Воскресенье':#line:78
        if OOOOO0000000OOOO0 !='Четверг'and OOOOO0000000OOOO0 !='Понедельник'and OOOOO0000000OOOO0 !='Вторник':#line:79
            O000000O0O0O000OO =OOOOO0000000OOOO0 [:-1 ]+'у'#line:80
        else :#line:81
            O000000O0O0O000OO =OOOOO0000000OOOO0 #line:82
    else :#line:83
        O000000O0O0O000OO ='Понедельник'#line:84
    O0O000O00O00O0OOO =f'Вот твое обычное расписание на <b>{O000000O0O0O000OO}</b> \n{OO000000O00OO0O0O} \n\nПосмотри изменения ниже \n{O000O0OO0O0OO0OO0} \n\n{O0O0O0OO000O000O0}'#line:85
    bot .send_message (O000O0000000OO00O .chat .id ,O0O000O00O00O0OOO ,parse_mode ='HTML')#line:86
    keys (O000O0000000OO00O )#line:87
def fullGen2 (OOO0OOOOOO0OOO0O0 ,OOOOO00O00OOO0OOO ):#line:90
    ALL2 .clear ()#line:91
    OO000O0OO000OO00O =ALL2 .main (OOOOO00O00OOO0OOO )#line:92
    for O00OO0OO000000O00 in range (len (OO000O0OO000OO00O )):#line:93
        O00O0O00O00OO00O0 ='\n'.join (OO000O0OO000OO00O )#line:94
    bot .send_message (OOO0OOOOOO0OOO0O0 .chat .id ,O00O0O00O00OO00O0 ,parse_mode ='HTML')#line:95
    keys (OOO0OOOOOO0OOO0O0 )#line:96
def fullGen (OO0OOO0000OOO00O0 ,O0000OOOOO0O00O0O ):#line:98
    ALL .clear ()#line:99
    OO0O0O0OOOO0OO0O0 =ALL .main (O0000OOOOO0O00O0O )#line:101
    for OO0000O000O0OOOO0 in range (len (OO0O0O0OOOO0OO0O0 )):#line:102
        OOO0OO00OOO000OO0 ='\n'.join (OO0O0O0OOOO0OO0O0 )#line:103
    bot .send_message (OO0OOO0000OOO00O0 .chat .id ,OOO0OO00OOO000OO0 ,parse_mode ='HTML')#line:104
    keys (OO0OOO0000OOO00O0 )#line:105
def zamenGen (OOO00OO0O0OOOO0O0 ,O0OO0OOO00OO00000 ):#line:107
    O0O0000O000OOO00O =datetime .date .today ()#line:108
    O0OOOO0OOOO0O0O00 =O0O0000O000OOO00O .weekday ()#line:109
    OOO00O00OO00OOOOO =daysOfWeek [O0OOOO0OOOO0O0O00 ]#line:110
    bot .send_message (OOO00OO0O0OOOO0O0 .chat .id ,'Смотрю везде, где только можно🔎')#line:111
    if OOO00O00OO00OOOOO =='Понедельник':#line:112
        OOOOOOOOOO00O0OOO ='Понедельник'+O0OO0OOO00OO00000 #line:113
        O0OOOO0OO00OO00OO =getattr (settings ,OOOOOOOOOO00O0OOO )#line:114
    elif OOO00O00OO00OOOOO =='Вторник':#line:115
        OOOOOOOOOO00O0OOO ='Вторник'+O0OO0OOO00OO00000 #line:116
        O0OOOO0OO00OO00OO =getattr (settings ,OOOOOOOOOO00O0OOO )#line:117
    elif OOO00O00OO00OOOOO =='Среда':#line:118
        OOOOOOOOOO00O0OOO ='Среда'+O0OO0OOO00OO00000 #line:119
        O0OOOO0OO00OO00OO =getattr (settings ,OOOOOOOOOO00O0OOO )#line:120
    elif OOO00O00OO00OOOOO =='Четверг':#line:121
        OOOOOOOOOO00O0OOO ='Четверг'+O0OO0OOO00OO00000 #line:122
        O0OOOO0OO00OO00OO =getattr (settings ,OOOOOOOOOO00O0OOO )#line:123
    elif OOO00O00OO00OOOOO =='Пятница':#line:124
        OOOOOOOOOO00O0OOO ='Пятница'+O0OO0OOO00OO00000 #line:125
        O0OOOO0OO00OO00OO =getattr (settings ,OOOOOOOOOO00O0OOO )#line:126
    elif OOO00O00OO00OOOOO =='Суббота':#line:127
        OOOOOOOOOO00O0OOO ='Понедельник'+O0OO0OOO00OO00000 #line:128
        O0OOOO0OO00OO00OO =getattr (settings ,OOOOOOOOOO00O0OOO )#line:129
    elif OOO00O00OO00OOOOO =='Воскресенье':#line:130
        OOOOOOOOOO00O0OOO ='Понедельник'+O0OO0OOO00OO00000 #line:131
        O0OOOO0OO00OO00OO =getattr (settings ,OOOOOOOOOO00O0OOO )#line:132
    Day .clear ()#line:134
    OOO00O0000O00OO00 =Day .main (O0OOOO0OO00OO00OO )#line:135
    for OO0OOO0000OO00000 in range (len (OOO00O0000O00OO00 )):#line:136
        O0O0OO0OO000OO0OO ='\n'.join (OOO00O0000O00OO00 )#line:137
    bot .send_message (OOO00OO0O0OOOO0O0 .chat .id ,'Жду ответа⏳')#line:139
    OOOOOOOOOO00O0OOO ='Замены'+O0OO0OOO00OO00000 #line:140
    O0OOOO0OO00OO00OO =getattr (settings ,OOOOOOOOOO00O0OOO )#line:141
    Zamen .clear ()#line:142
    OOOOOOO0OO0O0O0O0 =Zamen .main (O0OOOO0OO00OO00OO )#line:143
    for OO0OOO0000OO00000 in range (len (OOOOOOO0OO0O0O0O0 )):#line:144
        OOO0OOOOOO000OOOO ='\n'.join (OOOOOOO0OO0O0O0O0 )#line:145
    bot .send_message (OOO00OO0O0OOOO0O0 .chat .id ,'Ответ получен✅')#line:147
    CheckDateSheets1 .clear ()#line:148
    O0O0000O000OOO00O =CheckDateSheets1 .main ()#line:149
    try :#line:150
        for OO0OOO0000OO00000 in range (len (O0O0000O000OOO00O )):#line:151
            O0OO0OO0OO0O0OOO0 ='\n'.join (O0O0000O000OOO00O )#line:152
            O0OO0OO0OO0O0OOO0 =f"<b>{O0OO0OO0OO0O0OOO0}</b>"#line:153
    except :#line:154
        O0OO0OO0OO0O0OOO0 =f"<i>Ошибка в поиске даты</i>"#line:155
    if OOO00O00OO00OOOOO !='Суббота'and OOO00O00OO00OOOOO !='Воскресенье':#line:157
        if OOO00O00OO00OOOOO !='Четверг'and OOO00O00OO00OOOOO !='Понедельник'and OOO00O00OO00OOOOO !='Вторник':#line:158
            OO000OOOO0OO00OOO =OOO00O00OO00OOOOO [:-1 ]+'у'#line:159
        else :#line:160
            OO000OOOO0OO00OOO =OOO00O00OO00OOOOO #line:161
    else :#line:162
        OO000OOOO0OO00OOO ='Понедельник'#line:163
    OOO00O0OOOOO00O00 =f'Вот твое обычное расписание на <b>{OO000OOOO0OO00OOO}</b> \n{O0O0OO0OO000OO0OO} \n\nПосмотри изменения ниже \n{O0OO0OO0OO0O0OOO0} \n\n{OOO0OOOOOO000OOOO}'#line:164
    bot .send_message (OOO00OO0O0OOOO0O0 .chat .id ,OOO00O0OOOOO00O00 ,parse_mode ='HTML')#line:165
    keys (OOO00OO0O0OOOO0O0 )#line:166
def catGen (O00OOOOO00000O0O0 ):#line:168
    O000O0OOOOO0O0O00 ="https://cat14.p.rapidapi.com/v1/images/search"#line:169
    OOOOOOO0O0OO00O00 ={"x-api-key":"live_tkfn5Qu13T9qimIfGmAxBAFooC12t7GvENwLXIoJQRTgUv83zQ8mjz5cSpzahmyK","X-RapidAPI-Key":"c50c02fb65msh3b35b9a0adb8463p13826fjsn3118fa23ceef","X-RapidAPI-Host":"cat14.p.rapidapi.com"}#line:175
    OO000000O00OOOO0O =requests .get (O000O0OOOOO0O0O00 ,headers =OOOOOOO0O0OO00O00 )#line:177
    print (OO000000O00OOOO0O .json ())#line:179
    O0O000OOO00OOO0O0 =OO000000O00OOOO0O .json ()#line:180
    bot .send_photo (O00OOOOO00000O0O0 .chat .id ,O0O000OOO00OOO0O0 [0 ]['url'])#line:181
@bot .message_handler (content_types =['video'])#line:184
def message (OOOO00000OOO00O00 ):#line:185
    print (OOOO00000OOO00O00 )#line:186
@bot .message_handler (commands =['start','help'])#line:188
def keys (O0OOOO0O00OO0OOO0 ):#line:189
    global IsAll ,IsZamen #line:190
    O0O00OO00O0OOOOOO =types .ReplyKeyboardMarkup (row_width =2 )#line:191
    O0000OOO0O000000O =types .KeyboardButton ('Полное расписание')#line:192
    OOO0O0O0OOOOO0000 =types .KeyboardButton ('Изменения')#line:193
    O0O0O0OO0OOO0000O =types .KeyboardButton ('Покажи кота😼')#line:194
    O0O00OO00O0OOOOOO .add (O0000OOO0O000000O ,OOO0O0O0OOOOO0000 ,O0O0O0OO0OOO0000O )#line:195
    bot .send_message (O0OOOO0O00OO0OOO0 .chat .id ,'Привет😘',reply_markup =O0O00OO00O0OOOOOO )#line:196
    IsAll =False #line:197
    IsZamen =False #line:198
@bot .message_handler (func =lambda O0O0O0OOOOOOO00OO :O0O0O0OOOOOOO00OO .text =='Полное расписание')#line:200
def numb (OOOO0OO00O0OO000O ):#line:201
    global IsAll #line:202
    O000O0O00O0O0O00O =types .ReplyKeyboardMarkup (row_width =5 )#line:203
    O0OO000O0OOO0O00O =types .KeyboardButton ('5А')#line:204
    OO000O00O00O0OO00 =types .KeyboardButton ('5Б')#line:205
    OOOOOO0O0OO00O0OO =types .KeyboardButton ('5В')#line:206
    OO00O0O00O0O00OO0 =types .KeyboardButton ('5Г')#line:207
    O0OO000O0OOOO0O00 =types .KeyboardButton ('5Д')#line:208
    OO000O00OOOOOOO0O =types .KeyboardButton ('6А')#line:209
    OOO0000O0OOO000O0 =types .KeyboardButton ('6Б')#line:210
    O000000OOOOO00O00 =types .KeyboardButton ('6В')#line:211
    O0OOOOOOO0OO00O00 =types .KeyboardButton ('6Г')#line:212
    O0OO00O000OO0OO00 =types .KeyboardButton ('7А')#line:213
    O0OOOO0000O000O0O =types .KeyboardButton ('7Б')#line:214
    O0OOOOOO00000O00O =types .KeyboardButton ('7В')#line:215
    O000O00OO0OO0O00O =types .KeyboardButton ('7Г')#line:216
    OO0O0O0O00OOO00O0 =types .KeyboardButton ('8А')#line:217
    OO0OOOO000OO000O0 =types .KeyboardButton ('8Б')#line:218
    O0OOOOOOOOO0O00OO =types .KeyboardButton ('8В')#line:219
    O0OOO00OOO000OO0O =types .KeyboardButton ('8Г')#line:220
    O00000OO0O0O000O0 =types .KeyboardButton ('9А')#line:221
    OOO00OOOOOOOOO000 =types .KeyboardButton ('9Б')#line:222
    OO0000O0OO0O0OO00 =types .KeyboardButton ('9В')#line:223
    O00O0O0O0OO000O00 =types .KeyboardButton ('9Г')#line:224
    OOO00O0O00O0O0O00 =types .KeyboardButton ('10А')#line:225
    O00O0000OOO0000O0 =types .KeyboardButton ('10Б')#line:226
    OO0O0O0O0O0O00OO0 =types .KeyboardButton ('11А')#line:227
    O00OO0OOOOOOO0000 =types .KeyboardButton ('11Б')#line:228
    O00O0000O00O0OO0O =types .KeyboardButton ('Назад')#line:229
    O000O0O00O0O0O00O .add (O0OO000O0OOO0O00O ,OO000O00O00O0OO00 ,OOOOOO0O0OO00O0OO ,OO00O0O00O0O00OO0 ,O0OO000O0OOOO0O00 )#line:230
    O000O0O00O0O0O00O .add (OO000O00OOOOOOO0O ,OOO0000O0OOO000O0 ,O000000OOOOO00O00 ,O0OOOOOOO0OO00O00 )#line:231
    O000O0O00O0O0O00O .add (O0OO00O000OO0OO00 ,O0OOOO0000O000O0O ,O0OOOOOO00000O00O ,O000O00OO0OO0O00O )#line:232
    O000O0O00O0O0O00O .add (OO0O0O0O00OOO00O0 ,OO0OOOO000OO000O0 ,O0OOOOOOOOO0O00OO ,O0OOO00OOO000OO0O )#line:233
    O000O0O00O0O0O00O .add (O00000OO0O0O000O0 ,OOO00OOOOOOOOO000 ,OO0000O0OO0O0OO00 ,O00O0O0O0OO000O00 )#line:234
    O000O0O00O0O0O00O .add (OOO00O0O00O0O0O00 ,O00O0000OOO0000O0 ,OO0O0O0O0O0O00OO0 ,O00OO0OOOOOOO0000 )#line:235
    O000O0O00O0O0O00O .add (O00O0000O00O0OO0O )#line:236
    bot .send_message (OOOO0OO00O0OO000O .chat .id ,'Выбирай класс',reply_markup =O000O0O00O0O0O00O )#line:237
    IsAll =True #line:238
@bot .message_handler (func =lambda OOOO0OOOO0O0O00OO :OOOO0OOOO0O0O00OO .text =='Изменения')#line:240
def numbb (O0O00O0OO00OO0O0O ):#line:241
    global IsZamen #line:242
    OO00OOOO000OOO0O0 =types .ReplyKeyboardMarkup (row_width =5 )#line:243
    O0O00O00OO0O0O00O =types .KeyboardButton ('5А')#line:244
    O00OO0000OO000O00 =types .KeyboardButton ('5Б')#line:245
    O00O0OO0O0O0000O0 =types .KeyboardButton ('5В')#line:246
    O00OOO0O00000OO00 =types .KeyboardButton ('5Г')#line:247
    O0O000000OOOOOOO0 =types .KeyboardButton ('5Д')#line:248
    OOOOO0O0000OO000O =types .KeyboardButton ('6А')#line:249
    O0O0OOO0OO00OO00O =types .KeyboardButton ('6Б')#line:250
    O0OO0OOOO000000OO =types .KeyboardButton ('6В')#line:251
    O0O0O0OO000000OOO =types .KeyboardButton ('6Г')#line:252
    O0O0O0O000O00OO0O =types .KeyboardButton ('7А')#line:253
    OOO000000O0OO000O =types .KeyboardButton ('7Б')#line:254
    O0O0OOO000O0O0O0O =types .KeyboardButton ('7В')#line:255
    OOOOO00O00O0O0000 =types .KeyboardButton ('7Г')#line:256
    O0O0000O0OO00OO00 =types .KeyboardButton ('8А')#line:257
    O00OOOO0000OO00O0 =types .KeyboardButton ('8Б')#line:258
    O0O0OOOOO0OO00000 =types .KeyboardButton ('8В')#line:259
    OOOOOOO00OOO00O00 =types .KeyboardButton ('8Г')#line:260
    OOOOO0OO0OO00O0OO =types .KeyboardButton ('9А')#line:261
    O00O00OOOOO0O0000 =types .KeyboardButton ('9Б')#line:262
    OO00OOO0OOO00OO00 =types .KeyboardButton ('9В')#line:263
    OO0000O000O00O0OO =types .KeyboardButton ('9Г')#line:264
    O0OO0OOO000O0O0OO =types .KeyboardButton ('10А')#line:265
    O00OOO0OOO0O0OOOO =types .KeyboardButton ('10Б')#line:266
    O0O00O000O0OOO00O =types .KeyboardButton ('11А')#line:267
    OOO00000O0OO00000 =types .KeyboardButton ('11Б')#line:268
    O00OO000OOOOO0000 =types .KeyboardButton ('Назад')#line:269
    OO00OOOO000OOO0O0 .add (O0O00O00OO0O0O00O ,O00OO0000OO000O00 ,O00O0OO0O0O0000O0 ,O00OOO0O00000OO00 ,O0O000000OOOOOOO0 )#line:270
    OO00OOOO000OOO0O0 .add (OOOOO0O0000OO000O ,O0O0OOO0OO00OO00O ,O0OO0OOOO000000OO ,O0O0O0OO000000OOO )#line:271
    OO00OOOO000OOO0O0 .add (O0O0O0O000O00OO0O ,OOO000000O0OO000O ,O0O0OOO000O0O0O0O ,OOOOO00O00O0O0000 )#line:272
    OO00OOOO000OOO0O0 .add (O0O0000O0OO00OO00 ,O00OOOO0000OO00O0 ,O0O0OOOOO0OO00000 ,OOOOOOO00OOO00O00 )#line:273
    OO00OOOO000OOO0O0 .add (OOOOO0OO0OO00O0OO ,O00O00OOOOO0O0000 ,OO00OOO0OOO00OO00 ,OO0000O000O00O0OO )#line:274
    OO00OOOO000OOO0O0 .add (O0OO0OOO000O0O0OO ,O00OOO0OOO0O0OOOO ,O0O00O000O0OOO00O ,OOO00000O0OO00000 )#line:275
    OO00OOOO000OOO0O0 .add (O00OO000OOOOO0000 )#line:276
    bot .send_message (O0O00O0OO00OO0O0O .chat .id ,'Выбирай класс',reply_markup =OO00OOOO000OOO0O0 )#line:277
    IsZamen =True #line:278
def nokeys (O00OOOOOOO00O0O00 ):#line:280
    bot .send_message (O00OOOOOOO00O0O00 .chat .id ,'Убрал клавиаутру',reply_markup =types .ReplyKeyboardRemove ())#line:281
def compare_and_write_data (OOO0O0OO0OOO0O0O0 ):#line:283
    OOO0O0OO0OOO0O0O0 =str (OOO0O0OO0OOO0O0O0 )#line:284
    with open ('bd.txt','r')as O0O0OOOO0OOO0O0O0 :#line:285
        OOOOOOOO00O0O0OO0 =O0O0OOOO0OOO0O0O0 .read ().splitlines ()#line:286
    O0OO0OOOOOOO00000 =[]#line:288
    for O0OOO000O0O0O0O0O in OOO0O0OO0OOO0O0O0 :#line:290
        if O0OOO000O0O0O0O0O not in OOOOOOOO00O0O0OO0 :#line:291
            O0OO0OOOOOOO00000 .append (O0OOO000O0O0O0O0O )#line:292
    if O0OO0OOOOOOO00000 :#line:294
        with open ('bd.txt','a')as O0O0OOOO0OOO0O0O0 :#line:295
            O0O0OOOO0OOO0O0O0 .write (''.join (O0OO0OOOOOOO00000 )+'\n')#line:296
def write_data (OOOOOO00O00O000OO ):#line:298
    with open ('messages.txt','a')as O00O0O0OO0OO0OOO0 :#line:299
        O00O0O0OO0OO0OOO0 .write (''.join (OOOOOO00O00O000OO )+'\n')#line:300
@bot .message_handler (content_types =['text'])#line:302
def message (O0OO00O0O00O0O0O0 ):#line:303
    global day ,weekday_name ,tDay ,ress ,catt #line:304
    O0000O0OO0O0O000O =f'{O0OO00O0O00O0O0O0.text} Автор: {O0OO00O0O00O0O0O0.chat.id}'#line:305
    try :#line:306
        write_data (O0000O0OO0O0O000O )#line:307
    except :#line:308
        print ('Ошибка записи')#line:309
    try :#line:311
        compare_and_write_data (O0OO00O0O00O0O0O0 .chat .id )#line:312
    except :#line:313
        print ('Ошибка записи')#line:314
    O0OO00O0O00O0O0O0 .text =O0OO00O0O00O0O0O0 .text .lower ()#line:316
    print (O0OO00O0O00O0O0O0 .text ,'Автор:',O0OO00O0O00O0O0O0 .chat .id )#line:317
    if 'привет'in O0OO00O0O00O0O0O0 .text :#line:318
        bot .send_message (O0OO00O0O00O0O0O0 .chat .id ,O0OO00O0O00O0O0O0 .text )#line:319
    elif 'пришли бд'in O0OO00O0O00O0O0O0 .text :#line:321
        bot .send_document (824176864 ,open ('bd.txt','rb'))#line:322
    elif 'пришли смс'in O0OO00O0O00O0O0O0 .text :#line:324
        bot .send_document (824176864 ,open ('messages.txt','rb'))#line:325
    elif 'заканчиваем'in O0OO00O0O00O0O0O0 .text :#line:327
        settings .BotApi ='6331392580:AAHu804LMDy1zpxEvmNpNSvpfmM6XkuOuI0'#line:328
    elif 'назад'in O0OO00O0O00O0O0O0 .text :#line:330
        keys (O0OO00O0O00O0O0O0 )#line:331
    elif 'убери клавиатуру'in O0OO00O0O00O0O0O0 .text :#line:333
        nokeys (O0OO00O0O00O0O0O0 )#line:334
    elif 'покажи кота😼'in O0OO00O0O00O0O0O0 .text :#line:336
        catGen (O0OO00O0O00O0O0O0 )#line:337
    elif 'расписание 5а'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '5а'in O0OO00O0O00O0O0O0 .text ):#line:339
        O0OOO000O000O0OO0 =settings .ПолноеРасписание5А #line:340
        fullGen (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:341
    elif 'изменения 5а'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '5а'in O0OO00O0O00O0O0O0 .text ):#line:343
        OOOOO0O0O000OO0OO ='5А'#line:344
        zamenGen (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:345
    elif 'расписание 5б'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '5б'in O0OO00O0O00O0O0O0 .text ):#line:348
        O0OOO000O000O0OO0 =settings .ПолноеРасписание5Б #line:349
        fullGen (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:350
    elif 'изменения 5б'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '5б'in O0OO00O0O00O0O0O0 .text ):#line:352
        OOOOO0O0O000OO0OO ='5Б'#line:353
        zamenGen (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:354
    elif 'расписание 5в'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '5в'in O0OO00O0O00O0O0O0 .text ):#line:356
        O0OOO000O000O0OO0 =settings .ПолноеРасписание5В #line:357
        fullGen (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:358
    elif 'изменения 5в'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '5в'in O0OO00O0O00O0O0O0 .text ):#line:360
        OOOOO0O0O000OO0OO ='5В'#line:361
        zamenGen (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:362
    elif 'расписание 5г'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '5г'in O0OO00O0O00O0O0O0 .text ):#line:364
        O0OOO000O000O0OO0 =settings .ПолноеРасписание5Г #line:365
        fullGen (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:366
    elif 'изменения 5г'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '5г'in O0OO00O0O00O0O0O0 .text ):#line:368
        OOOOO0O0O000OO0OO ='5Г'#line:369
        zamenGen (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:370
    elif 'расписание 5д'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '5д'in O0OO00O0O00O0O0O0 .text ):#line:372
        O0OOO000O000O0OO0 =settings .ПолноеРасписание5Д #line:373
        fullGen (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:374
    elif 'изменения 5д'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '5д'in O0OO00O0O00O0O0O0 .text ):#line:376
        OOOOO0O0O000OO0OO ='5Д'#line:377
        zamenGen (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:378
    elif 'расписание 6а'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '6а'in O0OO00O0O00O0O0O0 .text ):#line:380
        O0OOO000O000O0OO0 =settings .ПолноеРасписание6А #line:381
        fullGen2 (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:382
    elif 'изменения 6а'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '6а'in O0OO00O0O00O0O0O0 .text ):#line:384
        OOOOO0O0O000OO0OO ='6А'#line:385
        zamenGen2 (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:386
    elif 'расписание 6б'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '6б'in O0OO00O0O00O0O0O0 .text ):#line:388
        O0OOO000O000O0OO0 =settings .ПолноеРасписание6Б #line:389
        fullGen2 (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:390
    elif 'изменения 6б'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '6б'in O0OO00O0O00O0O0O0 .text ):#line:392
        OOOOO0O0O000OO0OO ='6Б'#line:393
        zamenGen2 (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:394
    elif 'расписание 6в'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '6в'in O0OO00O0O00O0O0O0 .text ):#line:396
        O0OOO000O000O0OO0 =settings .ПолноеРасписание6В #line:397
        fullGen2 (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:398
    elif 'изменения 6в'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '6в'in O0OO00O0O00O0O0O0 .text ):#line:400
        OOOOO0O0O000OO0OO ='6В'#line:401
        zamenGen2 (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:402
    elif 'расписание 6г'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '6г'in O0OO00O0O00O0O0O0 .text ):#line:404
        O0OOO000O000O0OO0 =settings .ПолноеРасписание6Г #line:405
        fullGen2 (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:406
    elif 'изменения 6г'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '6г'in O0OO00O0O00O0O0O0 .text ):#line:408
        OOOOO0O0O000OO0OO ='6Г'#line:409
        zamenGen2 (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:410
    elif 'расписание 7а'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '7а'in O0OO00O0O00O0O0O0 .text ):#line:412
        O0OOO000O000O0OO0 =settings .ПолноеРасписание7А #line:413
        fullGen2 (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:414
    elif 'изменения 7а'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '7а'in O0OO00O0O00O0O0O0 .text ):#line:416
        OOOOO0O0O000OO0OO ='7А'#line:417
        zamenGen2 (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:418
    elif 'расписание 7б'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '7б'in O0OO00O0O00O0O0O0 .text ):#line:420
        O0OOO000O000O0OO0 =settings .ПолноеРасписание7Б #line:421
        fullGen2 (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:422
    elif 'изменения 7б'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '7б'in O0OO00O0O00O0O0O0 .text ):#line:424
        OOOOO0O0O000OO0OO ='7Б'#line:425
        zamenGen2 (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:426
    elif 'расписание 7в'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '7в'in O0OO00O0O00O0O0O0 .text ):#line:428
        O0OOO000O000O0OO0 =settings .ПолноеРасписание7В #line:429
        fullGen2 (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:430
    elif 'изменения 7в'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '7в'in O0OO00O0O00O0O0O0 .text ):#line:432
        OOOOO0O0O000OO0OO ='7В'#line:433
        zamenGen2 (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:434
    elif 'расписание 7г'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '7г'in O0OO00O0O00O0O0O0 .text ):#line:436
        O0OOO000O000O0OO0 =settings .ПолноеРасписание7Г #line:437
        fullGen2 (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:438
    elif 'изменения 7г'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '7г'in O0OO00O0O00O0O0O0 .text ):#line:440
        OOOOO0O0O000OO0OO ='7Г'#line:441
        zamenGen2 (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:442
    elif 'расписание 8а'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '8а'in O0OO00O0O00O0O0O0 .text ):#line:444
        O0OOO000O000O0OO0 =settings .ПолноеРасписание8А #line:445
        fullGen2 (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:446
    elif 'изменения 8а'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '8а'in O0OO00O0O00O0O0O0 .text ):#line:448
        OOOOO0O0O000OO0OO ='8А'#line:449
        zamenGen2 (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:450
    elif 'расписание 8б'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '8б'in O0OO00O0O00O0O0O0 .text ):#line:452
        O0OOO000O000O0OO0 =settings .ПолноеРасписание8Б #line:453
        fullGen2 (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:454
    elif 'изменения 8б'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '8б'in O0OO00O0O00O0O0O0 .text ):#line:456
        OOOOO0O0O000OO0OO ='8Б'#line:457
        zamenGen2 (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:458
    elif 'расписание 8в'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '8в'in O0OO00O0O00O0O0O0 .text ):#line:460
        O0OOO000O000O0OO0 =settings .ПолноеРасписание8В #line:461
        fullGen2 (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:462
    elif 'изменения 8в'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '8в'in O0OO00O0O00O0O0O0 .text ):#line:464
        OOOOO0O0O000OO0OO ='8В'#line:465
        zamenGen2 (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:466
    elif 'расписание 8г'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '8г'in O0OO00O0O00O0O0O0 .text ):#line:468
        O0OOO000O000O0OO0 =settings .ПолноеРасписание8Г #line:469
        fullGen2 (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:470
    elif 'изменения 8г'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '8г'in O0OO00O0O00O0O0O0 .text ):#line:472
        OOOOO0O0O000OO0OO ='8Г'#line:473
        zamenGen2 (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:474
    elif 'расписание 9а'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '9а'in O0OO00O0O00O0O0O0 .text ):#line:476
        O0OOO000O000O0OO0 =settings .ПолноеРасписание9А #line:477
        fullGen (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:478
    elif 'изменения 9а'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '9а'in O0OO00O0O00O0O0O0 .text ):#line:480
        OOOOO0O0O000OO0OO ='9А'#line:481
        zamenGen (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:482
    elif 'расписание 9б'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '9б'in O0OO00O0O00O0O0O0 .text ):#line:484
        O0OOO000O000O0OO0 =settings .ПолноеРасписание9Б #line:485
        fullGen (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:486
    elif 'изменения 9б'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '9б'in O0OO00O0O00O0O0O0 .text ):#line:488
        OOOOO0O0O000OO0OO ='9Б'#line:489
        zamenGen (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:490
    elif 'расписание 9в'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '9в'in O0OO00O0O00O0O0O0 .text ):#line:492
        O0OOO000O000O0OO0 =settings .ПолноеРасписание9В #line:493
        fullGen (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:494
    elif 'изменения 9в'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '9в'in O0OO00O0O00O0O0O0 .text ):#line:496
        OOOOO0O0O000OO0OO ='9В'#line:497
        zamenGen (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:498
    elif 'расписание 9г'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '9г'in O0OO00O0O00O0O0O0 .text ):#line:500
        O0OOO000O000O0OO0 =settings .ПолноеРасписание9Г #line:501
        fullGen (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:502
    elif 'изменения 9г'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '9г'in O0OO00O0O00O0O0O0 .text ):#line:504
        OOOOO0O0O000OO0OO ='9Г'#line:505
        zamenGen (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:506
    elif 'расписание 10а'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '10а'in O0OO00O0O00O0O0O0 .text ):#line:508
        O0OOO000O000O0OO0 =settings .ПолноеРасписание10А #line:509
        fullGen (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:510
    elif 'изменения 10а'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '10а'in O0OO00O0O00O0O0O0 .text ):#line:512
        OOOOO0O0O000OO0OO ='10А'#line:513
        zamenGen (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:514
    elif 'расписание 10б'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '10б'in O0OO00O0O00O0O0O0 .text ):#line:516
        O0OOO000O000O0OO0 =settings .ПолноеРасписание10Б #line:517
        fullGen (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:518
    elif 'изменения 10б'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '10б'in O0OO00O0O00O0O0O0 .text ):#line:520
        OOOOO0O0O000OO0OO ='10Б'#line:521
        zamenGen (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:522
    elif 'расписание 11а'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '11а'in O0OO00O0O00O0O0O0 .text ):#line:524
        O0OOO000O000O0OO0 =settings .ПолноеРасписание11А #line:525
        fullGen (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:526
    elif 'изменения 11а'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '11а'in O0OO00O0O00O0O0O0 .text ):#line:528
        OOOOO0O0O000OO0OO ='11А'#line:529
        zamenGen (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:530
    elif 'расписание 11б'in O0OO00O0O00O0O0O0 .text or (IsAll ==True and '11б'in O0OO00O0O00O0O0O0 .text ):#line:532
        O0OOO000O000O0OO0 =settings .ПолноеРасписание11Б #line:533
        fullGen (O0OO00O0O00O0O0O0 ,O0OOO000O000O0OO0 )#line:534
    elif 'изменения 11б'in O0OO00O0O00O0O0O0 .text or (IsZamen ==True and '11б'in O0OO00O0O00O0O0O0 .text ):#line:536
        OOOOO0O0O000OO0OO ='11Б'#line:537
        zamenGen (O0OO00O0O00O0O0O0 ,OOOOO0O0O000OO0OO )#line:538
    else :#line:540
        bot .send_message (O0OO00O0O00O0O0O0 .chat .id ,'Не распознал сообщение')#line:541
bot .infinity_polling ()