
## 列表

	# 创建列表
		l = []  		# 创建空列表
		l = [100] 		# 包含一个元素的列表
		l = [2,1,3] 	# 包含多个元素的列表
		l = list(2,1,3) # 同上

	# 下标访问
		# 列表有顺序之分：类似数组 l[2] 为第三个元素的值
		# 下标从零开始

	# 分片操作
		# 截取范围（含左下标，不含右下标）：左闭右开
		l = [2,1,3,6,4,5]
		print(l[1:4])   # [1,3,6]
		print(l[:])	 	# [2,1,3,6,4,5]
		print(l[:4])	# [2,1,3,6]
		print(l[2:])    # [3,6,4,5]

		# 分片操作可以控制增长幅度，默认为1
		print(l[1:5:1]) # [1,3,6,4] 
		print(l[1:5:2]) # [1,6]

		# 下标可以超出范围，超出后不再考虑多余下标内容
		print(l[1:10])  # [2,1,3,6,4,5]

		# 下标值、增长幅度可以为负数
		# 为负，则顺序是从右到左
		# 规定：数组最后一个元素下标为-1
		# 默认分片操作总是从左到右截取

		# 正常情况，分片操作左边的值一定小于右边的值
		print(l[-2:-4]) # []
		print(l[-4:-2]) # [3,6]

		# 若分片时需要左边大于右边，则增长幅度需要用负数
		print(l[-2:-4:-1]) # [4,6]
		# 可以为list正反颠倒提供思路

		# 分片操作是生成一个新的list
		# 可以调用内置函数id()查看变量的编号来确定内存地址
		a = 100
		c = a
		print(id(a)) 	 # 93941189949760 
		print(id(c)) 	 # 93941189949760
		             	 # 表明c和a同一块内存地址
		a = 101		 	 # 更改a的值
		print(a)	 	 # 101
		print(c)	 	 # 100
					 	 # 但 c 的值没变
		L1 = [1,2,3,4,5] # 
		L2 = L1[:]		 # 新的内存(L1的值改变L2不受影响)
		L3 = L1			 # 和L1同一内存(L1的值改变L3的值也改变)


	# 列表相加

		# 用加号链接两个列表
		a = [1,2,3,4,5]
		b = [5,6,7,8,9]
		c = ['a', 'b', 'c']
		d = a + b + c
		print(d)         # [1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 'a', 'b', 'c']


	# 列表乘号操作

		# 列表乘一个数n等于n个相同列表相加
		a = [1,2,3]
		b = a * 3
		print(b)         # [1, 2, 3, 1, 2, 3, 1, 2, 3] 


	# 成员资格运算

		# 判断一个元素是否在list里面
		a = [1,2,3,4,5]
		b = 8
		c = b in a     	  # c是一个布尔值True/False
		print(c)       	  # False
		b = 4
		print(b in a)  	  # True
		print(b not in a) # False


	# list的遍历

		a = [1,2,3,4,5]
		for i in a:
			print(i)

		b = ["I am a student."]
		for i in b:
			print(i)

		# 一般不用while遍历list，可以但麻烦，比如：
		length = len(a)
		indx = 0
		while indx < length:
			print(a[indx])
			indx += 1


	# 嵌套列表（双层列表）循环遍历

		# k,v,w的个数应该跟解包出来的变量个数一致
		a = [["one", 1], ["two", 2], ["thr", 3] ]
		for k,v in a:
			print(k, "--", v)
			# one -- 1
			# two -- 2
			# thr -- 3

		b = [["one", 1, "A"], ["two", 2, "B"], ["thr", 3, "C"] ]
		for k,v,w in b
			print(k, "--", v, "--", w)
			# one -- 1 -- A
			# two -- 2 -- B
			# thr -- 3 -- C


	# 列表内涵：list content

		# 通过简单方法创作列表
		a = ['a','b','c']
		# 对于所有a中的元素，逐个放入新列表b中
		b = [i for i in a]
		print(b)   		# ['a','b','c']

		# 所有 a 中元素乘10，放入新列表中
		a = [1,2,3,4,5]
		b = [i*10 for i in a]
		print(b)   		# [10,20,30,40,50]

		# 可以过滤原来列表的内容放入新列表中
		a = [x for x in range(1,35)]       # 生成一个从1到34的一个列表a:[1,2,3,4,...,34]
		b = [m for m in a if m % 2 == 0]   # a中所有偶数生成一个新列表b:[2,4,6,8,...,34]

		# 列表生成是可以嵌套的
		a = [i for i in range(1,4)]
		print(a)   		# [1,2,3]
		b = [i for i in range(100,400) if i % 100 == 0]
		print(b)   		# [100,200,300]
		c = [ m+n for m in a for n in b]
		print(c)   		# [101,201,301,102,202,302,103,203,303]
		d = [m+n for m in a for n in b if m+n < 250]
		print(d)   		# [101,201,202,103,203]

		# 列表c类似于下面的两层嵌套
		for m in a;
			for n in b:
				print(m+n,end=" ")
		print()


	# 列表什么都可以装，同一列表可以有不同的类型
		l = ["xx", 123, 4+5j, "sdfas", 'y', 233]


	# 关于列表的常用函数

		# len:求列表长度
		a = [x for x in range(1,100)]
		print(len(a))   # 99

		# max:求列表中的最大值 
		# min:求列表中的最小值
		print(max(a))   # 99
		print(min(a))   # 1
		b = ['man','film','python']
		print(max(b))   # python

		# list:将其他格式的数据转换为list (可迭代的数据才可以转换)
		s = "I am a student."
		print(list(s))  # ['I',' ','a','m',' ','a',' ','s','t','u','d','e','n','t','.']
		print(list(range(12,18))) # [12,13,14,15,16,17]

		# append:插入一个内容，在末尾追加
		a = [i for i in range(1,5)]
		print(a)      	# [1,2,3,4]
		a.append(100)
		print(a)      	# [1,2,3,4,100]

		# insert:指定位置插入，插在index前面  
		# 用法：insert(index,data)
		print(a)      	# [1,2,3,4,100]
		a.insert(3,666)
		print(a)      	# [1,2,3,666,4,100]

		# 删除 （ del / pop / remove ）

		# del: 删除元素，在原地址上删除
		a = [1,2,3,4,5,6]
		del a[2]
		print(a)        # [1,2,4,5,6]
		a = [1,2,3,4,5,6]
		print(id(a))    # id
		del a[2]	    # del一个元素是在原来的地址删除，而不是生成新的list
		print(id(a))    # id 地址不变
		print(a)	    # [1,2,4,5,6]
		del a           # del一个变量后不能继续使用该变量
		print(a)   	    # ！！！此时会报错，因为变量a已经被删除了

		# pop: 从最后一位拿出一个元素
		a = [1,2,3,666,4,100]
		print(a)        # [1,2,3,666,4,100] 
		last_ele = a.pop()
		print(last_ele) # 100
		print(a)        # [1,2,3,666,4]

		# remove: 删除列表中指定的元素(列表内必须要有这个指定的值),在原地址上进行删除
		print(a)        # [1,2,3,666,4]
		print(id(a))    # id
		a.remove(666)	# 应该提前判断有没有666这个元素
		print(a)		# [1,2,3,4]
		print(id(a))    # id 地址不变

		# 使用remove前应该用 try...excepty语句，或先行判断
		# if x in list:
		#	list.remove(x)

		# clear: 清空列表,在原地址操作
		print(a) 		# [1,2,3,4]
		print(id(a))	# id
		a.clear()
		print(a)		# []
		print(id(a))	# id 地址不变

		# 若不需要列表地址不变，则清空列表可以用以下方式：
		# a = []
		# a = list()

		# reverse: 翻转列表内容,在原地址上进行翻转
		a = [1,2,3,4,5]
		print(a)		# [1,2,3,4,5]
		print(id(a))	# id
		a.reverse()		
		print(a)		# [5,4,3,2,1]
		print(id(a))	# id 地址不变

		# extend: 扩展列表，需要俩列表，把列表b直接拼接到列表a后面
		a = [1,2,3]
		b = [4,5,6]
		print(a)        # [1,2,3]
		print(id(a))
		a.extend(b)
		print(a)        # [1,2,3,4,5,6] 
		print(id(a))    # 地址不变

		# count: 查找列表中某元素的个数
		a = [1,8,2,8,1,3,4,8]
		num_eig = a.count(8)
		print(num_eig)  # 3

		# copy: 拷贝,浅拷贝
		# 使用简单赋值是同一地址
		a = [1,2,3,4]	 
		# b = a         # 对list简单赋值就是传地址
		# b[2] = 666	# 也会对a的内容进行修改
		# print(a)    	# [1,2,666,4]
		# print(b)		# [1,2,666,4]

		# 若需要不同的地址则需要拷贝函数
		b = a.copy()    # 此时a与b为不同的地址

		# 深拷贝 与 浅拷贝 区别
		a = [1,2,3,[10,20,30]]
		b = a.copy()    # 浅拷贝，不拷贝第二层，第二层用原地址
		print(id(a[3])) # id
		print(id(b[3])) # b[3]和a[3]是同一个地址
		a[3][2] = 666	# a[3]修改了
		print(b[3])     # [10,20,666]  说明b[3]也被修改了