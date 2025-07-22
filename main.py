import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print("Произошла ошибка:", e)
        return None

def translate_text(text, target='ru'):
    try:
        return GoogleTranslator(source='auto', target=target).translate(text)
    except Exception as e:
        print("Ошибка при переводе:", e)
        return text

def word_game():
    print("Добро пожаловать в игру \"Угадай слово\"!")
    while True:
        word_dict = get_english_words()
        if not word_dict:
            break

        eng_word = word_dict.get("english_word")
        eng_def = word_dict.get("word_definition")

        rus_word = translate_text(eng_word)
        rus_def = translate_text(eng_def)

        print(f"\nОпределение: {rus_def}")
        user_input = input("Какое это слово на русском? ").strip().lower()

        if user_input == rus_word.lower():
            print("✅ Верно!")
        else:
            print(f"❌ Неверно. Правильный ответ: {rus_word} (англ. {eng_word})")

        play_again = input("\nХотите сыграть еще раз? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Спасибо за игру!")
            break

word_game()
