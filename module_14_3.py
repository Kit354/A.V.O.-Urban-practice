from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Рассчитать')
button_2 = KeyboardButton(text='Информация')
button_3 = KeyboardButton(text='Купить')
kb.add(button_1)
kb.insert(button_2)
kb.add(button_3)

lkb = InlineKeyboardMarkup()
lkb_button_1 = InlineKeyboardButton(text='Рассчитать норму каллорий', callback_data='calories')
lkb_button_2 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formula')
lkb.add(lkb_button_1)
lkb.insert(lkb_button_2)

lkb_2 = InlineKeyboardMarkup(row_width=4)
lkb_2_button_1 = InlineKeyboardButton(text='Продукт 1', callback_data='product_buying')
lkb_2_button_2 = InlineKeyboardButton(text='Продукт 2', callback_data='product_buying')
lkb_2_button_3 = InlineKeyboardButton(text='Продукт 3', callback_data='product_buying')
lkb_2_button_4 = InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
lkb_2.add(lkb_2_button_1, lkb_2_button_2, lkb_2_button_3, lkb_2_button_4)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer(f'Привет {message.from_user.first_name}! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Рассчитать')
async def mail_menu(message):
    await message.answer('Выберите опцию:', reply_markup=lkb)


@dp.callback_query_handler(text='formula')
async def get_formulas(call):
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await message.answer(
        f'Ваша норма колорий: {10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5}',
        reply_markup=kb)
    await state.finish()


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for number in range(1, 5):
        await message.answer(f'Название: Product{number} | Описание: описание {number}, | Цена: {number * 100}')
        with open(f'photo{number}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки.', reply_markup=lkb_2)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler()
async def all_messages(message):
    print('Введите команду /start, чтобы начать общение.')
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
