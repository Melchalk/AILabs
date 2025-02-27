import random

def draw_small_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

def draw_board(board):
    print("-" * 21)
    for i in range(5):
        print("|", board[0 + i * 5], "|", board[1 + i * 5], "|", board[2 + i * 5], "|", board[3 + i * 5], "|", board[4 + i * 5], "|")
        print("-" * 21)

def take_input(player_token, board):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if 1 <= player_answer <= len(board):
            if str(board[player_answer - 1]) not in "XO":
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

def computer_move(player_token, board):
    valid = False
    while not valid:
        computer_answer = board[random.randint(0, len(board) - 1)]

        if str(board[computer_answer - 1]) not in "XO":
            print(f"Ход компьютера - {computer_answer}")
            board[computer_answer - 1] = player_token
            valid = True

def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return

def two_users_main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X", board)
        else:
            take_input("O", board)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)

def one_user_main(board):
    counter = 0
    win = False
    while not win:
        draw_small_board(board)
        if counter % 2 == 0:
            take_input("X", board)
        else:
            computer_move("O", board)
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_small_board(board)


print("*" * 10, " Игра Крестики-нолики ", "*" * 10)

mode = int(input("Выберите режим игры - один(1) или два игрока(2): "))

if mode == 1:
    user_board = list(range(1, 10))
    one_user_main(user_board)
elif mode == 2:
    user_board = list(range(1, 26))
    two_users_main(user_board)
else:
    print("Некорректный режим, попробуйте снова")

input("Нажмите Enter для выхода!")