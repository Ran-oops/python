import os

#定义函数
def getdirsize(path):

    #声明一个用于累计文件夹大小的变量(局部)
    total = 0
    
    #获取所有的文件和文件夹路径
    allpath = os.listdir(path)
    #遍历所有文件和文件夹
    for onepath in allpath:
        #组合成绝对路径
        fullpath = os.path.join(path,onepath)
        #检测是文件还是文件夹
        if os.path.isfile(fullpath):
            #print(fullpath,'---文件')
            #获取文件大小，并且累积
            total += os.path.getsize(fullpath)
        elif os.path.isdir(fullpath):
            #print(fullpath,'---文件夹')
            #获取文件夹大小，并且累计
            total += getdirsize(fullpath)


    #返回当前文件夹的大小
    return total
    




#调用函数
size = getdirsize('C:\\xdl\\Desktop\\ab')
print(size)



'''
def getdirsize(C:\\xdl\\Desktop\\ab):

    #声明一个用于累计文件夹大小的变量(局部)
    total = 0
    
    #获取所有的文件和文件夹路径
    allpath = os.listdir(C:\\xdl\\Desktop\\ab)#allpath = ['a','b.txt']
    #遍历所有文件和文件夹
    for onepath in allpath:
        #组合成绝对路径
        fullpath = os.path.join(path,onepath)#a ->C:\\xdl\\Desktop\\ab\\a
        fullpath = os.path.join(path,onepath)#b.txt ->C:\\xdl\\Desktop\\ab\\b.txt
         #检测是文件还是文件夹
        if os.path.isfile(fullpath):
            #print(fullpath,'---文件')
            #获取文件大小，并且累积
            total += os.path.getsize(fullpath)
        elif os.path.isdir(fullpath):#真的是文件夹
            #print(fullpath,'---文件夹')
            #获取文件夹大小，并且累计
            total += 0


    #返回当前文件夹的大小
    return total
'''


#再次调用函数getdirsize(C:\\xdl\\Desktop\\ab\\a)
'''
def getdirsize(C:\\xdl\\Desktop\\ab\\a):

    #声明一个用于累计文件夹大小的变量(局部)
    total = 0
    
    #获取所有的文件和文件夹路径
    allpath = os.listdir(path)# [a.txt]
    #遍历所有文件和文件夹
    for onepath in allpath:
        #组合成绝对路径
        fullpath = os.path.join(path,onepath)#a.txt - >C:\\xdl\\Desktop\\ab\\a\\a.txt
        #检测是文件还是文件夹
        if os.path.isfile(fullpath):#文件
            #print(fullpath,'---文件')
            #获取文件大小，并且累积
            total += os.path.getsize(fullpath)
        

    #返回当前文件夹的大小
    return total  0
    

''’








