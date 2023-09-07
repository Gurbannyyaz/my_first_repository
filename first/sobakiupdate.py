import requests
import time

API_URL: str = 'https://api.telegram.org/bot'
API_DOGS_URL: str = 'https://random.dog/woof.json'
BOT_TOKEN: str = '6492123065:AAE8RiRC1AR6EYVNWTqLRtVwH-gDSSMBR-0'
ERROR_TEXT: str = 'Здесь должна была быть картинка с собачкой :('

offset: int = -2
counter: int = 0
dog_response: requests.Response
cat_link: str


while counter < 100:
    print('attempt =', counter)
    updates = requests.get(f'{API_URL}{BOT_TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            dog_response = requests.get(API_DOGS_URL)
            if dog_response.status_code == 200:
                dog_link = dog_response.json()['url']
                requests.get(f'{API_URL}{BOT_TOKEN}/sendPhoto?chat_id={chat_id}&photo={dog_link}')
            else:
                requests.get(f'{API_URL}{BOT_TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    time.sleep(1)
    counter += 1
