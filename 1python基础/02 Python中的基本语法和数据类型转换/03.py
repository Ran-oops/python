#字符串类型 string

#单引号声明字符串

strval = '两只小蜜蜂，飞在花丛中，一个飞得高，一个飞得低，高的对低的说，你个low bee'

print(type(strval))

print(strval)


#双引号声明字符串

strval2 = "两只老虎，两只老虎谈恋爱，两只都是公的，真变态啊，真变态"

print(type(strval2))

print(strval2)


#三引号声明字符串

#strval3 = '''FBI 美国联邦调查局  Warning 警告  FBI Warning...'''
strval3 = """FBI 美国联邦调查局  Warning 警告  FBI Warning..."""

print(type(strval3))

print(strval3)


#三种字符串声明方式的适用情况


#单引号适合文字中包含大量双引号的内容，但是包含单引号则不适合(html代码)
strval = '两只小蜜蜂，飞在花丛中，一个飞得高，一个飞得低，高的对低的说，你个"low bee"'

print(strval)

#双音还适合文字中包含大量单引号的内容，但是包含双引号则不适合（英文文章）
strval2 = "两只老虎，两只老虎谈恋爱，两只都是'公的'，真变态啊，真变态"
print(strval2)


#三引号适合文字中既包含单引号也包含双引号的内容，尤其对大型文字内容适合（适合大内容）
strval3 = """FBI '美国联邦调查局'  Warning "警告"  FBI Warning..."""
print(strval3)
