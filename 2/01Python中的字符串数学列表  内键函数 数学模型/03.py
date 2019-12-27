#format  字符串格式化

#格式1 按照位置传参

str1 = '{0}去厕所拉了{1}斤屎！{0}棒棒哒'

result = str1.format('邢天宇',12)

print(result)

result = str1.format('吴升宇',0.001)

print(result)


#格式2 按照名称对应

str1 = '{who}性别{sex}，爱好{hobby}，身高{height}，体重{weight}，外貌{face}～清新脱俗～'

result = str1.format(who = '崔耀辉',height = 120,weight = 210 ,face = '娘化',hobby = '娘们',sex = '未知')

print(result)


#格式3  使用序列和下标

str1 = '{0[0]}，性别{0[1]},爱好{0[2]},身高{0[3]}'

result = str1.format(['吕欣','女','男','未知'])

print(result)
