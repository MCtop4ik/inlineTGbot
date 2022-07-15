from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.dispatcher.filters import Text
import config

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

answ = dict()

urlkb = InlineKeyboardMarkup(row_width=1)

urlBtn = InlineKeyboardButton(text="Мой ютуб канал",
                              url="https://www.youtube.com/channel/UCLEIB1UIgRfWZ7F1ng8OJ-A/videos")
urlkb.add(urlBtn)


@dp.message_handler(commands=["Ссылки"])
async def url_command(message: types.Message):
    await message.answer("Ссылочки:", reply_markup=urlkb)


inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(text='Нажми меня', callback_data='like_1'),
                                             InlineKeyboardButton(text='Нажми меня', callback_data='like_-1'))


@dp.message_handler(commands=["test"])
async def url_command(message: types.Message):
    await message.answer("Инлайн кнопка:", reply_markup=inkb)


@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback: types.CallbackQuery):
    # await callback.message.answer('Нажата онлайн кнопка')
    res = int(callback.data.split('_')[1])
    if f'{callback.from_user.id}' not in answ:
        answ[f'{callback.from_user.id}'] = res
        await callback.answer("Вы проголосовали")
    else:
        await callback.answer("Вы УЖЕ проголосовали", show_alert=True)
    # await callback.answer('Нажата онлайн кнопка')
    # await callback.answer('Нажата онлайн кнопка', show_alert=True)


executor.start_polling(dp, skip_updates=True)
