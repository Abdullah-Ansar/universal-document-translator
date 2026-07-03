from services.translator import TranslatorService

translator = TranslatorService()

result = translator.translate(
    "Hello World",
    "en",
    "hi"
)

print(result)