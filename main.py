from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from asyncio import run

from googletrans import Translator
from OxfordUp import getDefinitions


translator = Translator()

API_TOKEN = '6786958928:AAE4XCxT7X3kSWw6WAsih6JLRg06Gh32y_A'
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def start_cmd(message:Message):
   await message.reply('Assalamu alaykum SpeakEnglish botiga xush kelibsiz!R')



@dp.message()
async def tarjimon(message: types.Message):
    lang = translator.detect(message.text).lang
    if len(message.text.split()) > 2:
        dest = 'uz' if lang == 'en' else 'en'
        await message.reply(translator.translate(message.text, dest).text)
    else:
        if lang == 'en':
            word_id = message.text
        else:
            word_id = translator.translate(message.text, dest='en').text

        lookup = getDefinitions(word_id)
        if lookup:
            await message.reply(f"Word: {word_id} \nDefinitions:\n{lookup['definitions']}")
        if lookup.get('audio'):
            await message.reply_voice(lookup['audio'])
        else:
            await message.reply('Bunday so`z topilmadi!')


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
        run(main())