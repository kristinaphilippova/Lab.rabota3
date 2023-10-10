#создание доски
def create_chessboard():
    chessboard = []
    for r in range(9):
        board_row = []
        for c in range(9):
            board_row.append("W" if (r + c) % 2 == 0 else "B")
        chessboard.append(board_row)
    return chessboard

#пооверка схожи ли цвета яцеек
def check_color(k, l, m, n):
    chessboard = create_chessboard()
    color1 = chessboard[k][l]
    color2 = chessboard[m][n]
    return color1 == color2

#Попадет ли конь на поле (m, n) за один ход
def knight_threat(k, l, m, n):
    knight_moves = [
        (k + 1, l + 2), (k + 2, l + 1), (k + 2, l - 1), (k + 1, l - 2),
        (k - 1, l - 2), (k - 2, l - 1), (k - 2, l + 1), (k - 1, l + 2)
    ]
    return (m, n) in knight_moves
#Проверяем клетки на угрозы коня
def check_threat(piece, k, l, m, n):
    elif piece == "knight":
        return knight_threat(k, l, m, n)
    else:
        return False
#Смотрим ходы ладьи, ферзя и слона
def is_valid_move(piece, k, l, m, n):
    if piece == 'ладья':
        if k == m or l == n:
            return True
    elif piece == 'ферзь':
        if k == m or l == n or abs(k - m) == abs(l - n):
            return True
    elif piece == 'слон':
        if abs(m - k) == abs(n - l):
            return True
    return False    
#основной код
k, l = map(int, input("Введите координаты первой клетки через пробел (Строка, столбец): ").split())
m, n = map(int, input("Введите координаты второй клетки через пробел (Строка, столбец): ").split())
#Проверка цвета через вызов функции check_color
same_color = check_color(k, l, m, n)
print(f"Цвета клеток ({k}, {l}) и ({m}, {n}) {'одинаковые' if same_color else 'разные'}.")

piece = input("Введите название фигуры (ферзь, ладья, слон или конь): ")

knight = knight_threat(k, l, m, n)
#Определяем промежуточное поле для ладьи, ферзя и слона
if piece == "слон" or piece == "ферзь" or piece == "ладья":
    if is_valid_move(piece, k, l, m, n):
        print("Можно сделать один ход до конечной позиции")
    else:
        for i in range(8):
            for j in range(8):
                if (is_valid_move(piece, k, l, i, j) and
                    is_valid_move(piece, i, j, m, n)):
                    print(f"В два хода выбранная фигура может попасть через клетку ({i}, {j})")
                    exit(0)
        print("Невозможно сделать двух ходов до конечной позиции")
elif knight:
    print("Переход возможен за один ход коня, следовательно есть угроза.")
else:
    print("Переход невозможен за один ход.")
