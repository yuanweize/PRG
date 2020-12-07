"""
Word-to-word translation from English to Czech with very limited dictionary
"""


DICTIONARY_ENG2CZ = {
    "one": "jedno",
    "course": "predmet",
    "please": "prosim",
    "enroll": "zapis",
    "to": "do",
    "me": "me",
    "the": "",
}


def translate_word(word, from_language, to_language):
    """
    If from_language and to_language are supported, return literal word translation. Otherwise,
    raise ValueError.
    """
    if from_language != "eng" or to_language != "cz":
        msg = "Translation from " + from_language + " to " + to_language + " is not supported"
        raise ValueError(msg)

    translation = DICTIONARY_ENG2CZ[word.lower()]
    if word[0].isupper():
        translation = translation.capitalize()
    return translation


def translate(sentence, from_language, to_language):
    """
    Return word-to-word translation of the sentence from from_language to to_language. If the
    combination of from_language and to_language is not supported, raise ValueError. Currently,
    only English (from_language='eng') to Czech (from_language='cz') translation is supported.
    """
    translated_words = []
    for word in sentence.split():
        translated_word = translate_word(word, from_language, to_language)
        translated_words.append(translated_word)
    return " ".join(translated_words)


if __name__ == "__main__":
    print("test:")
    print(translate("Please enroll me to the course", "eng", "cz"))
    print("Prosim zapiste me do predmetu")
