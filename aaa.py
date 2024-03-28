import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
TOKEN = '7170428854:AAGzZySURsa_L8wuTx8GRq7nEyJmiAR6AKI'
bot = telebot.TeleBot(TOKEN)
def generate_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    keyboard.add(KeyboardButton("О вузе"), KeyboardButton("Расписание"))
    keyboard.row(KeyboardButton("Помощь"))  # Эта кнопка будет в новом ряду.
    return keyboard

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = generate_keyboard()
    bot.send_message(message.chat.id, "Привет! Чем могу помочь?", reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text == "О вузе":
        bot.send_message(message.chat.id, 'Омский политех – один из крупнейших инженерных вузов России, который ведет подготовку специалистов с 1942 года. Высокий уровень образования, современные технологии и инновационный подход к обучению за 80-летнюю историю стали его визитной карточкой.\n\n'
                                          'Открытый региону университет ежегодно организует для его жителей и гостей различные научные, культурные и творческие мероприятия. Их участниками может стать любой желающий вне зависимости от возраста, статуса и профессии.\n\n'
                                          'В 2023 году вуз вошел в федеральный проект «Передовые инженерные школы» с программой развития ПИШ в области станкоинструментального машиностроения для авиационного двигателестроения и танкостроения.')
    elif message.text == "Расписание":
        bot.send_message(message.chat.id, "Расписание можно посмотреть на сайте:")
        bot.send_message(message.chat.id, 'https://rasp.omgtu.ru/ruz/main')
    elif message.text == "Помощь":
        bot.send_message(message.chat.id, "Вы можете обратиться за помощью по контактному номеру ОмГТУ:\n"
                                          "+7-(3812)-65-33-89 \n"
                                          "Также вы можете задать вопрос в официальное сообщество университета:\n"
                                          "https://vk.com/omskpoliteh")
    else:
        bot.send_message(message.chat.id, "Извините, я не понимаю. Попробуйте использовать кнопки для навигации.")

bot.polling()

