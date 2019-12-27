#OS模块

OS	操作系统的简称
os模块就是对操作系统进行操作

使用该模块必须先导入模块：

	import os

#os模块中的函数

getcwd() 获取当前的工作目录

	格式：os.getcwd()
	返回值：路径字符串


chdir() 修改当前工作目录

	格式:os.chdir()
	返回值:None

listdir() 获取指定文件夹中的所有文件和文件夹组成的列表

	格式:os.listdir(目录路径)
	返回值：目录中内容名称的列表

mkdir() 创建一个目录/文件夹

	格式：os.mkdir(目录路径)
	返回值：None

makedirs() 递归创建文件夹

	格式:os.makedirs(路径)

rmdir() 移除一个目录（必须是空目录）

	格式：os.rmdir(目录路径)
	返回值:None

removedirs() 递归删除文件夹

	格式：os.removedirs(目录路径)
	返回值：None

	注意：例如：删除 D:/a/b/c   如果abc文件夹中除了路径显示的文件夹之外没有任何其他文件或者文件夹，removedirs会移除掉所有文件夹a，b，c
	如果abc任意文件夹中包含其他文件和文件夹，则该成文件夹不会被删除，如果是最底层的c文件夹则会爆出非空错误！

rename() 修改文件和文件夹的名称

	格式：os.rename(源文件或文件夹，目标文件或文件夹)
	返回值：None

stat() 获取文件的相关 信息

	格式：os.stat(文件路径)
	返回值：包含文件信息的元组

system()执行系统命令
	
	格式:os.system()
	返回值：整型

	慎用！ 玩意来个rm -rf 你就爽了！

getenv() 获取系统环境变量

	格式：os.getenv(获取的环境变量名称)
	返回值：字符串

putenv() 设置系统环境变量

	格式：os.putenv('环境变量名称',值)
	返回值：无

	注意：putenv确实可以添加成功，但是无法使用正常的getenv检测到。

exit() 推出当前执行命令，直接关闭当前操作
	
	格式:exit() 
	返回值：无


##当前os模块的值

curdir
	
	os.curdir  获取当前路径   都是.	

pardir

	os.pardir 获取上层目录路径 都是..

path

	os.path os中的一个子模块，操作非常多

name

	os.name  当前系统的内核名称  win->nt  linux/unix->posix    

sep

	os.sep 获取当前系统的路径分割符号 window -> \  linux/unix -> /

extsep

	os.extsep 获取当前系统中文件名和后缀之间的分割符号，所有系统都是.

linesep
	
	os.linesep 获取当前系统的换行符号 window -> \r\n  linux/unix -> \n




##os.environ模块

os.environ 可以直接获取所有环境变量的信息组成的字典，如果希望更改环境变量，并且可以查询得到，就需要对os.environ进行操作

该模块的所有方法均是字典的方法，可以通过字典的os.environ的结果进行操作。


注意：无论使用os.getenv，putenv 还是使用os.environ进行环境变量的操作，都是只对当前脚本，临时设置而已，无法直接更新或者操作系统的环境变量设置。
	


##os.path模块
os.path是os模块中的子模块，包含很多和路径相关的操作

###函数部分

abspath() 将一个相对路径转化为绝对路径

	格式：os.path.abspath(相对路径)
	返回值：绝对路径字符串

basename() 获取路径中的文件夹或者文件名称（只要路径的最后一部分）

	格式：os.path.basename(路径)
	返回值：路径的最后一部分(可能是文件名也可能是文件夹名)

dirname() 获取路径中的路径部分(出去最后一部分)

	格式:os.path.dirname(路径)
	返回值：路径中除了最后一部分的内容字符串

join() 将2个路径合成一个路径

	格式：os.path.join(路径1,路径2)
	返回值：合并之后的路径

split（）将一个路径切割成文件夹和文件名部分

	格式：os.path.split(路径)
	返回值：元组

splitext() 将一个文件名切成名字和后缀两个部分

	格式：os.path.splitext(文件名称)
	返回值：元组  （名称,后缀）

getsize() 获取一个文件的大小

	格式:os.path.getsize(路径)
	返回值：整数


isfile() 检测一个路径是否是一个文件 

	格式：os.path.isfile(路径)
	返回值：布尔值

isdir() 检测一个路径是否是一个文件夹

	格式：os.path.isdir(路径)
	返回值：布尔值


getctime() 获取文件的创建时间！ get create time

	格式：os.path.getctime(文件路径)
	返回值：时间戳浮点数	


getmtime() 获取文件的修改时间！ get modify time

	格式：os.path.getmtime(文件路径)
	返回值：时间戳浮点数

getatime() 获取文件的访问时间！ get active time

	格式：os.path.getatime(文件路径)
	返回值：时间戳浮点数

exists() 检测指定的路径是否存在

	格式：os.path.exists(路径)
	返回值：布尔值


isabs() 检测一个路径是否是绝对路径

	格式:os.path.isabs(路径)
	返回值：布尔值

islink() 检测一个路径是否是链接

	格式:os.path.islink(路径)
	返回值:布尔值

	
samefile() 检测2个路径是否指向同一个文件

	格式:os.path.samefile(路径1,路径2)

	返回值：布尔值





#相对路径与绝对路径

相对路径：

	文件路径以当前文件所在文件夹为参考位置的路径就是相对路径，相对路径中常见的符号有.和..

	. 表示在当前文件夹中
	.. 表示在当前文件夹的上层文件夹中

	例如：	./abc.jpg 		
			../我和老师.avi    
			my.txt（省略了.）  
			abc/nidaye/nidama/不能看.exe（省略了.）


绝对路径:

	文件路径以某个精确位置作为参考位置的路径就是绝对路径，绝对路径因环境不同，参考点也略有不同。
	
		系统中(windows):以某个盘符作为参考位置的路径

			C:/window/bow...
			D:/die/niang/jiaren.exe

		系统中(linux): 以/(根)作为参照位置的路径

			/etc/host
			/var/apache/..

		url中（网址）: 以服务器地址作为参照位置的路径

			http://www.itxdl.cn/python/zhaosheng/teacher.php

			https://www.taobao.com/search/wawa.html
			
			ftp://192.168.0.1/python/zuoye/11/os.md