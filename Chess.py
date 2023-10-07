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

#Попадют ли фигуры на поле (m, n) за один ход
def rook_threat(k, l, m, n):
    return k == m or l == n

def bishop_threat(k, l, m, n):
    return abs(k - m) == abs(l - n)

def queen_threat(k, l, m, n):
    return rook_threat(k, l, m, n) or bishop_threat(k, l, m, n)

def knight_threat(k, l, m, n):
    knight_moves = [
        (k + 1, l + 2), (k + 2, l + 1), (k + 2, l - 1), (k + 1, l - 2),
        (k - 1, l - 2), (k - 2, l - 1), (k - 2, l + 1), (k - 1, l + 2)
    ]
    return (m, n) in knight_moves
#Проверяем клетки на угрозы
def check_threat(piece, k, l, m, n):
    if piece == "queen":
        return queen_threat(k, l, m, n)
    elif piece == "rook":
        return rook_threat(k, l, m, n)
    elif piece == "bishop":
        return bishop_threat(k, l, m, n)
    elif piece == "knight":
        return knight_threat(k, l, m, n)
    else:
        return False
        
k, l = map(int, input("Введите координаты первой клетки через пробел (Строка, столбец): ").split())
m, n = map(int, input("Введите координаты второй клетки через пробел (Строка, столбец): ").split())

same_color = check_color(k, l, m, n)
print(f"Цвета клеток ({k}, {l}) и ({m}, {n}) {'одинаковые' if same_color else 'разные'}.")

piece = input("Введите название фигуры (ферзь, ладья, слон или конь): ")

rook = rook_threat(k, l, m, n)
bishop = bishop_threat(k, l, m, n)
queen = queen_threat(k, l, m, n)
knight = knight_threat(k, l, m, n)


if rook:
    print("Переход возможен за один ход ладьи, следовательно есть угроза.")
elif bishop:
    print("Переход возможен за один ход слона, следовательно есть угроза.")
elif queen:
    print("Переход возможен за один ход ферзя, следовательно есть угроза.")
elif knight:
    print("Переход возможен за один ход коня, следовательно есть угроза.")
else:
    print("Переход невозможен за один ход.")
