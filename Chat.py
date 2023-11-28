import telebot
import requests

# Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
bot = telebot.TeleBot('telegram_bot_token')

url = 'https://api.voidevs.com/v1/ai/chat/completions'
model = 'gpt-3.5-turbo-0613'

# Initialize a dictionary to store the last 5 messages for each user
user_conversations = {}

def get_initial_system_message():
    return [{'role': 'system', 'content': 'You are a character in a dialogue and your name is Debrone, and you are very logical  and very scientific yet very kind you engage in infomative and tech related conversations'}]

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    user_id = message.from_user.id
    user_input = message.text

    # Retrieve or initialize conversation history for the user
    user_history = user_conversations.get(user_id, get_initial_system_message())
    
    # Keep only the last 4 user messages (and the initial system message)
    user_history = user_history[-4:]
    
    new_message = {'role': 'user', 'content': user_input}
    user_history.append(new_message)

    # Update the user's conversation history in the dictionary
    user_conversations[user_id] = user_history

    bot.send_chat_action(message.chat.id, 'typing')

    result = chat(model, user_history)
    if result and result['result']:
        bot.send_message(message.chat.id, f' {result["content"]}')
def chat(model, messages):
    try:
        data = {'model': model, 'stream': False, 'messages': messages}

        response = requests.post(url, json=data)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return False
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
