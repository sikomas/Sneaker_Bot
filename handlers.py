from aiogram import types
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import (Message, InlineKeyboardMarkup, InlineKeyboardButton,
                           CallbackQuery, LabeledPrice, PreCheckoutQuery, ReplyKeyboardRemove)
from aiogram.utils.callback_data import CallbackData

from config import admin_id
from load_all import dp, bot
from keyboard import start_menu

@dp.message_handler(CommandStart())
async def start_message(message: types.Message):

    await message.answer('👟 Добро пожаловать в магазин кроссовок Cry Store!\n \n' 
                         '✅ У нас Вы найдете лучшую обувь по доступным ценам\n \n'
                         '📩 Для получения дополнительной информации используйте клавиатуру бота', reply_markup=start_menu)
# Обработчик нажатия кнопки "Ассортимент"
@dp.message_handler(lambda message: message.text == '👟 Ассортимент')
async def show_assortment(message: types.Message):
    await message.answer("Здесь вы увидите наш ассортимент товаров.")

# Обработчик нажатия кнопки "Заказать"
@dp.message_handler(lambda message: message.text == '📩 Заказать')
async def order(message: types.Message):
    await message.answer("Вы перешли на страницу заказа.")

# Обработчик нажатия кнопки "Условия"
@dp.message_handler(lambda message: message.text == '✅ Условия')
async def show_assortment(message: types.Message):
    await message.answer("Мы требуем полной предоплаты для всех заказов. Это позволяет нам быть уверенными в серьезности намерений покупателя. Если бы мы отправляли товар с оплатой при получении, а покупатель передумал бы, нам пришлось бы оплатить доставку в обе стороны и ждать возврата товара, что заняло бы не менее месяца. В это время другие потенциальные покупатели могли бы остаться без возможности приобрести товар.")

