free chatgpt telegram bot
Powered by free chatgpt API with Text to speech
Overview

This Python script implements a chatbot using the Telebot library for Telegram and the OpenAI GPT-3.5 Turbo model for natural language processing. The chatbot engages in conversations with users, processing their input and generating responses through a free chatgpt API.

How to Use

    Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token obtained from BotFather.
    Ensure the required libraries (telebot, requests, and gTTS) are installed.

    run pip install -r requirements.txt
    Run the script

    

    Python 3.x
    Telebot library (pip install pyTelegramBotAPI)
    Requests library (pip install requests)

Setup

    Replace 'BOT_TOKEN' with your actual bot token from BotFather.

    python

bot_token = 'YOUR_BOT_TOKEN'

Ensure the required Python libraries are installed.

bash

pip install pyTelegramBotAPI requests

Run the script.

bash

python your_script_name.py
Telegram Bot Setup

    Create a new bot on Telegram using BotFather.
    Replace bot_token with the obtained token.


Error Handling

The script includes a reconnect_and_handle_errors function to gracefully handle connection issues by attempting to reconnect the bot after encountering an exception.
Note

    This script is a basic implementation and can be extended for more complex conversational scenarios.
  

Feel free to reach out if you have any questions or suggestions! 🚀✨
for other usecases of the API contact https://github.com/voidevs 
