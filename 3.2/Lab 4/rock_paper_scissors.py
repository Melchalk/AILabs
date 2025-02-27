from random import randint

t = ["Камень", "Бумага", "Ножницы", "Колодец"]

computer = t[randint(0,3)]
player = False

while not player:
    player = input("Камень, Ножницы, Бумага, Колодец? > ")

    if player == computer:
        print("Ничья!")

    elif player == "Камень":
        if computer == "Бумага":
            print("Ты проиграл!", computer, "накрывает", player)
        elif computer == "Колодец":
            print("Ты проиграл!", player, "тонет в", computer)
        else:
            print("Ты выиграл!", player, "разбивает", computer)

    elif player == "Бумага":
        if computer == "Ножницы":
            print("Ты проиграл!", computer, "режет", player)
        else:
            print("Ты победил!", player, "накрывает", computer)

    elif player == "Ножницы":
        if computer == "Камень":
            print("Ты проиграл!", computer, "разбивает", player)
        elif computer == "Колодец":
            print("Ты проиграл!", player, "тонет в", computer)
        else:
            print("Ты выиграл!", player, "режет", computer)

    elif player == "Колодец":
        if computer == "Бумага":
            print("Ты проиграл!", computer, "накрывает", player)
        else:
            print("Ты выиграл!", computer, "тонет в", player)

    else:
        print("Некорректный ход!")

    player = False

    computer = t[randint(0,3)]