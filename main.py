import requests

url = 'https://api.chatgpt.com/v1/completions'
api_key = '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'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

data = {
    'prompt': 'Привет, как дела?',
    'max_tokens': 50,
    'model': 'gpt-3.5-turbo'
}

response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    print("Ответ успешно получен:")
    print(response.json())
else:
    print("Ошибка при получении ответа:")
    print(response.text)
