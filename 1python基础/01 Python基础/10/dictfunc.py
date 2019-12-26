#函数

#clear()
dict1 = {'PI':'肛肠气体','SHI':'肛肠固体','NIAO':'肾脏液体'}

dict1.clear()

print(dict1)


#copy()
dict1 = {'PI':'肛肠气体','SHI':'肛肠固体','NIAO':'肾脏液体'}

dict2 = dict1.copy()

print(dict2)

#fromkeys()
list1 = ['dao','qiang','jian','qi','fu','yue','gou','cha']

result = {}.fromkeys(list1,'武器')

print(result)

#get()

dict1 = {'PI':'肛肠气体','SHI':'肛肠固体','NIAO':'肾脏液体'}

result = dict1.get('GOUPI','狗屁股里的气体')

print(result)


#items()
dict1 = {'PI':'肛肠气体','SHI':'肛肠固体','NIAO':'肾脏液体'}

result = dict1.items()

print(result)


#keys() & values()
'''
dict1 = {'PI':'肛肠气体','SHI':'肛肠固体','NIAO':'肾脏液体'}

result1 = dict1.keys()

print('keys=',result1)

result2 = dict1.values()

print(result2)


#pop

dict1 = {'PI':'肛肠气体','SHI':'肛肠固体','NIAO':'肾脏液体'}

result = dict1.pop('PI')
#result = dict1.pop('GOUPI','狗狗的屁屁')

print(result)
print(dict1)

#popitems()
dict1 = {'PI':'肛肠气体','SHI':'肛肠固体','NIAO':'肾脏液体'}

result = dict1.popitem()

print(result)

result = dict1.popitem()

print(result)

result = dict1.popitem()


print(result)



#setdefault()
dict1 = {'PI':'肛肠气体','SHI':'肛肠固体','NIAO':'肾脏液体'}



dict1.setdefault('GOUPI','狗狗的屁屁')

print(dict1)

#update()

dict1 = {'PI':'肛肠气体','SHI':'肛肠固体','NIAO':'肾脏液体'}

dict1.update(PI='菊花推进器')

#dict1.update({'PI':'菊花推进器'})

print(dict1)

'''
