import unittest
from deep_translator import MyMemoryTranslator
from translator import english_to_french, french_to_english

class TranslatorTests(unittest.TestCase):

    def setUp(self):
        self.translator = MyMemoryTranslator()

    def test_english_to_french(self):
        english_text = "Hello, how are you?"
        expected_result = "Bonjour, comment ça va ?"
        translated_text = self.translator.translate(text=english_text, lang_from='en', lang_to='fr')
        self.assertEqual(translated_text, expected_result)

    def test_french_to_english(self):
        french_text = "Bonjour, comment ça va ?"
        expected_result = "Hello, how are you?"
        translated_text = self.translator.translate(text=french_text, lang_from='fr', lang_to='en')
        self.assertEqual(translated_text, expected_result)


if __name__ == '__main__':
    unittest.main()