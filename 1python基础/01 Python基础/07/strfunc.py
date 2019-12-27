'''
#capitalize()  对于整个字符串的首字母大写

stren = 'if I lose myself'


result = stren.capitalize()

print(result)


#title()  每个单词的首字母的大写

stren = 'if I lose myself'

result = stren.title()

print(result)


#upper() 所有字母变为大写

stren = 'if I lose myself'

result = stren.upper()
print(result)



#lower() 将所有字母变为小写
stren = 'IF YOU FEEL MY LOVE'

result = stren.lower()
print(result)


#swapcase() 大小写转化
stren = 'if YOU feel MY love'
result = stren.swapcase()

print(result)


#len() 计算长度

str1 = '乙肝患者都是幸福的人！'
result = len(str1)

print(result)

#count() 计算某个字符串出现的次数
str1 = '胃病，肠道疾病，肝病消化内科，胃病是很不好治需要长期休养的病，我因为胃病3年没吃冰棍！'

result = str1.count('胃病',20,36)
print(result)


#find() 查找指定字符串第一次出现的位置
str1 = '美女，你会喷水吗？，我会喷火，还有5个兄弟等我们去救爷爷！'

result = str1.find('喷火',2,10)
print(result)


#index() 查找指定字符串第一次出现的位置

str1 = '美女，你会喷水吗？，我会喷火，还有5个兄弟等我们去救爷爷！'

result = str1.index('喷火',2,16)
print(result)



#startswith()
url = 'http://www.itxdl.cn/python/index.php'

result = url.startswith('https')

print(result)

#endswith()

url = 'http://www.itxdl.cn/python/index.php'

result = url.endswith('php')

print(result)



#islower & isupper() 检测大小写

stren = 'you hurt my heart deeply 吊！!'

resultlower = stren.islower()
print(resultlower)

resultupper = stren.isupper()
print(resultupper)


#isalnum()  & isalpha() & isdigit()  检测字符串组成

str1 = '12357568'

#result = str1.isalnum()

#result = str1.isalpha()

result = str1.isdigit()

print(result)


#isspace() 检测是否由空白字符组成
str1 = '''


            


'''

str1 = '           \r\n'
result = str1.isspace()

print(result)


#istitle()检测是否符合标题要求
stren = 'Buy Ew Bu Buy Ns'

result = stren.istitle()
print(result)


#isnumeric() 检测是否是数值字符串 效果和isdigit一致

str1 = '123454575690'
result = str1.isnumeric()
print(result)

#isdecimal() 检测是否是数值字符串

str1 = '123454575690.5'
result = str1.isdecimal()
print(result)



#split() 使用指定字符切割字符串

strshi = '离离原上草★一岁一枯荣★野火烧不尽★春风吹又生！'

result = strshi.split('★')

print(result)


#splitlines() 将字符串在回车换行出进行切割返回切割个之后的每部分字符串组成的列表
strshi = """关关雎鸠
在河之洲
窈窕淑女
君子好逑
"""

result =strshi.splitlines()

print(result)



#join() 使用指定字符串 将列表数据拼接
list1 = ['鹅鹅鹅','曲项向天歌','白毛浮绿水','红掌拨清波']

result = '◆'.join(list1)

print(result)

#zfill() 在原有字符串长度不足指定长度时，用0填充

str1 = 'bitch'

result = str1.zfill(15)

print(result)


#center()指定字符串长度，并且使得元字符串内容居中，其余位置使用指定字符填充

#ljust()
#rjust()
str1 = 'bitch'

#result = str1.center(15,'0')
#result = str1.ljust(15,'A')
result = str1.rjust(15,'B')
print(result)



#strip() 去掉左右2侧的指定字符，默认空格
#lstrip() 去掉左侧的指定字符，默认空格
#rstrip() 去掉右侧的指定字符，默认空格

str1 = 'AAAAAAbitchBBBBB'

#result = str1.strip('A')
#result = str1.lstrip('A')
result = str1.rstrip('A')

print(result)

'''

#字符串替换操作

str1 = '蜡笔小新的爸爸叫野原广志,蜡笔小新的妈妈是野原美伢,蜡笔小新的爷爷是野原银之介'

#maketrans()建立字符串映射表

table = ''.maketrans('小是','大叫')

print(table)

#translate() 替换操作

result = str1.translate(table)
print(result)
