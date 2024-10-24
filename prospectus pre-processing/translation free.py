import os
from translatepy import Translator
from langdetect import detect

def chunk_text(text, max_chunk_size=5000):
    """Yield successive max_chunk_size chunks from text."""
    for i in range(0, len(text), max_chunk_size):
        yield text[i:i + max_chunk_size]

def translate_text(text, target_language="en"):
    """Translate text to the target language using translatepy."""
    translator = Translator()
    translated_text = []
    for text_chunk in chunk_text(text):
        result = translator.translate(text_chunk, destination_language=target_language)
        translated_text.append(result.result)
    return ''.join(translated_text)

def detect_language(text):
    """Detect the language of the first reasonable chunk of text using langdetect."""
    first_chunk = next(chunk_text(text), None)
    if first_chunk is None:
        return None  # No text to detect from
    return detect(first_chunk)

def translate_file(source_path, target_path):
    """Read the file, detect the language, translate if not English, and write to the target path."""
    with open(source_path, 'r', encoding='utf-8') as file:
        text = file.read()

    detected_language = detect_language(text)
    print(f"Detected language: {detected_language} for file {source_path}")

    if detected_language != "en":
        text = translate_text(text)

    with open(target_path, 'w', encoding='utf-8') as file:
        file.write(text)

def main(source_dir, target_dir):
    for filename in os.listdir(source_dir):
        if filename.endswith('.txt'):
            source_path = os.path.join(source_dir, filename)
            target_path = os.path.join(target_dir, filename)

            translate_file(source_path, target_path)
            print(f"Translated {source_path} and saved to {target_path}")

if __name__ == "__main__":
    source_dir = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Translation File'
    target_dir = r'C:\Users\arnel\OneDrive - KU Leuven\Thesis Economics\Python\Translation File'
    
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    main(source_dir, target_dir)
