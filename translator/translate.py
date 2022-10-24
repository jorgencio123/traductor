from googletrans import Translator

def translate(text):
    translator = Translator()
    translation = translator.translate(text =text, src='es', dest='en')
    return translation.text
