import requests
from langs import langs


class Client(object):
    def __init__(self, api_key):
        """
        api_key: type <str>, see https://cloud.google.com/translate
        for more information on obtaining an API key.
        Loads the client interface for Google Translate API.
        """
        self._payload = {'key': api_key}
        self._url = 'https://www.googleapis.com/language/translate/v2?'
        self._source = None

    def build_payload(self, query, target, source):
        """
        Builds a dictionary of parameters as payload
        for the HTTP request.
        """
        payload = dict(q=query, target=target, **self._payload)
        if source:
            payload['source'] = source
        return payload

    def handle_response(self, response, source):
        """
        response: Object returned from requests, presumably
        passed from self.translate().
        Returns a Translation object.
        """
        self._response = response.json()['data']['translations'][0]
        return Translation(self._response, source)

    def translate(self, query, target, source=None):
        """
        query: type <str>, required.
        target: type <str>, required, see README.md for info on which
        languages are supported.
        source: type <str>, optional, Google Translate API can
        detect source language.

        """
        try:
            query = query.decode(encoding='utf-8')
            payload = self.build_payload(query, langs[target], langs.get(source, None))
            return self.handle_response(requests.get(self._url, params=payload), source)
        except TypeError:
            return '[query] and [target] parameters are required.'

class Translation(object):
    def __init__(self, response, source=None):
        """
        response: Object returned from Client's translate request.
        source: type <str>, language specified by user.
        Has detected_source_language and translated_text properties.
        """
        self._response = response
        self._source = source

    def get_source_language(self, detected_lang_code):
        for language, code in langs.iteritems():
            if code == detected_lang_code:
                return language

    @property
    def detected_source_language(self):
        """
        Returns the source language detected
        if the user does not provided a source language.
        """
        try:
            return self.get_source_language(self._response['detectedSourceLanguage'])
        except KeyError:
            return 'No detected source language, source provided by user: {}'.format(self._source)
    
    @property
    def translated_text(self):
        """Returns the translated text."""
        return self._response['translatedText']

