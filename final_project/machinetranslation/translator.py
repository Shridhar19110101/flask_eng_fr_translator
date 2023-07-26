"""
This module provides functions to translate text between English and French
using the MyMemoryTranslator from deep_translator.
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French.
    :param english_text: The English text to be translated.
    :type english_text: str
    :return: The translated French text.
    :rtype: str
    """
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English.
    :param french_text: The French text to be translated.
    :type french_text: str
    :return: The translated English text.
    :rtype: str
    """
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
