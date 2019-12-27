#字符串(在单引号的字符串中使用单引号)

#转义字符（去掉了'的字符串边界的意义）
#正斜线  / 反斜线 \

strval = '伟大领袖\'毛主席\'说过：一切不以结婚为目的的谈恋爱都是耍流氓！'

print(strval)


#其他的转义字符
#\n  换行操作
strval = '青青蛇儿口，\n黄蜂尾上针，\n两者皆有可，\n最毒妇人心'
print(strval)

#\"  双引号字符
strval = "青青\"蛇儿\"口，\n黄蜂尾上针，\n两者皆有可，\n最毒妇人心"
print(strval)


#\t  tab键  横向制表符
strval = "\t青青蛇儿口，\n黄蜂尾上针，\n两者皆有可，\n最毒妇人心"
print(strval)

#\\  输出一个\

strval = '青青蛇儿口,\\黄蜂尾上针，\\两者皆有可，\\n最毒妇人心'
print(strval)


#window  \r   希望回车换行   和\n组合成\r\n 表示回车换行使用
strval = '青青蛇儿口，\r\n黄蜂尾上针，\r\n两者皆有可，\r\n最毒妇人心'
print(strval)

#linux  \n 表示回车
#mac    \r 表示回车（mac os9以前版本）  现在也是\n


#\ 续行操作   （必须在每一行的最后写）
strval = '苍老师是一位肤白貌美，德\
艺双馨的好老师'

print(strval)


#元字符串（原始字符串）  禁止转义字符操作

strval = r'剩女最大的遗憾\n就是：\'死而无汉\''

print(strval)

