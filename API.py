import requests
import os


token_path = '/home/tim/yandex-IAM-token'
IAM_TOKEN = os.path.join(os.getcwd(), token_path)

with open(IAM_TOKEN) as f:
    IAM_TOKEN = f.read().strip()

FOLDER_ID = 'b1g7mgpi4g38kadsdauc'


def translate(target_language: str, text: str) -> str:
    body = {
        "targetLanguageCode": target_language,
        "texts": text,
        "folderId": FOLDER_ID,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {0}".format(IAM_TOKEN)
    }

    response = requests.post('https://translate.api.cloud.yandex.net/translate/v2/translate',
                             json=body,
                             headers=headers)

    print(response.json())
    return response.json()['translations'][0]['text']
