pygtaw
======

A tiny Google Translate API wrapper written in Python. An API key is needed to use this. More information on obtaining the API key can be found on the [Google Translate API site](https://cloud.google.com/translate/).

The full list of [supported languages](https://cloud.google.com/translate/v2/using_rest#language-params).

usage
-----
Identify your api key and make a new Client object.
```
>>> from pygtaw import Client
>>> api_key = 'ENTER_API_KEY'
>>> client = Client(api_key)
```
To make the translation request:
```
>>> query = 'Hello, world!'
>>> target = 'Korean'
>>> source = 'English'
>>> translation = client.translate(query, target, source)
>>> 
>>> print translation.translated_text
안녕하세요
```
You can send a translation request without a source as well--the Google Translate API can detect the source language:
```
>>> translation = client.translate('Hello', target='Spanish')
>>> print translation.translated_text
Hola
>>> print translation.detected_source_language
English
```
