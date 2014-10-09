import unittest
import responses
from translate import pygtaw

class TestPyGoogleTranslateAPIWrapper(unittest.TestCase):

    def setUp(self):
        self.make_client()

    def make_client(self):
        api_key = open('key').read()
        self.client = pygtaw.Client(api_key)

    def test_get_translated_text(self):
        hola = self.client.translate('Hola', 'English')
        self.assertEqual(hola.translated_text, 'Hi')

    def tearDown(self):
        self.make_client()


