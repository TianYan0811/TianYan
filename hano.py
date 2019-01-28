## 汉诺塔问题

def hano(n, a, b, c):
	'''
	汉诺塔的递归实现
	n: 有几个盘子
	a: 代表第一个塔:起始塔
	b: 代表第二个塔:过渡塔
	c: 代表第三个塔:目标塔
	'''
	if n == 1:
		print(a, "->", c)
		return None

	if n == 2:
		print(a, "->", b)
		print(a, "->", c)
		print(b, "->", c)
		return None
	# 把个n-1盘子从a塔借助c塔挪到b塔
	hano(n-1, a, c, b)
	print(a, "->", c)
	# 把个n-1盘子从b塔借助a塔挪到c塔
	hano(n-1, b, a, c)

# 调用
a = "A"
b = "B"
c = "C"
n = 5
hano(n, a, b, c)
