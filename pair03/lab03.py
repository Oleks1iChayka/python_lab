

# 1
print("--- Завдання 1 ---")
text = input("Введіть довільний текст: ")
vowels = "аеєиіїоуюяaeiou"
total_chars = len(text)
letters_count = sum(1 for c in text if c.isalpha())
digits_count = sum(1 for c in text if c.isdigit())
spaces_count = text.count(" ")
vowels_count = sum(1 for c in text.lower() if c in vowels)
words_count = len(text.split())

print(f"Символів: {total_chars}")
print(f"Літер: {letters_count}")
print(f"Цифр: {digits_count}")
print(f"Пробілів: {spaces_count}")
print(f"Голосних: {vowels_count}")
print(f"Слів: {words_count}")


# 2
print("\n--- Завдання 2 ---")
full_name = input("Введіть прізвище, ім'я та по батькові: ")
parts = full_name.split()

if len(parts) == 3:
    surname = parts[0].capitalize()
    name_initial = parts[1][0].upper() + "."
    patronymic_initial = parts[2][0].upper() + "."
    print(f"Результат: {surname} {name_initial}{patronymic_initial}")
else:
    print("Помилка: введіть рівно три слова (прізвище, ім'я, по батькові).")


# 3
print("\n--- Завдання 3 ---")
text1 = input("Введіть перший рядок: ")
text2 = input("Введіть другий рядок: ")

norm1 = text1.lower().replace(" ", "")
norm2 = text2.lower().replace(" ", "")

if sorted(norm1) == sorted(norm2):
    print(f"Рядки є анаграмами.\nНормалізований рядок 1: {norm1}\nНормалізований рядок 2: {norm2}")
else:
    print(f"Рядки НЕ є анаграмами.\nНормалізований рядок 1: {norm1}\nНормалізований рядок 2: {norm2}")


# 4
print("\n--- Завдання 4 ---")
sentence = input("Введіть речення: ")
words = sentence.split()

if words:
    min_len = len(min(words, key=len))
    max_len = len(max(words, key=len))

    shortest_words = list(set([w for w in words if len(w) == min_len]))
    longest_words = list(set([w for w in words if len(w) == max_len]))
    unique_words = set(w.lower() for w in words)

    print(f"Найдовші: {', '.join(longest_words)}")
    print(f"Найкоротші: {', '.join(shortest_words)}")
    print(f"Унікальних слів: {len(unique_words)}")

    old_word = input("Введіть слово для заміни: ")
    new_word = input("Введіть нове слово: ")
    
    new_sentence = sentence.replace(old_word, new_word)
    print(f"Після заміни: {new_sentence}")
else:
    print("Речення порожнє.")