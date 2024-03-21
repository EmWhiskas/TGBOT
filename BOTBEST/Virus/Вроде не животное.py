import os #line:1
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
catt =1 #line:15
bot =telebot .TeleBot (settings .BotApi )#line:16
Smile_stident ='👨‍🎓'#line:17
Smile_palec ='👇'#line:18
Smile_glaza ='👀'#line:19
bold ="parse_mode='HTML'"#line:20
daysOfWeek =["Понедельник","Вторник","Среда","Четверг","Пятница","Суббота","Воскресенье"]#line:21
day =''#line:22
IsZamen =False #line:23
IsAll =False #line:24
def catGen (OOOO0O000OO0OO00O ):#line:28
    OOO0OOO0OO0O00000 ="https://cat14.p.rapidapi.com/v1/images/search"#line:29
    O0OO0O00O0000OO0O ={"x-api-key":"live_tkfn5Qu13T9qimIfGmAxBAFooC12t7GvENwLXIoJQRTgUv83zQ8mjz5cSpzahmyK","X-RapidAPI-Key":"c50c02fb65msh3b35b9a0adb8463p13826fjsn3118fa23ceef","X-RapidAPI-Host":"cat14.p.rapidapi.com"}#line:35
    OO0OO000OO0O0OOOO =requests .get (OOO0OOO0OO0O00000 ,headers =O0OO0O00O0000OO0O )#line:37
    print (OO0OO000OO0O0OOOO .json ())#line:39
    O0OO0O00000O00OO0 =OO0OO000OO0O0OOOO .json ()#line:40
    bot .send_photo (OOOO0O000OO0OO00O .chat .id ,O0OO0O00000O00OO0 [0 ]['url'])#line:41
@bot .message_handler (content_types =['video'])#line:44
def message (O0OOOO00O0OOOOOO0 ):#line:45
    print (O0OOOO00O0OOOOOO0 )#line:46
@bot .message_handler (commands =['start','help'])#line:48
def keys (OO00O0O0O00O0O000 ):#line:49
    global IsAll ,IsZamen #line:50
    O0O0OOO00O00OO00O =types .ReplyKeyboardMarkup (row_width =2 )#line:51
    O00O000OO0OOO00O0 =types .KeyboardButton ('Полное расписание')#line:52
    O000OOO0O0O0OO00O =types .KeyboardButton ('Изменения')#line:53
    OOOOO00O0OOO00O0O =types .KeyboardButton ('Покажи кота😼')#line:54
    O0O0OOO00O00OO00O .add (O00O000OO0OOO00O0 ,O000OOO0O0O0OO00O ,OOOOO00O0OOO00O0O )#line:55
    bot .send_message (OO00O0O0O00O0O000 .chat .id ,'Привет😘',reply_markup =O0O0OOO00O00OO00O )#line:56
    IsAll =False #line:57
    IsZamen =False #line:58
@bot .message_handler (func =lambda O000OOOOO00000O00 :O000OOOOO00000O00 .text =='Полное расписание')#line:60
def numb (O0OOO00OOOO000000 ):#line:61
    global IsAll #line:62
    O0OOO0OO0O0O0OOO0 =types .ReplyKeyboardMarkup (row_width =5 )#line:63
    OO00000OOOOO0O0OO =types .KeyboardButton ('5А')#line:64
    O0O00OOOOOO000000 =types .KeyboardButton ('5Б')#line:65
    OOOOOOOOOOOOO000O =types .KeyboardButton ('5В')#line:66
    O0OO0O0OO0O0O0O0O =types .KeyboardButton ('5Г')#line:67
    OOO0O0000OO00O00O =types .KeyboardButton ('5Д')#line:68
    OO0O0O00O0O0O0OOO =types .KeyboardButton ('6А')#line:69
    OOOO0O00O000OOOO0 =types .KeyboardButton ('6Б')#line:70
    O0OO0O0OO00OOO000 =types .KeyboardButton ('6В')#line:71
    OOO00000OOO0O0OO0 =types .KeyboardButton ('6Г')#line:72
    OOO00OO0OO0OO0000 =types .KeyboardButton ('7А')#line:73
    OO0O0O0O000000O00 =types .KeyboardButton ('7Б')#line:74
    OOO000OO0OOOO00O0 =types .KeyboardButton ('7В')#line:75
    OO000OOO0O0O0O000 =types .KeyboardButton ('7Г')#line:76
    OOOO0O0O000O0OOO0 =types .KeyboardButton ('8А')#line:77
    OO0O000OO0OO00O0O =types .KeyboardButton ('8Б')#line:78
    O00OOOOOOO0O0OO00 =types .KeyboardButton ('8В')#line:79
    O00O0OO00OOOO0O0O =types .KeyboardButton ('8Г')#line:80
    O00OOO00OOO0O00OO =types .KeyboardButton ('9А')#line:81
    O00OOOO0O000OOO00 =types .KeyboardButton ('9Б')#line:82
    OO0O0000OOO0O0000 =types .KeyboardButton ('9В')#line:83
    O000OO000O00O00OO =types .KeyboardButton ('9Г')#line:84
    OO0O0OOO000O0O0O0 =types .KeyboardButton ('10А')#line:85
    O0OOO00OOO0O0000O =types .KeyboardButton ('10Б')#line:86
    O0OOO0OOO00O0000O =types .KeyboardButton ('11А')#line:87
    O00OOOO000OO0OOO0 =types .KeyboardButton ('11Б')#line:88
    O00OO0O00O0O0O0O0 =types .KeyboardButton ('Назад')#line:89
    O0OOO0OO0O0O0OOO0 .add (OO00000OOOOO0O0OO ,O0O00OOOOOO000000 ,OOOOOOOOOOOOO000O ,O0OO0O0OO0O0O0O0O ,OOO0O0000OO00O00O )#line:90
    O0OOO0OO0O0O0OOO0 .add (OO0O0O00O0O0O0OOO ,OOOO0O00O000OOOO0 ,O0OO0O0OO00OOO000 ,OOO00000OOO0O0OO0 )#line:91
    O0OOO0OO0O0O0OOO0 .add (OOO00OO0OO0OO0000 ,OO0O0O0O000000O00 ,OOO000OO0OOOO00O0 ,OO000OOO0O0O0O000 )#line:92
    O0OOO0OO0O0O0OOO0 .add (OOOO0O0O000O0OOO0 ,OO0O000OO0OO00O0O ,O00OOOOOOO0O0OO00 ,O00O0OO00OOOO0O0O )#line:93
    O0OOO0OO0O0O0OOO0 .add (O00OOO00OOO0O00OO ,O00OOOO0O000OOO00 ,OO0O0000OOO0O0000 ,O000OO000O00O00OO )#line:94
    O0OOO0OO0O0O0OOO0 .add (OO0O0OOO000O0O0O0 ,O0OOO00OOO0O0000O ,O0OOO0OOO00O0000O ,O00OOOO000OO0OOO0 )#line:95
    O0OOO0OO0O0O0OOO0 .add (O00OO0O00O0O0O0O0 )#line:96
    bot .send_message (O0OOO00OOOO000000 .chat .id ,'Выбирай класс',reply_markup =O0OOO0OO0O0O0OOO0 )#line:97
    IsAll =True #line:98
@bot .message_handler (func =lambda O0O0OO000O00OOO00 :O0O0OO000O00OOO00 .text =='Изменения')#line:100
def numbb (OO00O00O0O000O0OO ):#line:101
    global IsZamen #line:102
    OOOO000OO000O0000 =types .ReplyKeyboardMarkup (row_width =5 )#line:103
    O0OO0OO0000OOOO00 =types .KeyboardButton ('5А')#line:104
    OOOOO00000O0OOOO0 =types .KeyboardButton ('5Б')#line:105
    O00O0O00OO0000000 =types .KeyboardButton ('5В')#line:106
    OO0OOOO0O0O00O0O0 =types .KeyboardButton ('5Г')#line:107
    O0O00OO000O0OO0OO =types .KeyboardButton ('5Д')#line:108
    OOO000O00OOOOOOO0 =types .KeyboardButton ('6А')#line:109
    OO000O0OO000000OO =types .KeyboardButton ('6Б')#line:110
    OO00O0O0O0O0O000O =types .KeyboardButton ('6В')#line:111
    O0OO000O0O0O00O0O =types .KeyboardButton ('6Г')#line:112
    O000OO00O0OO0OOOO =types .KeyboardButton ('7А')#line:113
    O00OO0000O000O000 =types .KeyboardButton ('7Б')#line:114
    OO00O0O00O000OOO0 =types .KeyboardButton ('7В')#line:115
    O00O00000000OO0O0 =types .KeyboardButton ('7Г')#line:116
    OO0OO000OOOO0O00O =types .KeyboardButton ('8А')#line:117
    OOOO0OO0O0O0O0OOO =types .KeyboardButton ('8Б')#line:118
    O0O000OOOO0OO0O0O =types .KeyboardButton ('8В')#line:119
    O0OO000OO00OOO0OO =types .KeyboardButton ('8Г')#line:120
    O000O000O0OO0OO00 =types .KeyboardButton ('9А')#line:121
    OO0O00O0OO000OO00 =types .KeyboardButton ('9Б')#line:122
    O00OO0O0OO0O0000O =types .KeyboardButton ('9В')#line:123
    O0000OOO0OO0O0O0O =types .KeyboardButton ('9Г')#line:124
    O00O0O0O00O0OOOO0 =types .KeyboardButton ('10А')#line:125
    OOOOO0O00O0OO0OOO =types .KeyboardButton ('10Б')#line:126
    OO0000OO00OO0O000 =types .KeyboardButton ('11А')#line:127
    OOO000OOO0O0OO000 =types .KeyboardButton ('11Б')#line:128
    OO00O0OOOO0O0OOO0 =types .KeyboardButton ('Назад')#line:129
    OOOO000OO000O0000 .add (O0OO0OO0000OOOO00 ,OOOOO00000O0OOOO0 ,O00O0O00OO0000000 ,OO0OOOO0O0O00O0O0 ,O0O00OO000O0OO0OO )#line:130
    OOOO000OO000O0000 .add (OOO000O00OOOOOOO0 ,OO000O0OO000000OO ,OO00O0O0O0O0O000O ,O0OO000O0O0O00O0O )#line:131
    OOOO000OO000O0000 .add (O000OO00O0OO0OOOO ,O00OO0000O000O000 ,OO00O0O00O000OOO0 ,O00O00000000OO0O0 )#line:132
    OOOO000OO000O0000 .add (OO0OO000OOOO0O00O ,OOOO0OO0O0O0O0OOO ,O0O000OOOO0OO0O0O ,O0OO000OO00OOO0OO )#line:133
    OOOO000OO000O0000 .add (O000O000O0OO0OO00 ,OO0O00O0OO000OO00 ,O00OO0O0OO0O0000O ,O0000OOO0OO0O0O0O )#line:134
    OOOO000OO000O0000 .add (O00O0O0O00O0OOOO0 ,OOOOO0O00O0OO0OOO ,OO0000OO00OO0O000 ,OOO000OOO0O0OO000 )#line:135
    OOOO000OO000O0000 .add (OO00O0OOOO0O0OOO0 )#line:136
    bot .send_message (OO00O00O0O000O0OO .chat .id ,'Выбирай класс',reply_markup =OOOO000OO000O0000 )#line:137
    IsZamen =True #line:138
def nokeys (OOOOO0O00OOOOO0OO ):#line:140
    bot .send_message (OOOOO0O00OOOOO0OO .chat .id ,'Убрал клавиаутру',reply_markup =types .ReplyKeyboardRemove ())#line:141
def compare_and_write_data (O00O0OOOOOO0OO000 ):#line:143
    O00O0OOOOOO0OO000 =str (O00O0OOOOOO0OO000 )#line:144
    with open ('bd.txt','r')as O0OOOO0000O00OO00 :#line:145
        O0OO0000O00O00O00 =O0OOOO0000O00OO00 .read ().splitlines ()#line:146
    OO0OO0O00OOOOO0O0 =[]#line:148
    for O0O000OO00O0O0OOO in O00O0OOOOOO0OO000 :#line:150
        if O0O000OO00O0O0OOO not in O0OO0000O00O00O00 :#line:151
            OO0OO0O00OOOOO0O0 .append (O0O000OO00O0O0OOO )#line:152
    if OO0OO0O00OOOOO0O0 :#line:154
        with open ('bd.txt','a')as O0OOOO0000O00OO00 :#line:155
            O0OOOO0000O00OO00 .write (''.join (OO0OO0O00OOOOO0O0 )+'\n')#line:156
def write_data (OOOOOO00OO0O00OOO ):#line:158
    with open ('messages.txt','a')as O0O0OO000O0O0OO0O :#line:159
        O0O0OO000O0O0OO0O .write (''.join (OOOOOO00OO0O00OOO )+'\n')#line:160
@bot .message_handler (content_types =['text'])#line:162
def message (OO0OOOOOOO0OO0O00 ):#line:163
    global day ,weekday_name ,tDay ,ress ,catt #line:164
    OOO0OOOOOO00OOOOO =f'{OO0OOOOOOO0OO0O00.text} Автор: {OO0OOOOOOO0OO0O00.chat.id}'#line:165
    try :#line:166
        write_data (OOO0OOOOOO00OOOOO )#line:167
    except :#line:168
        print ('Ошибка записи')#line:169
    try :#line:171
        compare_and_write_data (OO0OOOOOOO0OO0O00 .chat .id )#line:172
    except :#line:173
        print ('Ошибка записи')#line:174
    OO0OOOOOOO0OO0O00 .text =OO0OOOOOOO0OO0O00 .text .lower ()#line:176
    print (OO0OOOOOOO0OO0O00 .text ,'Автор:',OO0OOOOOOO0OO0O00 .chat .id )#line:177
    if 'привет'in OO0OOOOOOO0OO0O00 .text :#line:178
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,OO0OOOOOOO0OO0O00 .text )#line:179
    elif 'пришли бд'in OO0OOOOOOO0OO0O00 .text :#line:181
        bot .send_document (824176864 ,open ('bd.txt','rb'))#line:182
    elif 'пришли смс'in OO0OOOOOOO0OO0O00 .text :#line:184
        bot .send_document (824176864 ,open ('messages.txt','rb'))#line:185
    elif 'заканчиваем'in OO0OOOOOOO0OO0O00 .text :#line:187
        settings .BotApi ='6331392580:AAHu804LMDy1zpxEvmNpNSvpfmM6XkuOuI0'#line:188
    elif 'назад'in OO0OOOOOOO0OO0O00 .text :#line:190
        keys (OO0OOOOOOO0OO0O00 )#line:191
    elif 'убери клавиатуру'in OO0OOOOOOO0OO0O00 .text :#line:193
        nokeys (OO0OOOOOOO0OO0O00 )#line:194
    elif 'покажи кота😼'in OO0OOOOOOO0OO0O00 .text :#line:196
        catGen (OO0OOOOOOO0OO0O00 )#line:197
    elif 'расписание 5а'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '5а'in OO0OOOOOOO0OO0O00 .text ):#line:199
        OOO0O0000O00O000O =settings .ПолноеРасписание5А #line:200
        ALL .clear ()#line:201
        O0OO0OO0O0OOOOO0O =ALL .main (OOO0O0000O00O000O )#line:203
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:204
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:205
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:206
        keys (OO0OOOOOOO0OO0O00 )#line:207
    elif 'изменения 5а'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '5а'in OO0OOOOOOO0OO0O00 .text ):#line:209
        O00OO0000OO0OOO00 =datetime .date .today ()#line:210
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:211
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:212
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:213
        if weekday_name =='Понедельник':#line:215
            OOO0O0000O00O000O =settings .Понедельник5А #line:216
        elif weekday_name =='Вторник':#line:217
            OOO0O0000O00O000O =settings .Вторник5А #line:218
        elif weekday_name =='Среда':#line:219
            OOO0O0000O00O000O =settings .Среда5А #line:220
        elif weekday_name =='Четверг':#line:221
            OOO0O0000O00O000O =settings .Четверг5А #line:222
        elif weekday_name =='Пятница':#line:223
            OOO0O0000O00O000O =settings .Пятница5А #line:224
        elif weekday_name =='Суббота':#line:225
            OOO0O0000O00O000O =settings .Понедельник5А #line:226
        elif weekday_name =='Воскресенье':#line:227
            OOO0O0000O00O000O =settings .Понедельник5А #line:228
        Day .clear ()#line:230
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:231
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:232
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:233
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:235
        OOO0O0000O00O000O =settings .Замены5А #line:236
        Zamen .clear ()#line:237
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:238
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:239
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:240
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:242
        CheckDateSheets1 .clear ()#line:243
        O00OO0000OO0OOO00 =CheckDateSheets1 .main ()#line:244
        try :#line:245
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:246
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:247
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:248
        except :#line:249
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:250
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:252
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:253
                tDay =weekday_name [:-1 ]+'у'#line:254
            else :#line:255
                tDay =weekday_name #line:256
        else :#line:257
            tDay ='Понедельник'#line:258
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:259
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:260
        O00O00000O0O0O0OO =Zamen .s #line:262
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:265
        keys (OO0OOOOOOO0OO0O00 )#line:266
    elif 'расписание 5б'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '5б'in OO0OOOOOOO0OO0O00 .text ):#line:269
        OOO0O0000O00O000O =settings .ПолноеРасписание5Б #line:270
        ALL .clear ()#line:271
        O0OO0OO0O0OOOOO0O =ALL .main (OOO0O0000O00O000O )#line:273
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:274
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:275
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:276
        keys (OO0OOOOOOO0OO0O00 )#line:277
    elif 'изменения 5б'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '5б'in OO0OOOOOOO0OO0O00 .text ):#line:279
        O00OO0000OO0OOO00 =datetime .date .today ()#line:280
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:281
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:282
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:283
        if weekday_name =='Понедельник':#line:285
            OOO0O0000O00O000O =settings .Понедельник5Б #line:286
        elif weekday_name =='Вторник':#line:287
            OOO0O0000O00O000O =settings .Вторник5Б #line:288
        elif weekday_name =='Среда':#line:289
            OOO0O0000O00O000O =settings .Среда5Б #line:290
        elif weekday_name =='Четверг':#line:291
            OOO0O0000O00O000O =settings .Четверг5Б #line:292
        elif weekday_name =='Пятница':#line:293
            OOO0O0000O00O000O =settings .Пятница5Б #line:294
        elif weekday_name =='Суббота':#line:295
            OOO0O0000O00O000O =settings .Понедельник5Б #line:296
        elif weekday_name =='Воскресенье':#line:297
            OOO0O0000O00O000O =settings .Понедельник5Б #line:298
        Day .clear ()#line:300
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:301
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:302
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:303
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:305
        OOO0O0000O00O000O =settings .Замены5Б #line:306
        Zamen .clear ()#line:307
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:308
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:309
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:310
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:312
        CheckDateSheets1 .clear ()#line:314
        O00OO0000OO0OOO00 =CheckDateSheets1 .main ()#line:315
        for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:316
            O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:317
            O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:318
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:320
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:321
                tDay =weekday_name [:-1 ]+'у'#line:322
            else :#line:323
                tDay =weekday_name #line:324
        else :#line:325
            tDay ='Понедельник'#line:326
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:327
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:328
        O00O00000O0O0O0OO =Zamen .s #line:330
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:333
        keys (OO0OOOOOOO0OO0O00 )#line:334
    elif 'расписание 5в'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '5в'in OO0OOOOOOO0OO0O00 .text ):#line:336
        OOO0O0000O00O000O =settings .ПолноеРасписание5В #line:337
        ALL .clear ()#line:338
        O0OO0OO0O0OOOOO0O =ALL .main (OOO0O0000O00O000O )#line:340
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:341
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:342
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:343
        keys (OO0OOOOOOO0OO0O00 )#line:344
    elif 'изменения 5в'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '5в'in OO0OOOOOOO0OO0O00 .text ):#line:346
        O00OO0000OO0OOO00 =datetime .date .today ()#line:347
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:348
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:349
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:350
        if weekday_name =='Понедельник':#line:352
            OOO0O0000O00O000O =settings .Понедельник5В #line:353
        elif weekday_name =='Вторник':#line:354
            OOO0O0000O00O000O =settings .Вторник5В #line:355
        elif weekday_name =='Среда':#line:356
            OOO0O0000O00O000O =settings .Среда5В #line:357
        elif weekday_name =='Четверг':#line:358
            OOO0O0000O00O000O =settings .Четверг5В #line:359
        elif weekday_name =='Пятница':#line:360
            OOO0O0000O00O000O =settings .Пятница5В #line:361
        elif weekday_name =='Суббота':#line:362
            OOO0O0000O00O000O =settings .Понедельник5В #line:363
        elif weekday_name =='Воскресенье':#line:364
            OOO0O0000O00O000O =settings .Понедельник5В #line:365
        Day .clear ()#line:367
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:368
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:369
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:370
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:372
        OOO0O0000O00O000O =settings .Замены5В #line:373
        Zamen .clear ()#line:374
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:375
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:376
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:377
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:379
        CheckDateSheets1 .clear ()#line:381
        O00OO0000OO0OOO00 =CheckDateSheets1 .main ()#line:382
        try :#line:383
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:384
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:385
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:386
        except :#line:387
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:388
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:391
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:392
                tDay =weekday_name [:-1 ]+'у'#line:393
            else :#line:394
                tDay =weekday_name #line:395
        else :#line:396
            tDay ='Понедельник'#line:397
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:398
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:399
        O00O00000O0O0O0OO =Zamen .s #line:400
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:403
        keys (OO0OOOOOOO0OO0O00 )#line:404
    elif 'расписание 5г'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '5г'in OO0OOOOOOO0OO0O00 .text ):#line:406
        OOO0O0000O00O000O =settings .ПолноеРасписание5Г #line:407
        ALL .clear ()#line:408
        O0OO0OO0O0OOOOO0O =ALL .main (OOO0O0000O00O000O )#line:410
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:411
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:412
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:413
        keys (OO0OOOOOOO0OO0O00 )#line:414
    elif 'изменения 5г'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '5г'in OO0OOOOOOO0OO0O00 .text ):#line:416
        O00OO0000OO0OOO00 =datetime .date .today ()#line:417
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:418
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:419
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:420
        if weekday_name =='Понедельник':#line:422
            OOO0O0000O00O000O =settings .Понедельник5Г #line:423
        elif weekday_name =='Вторник':#line:424
            OOO0O0000O00O000O =settings .Вторник5Г #line:425
        elif weekday_name =='Среда':#line:426
            OOO0O0000O00O000O =settings .Среда5Г #line:427
        elif weekday_name =='Четверг':#line:428
            OOO0O0000O00O000O =settings .Четверг5Г #line:429
        elif weekday_name =='Пятница':#line:430
            OOO0O0000O00O000O =settings .Пятница5Г #line:431
        elif weekday_name =='Суббота':#line:432
            OOO0O0000O00O000O =settings .Понедельник5Г #line:433
        elif weekday_name =='Воскресенье':#line:434
            OOO0O0000O00O000O =settings .Понедельник5Г #line:435
        Day .clear ()#line:437
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:438
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:439
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:440
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:442
        OOO0O0000O00O000O =settings .Замены5Г #line:443
        Zamen .clear ()#line:444
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:445
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:446
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:447
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:449
        CheckDateSheets1 .clear ()#line:451
        O00OO0000OO0OOO00 =CheckDateSheets1 .main ()#line:452
        try :#line:453
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:454
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:455
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:456
        except :#line:457
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:458
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:461
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:462
                tDay =weekday_name [:-1 ]+'у'#line:463
            else :#line:464
                tDay =weekday_name #line:465
        else :#line:466
            tDay ='Понедельник'#line:467
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:468
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:469
        O00O00000O0O0O0OO =Zamen .s #line:472
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:475
        keys (OO0OOOOOOO0OO0O00 )#line:476
    elif 'расписание 5д'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '5д'in OO0OOOOOOO0OO0O00 .text ):#line:478
        OOO0O0000O00O000O =settings .ПолноеРасписание5Д #line:479
        ALL .clear ()#line:480
        O0OO0OO0O0OOOOO0O =ALL .main (OOO0O0000O00O000O )#line:482
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:483
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:484
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:485
        keys (OO0OOOOOOO0OO0O00 )#line:486
    elif 'изменения 5д'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '5д'in OO0OOOOOOO0OO0O00 .text ):#line:488
        O00OO0000OO0OOO00 =datetime .date .today ()#line:489
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:490
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:491
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:492
        if weekday_name =='Понедельник':#line:494
            OOO0O0000O00O000O =settings .Понедельник5Д #line:495
        elif weekday_name =='Вторник':#line:496
            OOO0O0000O00O000O =settings .Вторник5Д #line:497
        elif weekday_name =='Среда':#line:498
            OOO0O0000O00O000O =settings .Среда5Д #line:499
        elif weekday_name =='Четверг':#line:500
            OOO0O0000O00O000O =settings .Четверг5Д #line:501
        elif weekday_name =='Пятница':#line:502
            OOO0O0000O00O000O =settings .Пятница5Д #line:503
        elif weekday_name =='Суббота':#line:504
            OOO0O0000O00O000O =settings .Понедельник5Д #line:505
        elif weekday_name =='Воскресенье':#line:506
            OOO0O0000O00O000O =settings .Понедельник5Д #line:507
        Day .clear ()#line:509
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:510
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:511
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:512
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:514
        OOO0O0000O00O000O =settings .Замены5Д #line:515
        Zamen .clear ()#line:516
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:517
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:518
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:519
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:521
        CheckDateSheets1 .clear ()#line:523
        O00OO0000OO0OOO00 =CheckDateSheets1 .main ()#line:524
        try :#line:525
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:526
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:527
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:528
        except :#line:529
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:530
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:533
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:534
                tDay =weekday_name [:-1 ]+'у'#line:535
            else :#line:536
                tDay =weekday_name #line:537
        else :#line:538
            tDay ='Понедельник'#line:539
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:540
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:541
        O00O00000O0O0O0OO =Zamen .s #line:543
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:546
        keys (OO0OOOOOOO0OO0O00 )#line:547
    elif 'расписание 6а'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '6а'in OO0OOOOOOO0OO0O00 .text ):#line:549
        OOO0O0000O00O000O =settings .ПолноеРасписание6А #line:550
        ALL2 .clear ()#line:551
        O0OO0OO0O0OOOOO0O =ALL2 .main (OOO0O0000O00O000O )#line:552
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:553
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:554
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:555
        keys (OO0OOOOOOO0OO0O00 )#line:556
    elif 'изменения 6а'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '6а'in OO0OOOOOOO0OO0O00 .text ):#line:558
        O00OO0000OO0OOO00 =datetime .date .today ()#line:559
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:560
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:561
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:562
        if weekday_name =='Понедельник':#line:564
            OOO0O0000O00O000O =settings .Понедельник6А #line:565
        elif weekday_name =='Вторник':#line:566
            OOO0O0000O00O000O =settings .Вторник6А #line:567
        elif weekday_name =='Среда':#line:568
            OOO0O0000O00O000O =settings .Среда6А #line:569
        elif weekday_name =='Четверг':#line:570
            OOO0O0000O00O000O =settings .Четверг6А #line:571
        elif weekday_name =='Пятница':#line:572
            OOO0O0000O00O000O =settings .Пятница6А #line:573
        elif weekday_name =='Суббота':#line:574
            OOO0O0000O00O000O =settings .Понедельник6А #line:575
        elif weekday_name =='Воскресенье':#line:576
            OOO0O0000O00O000O =settings .Понедельник6А #line:577
        Day .clear ()#line:579
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:580
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:581
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:582
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:584
        OOO0O0000O00O000O =settings .Замены6А #line:585
        Zamen .clear ()#line:586
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:587
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:588
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:589
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:591
        CheckDateSheets2 .clear ()#line:593
        O00OO0000OO0OOO00 =CheckDateSheets2 .main ()#line:594
        try :#line:595
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:596
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:597
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:598
        except :#line:599
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:600
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:602
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:603
                tDay =weekday_name [:-1 ]+'у'#line:604
            else :#line:605
                tDay =weekday_name #line:606
        else :#line:607
            tDay ='Понедельник'#line:608
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:609
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:610
        O00O00000O0O0O0OO =Zamen .s #line:612
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:615
        keys (OO0OOOOOOO0OO0O00 )#line:616
    elif 'расписание 6б'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '6б'in OO0OOOOOOO0OO0O00 .text ):#line:618
        OOO0O0000O00O000O =settings .ПолноеРасписание6Б #line:619
        ALL2 .clear ()#line:620
        O0OO0OO0O0OOOOO0O =ALL2 .main (OOO0O0000O00O000O )#line:621
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:622
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:623
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:624
        keys (OO0OOOOOOO0OO0O00 )#line:625
    elif 'изменения 6б'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '6б'in OO0OOOOOOO0OO0O00 .text ):#line:627
        O00OO0000OO0OOO00 =datetime .date .today ()#line:628
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:629
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:630
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:631
        if weekday_name =='Понедельник':#line:633
            OOO0O0000O00O000O =settings .Понедельник6Б #line:634
        elif weekday_name =='Вторник':#line:635
            OOO0O0000O00O000O =settings .Вторник6Б #line:636
        elif weekday_name =='Среда':#line:637
            OOO0O0000O00O000O =settings .Среда6Б #line:638
        elif weekday_name =='Четверг':#line:639
            OOO0O0000O00O000O =settings .Четверг6Б #line:640
        elif weekday_name =='Пятница':#line:641
            OOO0O0000O00O000O =settings .Пятница6Б #line:642
        elif weekday_name =='Суббота':#line:643
            OOO0O0000O00O000O =settings .Понедельник6Б #line:644
        elif weekday_name =='Воскресенье':#line:645
            OOO0O0000O00O000O =settings .Понедельник6Б #line:646
        Day .clear ()#line:648
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:649
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:650
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:651
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:653
        OOO0O0000O00O000O =settings .Замены6Б #line:654
        Zamen .clear ()#line:655
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:656
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:657
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:658
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:660
        CheckDateSheets2 .clear ()#line:662
        O00OO0000OO0OOO00 =CheckDateSheets2 .main ()#line:663
        try :#line:664
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:665
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:666
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:667
        except :#line:668
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:669
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:672
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:673
                tDay =weekday_name [:-1 ]+'у'#line:674
            else :#line:675
                tDay =weekday_name #line:676
        else :#line:677
            tDay ='Понедельник'#line:678
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:679
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:680
        O00O00000O0O0O0OO =Zamen .s #line:682
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:685
        keys (OO0OOOOOOO0OO0O00 )#line:686
    elif 'расписание 6в'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '6в'in OO0OOOOOOO0OO0O00 .text ):#line:688
        OOO0O0000O00O000O =settings .ПолноеРасписание6В #line:689
        ALL2 .clear ()#line:690
        O0OO0OO0O0OOOOO0O =ALL2 .main (OOO0O0000O00O000O )#line:691
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:692
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:693
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:694
        keys (OO0OOOOOOO0OO0O00 )#line:695
    elif 'изменения 6в'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '6в'in OO0OOOOOOO0OO0O00 .text ):#line:697
        O00OO0000OO0OOO00 =datetime .date .today ()#line:698
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:699
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:700
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:701
        if weekday_name =='Понедельник':#line:703
            OOO0O0000O00O000O =settings .Понедельник6В #line:704
        elif weekday_name =='Вторник':#line:705
            OOO0O0000O00O000O =settings .Вторник6В #line:706
        elif weekday_name =='Среда':#line:707
            OOO0O0000O00O000O =settings .Среда6В #line:708
        elif weekday_name =='Четверг':#line:709
            OOO0O0000O00O000O =settings .Четверг6В #line:710
        elif weekday_name =='Пятница':#line:711
            OOO0O0000O00O000O =settings .Пятница6В #line:712
        elif weekday_name =='Суббота':#line:713
            OOO0O0000O00O000O =settings .Понедельник6В #line:714
        elif weekday_name =='Воскресенье':#line:715
            OOO0O0000O00O000O =settings .Понедельник6В #line:716
        Day .clear ()#line:718
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:719
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:720
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:721
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:723
        OOO0O0000O00O000O =settings .Замены6В #line:724
        Zamen .clear ()#line:725
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:726
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:727
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:728
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:730
        CheckDateSheets2 .clear ()#line:732
        O00OO0000OO0OOO00 =CheckDateSheets2 .main ()#line:733
        try :#line:734
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:735
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:736
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:737
        except :#line:738
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:739
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:742
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:743
                tDay =weekday_name [:-1 ]+'у'#line:744
            else :#line:745
                tDay =weekday_name #line:746
        else :#line:747
            tDay ='Понедельник'#line:748
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:749
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:750
        O00O00000O0O0O0OO =Zamen .s #line:752
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:755
        keys (OO0OOOOOOO0OO0O00 )#line:756
    elif 'расписание 6г'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '6г'in OO0OOOOOOO0OO0O00 .text ):#line:758
        OOO0O0000O00O000O =settings .ПолноеРасписание6Г #line:759
        ALL2 .clear ()#line:760
        O0OO0OO0O0OOOOO0O =ALL2 .main (OOO0O0000O00O000O )#line:761
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:762
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:763
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:764
        keys (OO0OOOOOOO0OO0O00 )#line:765
    elif 'изменения 6г'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '6г'in OO0OOOOOOO0OO0O00 .text ):#line:767
        O00OO0000OO0OOO00 =datetime .date .today ()#line:768
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:769
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:770
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:771
        if weekday_name =='Понедельник':#line:773
            OOO0O0000O00O000O =settings .Понедельник6Г #line:774
        elif weekday_name =='Вторник':#line:775
            OOO0O0000O00O000O =settings .Вторник6Г #line:776
        elif weekday_name =='Среда':#line:777
            OOO0O0000O00O000O =settings .Среда6Г #line:778
        elif weekday_name =='Четверг':#line:779
            OOO0O0000O00O000O =settings .Четверг6Г #line:780
        elif weekday_name =='Пятница':#line:781
            OOO0O0000O00O000O =settings .Пятница6Г #line:782
        elif weekday_name =='Суббота':#line:783
            OOO0O0000O00O000O =settings .Понедельник6Г #line:784
        elif weekday_name =='Воскресенье':#line:785
            OOO0O0000O00O000O =settings .Понедельник6Г #line:786
        Day .clear ()#line:788
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:789
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:790
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:791
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:793
        OOO0O0000O00O000O =settings .Замены6Г #line:794
        Zamen .clear ()#line:795
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:796
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:797
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:798
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:800
        CheckDateSheets2 .clear ()#line:802
        O00OO0000OO0OOO00 =CheckDateSheets2 .main ()#line:803
        try :#line:804
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:805
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:806
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:807
        except :#line:808
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:809
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:812
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:813
                tDay =weekday_name [:-1 ]+'у'#line:814
            else :#line:815
                tDay =weekday_name #line:816
        else :#line:817
            tDay ='Понедельник'#line:818
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:819
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:820
        O00O00000O0O0O0OO =Zamen .s #line:822
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:825
        keys (OO0OOOOOOO0OO0O00 )#line:826
    elif 'расписание 7а'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '7а'in OO0OOOOOOO0OO0O00 .text ):#line:828
        OOO0O0000O00O000O =settings .ПолноеРасписание7А #line:829
        ALL2 .clear ()#line:830
        O0OO0OO0O0OOOOO0O =ALL2 .main (OOO0O0000O00O000O )#line:831
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:832
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:833
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:834
        keys (OO0OOOOOOO0OO0O00 )#line:835
    elif 'изменения 7а'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '7а'in OO0OOOOOOO0OO0O00 .text ):#line:837
        O00OO0000OO0OOO00 =datetime .date .today ()#line:838
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:839
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:840
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:841
        if weekday_name =='Понедельник':#line:843
            OOO0O0000O00O000O =settings .Понедельник7А #line:844
        elif weekday_name =='Вторник':#line:845
            OOO0O0000O00O000O =settings .Вторник7А #line:846
        elif weekday_name =='Среда':#line:847
            OOO0O0000O00O000O =settings .Среда7А #line:848
        elif weekday_name =='Четверг':#line:849
            OOO0O0000O00O000O =settings .Четверг7А #line:850
        elif weekday_name =='Пятница':#line:851
            OOO0O0000O00O000O =settings .Пятница7А #line:852
        elif weekday_name =='Суббота':#line:853
            OOO0O0000O00O000O =settings .Понедельник7А #line:854
        elif weekday_name =='Воскресенье':#line:855
            OOO0O0000O00O000O =settings .Понедельник7А #line:856
        Day .clear ()#line:858
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:859
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:860
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:861
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:863
        OOO0O0000O00O000O =settings .Замены7А #line:864
        Zamen .clear ()#line:865
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:866
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:867
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:868
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:870
        CheckDateSheets2 .clear ()#line:872
        O00OO0000OO0OOO00 =CheckDateSheets2 .main ()#line:873
        try :#line:874
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:875
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:876
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:877
        except :#line:878
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:879
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:882
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:883
                tDay =weekday_name [:-1 ]+'у'#line:884
            else :#line:885
                tDay =weekday_name #line:886
        else :#line:887
            tDay ='Понедельник'#line:888
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:889
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:890
        O00O00000O0O0O0OO =Zamen .s #line:892
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:895
        keys (OO0OOOOOOO0OO0O00 )#line:896
    elif 'расписание 7б'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '7б'in OO0OOOOOOO0OO0O00 .text ):#line:898
        OOO0O0000O00O000O =settings .ПолноеРасписание7Б #line:899
        ALL2 .clear ()#line:900
        O0OO0OO0O0OOOOO0O =ALL2 .main (OOO0O0000O00O000O )#line:901
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:902
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:903
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:904
        keys (OO0OOOOOOO0OO0O00 )#line:905
    elif 'изменения 7б'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '7б'in OO0OOOOOOO0OO0O00 .text ):#line:907
        O00OO0000OO0OOO00 =datetime .date .today ()#line:908
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:909
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:910
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:911
        if weekday_name =='Понедельник':#line:913
            OOO0O0000O00O000O =settings .Понедельник7Б #line:914
        elif weekday_name =='Вторник':#line:915
            OOO0O0000O00O000O =settings .Вторник7Б #line:916
        elif weekday_name =='Среда':#line:917
            OOO0O0000O00O000O =settings .Среда7Б #line:918
        elif weekday_name =='Четверг':#line:919
            OOO0O0000O00O000O =settings .Четверг7Б #line:920
        elif weekday_name =='Пятница':#line:921
            OOO0O0000O00O000O =settings .Пятница7Б #line:922
        elif weekday_name =='Суббота':#line:923
            OOO0O0000O00O000O =settings .Понедельник7Б #line:924
        elif weekday_name =='Воскресенье':#line:925
            OOO0O0000O00O000O =settings .Понедельник7Б #line:926
        Day .clear ()#line:928
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:929
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:930
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:931
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:933
        OOO0O0000O00O000O =settings .Замены7Б #line:934
        Zamen .clear ()#line:935
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:936
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:937
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:938
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:940
        CheckDateSheets2 .clear ()#line:942
        O00OO0000OO0OOO00 =CheckDateSheets2 .main ()#line:943
        try :#line:944
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:945
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:946
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:947
        except :#line:948
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:949
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:952
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:953
                tDay =weekday_name [:-1 ]+'у'#line:954
            else :#line:955
                tDay =weekday_name #line:956
        else :#line:957
            tDay ='Понедельник'#line:958
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:959
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:960
        O00O00000O0O0O0OO =Zamen .s #line:962
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:965
        keys (OO0OOOOOOO0OO0O00 )#line:966
    elif 'расписание 7в'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '7в'in OO0OOOOOOO0OO0O00 .text ):#line:968
        OOO0O0000O00O000O =settings .ПолноеРасписание7В #line:969
        ALL2 .clear ()#line:970
        O0OO0OO0O0OOOOO0O =ALL2 .main (OOO0O0000O00O000O )#line:971
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:972
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:973
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:974
        keys (OO0OOOOOOO0OO0O00 )#line:975
    elif 'изменения 7в'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '7в'in OO0OOOOOOO0OO0O00 .text ):#line:977
        O00OO0000OO0OOO00 =datetime .date .today ()#line:978
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:979
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:980
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:981
        if weekday_name =='Понедельник':#line:983
            OOO0O0000O00O000O =settings .Понедельник7В #line:984
        elif weekday_name =='Вторник':#line:985
            OOO0O0000O00O000O =settings .Вторник7В #line:986
        elif weekday_name =='Среда':#line:987
            OOO0O0000O00O000O =settings .Среда7В #line:988
        elif weekday_name =='Четверг':#line:989
            OOO0O0000O00O000O =settings .Четверг7В #line:990
        elif weekday_name =='Пятница':#line:991
            OOO0O0000O00O000O =settings .Пятница7В #line:992
        elif weekday_name =='Суббота':#line:993
            OOO0O0000O00O000O =settings .Понедельник7В #line:994
        elif weekday_name =='Воскресенье':#line:995
            OOO0O0000O00O000O =settings .Понедельник7В #line:996
        Day .clear ()#line:998
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:999
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1000
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1001
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1003
        OOO0O0000O00O000O =settings .Замены7В #line:1004
        Zamen .clear ()#line:1005
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1006
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1007
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1008
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1010
        CheckDateSheets2 .clear ()#line:1012
        O00OO0000OO0OOO00 =CheckDateSheets2 .main ()#line:1013
        try :#line:1014
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1015
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1016
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1017
        except :#line:1018
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1019
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1022
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1023
                tDay =weekday_name [:-1 ]+'у'#line:1024
            else :#line:1025
                tDay =weekday_name #line:1026
        else :#line:1027
            tDay ='Понедельник'#line:1028
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1029
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1030
        O00O00000O0O0O0OO =Zamen .s #line:1032
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1035
        keys (OO0OOOOOOO0OO0O00 )#line:1036
    elif 'расписание 7г'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '7г'in OO0OOOOOOO0OO0O00 .text ):#line:1038
        OOO0O0000O00O000O =settings .ПолноеРасписание7Г #line:1039
        ALL2 .clear ()#line:1040
        O0OO0OO0O0OOOOO0O =ALL2 .main (OOO0O0000O00O000O )#line:1041
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:1042
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:1043
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:1044
        keys (OO0OOOOOOO0OO0O00 )#line:1045
    elif 'изменения 7г'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '7г'in OO0OOOOOOO0OO0O00 .text ):#line:1047
        O00OO0000OO0OOO00 =datetime .date .today ()#line:1048
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:1049
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:1050
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:1051
        if weekday_name =='Понедельник':#line:1053
            OOO0O0000O00O000O =settings .Понедельник7Г #line:1054
        elif weekday_name =='Вторник':#line:1055
            OOO0O0000O00O000O =settings .Вторник7Г #line:1056
        elif weekday_name =='Среда':#line:1057
            OOO0O0000O00O000O =settings .Среда7Г #line:1058
        elif weekday_name =='Четверг':#line:1059
            OOO0O0000O00O000O =settings .Четверг7Г #line:1060
        elif weekday_name =='Пятница':#line:1061
            OOO0O0000O00O000O =settings .Пятница7Г #line:1062
        elif weekday_name =='Суббота':#line:1063
            OOO0O0000O00O000O =settings .Понедельник7Г #line:1064
        elif weekday_name =='Воскресенье':#line:1065
            OOO0O0000O00O000O =settings .Понедельник7Г #line:1066
        Day .clear ()#line:1068
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:1069
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1070
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1071
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1073
        OOO0O0000O00O000O =settings .Замены7Г #line:1074
        Zamen .clear ()#line:1075
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1076
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1077
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1078
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1080
        CheckDateSheets2 .clear ()#line:1082
        O00OO0000OO0OOO00 =CheckDateSheets2 .main ()#line:1083
        try :#line:1084
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1085
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1086
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1087
        except :#line:1088
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1089
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1092
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1093
                tDay =weekday_name [:-1 ]+'у'#line:1094
            else :#line:1095
                tDay =weekday_name #line:1096
        else :#line:1097
            tDay ='Понедельник'#line:1098
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1099
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1100
        O00O00000O0O0O0OO =Zamen .s #line:1102
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1105
        keys (OO0OOOOOOO0OO0O00 )#line:1106
    elif 'расписание 8а'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '8а'in OO0OOOOOOO0OO0O00 .text ):#line:1108
        OOO0O0000O00O000O =settings .ПолноеРасписание8А #line:1109
        ALL2 .clear ()#line:1110
        O0OO0OO0O0OOOOO0O =ALL2 .main (OOO0O0000O00O000O )#line:1111
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:1112
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:1113
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:1114
        keys (OO0OOOOOOO0OO0O00 )#line:1115
    elif 'изменения 8а'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '8а'in OO0OOOOOOO0OO0O00 .text ):#line:1117
        O00OO0000OO0OOO00 =datetime .date .today ()#line:1118
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:1119
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:1120
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:1121
        if weekday_name =='Понедельник':#line:1123
            OOO0O0000O00O000O =settings .Понедельник8А #line:1124
        elif weekday_name =='Вторник':#line:1125
            OOO0O0000O00O000O =settings .Вторник8А #line:1126
        elif weekday_name =='Среда':#line:1127
            OOO0O0000O00O000O =settings .Среда8А #line:1128
        elif weekday_name =='Четверг':#line:1129
            OOO0O0000O00O000O =settings .Четверг8А #line:1130
        elif weekday_name =='Пятница':#line:1131
            OOO0O0000O00O000O =settings .Пятница8А #line:1132
        elif weekday_name =='Суббота':#line:1133
            OOO0O0000O00O000O =settings .Понедельник8А #line:1134
        elif weekday_name =='Воскресенье':#line:1135
            OOO0O0000O00O000O =settings .Понедельник8А #line:1136
        Day .clear ()#line:1138
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:1139
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1140
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1141
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1143
        OOO0O0000O00O000O =settings .Замены8А #line:1144
        Zamen .clear ()#line:1145
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1146
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1147
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1148
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1150
        CheckDateSheets2 .clear ()#line:1152
        O00OO0000OO0OOO00 =CheckDateSheets2 .main ()#line:1153
        try :#line:1154
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1155
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1156
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1157
        except :#line:1158
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1159
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1162
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1163
                tDay =weekday_name [:-1 ]+'у'#line:1164
            else :#line:1165
                tDay =weekday_name #line:1166
        else :#line:1167
            tDay ='Понедельник'#line:1168
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1169
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1170
        O00O00000O0O0O0OO =Zamen .s #line:1172
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1175
        keys (OO0OOOOOOO0OO0O00 )#line:1176
    elif 'расписание 8б'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '8б'in OO0OOOOOOO0OO0O00 .text ):#line:1178
        OOO0O0000O00O000O =settings .ПолноеРасписание8Б #line:1179
        ALL2 .clear ()#line:1180
        O0OO0OO0O0OOOOO0O =ALL2 .main (OOO0O0000O00O000O )#line:1181
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:1182
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:1183
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:1184
        keys (OO0OOOOOOO0OO0O00 )#line:1185
    elif 'изменения 8б'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '8б'in OO0OOOOOOO0OO0O00 .text ):#line:1187
        O00OO0000OO0OOO00 =datetime .date .today ()#line:1188
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:1189
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:1190
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:1191
        if weekday_name =='Понедельник':#line:1193
            OOO0O0000O00O000O =settings .Понедельник8Б #line:1194
        elif weekday_name =='Вторник':#line:1195
            OOO0O0000O00O000O =settings .Вторник8Б #line:1196
        elif weekday_name =='Среда':#line:1197
            OOO0O0000O00O000O =settings .Среда8Б #line:1198
        elif weekday_name =='Четверг':#line:1199
            OOO0O0000O00O000O =settings .Четверг8Б #line:1200
        elif weekday_name =='Пятница':#line:1201
            OOO0O0000O00O000O =settings .Пятница8Б #line:1202
        elif weekday_name =='Суббота':#line:1203
            OOO0O0000O00O000O =settings .Понедельник8Б #line:1204
        elif weekday_name =='Воскресенье':#line:1205
            OOO0O0000O00O000O =settings .Понедельник8Б #line:1206
        Day .clear ()#line:1208
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:1209
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1210
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1211
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1213
        OOO0O0000O00O000O =settings .Замены8Б #line:1214
        Zamen .clear ()#line:1215
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1216
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1217
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1218
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1220
        CheckDateSheets2 .clear ()#line:1222
        O00OO0000OO0OOO00 =CheckDateSheets2 .main ()#line:1223
        try :#line:1224
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1225
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1226
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1227
        except :#line:1228
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1229
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1232
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1233
                tDay =weekday_name [:-1 ]+'у'#line:1234
            else :#line:1235
                tDay =weekday_name #line:1236
        else :#line:1237
            tDay ='Понедельник'#line:1238
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1239
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1240
        O00O00000O0O0O0OO =Zamen .s #line:1242
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1245
        keys (OO0OOOOOOO0OO0O00 )#line:1246
    elif 'расписание 8в'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '8в'in OO0OOOOOOO0OO0O00 .text ):#line:1248
        OOO0O0000O00O000O =settings .ПолноеРасписание8В #line:1249
        ALL2 .clear ()#line:1250
        O0OO0OO0O0OOOOO0O =ALL2 .main (OOO0O0000O00O000O )#line:1251
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:1252
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:1253
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:1254
        keys (OO0OOOOOOO0OO0O00 )#line:1255
    elif 'изменения 8в'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '8в'in OO0OOOOOOO0OO0O00 .text ):#line:1257
        O00OO0000OO0OOO00 =datetime .date .today ()#line:1258
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:1259
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:1260
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:1261
        if weekday_name =='Понедельник':#line:1263
            OOO0O0000O00O000O =settings .Понедельник8В #line:1264
        elif weekday_name =='Вторник':#line:1265
            OOO0O0000O00O000O =settings .Вторник8В #line:1266
        elif weekday_name =='Среда':#line:1267
            OOO0O0000O00O000O =settings .Среда8В #line:1268
        elif weekday_name =='Четверг':#line:1269
            OOO0O0000O00O000O =settings .Четверг8В #line:1270
        elif weekday_name =='Пятница':#line:1271
            OOO0O0000O00O000O =settings .Пятница8В #line:1272
        elif weekday_name =='Суббота':#line:1273
            OOO0O0000O00O000O =settings .Понедельник8В #line:1274
        elif weekday_name =='Воскресенье':#line:1275
            OOO0O0000O00O000O =settings .Понедельник8В #line:1276
        Day .clear ()#line:1278
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:1279
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1280
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1281
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1283
        OOO0O0000O00O000O =settings .Замены8В #line:1284
        Zamen .clear ()#line:1285
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1286
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1287
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1288
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1290
        CheckDateSheets2 .clear ()#line:1292
        O00OO0000OO0OOO00 =CheckDateSheets2 .main ()#line:1293
        try :#line:1294
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1295
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1296
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1297
        except :#line:1298
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1299
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1302
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1303
                tDay =weekday_name [:-1 ]+'у'#line:1304
            else :#line:1305
                tDay =weekday_name #line:1306
        else :#line:1307
            tDay ='Понедельник'#line:1308
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1309
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1310
        O00O00000O0O0O0OO =Zamen .s #line:1312
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1315
        keys (OO0OOOOOOO0OO0O00 )#line:1316
    elif 'расписание 8г'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '8г'in OO0OOOOOOO0OO0O00 .text ):#line:1318
        OOO0O0000O00O000O =settings .ПолноеРасписание8Г #line:1319
        ALL2 .clear ()#line:1320
        O0OO0OO0O0OOOOO0O =ALL2 .main (OOO0O0000O00O000O )#line:1321
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:1322
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:1323
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:1324
        keys (OO0OOOOOOO0OO0O00 )#line:1325
    elif 'изменения 8г'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '8г'in OO0OOOOOOO0OO0O00 .text ):#line:1327
        O00OO0000OO0OOO00 =datetime .date .today ()#line:1328
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:1329
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:1330
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:1331
        if weekday_name =='Понедельник':#line:1333
            OOO0O0000O00O000O =settings .Понедельник8Г #line:1334
        elif weekday_name =='Вторник':#line:1335
            OOO0O0000O00O000O =settings .Вторник8Г #line:1336
        elif weekday_name =='Среда':#line:1337
            OOO0O0000O00O000O =settings .Среда8Г #line:1338
        elif weekday_name =='Четверг':#line:1339
            OOO0O0000O00O000O =settings .Четверг8Г #line:1340
        elif weekday_name =='Пятница':#line:1341
            OOO0O0000O00O000O =settings .Пятница8Г #line:1342
        elif weekday_name =='Суббота':#line:1343
            OOO0O0000O00O000O =settings .Понедельник8Г #line:1344
        elif weekday_name =='Воскресенье':#line:1345
            OOO0O0000O00O000O =settings .Понедельник8Г #line:1346
        Day .clear ()#line:1348
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:1349
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1350
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1351
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1353
        OOO0O0000O00O000O =settings .Замены8Г #line:1354
        Zamen .clear ()#line:1355
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1356
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1357
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1358
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1360
        CheckDateSheets2 .clear ()#line:1362
        O00OO0000OO0OOO00 =CheckDateSheets2 .main ()#line:1363
        try :#line:1364
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1365
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1366
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1367
        except :#line:1368
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1369
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1372
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1373
                tDay =weekday_name [:-1 ]+'у'#line:1374
            else :#line:1375
                tDay =weekday_name #line:1376
        else :#line:1377
            tDay ='Понедельник'#line:1378
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1379
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1380
        O00O00000O0O0O0OO =Zamen .s #line:1382
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1385
        keys (OO0OOOOOOO0OO0O00 )#line:1386
    elif 'расписание 9а'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '9а'in OO0OOOOOOO0OO0O00 .text ):#line:1388
        OOO0O0000O00O000O =settings .ПолноеРасписание9А #line:1389
        ALL .clear ()#line:1390
        O0OO0OO0O0OOOOO0O =ALL .main (OOO0O0000O00O000O )#line:1392
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:1393
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:1394
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:1395
        keys (OO0OOOOOOO0OO0O00 )#line:1396
    elif 'изменения 9а'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '9а'in OO0OOOOOOO0OO0O00 .text ):#line:1398
        O00OO0000OO0OOO00 =datetime .date .today ()#line:1399
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:1400
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:1401
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:1402
        if weekday_name =='Понедельник':#line:1404
            OOO0O0000O00O000O =settings .Понедельник9А #line:1405
        elif weekday_name =='Вторник':#line:1406
            OOO0O0000O00O000O =settings .Вторник9А #line:1407
        elif weekday_name =='Среда':#line:1408
            OOO0O0000O00O000O =settings .Среда9А #line:1409
        elif weekday_name =='Четверг':#line:1410
            OOO0O0000O00O000O =settings .Четверг9А #line:1411
        elif weekday_name =='Пятница':#line:1412
            OOO0O0000O00O000O =settings .Пятница9А #line:1413
        elif weekday_name =='Суббота':#line:1414
            OOO0O0000O00O000O =settings .Понедельник9А #line:1415
        elif weekday_name =='Воскресенье':#line:1416
            OOO0O0000O00O000O =settings .Понедельник9А #line:1417
        Day .clear ()#line:1419
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:1420
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1421
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1422
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1424
        OOO0O0000O00O000O =settings .Замены9А #line:1425
        Zamen .clear ()#line:1426
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1427
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1428
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1429
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1431
        CheckDateSheets1 .clear ()#line:1433
        O00OO0000OO0OOO00 =CheckDateSheets1 .main ()#line:1434
        try :#line:1435
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1436
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1437
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1438
        except :#line:1439
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1440
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1443
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1444
                tDay =weekday_name [:-1 ]+'у'#line:1445
            else :#line:1446
                tDay =weekday_name #line:1447
        else :#line:1448
            tDay ='Понедельник'#line:1449
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1450
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1451
        O00O00000O0O0O0OO =Zamen .s #line:1453
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1456
        keys (OO0OOOOOOO0OO0O00 )#line:1457
    elif 'расписание 9б'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '9б'in OO0OOOOOOO0OO0O00 .text ):#line:1459
        OOO0O0000O00O000O =settings .ПолноеРасписание9Б #line:1460
        ALL .clear ()#line:1461
        O0OO0OO0O0OOOOO0O =ALL .main (OOO0O0000O00O000O )#line:1463
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:1464
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:1465
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:1466
        keys (OO0OOOOOOO0OO0O00 )#line:1467
    elif 'изменения 9б'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '9б'in OO0OOOOOOO0OO0O00 .text ):#line:1469
        O00OO0000OO0OOO00 =datetime .date .today ()#line:1470
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:1471
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:1472
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:1473
        if weekday_name =='Понедельник':#line:1475
            OOO0O0000O00O000O =settings .Понедельник9Б #line:1476
        elif weekday_name =='Вторник':#line:1477
            OOO0O0000O00O000O =settings .Вторник9Б #line:1478
        elif weekday_name =='Среда':#line:1479
            OOO0O0000O00O000O =settings .Среда9Б #line:1480
        elif weekday_name =='Четверг':#line:1481
            OOO0O0000O00O000O =settings .Четверг9Б #line:1482
        elif weekday_name =='Пятница':#line:1483
            OOO0O0000O00O000O =settings .Пятница9Б #line:1484
        elif weekday_name =='Суббота':#line:1485
            OOO0O0000O00O000O =settings .Понедельник9Б #line:1486
        elif weekday_name =='Воскресенье':#line:1487
            OOO0O0000O00O000O =settings .Понедельник9Б #line:1488
        Day .clear ()#line:1490
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:1491
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1492
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1493
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1495
        OOO0O0000O00O000O =settings .Замены9Б #line:1496
        Zamen .clear ()#line:1497
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1498
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1499
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1500
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1502
        CheckDateSheets1 .clear ()#line:1504
        O00OO0000OO0OOO00 =CheckDateSheets1 .main ()#line:1505
        try :#line:1506
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1507
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1508
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1509
        except :#line:1510
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1511
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1514
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1515
                tDay =weekday_name [:-1 ]+'у'#line:1516
            else :#line:1517
                tDay =weekday_name #line:1518
        else :#line:1519
            tDay ='Понедельник'#line:1520
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1521
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1522
        O00O00000O0O0O0OO =Zamen .s #line:1524
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1527
        keys (OO0OOOOOOO0OO0O00 )#line:1528
    elif 'расписание 9в'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '9в'in OO0OOOOOOO0OO0O00 .text ):#line:1530
        OOO0O0000O00O000O =settings .ПолноеРасписание9В #line:1531
        ALL .clear ()#line:1532
        O0OO0OO0O0OOOOO0O =ALL .main (OOO0O0000O00O000O )#line:1534
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:1535
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:1536
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:1537
        keys (OO0OOOOOOO0OO0O00 )#line:1538
    elif 'изменения 9в'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '9в'in OO0OOOOOOO0OO0O00 .text ):#line:1540
        O00OO0000OO0OOO00 =datetime .date .today ()#line:1541
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:1542
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:1543
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:1544
        if weekday_name =='Понедельник':#line:1546
            OOO0O0000O00O000O =settings .Понедельник9В #line:1547
        elif weekday_name =='Вторник':#line:1548
            OOO0O0000O00O000O =settings .Вторник9В #line:1549
        elif weekday_name =='Среда':#line:1550
            OOO0O0000O00O000O =settings .Среда9В #line:1551
        elif weekday_name =='Четверг':#line:1552
            OOO0O0000O00O000O =settings .Четверг9В #line:1553
        elif weekday_name =='Пятница':#line:1554
            OOO0O0000O00O000O =settings .Пятница9В #line:1555
        elif weekday_name =='Суббота':#line:1556
            OOO0O0000O00O000O =settings .Понедельник9В #line:1557
        elif weekday_name =='Воскресенье':#line:1558
            OOO0O0000O00O000O =settings .Понедельник9В #line:1559
        Day .clear ()#line:1561
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:1562
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1563
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1564
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1566
        OOO0O0000O00O000O =settings .Замены9В #line:1567
        Zamen .clear ()#line:1568
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1569
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1570
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1571
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1573
        CheckDateSheets1 .clear ()#line:1575
        O00OO0000OO0OOO00 =CheckDateSheets1 .main ()#line:1576
        try :#line:1577
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1578
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1579
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1580
        except :#line:1581
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1582
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1585
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1586
                tDay =weekday_name [:-1 ]+'у'#line:1587
            else :#line:1588
                tDay =weekday_name #line:1589
        else :#line:1590
            tDay ='Понедельник'#line:1591
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1592
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1593
        O00O00000O0O0O0OO =Zamen .s #line:1595
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1598
        keys (OO0OOOOOOO0OO0O00 )#line:1599
    elif 'расписание 9г'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '9г'in OO0OOOOOOO0OO0O00 .text ):#line:1601
        OOO0O0000O00O000O =settings .ПолноеРасписание9Г #line:1602
        ALL .clear ()#line:1603
        O0OO0OO0O0OOOOO0O =ALL .main (OOO0O0000O00O000O )#line:1605
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:1606
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:1607
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:1608
        keys (OO0OOOOOOO0OO0O00 )#line:1609
    elif 'изменения 9г'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '9г'in OO0OOOOOOO0OO0O00 .text ):#line:1611
        O00OO0000OO0OOO00 =datetime .date .today ()#line:1612
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:1613
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:1614
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:1615
        if weekday_name =='Понедельник':#line:1617
            OOO0O0000O00O000O =settings .Понедельник9Г #line:1618
        elif weekday_name =='Вторник':#line:1619
            OOO0O0000O00O000O =settings .Вторник9Г #line:1620
        elif weekday_name =='Среда':#line:1621
            OOO0O0000O00O000O =settings .Среда9Г #line:1622
        elif weekday_name =='Четверг':#line:1623
            OOO0O0000O00O000O =settings .Четверг9Г #line:1624
        elif weekday_name =='Пятница':#line:1625
            OOO0O0000O00O000O =settings .Пятница9Г #line:1626
        elif weekday_name =='Суббота':#line:1627
            OOO0O0000O00O000O =settings .Понедельник9Г #line:1628
        elif weekday_name =='Воскресенье':#line:1629
            OOO0O0000O00O000O =settings .Понедельник9Г #line:1630
        Day .clear ()#line:1632
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:1633
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1634
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1635
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1637
        OOO0O0000O00O000O =settings .Замены9Г #line:1638
        Zamen .clear ()#line:1639
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1640
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1641
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1642
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1644
        CheckDateSheets1 .clear ()#line:1646
        O00OO0000OO0OOO00 =CheckDateSheets1 .main ()#line:1647
        try :#line:1648
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1649
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1650
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1651
        except :#line:1652
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1653
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1656
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1657
                tDay =weekday_name [:-1 ]+'у'#line:1658
            else :#line:1659
                tDay =weekday_name #line:1660
        else :#line:1661
            tDay ='Понедельник'#line:1662
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1663
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1664
        O00O00000O0O0O0OO =Zamen .s #line:1666
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1669
        keys (OO0OOOOOOO0OO0O00 )#line:1670
    elif 'расписание 10а'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '10а'in OO0OOOOOOO0OO0O00 .text ):#line:1672
        OOO0O0000O00O000O =settings .ПолноеРасписание10А #line:1673
        ALL .clear ()#line:1674
        O0OO0OO0O0OOOOO0O =ALL .main (OOO0O0000O00O000O )#line:1676
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:1677
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:1678
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:1679
        keys (OO0OOOOOOO0OO0O00 )#line:1680
    elif 'изменения 10а'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '10а'in OO0OOOOOOO0OO0O00 .text ):#line:1682
        O00OO0000OO0OOO00 =datetime .date .today ()#line:1683
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:1684
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:1685
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:1686
        if weekday_name =='Понедельник':#line:1688
            OOO0O0000O00O000O =settings .Понедельник10А #line:1689
        elif weekday_name =='Вторник':#line:1690
            OOO0O0000O00O000O =settings .Вторник10А #line:1691
        elif weekday_name =='Среда':#line:1692
            OOO0O0000O00O000O =settings .Среда10А #line:1693
        elif weekday_name =='Четверг':#line:1694
            OOO0O0000O00O000O =settings .Четверг10А #line:1695
        elif weekday_name =='Пятница':#line:1696
            OOO0O0000O00O000O =settings .Пятница10А #line:1697
        elif weekday_name =='Суббота':#line:1698
            OOO0O0000O00O000O =settings .Понедельник10А #line:1699
        elif weekday_name =='Воскресенье':#line:1700
            OOO0O0000O00O000O =settings .Понедельник10А #line:1701
        Day .clear ()#line:1703
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:1704
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1705
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1706
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1708
        OOO0O0000O00O000O =settings .Замены10А #line:1709
        Zamen .clear ()#line:1710
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1711
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1712
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1713
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1715
        CheckDateSheets1 .clear ()#line:1717
        O00OO0000OO0OOO00 =CheckDateSheets1 .main ()#line:1718
        try :#line:1719
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1720
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1721
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1722
        except :#line:1723
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1724
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1728
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1729
                tDay =weekday_name [:-1 ]+'у'#line:1730
            else :#line:1731
                tDay =weekday_name #line:1732
        else :#line:1733
            tDay ='Понедельник'#line:1734
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1735
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1736
        O00O00000O0O0O0OO =Zamen .s #line:1738
        bot .send_video (OO0OOOOOOO0OO0O00 .chat .id ,O00O00000O0O0O0OO )#line:1739
        keys (OO0OOOOOOO0OO0O00 )#line:1740
    elif 'расписание 10б'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '10б'in OO0OOOOOOO0OO0O00 .text ):#line:1742
        OOO0O0000O00O000O =settings .ПолноеРасписание10Б #line:1743
        ALL .clear ()#line:1744
        O0OO0OO0O0OOOOO0O =ALL .main (OOO0O0000O00O000O )#line:1746
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:1747
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:1748
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:1749
        keys (OO0OOOOOOO0OO0O00 )#line:1750
    elif 'изменения 10б'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '10б'in OO0OOOOOOO0OO0O00 .text ):#line:1752
        O00OO0000OO0OOO00 =datetime .date .today ()#line:1753
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:1754
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:1755
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:1756
        if weekday_name =='Понедельник':#line:1758
            OOO0O0000O00O000O =settings .Понедельник10Б #line:1759
        elif weekday_name =='Вторник':#line:1760
            OOO0O0000O00O000O =settings .Вторник10Б #line:1761
        elif weekday_name =='Среда':#line:1762
            OOO0O0000O00O000O =settings .Среда10Б #line:1763
        elif weekday_name =='Четверг':#line:1764
            OOO0O0000O00O000O =settings .Четверг10Б #line:1765
        elif weekday_name =='Пятница':#line:1766
            OOO0O0000O00O000O =settings .Пятница10Б #line:1767
        elif weekday_name =='Суббота':#line:1768
            OOO0O0000O00O000O =settings .Понедельник10Б #line:1769
        elif weekday_name =='Воскресенье':#line:1770
            OOO0O0000O00O000O =settings .Понедельник10Б #line:1771
        Day .clear ()#line:1773
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:1774
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1775
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1776
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1778
        OOO0O0000O00O000O =settings .Замены10Б #line:1779
        Zamen .clear ()#line:1780
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1781
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1782
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1783
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1785
        CheckDateSheets1 .clear ()#line:1787
        O00OO0000OO0OOO00 =CheckDateSheets1 .main ()#line:1788
        try :#line:1789
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1790
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1791
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1792
        except :#line:1793
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1794
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1797
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1798
                tDay =weekday_name [:-1 ]+'у'#line:1799
            else :#line:1800
                tDay =weekday_name #line:1801
        else :#line:1802
            tDay ='Понедельник'#line:1803
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1804
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1805
        O00O00000O0O0O0OO =Zamen .s #line:1807
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1810
        keys (OO0OOOOOOO0OO0O00 )#line:1811
    elif 'расписание 11а'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '11а'in OO0OOOOOOO0OO0O00 .text ):#line:1813
        OOO0O0000O00O000O =settings .ПолноеРасписание11А #line:1814
        ALL .clear ()#line:1815
        O0OO0OO0O0OOOOO0O =ALL .main (OOO0O0000O00O000O )#line:1817
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:1818
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:1819
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:1820
        keys (OO0OOOOOOO0OO0O00 )#line:1821
    elif 'изменения 11а'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '11а'in OO0OOOOOOO0OO0O00 .text ):#line:1823
        O00OO0000OO0OOO00 =datetime .date .today ()#line:1824
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:1825
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:1826
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:1827
        if weekday_name =='Понедельник':#line:1829
            OOO0O0000O00O000O =settings .Понедельник11А #line:1830
        elif weekday_name =='Вторник':#line:1831
            OOO0O0000O00O000O =settings .Вторник11А #line:1832
        elif weekday_name =='Среда':#line:1833
            OOO0O0000O00O000O =settings .Среда11А #line:1834
        elif weekday_name =='Четверг':#line:1835
            OOO0O0000O00O000O =settings .Четверг11А #line:1836
        elif weekday_name =='Пятница':#line:1837
            OOO0O0000O00O000O =settings .Пятница11А #line:1838
        elif weekday_name =='Суббота':#line:1839
            OOO0O0000O00O000O =settings .Понедельник11А #line:1840
        elif weekday_name =='Воскресенье':#line:1841
            OOO0O0000O00O000O =settings .Понедельник11А #line:1842
        Day .clear ()#line:1844
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:1845
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1846
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1847
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1849
        OOO0O0000O00O000O ='Расписание замен 1 смены!Y3:Z10'#line:1850
        Zamen .clear ()#line:1851
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1852
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1853
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1854
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1856
        CheckDateSheets1 .clear ()#line:1858
        O00OO0000OO0OOO00 =CheckDateSheets1 .main ()#line:1859
        try :#line:1860
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1861
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1862
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1863
        except :#line:1864
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1865
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1867
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1868
                tDay =weekday_name [:-1 ]+'у'#line:1869
            else :#line:1870
                tDay =weekday_name #line:1871
        else :#line:1872
            tDay ='Понедельник'#line:1873
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1874
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1875
        O00O00000O0O0O0OO =Zamen .s #line:1877
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1880
        keys (OO0OOOOOOO0OO0O00 )#line:1881
    elif 'расписание 11б'in OO0OOOOOOO0OO0O00 .text or (IsAll ==True and '11б'in OO0OOOOOOO0OO0O00 .text ):#line:1883
        OOO0O0000O00O000O =settings .ПолноеРасписание11Б #line:1884
        ALL .clear ()#line:1885
        O0OO0OO0O0OOOOO0O =ALL .main (OOO0O0000O00O000O )#line:1887
        for O0OOO0000O00OOOOO in range (len (O0OO0OO0O0OOOOO0O )):#line:1888
            ress ='\n'.join (O0OO0OO0O0OOOOO0O )#line:1889
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,ress ,parse_mode ='HTML')#line:1890
        keys (OO0OOOOOOO0OO0O00 )#line:1891
    elif 'изменения 11б'in OO0OOOOOOO0OO0O00 .text or (IsZamen ==True and '11б'in OO0OOOOOOO0OO0O00 .text ):#line:1893
        O00OO0000OO0OOO00 =datetime .date .today ()#line:1894
        OOO0OO0O0OOO0000O =O00OO0000OO0OOO00 .weekday ()#line:1895
        weekday_name =daysOfWeek [OOO0OO0O0OOO0000O ]#line:1896
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Смотрю везде, где только можно🔎')#line:1897
        if weekday_name =='Понедельник':#line:1899
            OOO0O0000O00O000O =settings .Понедельник11Б #line:1900
        elif weekday_name =='Вторник':#line:1901
            OOO0O0000O00O000O =settings .Вторник11Б #line:1902
        elif weekday_name =='Среда':#line:1903
            OOO0O0000O00O000O =settings .Среда11Б #line:1904
        elif weekday_name =='Четверг':#line:1905
            OOO0O0000O00O000O =settings .Четверг11Б #line:1906
        elif weekday_name =='Пятница':#line:1907
            OOO0O0000O00O000O =settings .Пятница11Б #line:1908
        elif weekday_name =='Суббота':#line:1909
            OOO0O0000O00O000O =settings .Понедельник11Б #line:1910
        elif weekday_name =='Воскресенье':#line:1911
            OOO0O0000O00O000O =settings .Понедельник11Б #line:1912
        Day .clear ()#line:1914
        OOO0OOOOOOOOO0O0O =Day .main (OOO0O0000O00O000O )#line:1915
        for O0OOO0000O00OOOOO in range (len (OOO0OOOOOOOOO0O0O )):#line:1916
            ress ='\n'.join (OOO0OOOOOOOOO0O0O )#line:1917
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Жду ответа⏳')#line:1919
        OOO0O0000O00O000O =settings .Замены11Б #line:1920
        Zamen .clear ()#line:1921
        O0O0OO00O00O0OO00 =Zamen .main (OOO0O0000O00O000O )#line:1922
        for O0OOO0000O00OOOOO in range (len (O0O0OO00O00O0OO00 )):#line:1923
            OO00OO0OO00O0O000 ='\n'.join (O0O0OO00O00O0OO00 )#line:1924
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Ответ получен✅')#line:1926
        CheckDateSheets1 .clear ()#line:1928
        O00OO0000OO0OOO00 =CheckDateSheets1 .main ()#line:1929
        try :#line:1930
            for O0OOO0000O00OOOOO in range (len (O00OO0000OO0OOO00 )):#line:1931
                O00O00O0OO0OOO0OO ='\n'.join (O00OO0000OO0OOO00 )#line:1932
                O00O00O0OO0OOO0OO =f"<b>{O00O00O0OO0OOO0OO}</b>"#line:1933
        except :#line:1934
            O00O00O0OO0OOO0OO =f"<i>Ошибка в поиске даты</i>"#line:1935
        if weekday_name !='Суббота'and weekday_name !='Воскресенье':#line:1938
            if weekday_name !='Четверг'and weekday_name !='Понедельник'and weekday_name !='Вторник':#line:1939
                tDay =weekday_name [:-1 ]+'у'#line:1940
            else :#line:1941
                tDay =weekday_name #line:1942
        else :#line:1943
            tDay ='Понедельник'#line:1944
        O0O0O0O00O0O0OOO0 =f'Вот твое обычное расписание на <b>{tDay}</b> \n{ress} \n\nПосмотри изменения ниже \n{O00O00O0OO0OOO0OO} \n\n{OO00OO0OO00O0O000}'#line:1945
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,O0O0O0O00O0O0OOO0 ,parse_mode ='HTML')#line:1946
        O00O00000O0O0O0OO =Zamen .s #line:1948
        '''
        bot.send_video(msg.chat.id, video)
        '''#line:1951
        keys (OO0OOOOOOO0OO0O00 )#line:1952
    else :#line:1954
        bot .send_message (OO0OOOOOOO0OO0O00 .chat .id ,'Не распознал сообщение')#line:1955
bot .infinity_polling ()