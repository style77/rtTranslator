import json
import speech_recognition as sr

GOOGLE_SUPPORTED_LANGUAGES = [
    "af",
    "eu",
    "bg",
    "ca",
    "ar-EG",
    "ar-JO",
    "ar-KW",
    "ar-LB",
    "ar-QA",
    "ar-AE",
    "ar-MA",
    "ar-IQ",
    "ar-DZ",
    "ar-BH",
    "ar-LY",
    "ar-OM",
    "ar-SA",
    "ar-TN",
    "ar-YE",
    "cs",
    "nl-NL",
    "en-AU",
    "en-CA",
    "en-IN",
    "en-NZ",
    "en-ZA",
    "en-GB",
    "en-US",
    "fi",
    "fr-FR",
    "gl",
    "de-DE",
    "he",
    "hu",
    "is",
    "it-IT",
    "id",
    "ja",
    "ko",
    "la",
    "zh-CN",
    "zh-TW",
    "zh-CN",
    "zh-HK",
    "zh-yue",
    "ms-MY",
    "no-NO",
    "pl",
    "xx-piglatin",
    "pt-PT",
    "pt-BR",
    "ro-RO",
    "ru",
    "sr-SP",
    "sk",
    "es-AR",
    "es-BO",
    "es-CL",
    "es-CO",
    "es-CR",
    "es-DO",
    "es-EC",
    "es-SV",
    "es-GT",
    "es-HN",
    "es-MX",
    "es-NI",
    "es-PA",
    "es-PY",
    "es-PE",
    "es-PR",
    "es-ES",
    "es-US",
    "es-UY",
    "es-VE",
    "sv-SE",
    "tr",
    "zu",
]

TRANSLATOR_SUPPORTED_LANUAGES = set(
    lang[:2] for lang in GOOGLE_SUPPORTED_LANGUAGES
)


class Config:
    def __init__(self, path: str):
        with open(path, "r") as f:
            self.config = json.load(f)

    def __getitem__(self, item):
        return self.config[item]

    def source_language(self, app):
        lang = self.config["source_language"]

        if app.provider is sr.Recognizer().recognize_google:
            if lang not in GOOGLE_SUPPORTED_LANGUAGES:
                raise ValueError(
                    f"Language {lang} is not supported by Google. Checkout the list of supported languages: https://stackoverflow.com/questions/14257598/what-are-language-codes-in-chromes-implementation-of-the-html5-speech-recogniti/14302134#14302134"
                )

        return lang

    @property
    def target_language(self):
        lang = self.config["target_language"]

        if lang not in TRANSLATOR_SUPPORTED_LANUAGES:
            raise ValueError(
                f"Language {lang} is not supported by the translator. Checkout the list of supported languages: https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages"
            )

        return lang