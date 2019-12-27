#检测字符串是否以指定的内容结尾  endswith

str1 = '锄禾日当午，地雷买下土，老师走过去，炸成二百五'

result = str1.endswith('二百五')

print(result)


#检测字符串是否以指定的内容开头 startswith

result = str1.startswith('锄禾')

print(result)


#检测字符串是否都是大写字母 isupper

str1 = 'YOU HURT MY HEART DEEPLY!'

result = str1.isupper()

print(result)

#检测字符串是否都是小写字母 islower

str1 = 'you hurt my heart deeply！你深深的伤害了我！'

result = str1.islower()

print(result)


#检测是否是由数字字符，英文字母与和文字组成 isalnum

str1 = '0123456789中文ANCDEFGH'

result = str1.isalnum()

print(result)


#检测字符串是否由字母和文字组成  isalpha

str1 = 'AFRGDFHDGH汉字中文'

result = str1.isalpha()

print(result)


#检测字符串是否由10进制数字组成 isdigit

str1 = '00001234567890'

result = str1.isdigit()

print(result)


#检测字符是否由空白字符组成 isspace

str1 = '\t\n\r '

result = str1.isspace()

print(result)


#检测字符串是否符合title()操作之后的结果 istitle()

str1 = 'You Can You Up No Can No Bibi'

result = str1.istitle()

print(result)

#检测字符串是否是数值字符串（纯整型）isnumeric  和isdigit相似

str1 = '1235'

result = str1.isnumeric()

print(result)


#检测字符串是否是纯数值字符串组成isdecimal

str1 = '12352354580022'

result = str1.isdecimal()

print(result)


