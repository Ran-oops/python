
lists = [23,6,1,3,6,8,0,3,5,9]
#       [1,0,1,1,0,0,0,1,1,1]

#       [6,6,8,0,23,1,3,3,5,9]

#要传入的函数
def yushu(x):

    return x % 2

lists.sort(key = yushu)

print(lists)
