import random

def generate_password():
    password = []
    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(65, 90)))

    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(97, 122)))

    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(48, 57)))

    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(33, 148)))

    return password

is_end = False
passwords = open("passwords.txt", "w")

while not is_end:
    website = input("Введите название сайта: ")
    login = input("Введите свой логин: ")

    new_password = generate_password()
    random.shuffle(new_password)

    passwords.write(str.join('\n', [website, login, str.join('', new_password)]))

    exit_check = input("Для завершения введите 'q'")
    is_end = exit_check == 'q'

passwords.close()