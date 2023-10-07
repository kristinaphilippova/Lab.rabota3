#создание доски
def create_chessboard():
    chessboard = []
    for r in range(8):
        board_row = []
        for c in range(8):
            board_row.append("W" if (r + c) % 2 == 0 else "B")
        chessboard.append(board_row)
    return chessboard

#пооверка схожи ли цвета яцеек
def check_color(k, l, m, n):
    chessboard = create_chessboard()
    color1 = chessboard[k][l]
    color2 = chessboard[m][n]
    return color1 == color2

k, l = map(int, input("Введите координаты первой клетки через пробел (Строка, столбец): ").split())
m, n = map(int, input("Введите координаты второй клетки через пробел (Строка, столбец): ").split())

same_color = check_color(k, l, m, n)
print(f"Цвета клеток ({k}, {l}) и ({m}, {n}) {'одинаковые' if same_color else 'разные'}.")
