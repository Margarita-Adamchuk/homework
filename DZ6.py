# игра крестики нолики

board = list(range(1, 10))
def draw_board(board):
    print("--+---+---")
    for i in range(3):
        print(f"{board[0+i*3]} | {board[1+i*3]} | {board[2+i*3]}")
        print("--+---+---")

def play(XO):
    correct = False
    while not correct:
        answer = input("Какой ваш следующий ход?")
        try:
            answer = int(answer)
        except ValueError:
            print("Некоректный ввод. Вы уверены что ввели число?")
            continue
        if 9 >= answer >= 1:
            if str(board[answer-1]) not in "XO":
                board[answer-1] = XO
                correct = True
            else:
                print("Ячейка занята!!!!")
                continue
        else:
            print("Некоректный ввод. Нужно вводить числа от 1 до 9")

def chek_win(board):
    win_cod = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for item in win_cod:
        if board[item[0]] == board[item[1]] == board[item[2]]:
            return board[item[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter %2 == 0:
            play("X")
        else:
            play("O")
        counter += 1
        if counter > 4:
            chek = chek_win(board)
            if chek:
                print(f"{chek} WIN!!!")
                win = True
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)

main(board)


