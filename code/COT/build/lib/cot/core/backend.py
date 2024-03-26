import time
import requests
import json



api_key = "sk-wzC9F9pR6895D02bd364T3BlBKFJ194A2fb2c0Fa493bADA7"
api_base = "https://api.ohmygpt.com/v1/chat/completions"
# GPT API


def call_chat_gpt(messages, model='gpt-4-1106-preview', stop=None, temperature=0., top_p=1.0, max_tokens=2096):
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

# messages = [
#     {"role": "system", "content": "You are a helpful math word problem solver."},
#     {"role": "user", "content": "WHAT IS 1+1?"}
# ]


# print(call_chat_gpt(messages))