import requests

langs = {
            'Afrikaans': 'af',
            'Albanian': 'sq',
            'Arabic': 'ar',
            'Azerbaijani': 'az',
            'Basque': 'eu',
            'Belarusian': 'be',
            'Bengali': 'bn',
            'Bulgarian': 'bg',
            'Catalan': 'ca',
            'Chinese Simplified': 'zh-CN',
            'Chinese Traditional': 'zh-TW',
            'Croatian': 'hr',
            'Czech': 'cs',
            'Danish': 'da',
            'Dutch': 'nl',
            'English': 'en',
            'Esperanto': 'eo',
            'Estonian': 'et',
            'Filipino': 'tl',
            'Finnish': 'fi',
            'French': 'fr',
            'Galician': 'gl',
            'Georgian': 'ka',
            'German': 'de',
            'Greek': 'el',
            'Gujarati': 'gu',
            'Haitian Creole': 'ht',
            'Hebrew': 'iw',
            'Hindi': 'hi',
            'Hungarian': 'hu',
            'Icelandic': 'is',
            'Indonesian': 'id',
            'Irish': 'ga',
            'Italian': 'it',
            'Japanese': 'ja',
            'Kannada': 'kn',
            'Korean': 'ko',
            'Latin': 'la',
            'Latvian': 'lv',
            'Lithuanian': 'lt',
            'Macedonian': 'mk',
            'Malay': 'ms',
            'Maltese': 'mt',
            'Norwegian': 'no',
            'Persian': 'fa',
            'Polish': 'pl',
            'Portuguese': 'pt',
            'Romanian': 'ro',
            'Russian': 'ru',
            'Serbian': 'sr',
            'Slovak': 'sk',
            'Slovenian': 'sl',
            'Spanish': 'es',
            'Swahili': 'sw',
            'Swedish': 'sv',
            'Tamil': 'ta',
            'Telugu': 'te',
            'Thai': 'th',
            'Turkish': 'tr',
            'Ukrainian': 'uk',
            'Urdu': 'ur',
            'Vietnamese': 'vi',
            'Welsh': 'cy',
            'Yiddish': 'yi'
        }


class Client(object):
    def __init__(self, api_key):
        self._payload = {'key': api_key}
        self._url = 'https://www.googleapis.com/language/translate/v2?'
        self._response = None

    def build_translation_request(self, target, source, query):
        payload = dict(target=target, q=query, **self._payload)
        if source:
            payload['source'] = source
        return payload

    def translate(self, target='Spanish', source, query):
        payload = self.build_translation_request(langs[target], langs.get(source, None), query)
        r = requests.get(self._url, params=payload)
        self._response = r.json()['data']['translations'][0]

    @property
    def source_language_detected(self):
        return self._response['detectedSourceLanguage']
    
    @property
    def translated_text(self):
        return self._response['translatedText']
