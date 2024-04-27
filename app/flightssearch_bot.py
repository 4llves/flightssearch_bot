import os
from dotenv import load_dotenv
from pyrogram import Client, filters
from server import start_server
import threading

load_dotenv()

# Dicionário para armazenar as respostas do usuário
respostas = {}

# Lista de perguntas
perguntas = [
    "Qual é o seu nome?",
    "Qual é a sua idade?",
    "Qual é a sua cidade?"
]

def bot():
    app = Client(
        'flightssearch_bot',
        api_id = os.environ["TELEGRAM_API_ID"],
        api_hash = os.environ["TELEGRAM_API_HASH"],
        bot_token = os.environ["TELEGRAM_BOT_TOKEN"]
    )

    @app.on_message(filters.command('help'))
    async def help(client, message):
        print('Recebendo dados... 👌')
        await message.reply(
            'Lista de comandos: '
            '''
                /chat_id para capturar o id do chat e usar na API
                /perguntas testa ai
            '''
        )

    @app.on_message(filters.command('perguntas'))
    async def proxima_pergunta(client, message, index):
        await message.reply(perguntas[index])
    
    async def lidar_com_resposta(client, message):
        global respostas
        global perguntas

        # Verifica se há perguntas pendentes
        if len(respostas) < len(perguntas):
            index = len(respostas)  # Índice da próxima pergunta
            resposta = message.text  # Captura a resposta do usuário
            respostas[index] = resposta  # Salva a resposta

            # Verifica se todas as perguntas foram respondidas
            if len(respostas) < len(perguntas):
                await proxima_pergunta(client, message, index)
            else:
                # Todas as perguntas foram respondidas, faça algo com as respostas
                await message.reply("Obrigado por responder a todas as perguntas!")
                await message.reply("Aqui estão suas respostas:")
                for index, resposta in respostas.items():
                    await message.reply(f"Pergunta {index + 1}: {perguntas[index]} Resposta: {resposta}")

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

if __name__ == '__main__':
    bot()
