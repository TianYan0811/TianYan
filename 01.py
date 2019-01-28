"""
定义一个学生类，用来形容学生
"""
# 定义一个空类
class Student():
    pass

# 定义一个对象
ming = Student()

# 再定义一个类，用来描述一个听Python的学生
class PythonStudent():
    # 用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print("我在做作业")
        # 推荐在函数末尾使用return语句
        return None

# 实例化一个叫yue的学生，是一个具体的人
yue = PythonStudent()
print(yue.name)
print(yue.age)
# 注意成员函数的调用没有传参
yue.doHomework()
