import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')













BOT_TOKEN = "7340945997:AAFVjA4ugiUoe2U2hrZaEHWpx_kTtiZjCsg"


ADMIN_CHAT_ID = 5534397208  



# Создание бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

class Form(StatesGroup):
    name = State()
    age = State()
    city = State()
    phone = State()
    email = State()
    message = State()

# Функция для создания меню кнопок
def create_menu(text, callback_data):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(text=text, callback_data=callback_data)
    keyboard.add(button)
    return keyboard

# Обработчик команды /help
@dp.message_handler(commands=['help'])
async def help_start(message: types.Message):
    await message.answer(
        "Привет! Давай познакомимся. Нажми на кнопку 'Начать'.",
        reply_markup=create_menu('Начать', 'start')
    )

# Обработчик нажатия кнопки "Начать"
@dp.callback_query_handler(text='start')
async def start_form(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.edit_text("Как тебя зовут?")
    await Form.name.set()

# Обработчик ввода имени
@dp.message_handler(state=Form.name)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text

    await message.answer("Сколько тебе лет?")
    await Form.next()

# Обработчик ввода возраста
@dp.message_handler(state=Form.age)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text

    await message.answer("В каком городе ты живешь?")
    await Form.next()

# Обработчик ввода города
@dp.message_handler(state=Form.city)
async def process_city(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['city'] = message.text

    await message.answer("Какой твой номер телефона?")
    await Form.next()

# Обработчик ввода номера телефона
@dp.message_handler(state=Form.phone)
async def process_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text

    await message.answer("Какой твой email?")
    await Form.next()

# Обработчик ввода email
@dp.message_handler(state=Form.email)
async def process_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text

    await message.answer("Напиши краткое сообщение для админа")
    await Form.next()

# Обработчик ввода сообщения
@dp.message_handler(state=Form.message)
async def process_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message'] = message.text

        # Отправка сообщения админу
        await bot.send_message(
            ADMIN_CHAT_ID,
            f"Новая анкета:\n\n"
            f"Имя: {data['name']}\n"
            f"Возраст: {data['age']}\n"
            f"Город: {data['city']}\n"
            f"Телефон: {data['phone']}\n"
            f"Email: {data['email']}\n"
            f"Сообщение: {data['message']}"
        )

    await message.answer("Спасибо! Твоя анкета отправлена админу!")
    await state.finish()

# Запуск бота
if __name__ == '__main__':
    asyncio.run(dp.start_polling())
c





