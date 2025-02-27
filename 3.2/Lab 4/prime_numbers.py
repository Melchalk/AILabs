def is_prime(x):
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False

    return True

def gen_prime(number):
    bigger_prime = number
    smaller_prime = number

    while not is_prime(bigger_prime) and not is_prime(smaller_prime):
        bigger_prime += 1
        smaller_prime -= 1

    if is_prime(bigger_prime):
        return bigger_prime

    return smaller_prime

while True:
    answer = input('Показать следующее простое число? (Y/N) ')
    if answer.lower().startswith('y'):
        user_number = int(input("Введите свое число: "))

        if is_prime(user_number):
            print("Это число простое")
        else:
            print("Это число не простое. Вот ближайшее простое число: ")
            print(gen_prime(user_number))
    else:
        break
