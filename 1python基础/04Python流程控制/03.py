#list类型转换

var = '123'#字符串
var = ('脉动','卖不动','尖叫','乐虎')#元组
var = {'md':'4','jj':'3.5','lh':'6'}#字典
var = {'旺旺雪饼','法式小面包','奥利奥'}#集合

#输出原有类型和值
print(type(var),var)

#类型转换
newvar = list(var)

#输出转换之后的类型和值
print(type(newvar),newvar)
