#tuple元组的转换

var  = '今生为你偷'#字符串
var = ['法师','牧师','萨满','战士']#列表
var = {'hei':'吴升宇','bigeye':'牛广林'}#字典
var = {'牛肉','羊肉','鱼肉','人造肉'}#集合


#输出原有数据类型和值
print(type(var),var)

#转换操作
newvar = tuple(var)

#输出转换之后的类型和值
print(type(newvar),newvar)
