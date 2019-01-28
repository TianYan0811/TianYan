## 变量作用域
	# global 全局变量
	# local  局部变量
	# 可以用 global 将局部提升为全局


	## 关键字参数:

# 语法：
def func(p1= 'v1', p2='v2', p3='v3'):
	pass
	# func_body
# 调用：
value1 = '1'
value2 = '2'
value3 = '3'
func(p1=value1, p2=value2, p3=value3)
# 调用时参数可以调换位置、可以省略某些参数

# 案例如下
def func(name="Yqz", age=0, addr="family"):
	print("名字:{0}, 年龄:{1},地址:{2}".format(name,age,addr))
# 调用：
n = "Xv"
ag = 13
ad = "HeHe"
func(name=n, addr=ad, age=ag)


	## 收集参数


# 语法：
def func( *args):
	pass
	# func_body
# 调用：
v1 = '1'
v2 = 2
v3 = 'xxx'
func(v1, v2, v3, ...)
# 调用时可以不带参数，此时args为空'tuple'

# 案例如下
def stu( *args):
	print(type(args))
	for item in args:
		print(item)
# 调用
stu(1,2,"xxYYzz",45,"gaa")
# 调用时可以容纳各种参数


	## 关键字收集参数

# 语法：
def func( ** kwargs):
	pass
	# func_body
# 调用：
func(p1=v1, p2=v2, p3=v3)
# 访问kwargs时用字典格式访问( key + value )

# 案例如下
def stu1( **kwargs):
	print(type(kwargs))
	for k,v in kwargs.items():
		print(k, "---", v)
# 调用
stu1(name="Yqz", age=19, addr="Family")
print("*" * 30)
stu1(name="hehe")


	## 参数混合使用的案例


# 顺序：普通参数->收集参数->关键字参数->关键字收集参数
def func(name, age, *args, hobby="xx", **kwargs):
		print(name)
		print(age)
		print(hobby)
		for i in args:
			print(i)
		for item in kwargs.items():
			print(item)


## 收集参数的解包问题

# 对list类型收集参数解包
def fun( *args):
	pass
	# func_body
# 调用：
li = [345, "hahah", "fca"]
fun(*li)

# 对dict类型收集参数解包
def fu( **kwargs):
	pass
	# func_body
# 调用：
v1 = '1'
v2 = '2'
v3 = 'xxx'
# dic = {k1=v1, k2=v2, k3=v3}
# fu(**dic)


## 函数文档
	# 作用是对当前函数提供相关参考信息
	# 文档写法：
		# 在函数内部开始的第一行使用三引号字符串定义符
		# 一般居具有特定格式（文字说明、参数、返回值）
	# 文档查看
		# 使用help()函数，如help(funvc)
		# 使用__doc__, 如func.__doc__

# 案例如下
def f(name, age, *args):
	"""
	这是文档的文字内容
	:param name: 表示学生的名字
	:param age: 表示学生的年龄
	:return: 此函数没有返回值
	"""
	print("This is the func.")


	## 函数传值传址的区别

def fun1(n_t):
	n_t[2] = 300
	print(n_t)
	return None

def fun2(n_t):
	n_t += 100
	print(n_t)
	return None

# 复杂变量：传地址（函数内外是同一份）list/set/dict/tuple...
an = [1, 2, 3, 4, 5, 6]
fun1(an)	# [1,2,300,4,5,6]
print(an) 	# [1,2,300,4,5,6]
# 简单变量：传值（复印一份、函数内外不同）
bn = 9
fun2(bn)	# 109
print(bn) 	# 9