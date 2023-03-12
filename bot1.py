import telebot #подключение библиотеки для взаимодействия с ботом
bot = telebot.TeleBot('1870131373:AAH9KpxqpWVCfppdDoLzXkuWiHhowjPnSaQ') #настройка бота
list_of_chooses = [] #список, который понадобится нам далее для запис пути
    
@bot.message_handler(commands=['start']) 
#обработчик сообщений. Контролироет то, какой тип сообщений присылает бот
#в данном случае для начала общения нужно ввести команду '/start'
def start_command(message): #название функции
   keyboard = telebot.types.ReplyKeyboardMarkup(True) 
   #создание двух кнопок на которые пользователь может нажать
   keyboard.row('Давай', 'Не сегодня')
#те самые две кнопки, чтобы либо начать взаимодействие с ботом, либо прервать
   bot.send_message(message.chat.id, 'Привет! Я читай-бот, который поможет выбрать интересную книгу по вкусу. Давай начнем?', reply_markup=keyboard)
   #приветствие бота. Выводится после команды "/start"

@bot.message_handler(content_types=['text', 'stiker']) 
#обработчик сообщений. Контролироет то, какой тип сообщений присылает бот
def send_text(message): #название функции
    if message.text == 'Давай': #если текст в сообщении 'Давай'
        bot.send_message(message.chat.id, 'Приступаем!') 
        #отправить ответ пользователю
        choose_gerne(message) #начать опрос
    elif message.text == 'Не сегодня':  #если текст в сообщении 'Не сегодня'
        bot.send_message(message.chat.id, 'Мы ждем тебя!') 
        #отправить ответ пользователю
    else: #если текст в сообщении не знаком программе
        bot.send_message(message.chat.id, 'Я такого не знаю. Но скоро обязательно разберусь, что это значит') 
        #отправить ответ пользователю


@bot.message_handler(content_types=['text'])     
def choose_gerne(message): #название функции
    markup1 = telebot.types.InlineKeyboardMarkup(row_width=2) #настройка ширины кнопок
    #варианты ответов:
    markup1.add(telebot.types.InlineKeyboardButton(text='Исторический роман' , callback_data = 1))
    #каждый вариант ответа нумеруется, чтобы потом можно было проследить путь и в зависимости от вариантов ответа выдать результат
    markup1.add(telebot.types.InlineKeyboardButton(text='Классика', callback_data = 2))
    markup1.add(telebot.types.InlineKeyboardButton(text='Детектив', callback_data = 3))
    markup1.add(telebot.types.InlineKeyboardButton(text='Фентази и фантастика' , callback_data = 4))
    markup1.add(telebot.types.InlineKeyboardButton(text='Саморазвитие и психология', callback_data = 5))

    bot.send_message(message.chat.id, text="Выберете жанр", reply_markup=markup1) #сообщение, объясняющее что именно нужно выбрать

@bot.message_handler(content_types=['text'])
def choose_time(message):
    markup2 = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup2.add(telebot.types.InlineKeyboardButton(text='Средневековье' , callback_data = 6))
    markup2.add(telebot.types.InlineKeyboardButton(text='Ренессанс/Эпоха просвещения', callback_data = 7))
    markup2.add(telebot.types.InlineKeyboardButton(text='Ближе к современности', callback_data = 8))
    bot.send_message(message.chat.id, text="Выберете время в которое будут происходить события", reply_markup=markup2)

@bot.message_handler(content_types=['text'])
def choose_place(message):
    markup3 = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup3.add(telebot.types.InlineKeyboardButton(text='Восточная или Северная Европа' , callback_data = 9))
    markup3.add(telebot.types.InlineKeyboardButton(text='Россия', callback_data = 10))
    bot.send_message(message.chat.id, text="Где происходят события", reply_markup=markup3)

@bot.message_handler(content_types=['text'])
def choose_klassic(message):
    markup4 = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup4.add(telebot.types.InlineKeyboardButton(text='Зарубежная классика' , callback_data = 11))
    markup4.add(telebot.types.InlineKeyboardButton(text='Советская классика', callback_data = 12))
    markup4.add(telebot.types.InlineKeyboardButton(text='Отечественная классика', callback_data = 13))
    bot.send_message(message.chat.id, text="Что предпочитаете?", reply_markup=markup4)

@bot.message_handler(content_types=['text'])
def choose_detective(message):
    markup5 = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup5.add(telebot.types.InlineKeyboardButton(text='Триллер' , callback_data = 14))
    markup5.add(telebot.types.InlineKeyboardButton(text='Классический', callback_data = 15))
    bot.send_message(message.chat.id, text="Какой вид детектива?", reply_markup=markup5)

@bot.message_handler(content_types=['text'])
def choose_fentasy(message):
    markup6 = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup6.add(telebot.types.InlineKeyboardButton(text='Магия' , callback_data = 16))
    markup6.add(telebot.types.InlineKeyboardButton(text='Наука', callback_data = 17))
    bot.send_message(message.chat.id, text="Что вам больше нравится?", reply_markup=markup6)

@bot.message_handler(content_types=['text'])
def choose_magic(message):
    markup7 = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup7.add(telebot.types.InlineKeyboardButton(text='Эпическое' , callback_data = 18))
    markup7.add(telebot.types.InlineKeyboardButton(text='Игровое', callback_data = 19))
    bot.send_message(message.chat.id, text="Какое фентази вы предпочитаете?", reply_markup=markup7)

@bot.message_handler(content_types=['text'])
def choose_ps(message):
    markup8 = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup8.add(telebot.types.InlineKeyboardButton(text='Биография' , callback_data = 20))
    markup8.add(telebot.types.InlineKeyboardButton(text='Религия', callback_data = 21))
    markup8.add(telebot.types.InlineKeyboardButton(text='Личный рост', callback_data = 22))
    bot.send_message(message.chat.id, text="Виды книг", reply_markup=markup8)

@bot.message_handler(content_types=['text'])
def choose_rel(message):
    markup9 = telebot.types.InlineKeyboardMarkup(row_width=2)
    markup9.add(telebot.types.InlineKeyboardButton(text='Христианство' , callback_data = 23))
    markup9.add(telebot.types.InlineKeyboardButton(text='Ислам', callback_data = 24))
    bot.send_message(message.chat.id, text="Какая религия вам интересна?", reply_markup=markup9)

@bot.message_handler(content_types=['text'])   
#обработчик сообщений. Контролироет то, какоц тип сообщений присылает бот
def try_again(message): #название функции
    markup10 = telebot.types.InlineKeyboardMarkup(row_width=1) #длинна кнопок
    markup10.add(telebot.types.InlineKeyboardButton(text='ОК' , callback_data = 25)) #варианты ответа
    bot.send_message(message.chat.id, text="Попробуем ещё раз?", reply_markup=markup10)
    
@bot.callback_query_handler(func = lambda call: True) 
def callback_inline_first(call): #название функции
    if call.data == '1': #если пользователь выбрал вариант ответа под номером 1, то
        list_of_chooses.append(call.data) #добавить 1 в список, по которому отслежвается путь
        choose_time(call.message) #выбрать следующую определённуюю функцию, предоставляющую выбор
    elif call.data == '6': #если польхзователь выбрал вариант ответа под номером 6, то
        list_of_chooses.append(call.data)
        choose_place(call.message) 
    elif call.data == '9': #если польхзователь выбрал вариант ответа под номером 9, то
        list_of_chooses.append(call.data) #добавить 9 в список, по которому отслежвается путь
        #девятка является послежней в пути в выборе книги, поэтому если пользователь дошёл до нее, то нужно печатать результат
        get_result(call.message) #вызов функции печатающей результат
    elif call.data == '10':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)

    elif call.data == '7':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)
    elif call.data == '8':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)

    elif call.data == '2':
        list_of_chooses.append(call.data)
        choose_klassic(call.message)
    elif call.data == '11':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)
    elif call.data == '12':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)
    elif call.data == '13':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)

    elif call.data == '3':
        list_of_chooses.append(call.data)
        choose_detective(call.message)
    elif call.data == '14':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)
    elif call.data == '15':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)
    
    elif call.data == '4':
        list_of_chooses.append(call.data)
        choose_fentasy(call.message)
    elif call.data == '16':
        list_of_chooses.append(call.data)
        choose_magic(call.message)
    elif call.data == '17':
        list_of_chooses.append(call.data)
        get_result(call.message)
    elif call.data == '18':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)
    elif call.data == '19':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)

    elif call.data == '5':
        list_of_chooses.append(call.data)
        choose_ps(call.message)
    elif call.data == '20':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)
    elif call.data == '21':
        list_of_chooses.append(call.data)
        choose_rel(call.message)
    elif call.data == '22':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)
    elif call.data == '23':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)
    elif call.data == '24':
        list_of_chooses.append(call.data)
        print(list_of_chooses)
        get_result(call.message)
    elif call.data == '25':
        list_of_chooses.clear()
        choose_gerne(call.message)
      
def get_result(message):
    l = ''.join(list_of_chooses) #преобразование массива в строку
    if l == '169': #если пользователь шёл по пути 169 (то есть выбирал варианты ответа соответствующие именно этим числам), 
        #то результатом будет:
        bot.send_message(message.chat.id, 'Крестоносцы (Генрик Сенкевич)') #печатает результат
    elif l == '1610':
        bot.send_message(message.chat.id, 'Земля незнаемая (Тумасов Б.Е.)')
    elif l == '17':
        bot.send_message(message.chat.id, 'Образы Италии (Павел Муратов)')
    elif l == '18':
        bot.send_message(message.chat.id, 'Неизвестность (Алексей Спаповской)')
    elif l == '211':
        bot.send_message(message.chat.id, 'Унесённые ветром (Маргарет Митчелл)')
    elif l == '212':
        bot.send_message(message.chat.id, 'Земля Санникова (Владимир Обручев)')
    elif l == '213':
        bot.send_message(message.chat.id, 'Два капитана (Вениамин Каверин)')
    elif l == '314':
        bot.send_message(message.chat.id, 'Лес пропавших дев (Джун Хёр)')
    elif l == '315':
        bot.send_message(message.chat.id, 'Десять негритят (Агата Кристи)')
    elif l == '41618':
        bot.send_message(message.chat.id, 'Сага о копье (Маргарет Уэйс и Трейси Хикмэн)')
    elif l == '417':
        bot.send_message(message.chat.id, 'Дюна (Фрэнк Герберт)')
    elif l == '41619':
        bot.send_message(message.chat.id, 'Свободные миры. Змеиные войны (Анатолий Арсеньев)')
    elif l == '520':
        bot.send_message(message.chat.id, 'Великие пары (Дмитрий Быков)')
    elif l == '52123':
        bot.send_message(message.chat.id, 'Несвятые Святые (Шевкунов)')
    elif l == '52124':
        bot.send_message(message.chat.id, 'Познание смыслов (Джемаль Гейдар)')
    elif l == '522':
        bot.send_message(message.chat.id, 'Теория невероятности (Виктория Ледерман)')
    
    try_again(message) #функция с вопросом, попробовать ли еще раз пройти опрос(была описана ранее)

bot.polling() #запуск бота


    
#@bot.message_handler(content_types=['text'])
#def send_text(message):
    
   
#@bot.message_handler(content_types=["text"])
#def text_command(message):
#   bot.send_message(message.chat.id, message.text)
   
#@bot.message_handler(content_types=["photo"])
#def photo_command(message):
#  bot.send_photo(message.chat.id, message.photo[0].file_id, message.caption)

    # @bot.message_handler(content_types=['text'])


#def handle_message(message):
    