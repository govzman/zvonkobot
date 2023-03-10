# -*- coding: utf-8-1 -*-
import telepot
from telepot.loop import MessageLoop
import schedule
import sqlite3
import sys
import traceback
import time
from configure import config

TOKEN = config["token"]
bot = telepot.Bot(TOKEN)
CLASSES = ['5�', '5�', "5�", "5�", "5�", "5�", '6�', '6�', "6�", "6�", 
           "6�", '7�', '7�', "7�", "7�", "7�", '8�', '8�', "8�", "8�", 
           "8�", "8�", '9�', '9�', "9�", "9�", "9�", "9�", '10�', '10�',
           "10�", "10�", '11�', '11�', "11�", "11�", "11�"]

def handle(msg, urok=0):
    answer = 'error'
    content_type, chat_type, chat_id = telepot.glance(msg)
    text = msg["text"].lower()
    try:
        if text == '/start':
            con = sqlite3.connect("users2.db")
            cur = con.cursor()
            result = cur.execute("SELECT id FROM users WHERE dialog_id = " + str(chat_id)).fetchone()
            result2 = cur.execute("SELECT id FROM users WHERE id > -1 ").fetchall()
            if result == None:
                cur.execute("INSERT INTO users VALUES (" + str(len(result2)) + ", " + str(chat_id) + ", 0, '-')")          
            answer = '������! � ���� ���������� ���� � �������, ������ ��� ���� �����, ������� ������� /class 10�'
            con.commit()
            con.close()
        elif '/class' in text:
            if text.split()[0] == '/class' and len(text.split()) == 2:
                if len(text.split()[1]) == 2 or len(text.split()[1]) == 3:
                    if text.split()[1][-1].isalpha() and text.split()[1][-2].isdigit() and text.split()[1][0].isdigit():  
                        if text.split()[1][:-1] + text.split()[1][-1].lower() in CLASSES:
                            con = sqlite3.connect("users2.db")
                            cur = con.cursor()
                            print("UPDATE users SET class = " + text.split()[1][:-1] + ", class_letter = '" + text.split()[1][-1] + "' WHERE dialog_id = " + str(chat_id))
                            cur.execute("UPDATE users SET class = " + text.split()[1][:-1] + ", class_letter = '" + text.split()[1][-1].upper() + "' WHERE dialog_id = " + str(chat_id))
                            con.commit()
                            bot.sendMessage(chat_id, "�������, ������ �� ������� �������� ���������� � ������� � ������!")
                            return
                        else:
                            bot.sendMessage(chat_id, "������ ������ ���! ����� ����� ����� �������: /class 7�")
                            return
            answer = '������������ ������� :( ������: /class 10�'
        elif 'supertextwhatdoingbellthatsintresting' in text:
            print("bell")
            con = sqlite3.connect("users2.db")
            cur = con.cursor()
            result = cur.execute("SELECT * FROM users WHERE id > -1 ").fetchall()              
            for i in list(result): 
                try:
                    if text[-1] != '2':
                        answer = '������ c �����! '
                    else:
                        answer = '������ �� ����! '  
                    try:
                        if i[2] == 0:
                            try:
                                bot.sendMessage(i[1], str('������ ������, �� � �� ���� � ���� ��, ��� ��� �� �� ������ ���� �����, ����� ��� �������� /class *���� �����*'))
                            except:
                                pass
                    except:
                        pass
                    else:
                        result2 = cur.execute("SELECT lesson" + str(urok)[0] + " FROM classes" + str(i[2]) + str(i[3]).upper() + " WHERE day = '" + 
                                              time.ctime(time.time()).split()[0] + "'").fetchone()
                        if urok == 8.1 and i[2] <= 9:
                            try:
                                bot.sendMessage(i[1], str(answer))
                            except:
                                pass  
                        elif urok == 8.2 and i[2] >= 10:
                            try:
                                bot.sendMessage(i[1], str(answer))
                            except:
                                pass                    
                        elif result2[0] != '-' and urok != 8.1 and urok != 8.2:
                            if text[-1] != '2':
                                try:
                                    result3 = cur.execute("SELECT lesson" + str(urok + 1)[0] + " FROM classes" + str(i[2]) + str(i[3]).upper() + " WHERE day = '" + 
                                              time.ctime(time.time()).split()[0] + "'").fetchone()
                                    if result3[0] == '-':
                                        answer += '��� ��� ��������� ����!'
                                    else:
                                        answer += ('��������� ���� - ' + result3[0])
                                except:
                                    answer += '��� ��� ��������� ����!'
                            bot.sendMessage(i[1], str(answer))
                except:
                    pass
            con.close()
            return
        elif 'class' in text:
            bot.sendMessage(chat_id, "������ �������: /class 10�")
            return
        elif '�������' in text:
            bot.sendMessage(chat_id, "����������)")
            return
        else:
            answer = '��������� �� ������ :`( � ������ ��� �������� �������'
    except Exception as e:
        answer = '������:\n' + traceback.format_exc()
    try:
        bot.sendMessage(chat_id, str(answer))
    except:
        pass

MessageLoop(bot, handle).run_as_thread()

s_uroka = {'message_id': 224, 'from': {'id': 663532936, 'is_bot': False, 'first_name': 'Ilya',
                                    'last_name': 'IlyaG', 'username': 'govzman', 'language_code': 'ru'}, 
                           'chat': {'id': 663532936, 'first_name': 'Ilya', 'last_name': 'IlyaG', 
                                    'username': 'govzman', 'type': 'private'}, 'date': 1600524832, 'text': 'supertextwhatdoingbellthatsintresting'}

na_urok = {'message_id': 224, 'from': {'id': 663532936, 'is_bot': False, 'first_name': 'Ilya',
                                    'last_name': 'IlyaG', 'username': 'govzman', 'language_code': 'ru'}, 
                           'chat': {'id': 663532936, 'first_name': 'Ilya', 'last_name': 'IlyaG', 
                                    'username': 'govzman', 'type': 'private'}, 'date': 1600524832, 'text': 'supertextwhatdoingbellthatsintresting2'}
 
schedule.every().day.at("8:30").do(handle, msg=na_urok, urok=1)
schedule.every().day.at("9:10").do(handle, msg=s_uroka, urok=1)
schedule.every().day.at("9:20").do(handle, msg=na_urok, urok=2)
schedule.every().day.at("10:00").do(handle, msg=s_uroka, urok=2)
schedule.every().day.at("10:10").do(handle, msg=na_urok, urok=3)
schedule.every().day.at("10:50").do(handle, msg=s_uroka, urok=3)
schedule.every().day.at("11:00").do(handle, msg=na_urok, urok=4)
schedule.every().day.at("11:40").do(handle, msg=s_uroka, urok=4)
schedule.every().day.at("11:50").do(handle, msg=na_urok, urok=5)
schedule.every().day.at("12:30").do(handle, msg=s_uroka, urok=5)
schedule.every().day.at("12:40").do(handle, msg=na_urok, urok=6)
schedule.every().day.at("13:20").do(handle, msg=s_uroka, urok=6)
schedule.every().day.at("13:30").do(handle, msg=na_urok, urok=7)
schedule.every().day.at("14:10").do(handle, msg=s_uroka, urok=7)
schedule.every().day.at("14:40").do(handle, msg=na_urok, urok=8.1)
schedule.every().day.at("15:20").do(handle, msg=s_uroka, urok=8.1)
schedule.every().day.at("14:20").do(handle, msg=na_urok, urok=8.2)
schedule.every().day.at("15:00").do(handle, msg=s_uroka, urok=8.2)
schedule.every().day.at("15:20").do(handle, msg=na_urok, urok=9)
schedule.every().day.at("16:00").do(handle, msg=s_uroka, urok=9)

# Keep the program running.
_a = ''
while _a != 'stop':
    if time.ctime(time.time()).split()[0] not in ['Sun', 'Sat']:    
        schedule.run_pending()