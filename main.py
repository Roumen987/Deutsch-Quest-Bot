import asyncio
import random
import json
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "8669418178:AAEIsi_VfN2kKKI9upq9FWFVhScW9MhVPtQ"

bot = Bot(token=TOKEN)
dp = Dispatcher()

categories = {

"Животные": {
    "Hund": "собака",
    "Katze": "кошка",
    "Vogel": "птица",
    "Fisch": "рыба",
    "Pferd": "лошадь",
    "Kuh": "корова",
    "Schwein": "свинья",
    "Maus": "мышь",
    "Hase": "заяц",
    "Bär": "медведь",
    "Wolf": "волк",
    "Fuchs": "лиса",
    "Löwe": "лев",
    "Tiger": "тигр",
    "Elefant": "слон",
    "Affe": "обезьяна",
    "Ziege": "коза",
    "Schaf": "овца",
    "Huhn": "курица",
    "Ente": "утка"
},

"Школа": {
    "Schule": "школа",
    "Lehrer": "учитель",
    "Schüler": "ученик",
    "Buch": "книга",
    "Heft": "тетрадь",
    "Stift": "ручка",
    "Bleistift": "карандаш",
    "Tafel": "доска",
    "Klasse": "класс",
    "Hausaufgabe": "домашнее задание",
    "Prüfung": "экзамен",
    "Frage": "вопрос",
    "Antwort": "ответ",
    "Wort": "слово",
    "Sprache": "язык",
    "Lektion": "урок",
    "Papier": "бумага",
    "Tasche": "сумка",
    "Lineal": "линейка",
    "Radiergummi": "ластик"
},
    "Транспорт": {
    "Auto": "машина",
    "Bus": "автобус",
    "Zug": "поезд",
    "Flugzeug": "самолет",
    "Fahrrad": "велосипед",
    "Motorrad": "мотоцикл",
    "Taxi": "такси",
    "Straßenbahn": "трамвай",
    "U-Bahn": "метро",
    "Schiff": "корабль",
    "Boot": "лодка",
    "Bahnhof": "вокзал",
    "Flughafen": "аэропорт",
    "Ticket": "билет",
    "Reise": "путешествие",
    "Straße": "улица",
    "Brücke": "мост",
    "Ampel": "светофор",
    "Fahrer": "водитель",
    "Passagier": "пассажир"
},

   "Природа": {
    "Baum": "дерево",
    "Blume": "цветок",
    "Gras": "трава",
    "Wald": "лес",
    "Berg": "гора",
    "Fluss": "река",
    "See": "озеро",
    "Meer": "море",
    "Himmel": "небо",
    "Sonne": "солнце",
    "Mond": "луна",
    "Stern": "звезда",
    "Regen": "дождь",
    "Schnee": "снег",
    "Wind": "ветер",
    "Wolke": "облако",
    "Erde": "земля",
    "Stein": "камень",
    "Feuer": "огонь",
    "Wasser": "вода"
},

  "Еда": {
    "Brot": "хлеб",
    "Milch": "молоко",
    "Apfel": "яблоко",
    "Banane": "банан",
    "Orange": "апельсин",
    "Kartoffel": "картофель",
    "Tomate": "помидор",
    "Gurke": "огурец",
    "Käse": "сыр",
    "Butter": "масло",
    "Ei": "яйцо",
    "Fleisch": "мясо",
    "Fisch": "рыба",
    "Suppe": "суп",
    "Salat": "салат",
    "Wurst": "колбаса",
    "Kuchen": "торт",
    "Zucker": "сахар",
    "Saft": "сок",
    "Wasser": "вода"
},

"Технологии": {
    "Computer": "компьютер",
    "Handy": "телефон",
    "Bildschirm": "монитор",
    "Tastatur": "клавиатура",
    "Maus": "мышь",
    "Internet": "интернет",
    "Programm": "программа",
    "Datei": "файл",
    "Ordner": "папка",
    "Spiel": "игра",
    "Passwort": "пароль",
    "Benutzer": "пользователь",
    "Webseite": "сайт",
    "Nachricht": "сообщение",
    "Kamera": "камера",
    "Drucker": "принтер",
    "Laptop": "ноутбук",
    "Server": "сервер",
    "Netzwerk": "сеть",
    "Akku": "батарея"
},

"Семья": {
    "Mutter": "мама",
    "Vater": "папа",
    "Bruder": "брат",
    "Schwester": "сестра",
    "Oma": "бабушка",
    "Opa": "дедушка",
    "Onkel": "дядя",
    "Tante": "тетя",
    "Sohn": "сын",
    "Tochter": "дочь",
    "Kind": "ребенок",
    "Familie": "семья",
    "Freund": "друг",
    "Freundin": "подруга",
    "Mann": "мужчина",
    "Frau": "женщина",
    "Baby": "малыш",
    "Eltern": "родители",
    "Gast": "гость",
    "Nachbar": "сосед"
},

"Время": {
    "Zeit": "время",
    "Tag": "день",
    "Nacht": "ночь",
    "Morgen": "утро",
    "Abend": "вечер",
    "Woche": "неделя",
    "Monat": "месяц",
    "Jahr": "год",
    "Stunde": "час",
    "Minute": "минута",
    "Sekunde": "секунда",
    "Montag": "понедельник",
    "Dienstag": "вторник",
    "Mittwoch": "среда",
    "Donnerstag": "четверг",
    "Freitag": "пятница",
    "Samstag": "суббота",
    "Sonntag": "воскресенье",
    "Heute": "сегодня",
    "Morgen": "завтра"
}
}
USERS_FILE = "users.json"
ADMIN_ID = 5219697862

active_quizzes = {}
blitz_games = {}

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}

    with open(USERS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_users(users):
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(users, file, ensure_ascii=False, indent=4)


def get_user(user):
    users = load_users()

    user_id = str(user.id)

    if user_id not in users:
        users[user_id] = {
    "name": user.full_name,
    "xp": 0,
    "correct": 0,
    "wrong": 0,
    "streak": 0,
    "best_streak": 0,
    "best_blitz": 0
}

        save_users(users)

    return users


async def send_question(chat_id):
    if chat_id not in active_quizzes:
        return
    category = active_quizzes[chat_id]["category"]

    words = categories[category]

    german_word = random.choice(list(words.keys()))
    correct_answer = words[german_word]

    options = list(words.values())
    options.remove(correct_answer)

    wrong_answers = random.sample(options, 3)

    answers = wrong_answers + [correct_answer]
    random.shuffle(answers)

    builder = InlineKeyboardBuilder()

    for answer in answers:
        builder.button(
            text=answer,
            callback_data=f"answer:{answer}"
        )

    builder.adjust(1)

    active_quizzes[chat_id]["word"] = german_word
    active_quizzes[chat_id]["correct"] = correct_answer
    active_quizzes[chat_id]["answered"] = False
   
    await bot.send_message(
    chat_id,
    f"📚 Категория: {category}\n\n🇩🇪 Что означает слово:\n\n{german_word}",
    reply_markup=builder.as_markup()
)

@dp.message(Command("blitz"))
async def blitz_handler(message: Message):

    chat_id = message.chat.id

    blitz_games[chat_id] = {
        "start_time": asyncio.get_event_loop().time(),
        "correct": 0,
        "wrong": 0
    }

    active_quizzes[chat_id] = {
        "running": True,
        "category": random.choice(list(categories.keys())),
        "mode": "blitz"
    }

    await message.answer(
        "⚡ Блиц начался!\n\n"
        "У тебя 60 секунд."
    )

    await send_question(chat_id)

@dp.message(Command("start"))
async def start_handler(message: Message):
    await message.answer(
        "🇩🇪 Deutsch Quest Bot\n\n"
        "Команды:\n"
        "/quiz - начать викторину\n"
        "/stop - остановить викторину\n"
        "/stats - статистика\n"
        "/top - рейтинг игроков\n"
        "/blitz - блиц режим\n"
        "/dictionary - словарь\n"
    )


@dp.message(Command("quiz"))
async def quiz_handler(message: Message):

    builder = InlineKeyboardBuilder()

    for category in categories.keys():
        builder.button(
            text=category,
            callback_data=f"category:{category}"
        )

    builder.adjust(2)

    await message.answer(
        "📚 Выбери категорию:",
        reply_markup=builder.as_markup()
    )

    @dp.callback_query(F.data.startswith("category:"))
    async def category_handler(callback: CallbackQuery):

        category = callback.data.split(":", 1)[1]

        active_quizzes[callback.message.chat.id] = {
            "running": True,
            "category": category
        }

        await callback.answer()

        await send_question(callback.message.chat.id)


@dp.message(Command("stop"))
async def stop_handler(message: Message):

    if message.chat.id in active_quizzes:
        del active_quizzes[message.chat.id]

    await message.answer(
        "🛑 Викторина остановлена."
    )


@dp.callback_query(F.data.startswith("answer:"))
async def answer_handler(callback: CallbackQuery):

    chat_id = callback.message.chat.id
    if (
     chat_id in blitz_games
        and asyncio.get_event_loop().time()
        - blitz_games[chat_id]["start_time"] >= 60
        ):

        result = blitz_games[chat_id]

        await callback.message.answer(
            f"⏰ Время вышло!\n\n"
            f"✅ Правильных: {result['correct']}\n"
            f"❌ Ошибок: {result['wrong']}"
        )

        del blitz_games[chat_id]

        if chat_id in active_quizzes:
            del active_quizzes[chat_id]

        return
        if chat_id not in active_quizzes:
            await callback.answer("Викторина не активна")
            return

    quiz = active_quizzes[chat_id]

    if quiz["answered"]:
        await callback.answer(
            "На этот вопрос уже ответили!",
            show_alert=True
        )
        return

    quiz["answered"] = True

    answer = callback.data.split(":", 1)[1]

    users = get_user(callback.from_user)
    user = users[str(callback.from_user.id)]

    if answer == quiz["correct"]:

        user["xp"] += 10
        user["correct"] += 1
        user["streak"] += 1
        if chat_id in blitz_games:
            blitz_games[chat_id]["correct"] += 1
        if user["streak"] > user["best_streak"]:
            user["best_streak"] = user["streak"]

        save_users(users)

        await callback.message.answer(
            f"✅ Верно! +10 XP\n"
            f"🔥 Серия: {user['streak']}"
        )

    else:

        user["wrong"] += 1
        user["streak"] = 0
        if chat_id in blitz_games:
            blitz_games[chat_id]["wrong"] += 1
        save_users(users)

        await callback.message.answer(
            f"❌ Неверно!\n"
            f"Правильный ответ: {quiz['correct']}"
        )

    await callback.answer()

    await asyncio.sleep(1)

    if chat_id in active_quizzes:
        await send_question(chat_id)


@dp.message(Command("stats"))
async def stats_handler(message: Message):

    users = get_user(message.from_user)

    user = users[str(message.from_user.id)]

    level = user["xp"] // 100 + 1
    next_level_xp = level * 100
    remaining = next_level_xp - user["xp"]

    await message.answer(
        f"📊 Твоя статистика\n\n"
        f"🏆 XP: {user['xp']}\n"
        f"⭐ Уровень: {level}\n"
        f"📈 До следующего уровня: {remaining} XP\n"
        f"✅ Верных: {user['correct']}\n"
        f"❌ Ошибок: {user['wrong']}\n"
        f"🔥 Серия: {user['streak']}\n"
        f"🏅 Лучшая серия: {user['best_streak']}"
    )


@dp.message(Command("top"))
async def top_handler(message: Message):

    users = load_users()

    top_users = sorted(
        users.items(),
        key=lambda x: x[1]["xp"],
        reverse=True
    )[:10]

    text = "🏆 ТОП ИГРОКОВ\n\n"

    for i, (_, user) in enumerate(top_users, start=1):
        text += f"{i}. {user['name']} — {user['xp']} XP\n"

    await message.answer(text)

@dp.message(Command("dictionary"))
async def dictionary_handler(message: Message):

    text = "📚 СЛОВАРЬ\n\n"

    for category, words in categories.items():

        text += f"📂 {category}\n"

        for german, russian in words.items():
            text += f"🇩🇪 {german} — {russian}\n"

        text += "\n"

    if len(text) > 4000:
        parts = [text[i:i+4000] for i in range(0, len(text), 4000)]

        for part in parts:
            await message.answer(part)
    else:
        await message.answer(text)

@dp.message(Command("admin"))
async def admin_handler(message: Message):

    if message.from_user.id != ADMIN_ID:
        await message.answer("⛔ Доступ запрещён")
        return

    users = load_users()

    text = "👑 АДМИН-ПАНЕЛЬ\n\n"

    for uid, user in users.items():
        text += (
            f"{user['name']}\n"
            f"ID: {uid}\n"
            f"XP: {user['xp']}\n"
            f"🔥 Серия: {user['best_streak']}\n"
            f"✅ {user['correct']} | ❌ {user['wrong']}\n\n"
        )

    await message.answer(text)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())