# -*- coding: utf-8

import os
from google.cloud import translate

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'D:\UdemyCourses\gammacards-app\translation-demo\gammacards-goole-api.json'

def translate_text(text, target='en'):
    translate_client = translate.Client()
    result = translate_client.translate(text, target_language=target)

    print('1. Text:', result['input'] )
    print('1. English Translation:', result ['translatedText'])
    print('1. Detected source lang: ', result['detectedSourceLanguage'])

example_text = "你可以直接点击页面上的,这不是垃圾邮件."
translate_text(example_text)

translate_client = translate.Client()
text = 'Good Morning. Goodbye. And Hello'
target = 'ja'
output = translate_client.translate(
    text,
    target_language=target
)
print("2. output", output)


'''
def translate_text(text,target='en'):
    """
    Target must be an ISO 639-1 language code.
    https://cloud.google.com/translate/docs/languages
    """
    translate_client = translate.Client()
    result = translate_client.translate(
        text,
        target_language=target)

    print(u'Text: {}'.format(result['input']))
    print(u'Translation: {}'.format(result['translatedText']))
    print(u'Detected source language: {}'.format(
        result['detectedSourceLanguage']))
'''


