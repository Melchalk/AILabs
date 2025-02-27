import random

list_of_words = ['яблоко', 'победа', 'программирование', 'терминал', 'ноутбук',
                 'валентинка', 'бутылка', 'тетрадь', 'работа', 'обучение']

random_word = list_of_words[random.randint(0, len(list_of_words) - 1)]
set_of_symbols = set(random_word)
discovered_symbols = set()
user_health = 5
computer_health = 5

def check_symbol(symbol, user_motion):
    global user_health, computer_health, discovered_symbols, set_of_symbols
    assert len(symbol) == 1

    if symbol in discovered_symbols:
        print('Вы уже вводили эту букву, попробуйте что-нибудь другое')
    elif symbol not in set_of_symbols:
        if user_motion:
            user_health -= 1
            health = user_health
        else:
            computer_health -= 1
            health = computer_health
        print('Этой буквы нет в слове. Текущее кол-во жизней: {}'.format(health))
    elif symbol in set_of_symbols:
        print('Буква есть в слове!')
        discovered_symbols.add(symbol)

print('_ ' * len(random_word))
is_user_motion = True

while discovered_symbols != set_of_symbols and (computer_health > 0 or user_health > 0):
    if is_user_motion and user_health > 0:
        user_symbol = input('> ')
        check_symbol(user_symbol, is_user_motion)

    elif computer_health > 0:
        computer_guess = chr(random.randint(ord('а'), ord('я')))
        print("Вариант компьютера:{}".format(computer_guess))
        check_symbol(computer_guess, is_user_motion)

    is_user_motion = is_user_motion == False
    current_word_progress = ''
    for ch in random_word:
        current_word_progress += '_ ' if ch not in discovered_symbols else ch + ' '

    print(current_word_progress)

if computer_health == 0 and user_health == 0:
    print('Жизни закончились :(')
else:
    if is_user_motion:
        print("Победил компьютер")
    else:
        print("Победил игрок")
    print('Поздравляю, вы правильно набрали слово {}'.format(random_word))