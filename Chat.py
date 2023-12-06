######
import requests
import json
import telebot
import time

# Set up the Telegram Bot API token (replace 'YOUR_BOT_TOKEN' with your actual token)
bot_token = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(bot_token)

# OpenAI API URL
openai_url = 'https://api.voidevs.com/v1/ai/chat/completions'

# Default model and messages
model = 'gpt-3.5-turbo-1106'
user_messages = {}


# Function to handle OpenAI chat requests
def chat_with_openai(user_id, messages):
    try:
        data = {'model': model, 'stream': False, 'messages': messages}
        response = requests.post(openai_url, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"OpenAI Error: {response.status_code}, {response.text}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"OpenAI Error: {e}")
        return False


# Function to get user input from Telegram
@bot.message_handler(func=lambda message: True)
def get_user_input(message):
    user_id = message.from_user.id

    if user_id not in user_messages:
        user_messages[user_id] = []

    user_message = {'role': 'user', 'content': message.text}
    user_messages[user_id].append(user_message)

    # Simulate typing
    bot.send_chat_action(message.chat.id, 'typing')
    time.sleep(2)  # Simulate typing for 2 seconds (adjust as needed)

    # Chat with OpenAI
    result = chat_with_openai(user_id, user_messages[user_id])

    # Print OpenAI response
    if result['result']:
        bot.reply_to(message, result['content'])
    else:
        bot.reply_to(message, str(result))
def run_bot():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Error: {e}")
            # Wait for a short time before attempting to restart
            time.sleep(5)


# Start the bot
run_bot()
