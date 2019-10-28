# Задание 4. Уровень - гросмейстер.
# Условие: Известно, что на доске 8×8 можно расставить 8 ферзей так, ч
# тобы они не били друг друга. Вам дана расстановка 8 ферзей на доске, определите, 
# есть ли среди них пара бьющих друг друга.

# Входные данные: программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.

# Выходные данные : eсли ферзи не бьют друг друга, выведите слово NO, иначе выведите YES.

# Пример:
# Ввод:                                        # Вывод:
# 1 7
# 2 4
# 4 8 
# 3 2
# 8 5
# 7 3
# 6 1 
# 5 6                                          NO
u = 8
count_beats = 0	
net = []
for i in range (u):
	(a, b) = input().split()
	(a, b) = (int(a), int(b))
	if (a, b) in net: 
		count_beats += 1
#	for bitpoint in net:
#		if bitpoint == (a, b):
#			count_beats += 1
	for j in range(1, u + 1):
		net.append( (a, j) )
		net.append( (j, b) )
		net.append( (a + j, b + j) )
		net.append( (a - j, b + j) )
		net.append( (a + j, b - j) )
		net.append( (a - j, b - j) )
	#print(net)
if count_beats != 0:
	print('YES')
else:
	print('NO')