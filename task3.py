# Задача 3. Уровень - шахматный мачо.
# Условие: в шахматах конь ходит буквой Г. В школе BPS есть особый конь на шахматной доске: он тоже ходит буквой Г,
# только по горизонтали он может пройти 2 клетки, а по вертикали 5, или наоборот. Даны две различные клетки шахматной доски.
# Требуется определить,
# возможно ли конем из школы BPS перейти из одной клетки шахматной доски в другую.

# Входные данные : 4 целых числа (все > 0). В первой строке вводится номер столбца 1 клетки. На второй строке - номер
# строки первой клетки. Потом аналогично на третьей и четвертой строках вводится информацию о 2 клетке.

# Выходные данные: "YESSSS!" если такой ход возможен, "No no" - если такой ход невозможен.

# Пример:
# Ввод:                                              # Вывод:
# 1
# 1
# 4
# 3                                                  No no


# 3
# 6
# 1
# 1                                                  YESSSS!

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a - c) == 2 and abs(b - d) == 5 or abs(b - d) == 2 and abs(a - c) == 5:
	print('YESSSS!')
else:
	print('No no')