#字典函数

dict1 = {'noodles':'面条','dumpling':'饺子','humberger':'汉堡','chicken':'炸鸡'}

#clear() 清空字典

dict1.clear()

print(dict1)

#copy 复制字典

dict1 = {'noodles':'面条','dumpling':'饺子','humberger':'汉堡','chicken':'炸鸡'}

dict2 = dict1.copy()

print(dict2)

#fromkeys  使用一个序列和固定的值组成字典

lists = ['手机','充电器','充电线','充电宝']

result = {}.fromkeys(lists,'手机配件')

print(result)

#get() 获取字典的值
dict1 = {'noodles':'面条','dumpling':'饺子','humberger':'汉堡','chicken':'炸鸡'}

#通过键获取值
print(dict1['dumpling'])

#get获取值
result = dict1.get('dumpling')
print(result)

#不存在的键
#print(dict1['momo'])

result = dict1.get('momo','旺仔小馒头')
print(result)


#items() 获取键值组成的二级列表

dict1 = {'noodles':'面条','dumpling':'饺子','humberger':'汉堡','chicken':'炸鸡'}

result = dict1.items()

print(result)

#keys 获取所有键组成的列表

result = dict1.keys()

print(result)


#values获取所有值组成的列表

result = dict1.values()

print(result)

#pop 移除字典中指定的元素
dict1 = {'noodles':'面条','dumpling':'饺子','humberger':'汉堡','chicken':'炸鸡'}

#删除已存在的键
#result = dict1.pop('humberger')
#print(dict1)
#print(result)

#删除不存在的键

result = dict1.pop('momo','对不起，没有该键')
print(dict1)
print(result)

#popitem() 移除字典的中的键值对
dict1 = {'noodles':'面条','dumpling':'饺子','humberger':'汉堡','chicken':'炸鸡'}

dict1.popitem()
dict1.popitem()
dict1.popitem()

print(dict1)

#setdefault（） 添加字典的值

dict1 = {'noodles':'面条','dumpling':'饺子','humberger':'汉堡','chicken':'炸鸡'}

#值操作
#dict1['flower'] = '强爆鸡米花'
#print(dict1)

#函数操作
dict1.setdefault('leg','鸡腿')
print(dict1)

#update() 更新字典的值
dict1 = {'noodles':'面条','dumpling':'饺子','humberger':'汉堡','chicken':'炸鸡'}

#更新/设置操作
#dict1['humberger'] = '肉夹馍'
#print(dict1)

#函数操作
#dict1.update(humberger= '白吉馍')
#print(dict1)


dict1.update({'humberger': '白吉馍','dumpling':'包子'})
print(dict1)



