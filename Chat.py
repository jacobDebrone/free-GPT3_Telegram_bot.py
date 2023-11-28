import telebot
import requests
import json
import time
import traceback

class OpenAIAPI:
    def __init__(self, url, model):
        self.url = url
        self.model = model

    def generate_response(self, messages):
        try:
            data = {'model': self.model, 'stream': False, 'messages': messages}
            response = requests.post(self.url, json=data)

            if response.status_code == 200:
                return response.json()
            else:
                print(f"Error: {response.status_code}, {response.text}")
                return False

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return False

class MessageHandler:
    def __init__(self, bot, openai_api):
        self.bot = bot
        self.openai_api = openai_api
        self.user_messages = {}

    def handle_user_message(self, user_id, user_input):
        if user_id not in self.user_messages:
            system_message = {'role': 'system', 'content': f'You are a helpful assistant and your name is Debrone for user {user_id}, and you are very logical and very scientific yet very kind'}
            self.user_messages[user_id] = [system_message]

        new_message = {'role': 'user', 'content': user_input}
        self.user_messages[user_id].append(new_message)
        self.bot.send_chat_action(user_id, 'typing')

    def handle_ai_response(self, user_id, ai_response):
        if user_id in self.user_messages:
            new_message = {'role': 'ai', 'content': ai_response}
            self.user_messages[user_id].append(new_message)
            self.bot.send_message(user_id, f'.: {ai_response}')

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
bot_token = 'Your_telegram_bot_token'
bot = telebot.TeleBot(bot_token)

url = 'https://api.voidevs.com/v1/ai/chat/completions'
model = 'gpt-3.5-turbo-0613'

openai_api = OpenAIAPI(url, model)
message_handler = MessageHandler(bot, openai_api)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    user_id = message.chat.id
    user_input = message.text

    message_handler.handle_user_message(user_id, user_input)
    result = openai_api.generate_response(message_handler.user_messages[user_id])

    if result and result['result']:
        message_handler.handle_ai_response(user_id, result['content'])


def reconnect_and_handle_errors():
    global bot
    while True:
        try:
            bot.stop_polling()
            bot = telebot.TeleBot(bot_token)
            bot.infinity_polling(timeout=30, long_polling_timeout=5)
        except Exception as e:
            print(f"Reconnection failed: {e}")
            traceback.print_exc()
            time.sleep(10)  # Add a longer delay before attempting to reconnect again

# Start the bot
try:
    bot.infinity_polling(timeout=30, long_polling_timeout=5)
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
    reconnect_and_handle_errors()
