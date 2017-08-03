# -*- coding: utf-8 -*-
L = ['Bart', 'Lisa', 'Adam']
for name in L:
	print('hello,'+ name)

print('杨辉三角解释生成器generator')
def triangles():
	for n in range(1,11):
		LS = []
		for i in range(n):#0
			if i == 0 or i == n-1:
				LS.append(1)
			else:
				LS.append(LF[i-1]+LF[i])
		LF = LS
		yield LS
	return None
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
	