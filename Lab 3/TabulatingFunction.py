def get_cubic_root(x):
    return x ** (1 / 3)

def print_tabulating_function(a, b, n, func):
    print("x\ty")
    for i in range(a, b + 1, n):
        print(f"{i}\t{func(i)}")

a = int(input())
b = int(input())
c = int(input())
print_tabulating_function(a, b, c, get_cubic_root)