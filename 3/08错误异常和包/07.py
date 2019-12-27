
#导入sys模块
import sys

#获取模块搜索路径
print(sys.path)

#向搜索路径列表中添加心的路径
sys.path.append('/home/itxdl/py04')

#获取模块搜索路径
print(sys.path)


#导入自定义的模块路径中的模块
import ww
import ll