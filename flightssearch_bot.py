import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from pyrogram.types import (
    ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
)

load_dotenv()

app = Client(
    'flightssearch_bot',
    api_id = os.environ["TELEGRAM_API_ID"],
    api_hash = os.environ["TELEGRAM_API_HASH"],
    bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
)

@app.on_message(filters.command('help'))
async def help(client, message):
    print(message.chat.username, message.text)
    await message.reply(        
        'Lista de comandos: '
        '''
            /chat_id para capturar o id do chat e usar na API
        '''
    )

@app.on_message(filters.command('chat_id'))
async def help(client, message):
    id = message.chat.id    
    await message.reply(
        f'Olá {message.chat.username}, seu chat_id é: {id}. '
        'Cole seu chat_id no campo solicitado da API.'
    )

@app.on_message(filters.audio | filters.voice)
async def help(client, message):    
    await message.reply(
        'Descuple, mas não consigo processar audios. Tente usar o comando /help para mais informações.'
    )

@app.on_message(filters.sticker | filters.photo | filters.video)
async def help(client, message):
    await message.reply(
        'Descuple, mas não consigo processar imagens ou videos. Tente usar o comando /help para mais informações.'
    )

@app.on_message()
async def message(client, message):
    await message.reply(
        f'Olá {message.chat.username}, sou o Flights Search. Clique ou digite /help para mais comandos'
    )

print('Rodando...')
app.run()
