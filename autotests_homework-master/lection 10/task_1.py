import random
import string


def generate_random_name():
    """
    Генератор, который бесконечно создает случайные имена из двух слов.
    Каждое слово состоит из латинских букв (строчных) длиной от 1 до 15 символов.
    """
    while True:
        # Генерируем длину первого слова (от 1 до 15 символов)
        length1 = random.randint(1, 15)
        # Генерируем длину второго слова (от 1 до 15 символов)
        length2 = random.randint(1, 15)

        # Генерируем первое слово
        word1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(length1))
        # Генерируем второе слово
        word2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(length2))

        # Возвращаем два слова, разделенные пробелом
        yield f"{word1} {word2}"