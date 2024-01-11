import time
import requests
import json


api_key = "sk-LPPQ0Nc553d7078f6287T3BLbkFJ9cd1B2c52fF7451FAF98"
api_base = "https://api.ohmygpt.com/v1/chat/completions"

# GPT API


def call_chat_gpt(messages, model='gpt-4-1106-preview', stop=None, temperature=0., top_p=1.0, max_tokens=1048):
    wait = 1
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    payload = {
        'model': model,
        'max_tokens': max_tokens,
        'stop': stop,
        'messages': messages,
        'temperature': temperature,
        'top_p': top_p,
        'n': 1
    }

    while True:
        try:
            response = requests.post(
                api_base, headers=headers, data=json.dumps(payload))
            # Raises an HTTPError if the HTTP request returned an unsuccessful status code
            response.raise_for_status()

            ans = response.json()
            print(ans)
            return ans['choices'][0]['message']['content']
        except requests.exceptions.HTTPError as e:
            if response.status_code == 429:
                time.sleep(min(wait, 60))
                wait *= 2
            else:
                raise
    raise RuntimeError('Failed to call chat gpt')


messages = [{'role': 'system', 'content': 'hello'}, {
            'role': 'user', 'content': '$$$9.95-2.6-3.42$$ = '}]
ans = call_chat_gpt(messages)


print(ans)
