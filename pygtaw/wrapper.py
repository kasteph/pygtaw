import requests
from langs import langs


class Client(object):
    def __init__(self, api_key):
        """
        api_key: type <str>, see https://cloud.google.com/translate
        for more information on obtaining an API key.
        Loads the client interface for Google Translate API.
        """
        self._key = api_key
        self._url = 'https://www.googleapis.com/language/translate/v2?'

    def _build_payload(self, query, target, source):
        """
        Builds a dictionary of parameters as payload
        for the HTTP request.
        """
        payload = {
            'q': query,
            'target': target,
            'key': self._key
        }
        if source:
            payload['source'] = source
        return payload

    def _handle_response(self, response):
        """
        response: Object returned from requests, presumably
        passed from self.translate().
        Returns a Translation object.
        """
        if response.status_code in [400, 402, 404, 500]:
            self._exceptions(response)
        try:
            response = response.json()['data']['translations'][0]
            return Translation(response, self._source)
        # when 'data' cannot be retrieved possibly due to a 403
        except KeyError:
            self._exceptions(response)

    def _exceptions(self, response):
        raise Exception(response.status_code, response.json()['error']['message'])

    def translate(self, query, target, source=None):
        """
        query: type <str>, required.
        target: type <str>, required, see README.md for info on which
        languages are supported.
        source: type <str>, optional, Google Translate API can
        detect source language.

        """
        try:
            self._source = source
            payload = self._build_payload(query, langs[target], langs.get(self._source, None))
            response = requests.get(self._url, params=payload)
            return self._handle_response(response)
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

    def _get_source_language(self, detected_lang_code):
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
            return self._get_source_language(self._response['detectedSourceLanguage'])
        except KeyError:
            return 'No detected source language, source provided by user: {}'.format(self._source)
    
    @property
    def translated_text(self):
        """Returns the translated text."""
        return self._response['translatedText']

