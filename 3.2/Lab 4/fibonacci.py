def fib_sequence(n):
    assert n > 0
    series = [1]

    while len(series) < n:
        if len(series) == 1:
            series.append(1)
        else:
            series.append(series[-1] + series[-2])

    for i in range(len(series)):
        series[i] = str(series[i])

    return ', '.join(series)

def fib_recurse(n):
    if n == 1: return 1
    elif n == 2: return 1
    else: return  fib_recurse(n - 1) + fib_recurse(n - 2)

print(fib_sequence(int(input('Сколько чисел? '))))
print(fib_recurse(int(input("Введите число: "))))