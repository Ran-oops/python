#格式限定符号

#限制长度和对其方式

str1 = '{0:●^10}后面可以添加其他内容'

result = str1.format('吴升宇')

print(result)


#限制精度

str1 = '邢天宇拉屎一共拉了{0:.1f}斤'

result = str1.format(12.3823534)

print(result)


#进制转换

str1 = '邢天宇体重{0:d}斤'

result = str1.format(180)

print(result)

#金融数字间隔

str1 = '邢天宇一共具有{0:,}越南盾'

result = str1.format(12345678912)

print(result)
