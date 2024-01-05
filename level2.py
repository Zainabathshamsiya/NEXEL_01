# Dictionary for English to Spanish translations
translations = {
    "hello": "hola",
    "goodbye": "adiós",
    "cat": "gato",
    # Add more words and their translations here
}

def translate_to_spanish(word):
    if word.lower() in translations:
        return translations[word.lower()]
    else:
        return "Translation not found for this word"

# Example usage
word_to_translate = input("Enter a word in English: ")
translation = translate_to_spanish(word_to_translate)
print(f"The translation of '{word_to_translate}' in Spanish is: {translation}")