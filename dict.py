
# 字典-dict

	# 字典是一种组合数据，没有顺序的组合数据，数据以键值对形式出现

	# 字典的特征
		# 字典是序列类型，但是是无序序列，所以没有分片和索引
		# 字典中的数据每个数据都由键值对组成，即kv对
			# key: 必须是可哈希的值，如 int,string,float,tuple, 但是，list,set,dict不行
			# value: 任何值

	# 字典的创建

d = {}			# 空字典
print(d)		# {}

d = dict()		# 空字典
print(d)		# {}

d = {"one": 1, "two": 2, "three": 3}
print(d)		# {'one': 1, 'two': 2, 'three': 3}

d = dict({"one": 1, "two": 2, "three": 3})
print(d)		# {'one': 1, 'two': 2, 'three': 3}

d = dict(one=1, two=2, three=3)  # 利用关键字参数
print(d)		# {'one': 1, 'two': 2, 'three': 3}

d = dict([("one", 1), ("two", 2), ("three", 3)])
print(d)		# {'one': 1, 'two': 2, 'three': 3}


	# 字典常见操作


# 访问数据 (注意下标是键值key)
d = {"one": 1, "two": 2, "three": 3}
print(d["one"]) # 1

d["one"] = "eins"
print(d)        # {'one': 'eins', 'two': 2, 'three': 3}

# 删除某键值对 ( 用 del )
del d['one']
print(d)		# {'two': 2, 'three': 3}

# 成员检测，in ， not in (检测的是key)
d = {'one': 1, 'two': 2, 'three': 3}
if 2 in d:
	print("val")
if 'two' in d:
	print('key')  # 输出 key
if ('two', 2) in d:
	print("kv")
			
		# 字典的遍历
		# 按 key 来使用for循环

d = {'one': 1, 'two': 2, 'three': 3}
for k in d:
	print(k, d[k])
	# one 1
	# two 2
	# three 3
# 以上可以改写为:
for k in d.keys():
	print(k, d[k])
	# one 1
	# two 2
	# three 3
# 只访问字典的值
for v in d.values():
	print(v)
	# 1
	# 2
	# 3
# 注意特殊用法的格式
for k, v in d.items():
	print(k, '--', v)
	# 'one' -- 1
	# 'two' -- 2
	# 'three' -- 3


	# 字典生成式


d = {'one': 1, 'two': 2, 'three': 3}
dd = {k: v for k, v in d.items()}
print(dd)			# {'one': 1, 'two': 2, 'three': 3}

dd = {k: v for k, v in d.items() if v % 2 == 0}
print(dd)			# {'two': 2}


	# 字典相关函数


d = {'one': 1, 'two': 2, 'three': 3}
# len,max,min,dict,clear

# str(字典): 返回字典的字符串格式
print(str(d))   	# {'one': 1, 'two': 2, 'three': 3}

# items: 返回字典的键值对组成的元组格式（可迭代）
print(d.items())	# dict_items([('one', 1),('two', 2),('three', 3)])

# keys : 返回字典的键组成的一个可迭代的结构
print(d.keys()) 	# dict_keys(['one','two','three'])

# values: 同理，返回一个可迭代的结构
print(d.values())	# dict_values([1,2,3])

# get: 根据指定键返回相应的值，好处是可以设置默认值（get默认值是None，可以设置）
print(d.get('Emm')) # None
print(d.get('one', 100)) # 1       # 找到键值'one'所以get返回'one'的v
print(d.get('Emm', 100)) # 100		# 找不到'Emm'所以get默认返回100

# fromkeys: 使用指定的序列作为键，使用一个值作为字典的所有的键的值
l = ['eins', 'zwei', 'drei']
d = dict.fromkeys(l, 'ha')
print(d)			# {'eins':'ha', 'zwei':'ha', 'drei':'ha'}