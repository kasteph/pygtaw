import unittest
import responses
from pygtaw import Client

class TestPyGoogleTranslateAPIWrapper(unittest.TestCase):

    def setup(self):
        api_key = open('key').read()
        self.client = Client(api_key)

    def test_get_translated_text(self):
        self.setup()
        self.client.translate('Hola', 'English')
        self.assertEqual(self.client.translated_text, 'Hi')



