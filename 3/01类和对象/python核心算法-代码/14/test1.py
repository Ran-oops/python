#object类  系统自带

#Human类   自定义
class Human:
    pass
#Woman类  自定义
class Woman(Human):
    pass


#获取人类对象
rl = Human()
#获取woman对象
nr = Woman()


#检测  rl 和 HUman  object的关系
# result = isinstance(rl,Human)
# print(result)
#
# result = isinstance(rl,object)
# print(result)


#检测nr和Woman，Human object的关系

# result = isinstance(nr,Woman)
# print(result)

result = isinstance(nr,Human)
print(result)
#
# result = isinstance(nr,object)
# print(result)