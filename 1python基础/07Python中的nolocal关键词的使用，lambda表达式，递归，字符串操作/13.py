'''
#使用指定的字符 将字符串切割成序列 split
#str1 = '在所有男人的眼中,店铺只有两类：一类是有凳子的,一类是没有凳子的'

str1 = '对待女朋友要一门心思，一心一意，一生一世，一人一狗！'

result = str1.split('一')

print(result)



str1 = '哭疼老叔昏压,小qiao流水任jia,鼓捣细feng手麻,吸yangxi下,断肠人在刷牙～'

result = str1.split(',')

print(result)
'''


#使用\n的字符 将字符串切割成序列splitlines

str1 = '哭疼老叔昏压\n小qiao流水任jia\n鼓捣细feng手麻\n吸yangxi下\n断肠人在刷牙～'


result = str1.splitlines()#等价于 result = str1.split('\n')

print(result)

#使用指定字符将序列连接成字符出啊 join

newstr = '★'.join(result)

print(newstr)
