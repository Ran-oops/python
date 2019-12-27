#制作一个统计文件夹大小的函数

import os

def getdirsize(dirpath):

    #统计文件夹大小的变量
    total = 0
    #获取当前文件夹中的所有文件和文件夹
    allname = os.listdir(dirpath)
    #遍历所有获取的文件和文件夹列表，统计他们的大小

    for name in allname:
        #组合成完整的路径
        fullpath = os.path.join(dirpath,name)
        #检测是否是文件或者文件夹
        if os.path.isfile(fullpath):
            #是文件，获取大小，统计下来
            total += os.path.getsize(fullpath)
        elif os.path.isdir(fullpath):
            #是文件夹，获取大小，统计下来
            total += getdirsize(fullpath)

    #计算完毕返回结果
    return total
                
    






#调用文件夹大小统计函数
size = getdirsize('D:\\Program Files')
print(size)
