from deep_translator import GoogleTranslator


class TranslatorService:

    def translate(self, text, source, target):

        if not text.strip():
            return text

        return GoogleTranslator(
            source=source,
            target=target
        ).translate(text)