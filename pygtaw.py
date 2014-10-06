import requests
import copy

class Client(object):
    def __init__(self, api_key):
        self.payload = {'key': api_key}
        self.url = 'https://www.googleapis.com/language/translate/v2?'
        
    def translate(self, target='es', source=None, query=None):
        payload = copy.copy(self.payload)
        if source:
            payload['source'] = source
        payload['target'] = target
        payload['q'] = query
        r = requests.get(self.url, params=payload)
        return r.json()
