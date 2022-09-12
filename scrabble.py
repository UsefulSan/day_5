import random as r

alphabet = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о",
            "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я")
user_1_letters = []
user_2_letters = []
list_used_words = []
final_result = {}

def random_letters(user_name_letter, user_name, new_letters=1):
    """Создаётся список из рандомных букв для каждого участника
    :type user_name_letter: list
    """
    for i in range(new_letters):
        got_letter = r.choice(alphabet)
        user_name_letter.append(got_letter)
    print(f'{user_name} - имеет буквы: "' + ", ".join(user_name_letter) + '"')
    return user_name_letter


def words(user_input, list_used_words, opened_file):
    """Проверка на наличие слова в russian_word.txt. Добавление использованного слова в список"""
    if user_input in opened_file and user_input not in list_used_words:
        list_used_words.append(user_input)
        print('Такое слово существует и его ещё не называли.')
        return True
    elif user_input in opened_file and user_input in list_used_words:
        print('Вы уже называли это слово.')
        return False
    else:
        print('Такого слова нет ')
        return False


def stop_game(user_input):
    """Останавливает игру если игрок вводит stop"""
    if user_input == 'stop':
        return False
    return True


def correct_user_choice(user_input, user_name_letter):
    """Проверка вводимых букв на то, что они есть в списке предложенных"""
    while True:
        for n in user_input:
            if n not in user_name_letter:
                user_input = input('Таких букв у тебя нет, напиши заново ')
            return user_input


def record_score(user_input, user_name):
    """Подсчёт очков и запись результата очков"""
    if 0 < (len(user_input)) < 4:
        final_result[user_name] += len(user_input)
    else:
        final_result[user_name] += (len(user_input) + 2)
    return None


def change_letters(user_input, user_name_letters):
    """Убирает использованные буквы, добавляет нужное количество букв"""
    for i in user_input:
        if i in user_name_letters:
            user_name_letters.remove(i)
    #random_letters(user_name_letter, user_name, new_letters=1)
    new_letters = len(user_input) + 1 #Дописать количество букв начисляемых
    return new_letters


def player_order(user_input, user_name, user_name_letters, list_used_words, opened_file):

    correct_user_choice(user_input, user_name_letters)
    words_2 = words(user_input, list_used_words, opened_file)
    if not words_2:
        random_letters(user_name_letters, user_name, 1)
    else:
        change_letters_2 = change_letters(user_input, user_name_letters)
        random_letters(user_name_letters, user_name, change_letters_2)
        record_score(user_input, user_name)


def main():
    print('Привет. \nМы начинаем играть в Scrable\n')
    #user_name_1 = input('Как зовут перового игрока? ')
    #user_name_2 = input('Как зовут второго игрока? ')
    user_name_1 = '1'
    user_name_2 = '2'
    final_result[user_name_1] = 0
    final_result[user_name_2] = 0
    print(f'{user_name_1} vs {user_name_2} \n(раздаю случайные буквы)')
    random_letters(user_1_letters, user_name_1, 7)
    random_letters(user_2_letters, user_name_2, 7)
    with open('russian_word.txt', encoding='utf-8') as f:
        opened_file = f.read().splitlines()
    counter = 0
    flag = True
    while flag:
        counter += 1
        if counter % 2 == 0:
            user_input = input(f"Ходит {user_name_2}. Введи слово ")
            if not stop_game(user_input):
                break
            player_order(user_input, user_name_2, user_2_letters, list_used_words, opened_file)
        else:
            user_input = input(f"Ходит {user_name_1}. Введи слово ")
            if not stop_game(user_input):
                break
            player_order(user_input, user_name_1, user_1_letters, list_used_words, opened_file)


if __name__ == '__main__':
    main()
