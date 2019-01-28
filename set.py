
## 集合-set
	
	# 集合是高中数学的概念
	# 集合元素是：确定的、无序的、唯一的

	# 集合的定义
		s = set()
		s = {1,2,3,4,5}     # 这种定义大括号内一定要有值，否则定义出来的是一个dict类型

	# 集合的特征

		# 集合的数据是无序的，即无法使用 索引 和 分片
		# 集合内部数据元素具有唯一性，集合可以用来排除重复数据
		# 集合内的数据，只能放置 可哈希数据（如：str,int,float,tuple,冰冻集合等）

	# 集合的序列操作

		# 成员检测（ in, not in ）
		s = {4,5,"i","Y","sos"}
		print(s)
		if "i" in s:
			print("Yes")    # Yes
		if "Ha" not in s:
			print("emm")	# emm

	# 集合的遍历

		# for 循环遍历
		s = {4,5,"i","love","wangxiaojing"}
		for i in s:
			print(i, end=" ")   # i 4 5 wangxiaojing love

		# 带有元组的集合遍历
		s = {(1,2,3), ('i','a','bb'), (4,5,6)}
		for k,m,m in s:
			print(k, "--", m, "--", n)
		# 4 -- 5 -- 6
		# i -- a -- bb
		# 1 -- 2 -- 3 
		for k in s:
			print(k)
		# (4, 5, 6)
		# ('i', 'a', 'bb')
		# (1, 2, 3)

	# 集合的内涵

		# 普通集合内涵
		s = {1,1,1,2,2,4}	# 集合在初始化后自动过滤掉重复元素
		print(s)  			# {2,1,4}
		ss = {i for i in s}
		print(ss) 			# {4,2,1}

		# 带条件的集合内涵
		sss = {i for i in s if i % 2 == 0}
		print(sss) 			# {2,4}

		# 多层循环的集合内涵
		s1 = {1,2,3,4}
		s2 = {"i","love","wa"}
		s = {m*n for m in s2 for n in s1}
		print(s)
		# {'iii','i','lovelovelove','ii','wa',....}
		s = {m*n for m in s2 for n in s1 if n == 2}
		print(s)
		# {'ii','lovelove','wawa'}

	# 集合函数/关于集合的函数

		# len,max,min:参考之前的函数
		s = {1,2,43,56,1122,40,2,1}
		print(len(s))		# 6
		print(max(s))		# 1122
		print(min(s))		# 1

		# add: 向集合内添加元素
		s = {1}
		s.add(334)
		print(s)  			# {1,334}

		# clear: 清空集合（在原地址）
		s = {1,2,3,4,5}
		s.clear()
		print(s)   			# {}  ( set() ???) 

		# copy:    拷贝
		# remove:  删除指定的值，若指定值不存在，则报错
		# discard: 删除指定的值，若指定值不存在，不报错 
		s = {2,3,4,1,666}
		s.remove(4)			# 
		print(s)			# {1,2,3,666}
		s.discard(1)		# 
		print(s)			# {2,3,666}
		s.discard(111)		# 不报错
		print(s)			# {2,3,666}
		s.remove(222)		# 报错
		print(s)			# 

		# pop: 随机移除一个元素
		s = {1,2,3}
		d = s.pop()
		print(d)			# 1 
		print(s)			# {2,3}

		# 集合函数
		# intersection: 交集
		# difference: 差集
		# union: 并集
		# issubset: 检查一个集合是否是另一个的子集
		# issuperset: 检查一个集合是否是另一个的超集
		s1 = {1,2,3,4,5,6}
		s2 = {5,6,7,8,9}
		s_1 = s1.intersection(s2)
		print(s_1)  		# {5,6}
		s_2 = s1.difference(s2)
		print(s_2)			# {1,2,3,4}
		s_3 = s1.issubset(s2)
		print(s_3)			# False

		# 集合的数学操作
		s_4 = s1 - s2
		print(s_4)			# {1,2,3,4}
		# 不支持 s1 + s2  （？？？）

	# 冰冻集合-frozenset

		# frozenset是一种特殊的集合
		# 不允许进行任何修改的集合
		s = frozenset()
		print(type(s))  	# <class 'frozenset'>
		print(s) 			# frozenset()