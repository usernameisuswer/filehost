import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import ContentType

TG_BOT_TOKEN = "YOUR_BOT_TOKEN"
bot = Bot(token=TG_BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=ContentType.DOCUMENT)
async def handle_document(message: types.Message):
    file_id = message.document.file_id
    file_info = await bot.get_file(file_id)
    file_path = file_info.file_path
    downloaded_file = await bot.download_file(file_path)
    
    with open(file_info.file_unique_id + "_" + message.document.file_name, 'wb') as new_file:
        new_file.write(downloaded_file.read())
    
    # Upload file to file host site
    files = {'file': open(file_info.file_unique_id + "_" + message.document.file_name, 'rb')}
    response = requests.post("https://hikkabot.serv00.net/upload.php", files=files)
    
    os.remove(file_info.file_unique_id + "_" + message.document.file_name)

    await message.answer(f"File has been uploaded to file host site: {response.text}")
