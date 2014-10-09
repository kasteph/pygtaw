import requests
from langs import langs


class Client(object):
    """
    api_key: type <str>, see https://cloud.google.com/translate
    for more information on obtaining an API key.
    Loads the client interface for Google Translate API.
    """
    def __init__(self, api_key):
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

    def translate(self, query, target='Spanish', source=None):
        """
        query: type <str>, required.
        target: type <str>, required, see README.md for info on which
        languages are supported.
        source: type <str>, not required, Google Translate API can
        detect source language.

        """
        query.decode(encoding='utf-8')
        payload = self.build_payload(query, langs[target], langs.get(source, None))
        return self.handle_response(requests.get(self._url, params=payload), source)

class Translation(object):
    def __init__(self, response, source=None):
        self._response = response
        self._source = source

    @property
    def detected_source_language(self):
        """
        Returns the source language detected
        if the user does not provided a source language.
        """
        try:
            return self._response['detectedSourceLanguage']
        except KeyError:
            return 'No detected source language, source provided by user: {}'.format(self._source)
    
    @property
    def translated_text(self):
        """Returns the translated text."""
        return self._response['translatedText']

