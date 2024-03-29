from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='👟 Ассортимент'),
            KeyboardButton(text='📩 Заказать'),
            KeyboardButton(text='✅ Условия')

        ],
        [
            KeyboardButton(text='💵 Реф. система'),
            KeyboardButton(text='👨‍💻 Отзывы'),
            KeyboardButton(text='☎️ Контакты')
        ]
    ], resize_keyboard=True
)




