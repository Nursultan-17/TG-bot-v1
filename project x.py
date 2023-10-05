import telebot
import json
from telebot import types
import sqlite3
#------------------------------------------------------------------------

token = "6479649685:AAHiN88U1nt3drFnEzoNwgYH1T0PxMWj4yc"
bot = telebot.TeleBot(token)

file = open('cars.json', 'r', encoding='utf-8')
cars = json.loads(file.read())
file.close()

# query = 'CREATE TABLE Users(' \
#         'id SERIAL PRIMARY KEY,' \
#         'name VARCHAR(50),' \
#         'surname VARCHAR(50),' \
#         'login VARCHAR(50),' \
#         'password VARCHAR(64),' \
#         'status VARCHAR(50)' \
#         ')'

authorized = False
authorized_cr = False
authorized_ad = False
s_ch = ""


@bot.message_handler(commands=['start'])
def get_user_name(message):
    global hadename
    hadename = ""
    text = "Здравствуйте " + str(message.from_user.first_name) + " " + str(message.from_user.last_name) + " " + "верно? Если нет то введите ваши Имя и Фамилию"
    if message.from_user.last_name == None:
        text = "Здравствуйте " + str(message.from_user.first_name) + " " + hadename + " " + "верно? Если нет то введите ваши Имя и Фамилию"
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, username)

def username(message):
    global name
    if message.text == "Da":
        name = message.from_user.first_name + " " + message.from_user.last_name
    if message.text == "Да":
        name = message.from_user.first_name + " " + message.from_user.last_name
    if message.text == "да":
        name = message.from_user.first_name + " " + message.from_user.last_name
    if message.text == "da":
        name = message.from_user.first_name + " " + message.from_user.last_name

    else:
         name = message.text
    bot.send_message(message.chat.id, 'какую машину вы хотите?')
    bot.register_next_step_handler(message, getnamecar)

def getnamecar(message):
    global name_car
    name_car = message.text
    bot.send_message(message.chat.id,"какого года")
    bot.register_next_step_handler(message, getyear)

def getyear(message):
    global year
    year = message.text
    bot.send_message(message.chat.id, "ваш номер телефона")
    bot.register_next_step_handler(message, gettel)

def gettel(message):
    global tel
    tel = message.text
    bot.send_message(message.chat.id, "бюджет?")
    bot.register_next_step_handler(message, getprice)

def getprice(message):
    global price
    global user_name
    global zaiavki
    price = message.text
    if message.from_user.username == None:
        user_name = message.from_user.first_name
    else:
        user_name = message.from_user.username
    bot.send_message(message.chat.id, "хорошо с вами свяжутся наши специалисты")
    zaiavki = str('name -' + name + '\n' + 'make -' + name_car + '\n' + 'year - '+ year + '\n' + 'price -'+ price + '\n' + 'user name -' + user_name + '\n' + tel)
    file = open('ziavka.txt','w')
    file.write(zaiavki)
    bot.send_message(5163171438, zaiavki)

@bot.message_handler(commands=['catalog'])
def catalog(message):
    global cars
    text = ''
    counter = 1
    for car in cars:
        text += str(counter) + ') ' + car['make'] + ' ' + car['model'] + ' - ' + str(car['price']) + '$\n'
        counter += 1
    keyboard = types.InlineKeyboardMarkup()
    b_info_1 = types.InlineKeyboardButton('Info 1', callback_data='/info 1')
    b_info_2 = types.InlineKeyboardButton('Info 2', callback_data='/info 2')
    b_info_3 = types.InlineKeyboardButton('Info 3', callback_data='/info 3')
    b_info_4 = types.InlineKeyboardButton('Info 4', callback_data='/info 4')
    b_info_5 = types.InlineKeyboardButton('Info 5', callback_data='/info 5')
    b_info_6 = types.InlineKeyboardButton('Info 6', callback_data='/info 6')
    b_info_7 = types.InlineKeyboardButton('Info 7', callback_data='/info 7')
    b_info_8 = types.InlineKeyboardButton('Info 8', callback_data='/info 8')
    b_info_9 = types.InlineKeyboardButton('Info 9', callback_data='/info 9')
    b_info_10 = types.InlineKeyboardButton('Info 10', callback_data='/info 10')
    keyboard.add(b_info_1)
    keyboard.add(b_info_2)
    keyboard.add(b_info_3)
    keyboard.add(b_info_4)
    keyboard.add(b_info_5)
    keyboard.add(b_info_6)
    keyboard.add(b_info_7)
    keyboard.add(b_info_8)
    keyboard.add(b_info_9)
    keyboard.add(b_info_10)
    bot.send_message(message.chat.id, text, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda x: True)
def keyboard_call(call):
    index = int(call.data.split()[1]) - 1
    car = cars[index]
    text = 'make -' + cars[index]['make'] + "\n" + "model -" + cars[index]["model"] + "\n" + "year -" + str(
        cars[index]["year"]) + "\n" + "color -" + cars[index][
                   "color"] + "\n" + "price -" + str(cars[index]["price"]) + "\n" + "condition -" + cars[index][
                   "condition"]
    if call.data == '/info 1':
        bot.send_message(call.message.chat.id, text)
        bot.send_photo(call.message.chat.id, open('lexus ls.jpg', 'rb'))
    if call.data == '/info 2':
        bot.send_message(call.message.chat.id, text)
        bot.send_photo(call.message.chat.id, open('saturn ion.jpg', 'rb'))
    if call.data == '/info 3':
        bot.send_message(call.message.chat.id, text)
        bot.send_photo(call.message.chat.id, open('lancer.jpg', 'rb'))
    if call.data == '/info 4':
        bot.send_message(call.message.chat.id, text)
        bot.send_photo(call.message.chat.id, open('bentley.jpg', 'rb'))
    if call.data == '/info 5':
        bot.send_message(call.message.chat.id, text)
        bot.send_photo(call.message.chat.id, open('pantiac.jpg', 'rb'))
    if call.data == '/info 6':
        bot.send_message(call.message.chat.id, text)
        bot.send_photo(call.message.chat.id, open('Isuzu.jpg', 'rb'))
    if call.data == '/info 7':
        bot.send_message(call.message.chat.id, text)
        bot.send_photo(call.message.chat.id, open('evo.jpg', 'rb'))
    if call.data == '/info 8':
        bot.send_message(call.message.chat.id, text)
        bot.send_photo(call.message.chat.id, open('ford e 150.jpg', 'rb'))
    if call.data == '/info 9':
        bot.send_message(call.message.chat.id, text)
        bot.send_photo(call.message.chat.id, open('ford mustang.jpg', 'rb'))
    if call.data == '/info 10':
        bot.send_message(call.message.chat.id, text)
        bot.send_photo(call.message.chat.id, open('audi tt.jpg', 'rb'))


@bot.message_handler(commands=['registration'])
def User_reg(message):
    text = "Имя состоит мин 1 макс 50 символов\n" \
           "Фамилия состоит мин 1 макс 50 символов\n" \
           "В логине не должно быть пробелов\n" \
           "Логин должен состоять мин 4 макс 50 символов\n" \
           "В логине должна быть минимум 1 заглавная буква\n" \
           "Логин не должен быть таким же, как и пароль\n" \
           "Кроме букв алфавита(латиницы) и цифр в логине ничего не может быть\n" \
           "пароль должен состоять мин 8 макс 50 символов\n" \
           "В пароле не должно быть пробелов\n" \
           "В пароле должна быть минимум 1 заглавная буква\n" \
           "Кроме букв алфавита(латиницы) и цифр в пароле ничего не может быть"
    bot.send_message(message.chat.id, text)
    text2 ="Введите свое имя или введите «выход», чтобы выйти:"
    bot.send_message(message.chat.id, text2)
    bot.register_next_step_handler(message, get_name)

def get_name(message):
    if message.text == "выход":
        return bot.send_message(message.chat.id, "Вы вышли из регистраций")
    global name
    name = message.text
    text3 = "Введите свою фамилию или введите «выход», чтобы выйти:"
    bot.send_message(message.chat.id, text3)
    bot.register_next_step_handler(message, get_surname)

def get_surname(message):
    if message.text == "выход":
        return bot.send_message(message.chat.id, "Вы вышли из регистраций")
    global surname
    surname = message.text
    text4 = "Введите свой логин или введите «exit», чтобы выйти:"
    bot.send_message(message.chat.id, text4)
    bot.register_next_step_handler(message, get_login)

def get_login(message):
    connect = sqlite3.connect("projectTG.db")
    cursor = connect.cursor()
    if message.text == "exit":
        return bot.send_message(message.chat.id, "Вы вышли из регистраций")
    global login
    login = message.text
    if ' ' in login:
        return bot.send_message(message.chat.id, "В логине не должно быть пробелов"),bot.register_next_step_handler(message, get_login)
    if len(login) < 4 or len(login) > 50:
        return bot.send_message(message.chat.id, "Логин должен состоять мин 4 макс 50 символов"),bot.register_next_step_handler(message, get_login)
    if login.islower() and not login.isnumeric():
        return bot.send_message(message.chat.id, "В логине должна быть минимум 1 заглавная буква"),bot.register_next_step_handler(message, get_login)
    for letter in login:
        if 48 <= ord(letter) <= 57 or 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
            continue
        else:
            return bot.send_message(message.chat.id,"Кроме букв алфавита(латиницы) и цифр в логине ничего не может быть"),bot.register_next_step_handler(message, get_login)
    cursor.execute("SELECT login FROM Users WHERE login='" + login + "'")
    b = str(cursor.fetchone())
    if b[2:-3] == login:
        return bot.send_message(message.chat.id, "логин уже занят"),bot.register_next_step_handler(message, get_login)
    text5 = "Введите свой пароль или введите «exit», чтобы выйти:"
    bot.send_message(message.chat.id, text5)
    bot.register_next_step_handler(message, get_password)
    cursor.close()
    connect.close()

def get_password(message):
    if message.text == "exit":
        return bot.send_message(message.chat.id, "Вы вышли из регистраций")
    global password
    password = message.text
    if len(password) < 8 or len(password) > 50:
        return bot.send_message(message.chat.id, "пароль должен состоять мин 8 макс 50 символов"),bot.register_next_step_handler(message, get_password)
    if ' ' in password:
        return bot.send_message(message.chat.id, "В пароле не должно быть пробелов"),bot.register_next_step_handler(message, get_password)
    if password.islower() and not password.isnumeric():
        return bot.send_message(message.chat.id, "В пароле должна быть минимум 1 заглавная буква"),bot.register_next_step_handler(message, get_password)
    for letter in password:
        if 48 <= ord(letter) <= 57 or 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
            continue
        else:
            return bot.send_message(message.chat.id, "Кроме букв алфавита(латиницы) и цифр в пароле ничего не может быть"),bot.register_next_step_handler(message, get_password)
    if login == password:
        return bot.send_message(message.chat.id, "Логин не должен быть таким же, как и пароль"),bot.register_next_step_handler(message, get_password)
    text5 = "Введите свой статус если его нет введите просто «User» или введите «выход», чтобы выйти:"
    bot.send_message(message.chat.id, text5)
    bot.register_next_step_handler(message, get_status)

def get_status(message):
    connect = sqlite3.connect("projectTG.db")
    cursor = connect.cursor()
    if message.text == "выход":
        return bot.send_message(message.chat.id, "Вы вышли из регистраций")
    global status
    status = message.text
    reg_db = "insert into Users (name,surname,login,password,status)values('" + str(name) + "','" + str(surname) + "','" + str(login) + "','" + str(password) + "','" + str(status) + "')"
    cursor.execute(reg_db)
    connect.commit()
    connect.close()
    cursor.close()
    text6 = "Регистрация прошла успешно"
    return bot.send_message(message.chat.id, text6)

@bot.message_handler(commands=['signin'])
def sign_in(message):
    text = "Введите логин"
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, get_s_log)

def get_s_log(message):
    global s_log
    global s_ch
    connect = sqlite3.connect("projectTG.db")
    cursor = connect.cursor()
    s_log = message.text
    cursor.execute("SELECT login FROM Users WHERE login='" + str(s_log) + "'")
    b = str(cursor.fetchone())
    if b[2:-3] != s_log:
        return bot.send_message(message.chat.id, "Логин не верный")
    cursor.execute("SELECT login,status FROM Users WHERE login='" + str(s_log) + "'")
    s_ch = str(cursor.fetchall())
    text = "Введите пароль"
    bot.send_message(message.chat.id, text)
    bot.register_next_step_handler(message, get_s_pass)
    cursor.close()
    connect.close()

def get_s_pass(message):
    connect = sqlite3.connect("projectTG.db")
    cursor = connect.cursor()
    global s_pass
    global s_ch
    global authorized_cr
    global authorized
    s_pass = message.text
    cursor.execute("SELECT password FROM Users WHERE password='" + str(s_pass) + "'")
    b = str(cursor.fetchone())
    if b[2:-3] != s_pass:
        return bot.send_message(message.chat.id, "Пароль не верный")
    if s_ch.split("'")[3] == "creator":
        authorized_cr = True
        bot.send_message(message.chat.id, "creator mode ON")
    authorized = True
    text = "Авторизация прошла успешно!"
    cursor.close()
    connect.close()
    return bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['logout'])
def log_out(message):
    global authorized
    global authorized_cr
    if authorized == True:
        authorized = False
        authorized_cr = False
        return bot.send_message(message.chat.id, "Вы вышли из свой учетной записи")
    if authorized_cr == True:
        authorized_cr = False
        return bot.send_message(message.chat.id, "creator mode OFF")
    return bot.send_message(message.chat.id, "Вы не авторизованы")

@bot.message_handler(content_types=['text'])
def creator_m(message):
    global authorized_cr
    connect = sqlite3.connect("projectTG.db")
    cursor = connect.cursor()
    if authorized_cr == True:
        if message.text == "print all users":
            cursor.execute("SELECT * from Users")
            users = str(cursor.fetchall())
            cursor.close()
            connect.close()
            return bot.send_message(message.chat.id, users)
        if message.text == "delete":
            bot.send_message(message.chat.id,"Введите логин удаляемого пользователя")
            bot.register_next_step_handler(message, delete_user)

def delete_user(message):
    connect = sqlite3.connect("projectTG.db")
    cursor = connect.cursor()
    global authorized_cr
    if authorized_cr == True:
        user = str(message.text)
        cursor.execute("delete from Users where login =" +"'"+user+"'")
        connect.commit()
        cursor.close()
        connect.close()
        return bot.send_message(message.chat.id,"пользователь удален")


@bot.message_handler(commands=['help'])
def help(message):
    text = 'Hello, I am car shop bot!\n' \
                '/catalog - Show all autos🚗'+'\n'+ '/info n - show info car'

    bot.send_message(message.chat.id,text)




bot.infinity_polling()