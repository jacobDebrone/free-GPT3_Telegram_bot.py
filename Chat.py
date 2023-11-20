
import requests
import json


url = 'https://api.voidevs.com/v1/ai/chat/completions'


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


def streaming_chat(model, messages):
    try:
        data = {'model': model, 'stream': True, 'messages': messages}

        response = requests.post(url, json=data, stream=True)
        
        if response.status_code == 200:
            buffer = ''
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    buffer += chunk.decode('utf-8')
                    lines = buffer.split('\n')
                    for line in lines[:-1]:
                        data = json.loads(line)
                        yield data

                    buffer = lines[-1]
        else:
            print(f"Error: {response.status_code}, {response.text}")
            yield False

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        yield False


model = 'gpt-3.5-turbo-0613'
messages = [{'role': 'system', 'content': 'You are a helpful assistant and your name is Debrone, and you are a logical character and very scientific yet very kind'}]

# To get the answer normally
while True:
     user_input = str(input("user:  " ))
     new_message = {'role': 'user', 'content': user_input} 
     messages.append(new_message)
     result = chat(model, messages)
     if result['result']:
          print("AI:  " , result['content'])
