
import wikipedia
import logging


from aiogram import Bot, Dispatcher, executor, types 

API_TOKEN = '5465410568:AAFuYOPwmWc8SygrMoCNY9uFSxDr7uHqmyY'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN) 
dp = Dispatcher(bot) 
wikipedia.set_lang("uz")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply(f"*Assalomu alekum {message.from_user.username} \nbotimizga xush kelibsiz \nWikipediyadan nima qidiramiza😉😉*",parse_mode='markdown')
    print(message.from_user.username)


@dp.message_handler()
async def wiki(message: types.Message):
    try:
        natija = wikipedia.summary(message.text)
        await message.answer('Maqola topildi🤙')
        await message.answer(natija)

    except:
        await message.answer('Maqola topilmadi🖕') 


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

















































