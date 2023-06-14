from deep_translator import MyMemoryTranslator


def english_to_french(english_text: str) -> str:
    """
    This function translates English to French using MyMemory Translator.
    """
    translator = MyMemoryTranslator()
    french_text = translator.translate(text=english_text, from_lang='autodetect', to_lang='fr')
    return french_text

def french_to_english(french_text: str) -> str:
    """
    This function translates French to English using MyMemory Translator.
    """
    translator = MyMemoryTranslator()
    english_text = translator.translate(text=french_text, from_lang='autodetect', to_lang='en')
    return english_text

