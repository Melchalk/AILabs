import random

random_number = random.randint(1, 100)

user_guess = 0
computer_guess = random.randint(1, 100)
computer_max = 101
computer_min = 0

def check_number(guess, computer_motion):
    global computer_min, computer_max
    if random_number > guess:
        if computer_motion and guess > computer_min:
            computer_min = guess
        print('Больше, чем {}!'.format(guess))
    elif random_number < guess:
        if computer_motion and guess < computer_max:
            computer_max = guess
        print('Меньше, чем {}!'.format(guess))
    else:
        print('Верно! Я загадал число {}'.format(random_number))

print('Я загадал число от 1 до 100, попробуй его угадать!')

user_motion = True

while user_guess != random_number and computer_guess != random_number:
    is_computer_motion = user_motion == False
    if user_motion:
        user_guess = int(input('> '))
        check_number(user_guess, is_computer_motion)
    else:
        computer_guess = (computer_max + computer_min) // 2
        check_number(computer_guess, is_computer_motion)
    user_motion = is_computer_motion