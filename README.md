free chatgpt telegram bot
Overview

This Python script implements a chatbot using the Telebot library for Telegram and the OpenAI GPT-3.5 Turbo model for natural language processing. The chatbot engages in conversations with users, processing their input and generating responses through a free chatgpt API.
Features

    Handles user messages and maintains conversation history for each user.
    Sends system messages to users introducing the chatbot's persona (Debrone).
    Utilizes the OpenAIAPI class to interact with the OpenAI GPT-3.5 Turbo model for response generation.
    Handles errors and connection issues gracefully with the reconnect_and_handle_errors function.

How to Use

    Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token obtained from BotFather.
    Ensure the required libraries (telebot, requests, json, time, and traceback) are installed.
    Run the script.

Classes
OpenAIAPI

    __init__(self, url, model): Initializes the OpenAIAPI object with the API endpoint URL and the GPT model.
    generate_response(self, messages): Sends user messages to the OpenAI API and retrieves the generated response.

MessageHandler

    __init__(self, bot, openai_api): Initializes the MessageHandler object with a Telegram bot and an OpenAIAPI object.
    handle_user_message(self, user_id, user_input): Handles incoming user messages, adds them to the conversation history.
    handle_ai_response(self, user_id, ai_response): Handles AI responses, adds them to the conversation history, and sends them to the user.

Telegram Bot Setup

    Create a new bot on Telegram using BotFather.
    Replace bot_token with the obtained token.


Error Handling

The script includes a reconnect_and_handle_errors function to gracefully handle connection issues by attempting to reconnect the bot after encountering an exception.
Note

    This script is a basic implementation and can be extended for more complex conversational scenarios.
  

Feel free to reach out if you have any questions or suggestions! 🚀✨
