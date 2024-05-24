import requests 

import env 
############################
# 英語を日本語に翻訳していく
############################
def deepl(text):
    deepl_api = env.os.environ.get('DEEPL_API')

    source_lang = 'EN'
    target_lang = 'JA'

    params = {
        'auth_key': deepl_api,
        'text': text,
        'source_lang': source_lang,
        'target_lang': target_lang
    }

    response = requests.post('https://api-free.deepl.com/v2/translate', data=params)
    result = response.json()['translations'][0]['text']
    
    return result

