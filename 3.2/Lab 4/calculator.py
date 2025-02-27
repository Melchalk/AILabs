def calc(a, b, op):
    if op not in '+-/*^%√':
        return 'Пожалуйста, выберите тип операции: "+, -, *, /, ^, %, √"!'

    result = ''
    match op:
        case '+': result = str(a + b)
        case '-': result = str(a - b)
        case '*': result = str(a * b)
        case '/': result = str(a / b)
        case '^': result = str(a**b)
        case '%': result = str(a%b)
        case '√': result = str(a**(1/b))

    return f"{str(x)} {op} {str(y)} = {result}"

x = int(input('Пожалуйста, введите первое число: '))
y = int(input('Пожалуйста, введите второе число: '))

user_op = input('Какой вид операции Вы желаете осуществить?\nВыберите между "+, -, *, /, ^, %, √" : ')

print(calc(x, y, user_op))