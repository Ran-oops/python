import tkinter
import tkinter.filedialog
import tkinter.colorchooser
root=tkinter.Tk()

root.minsize(300,300)
'''
def simple():
    result=tkinter.simpledialog.askinteger('信息收集','请输入年龄',initialvalue=18)
    print('年龄：',result)
btn=tkinter.Button(root,text='按钮',command=simple)
btn.pack()
'''
'''
from  tkinter import *
#root = Tk()
#定义点击菜单触发的方法
def hello():
    print('hello!')
def openonefile():
    result=tkinter.filedialog.askopenfilename(title='dakai')
    print(result)
def openmorefile():
    result = tkinter.filedialog.askopenfilenames()
    print(result)

#创建总菜单
menubar =tkinter. Menu(root)
# 创建一个下拉菜单，并且加入文件菜单
filemenu =tkinter. Menu(menubar,tearoff = 0)
#创建下来菜单的选项
filemenu.add_command(label="打开一个文件", command=openonefile)
filemenu.add_command(label="打开多个文件", command=openmorefile)
#创建下拉菜单的分割线
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
#将文件菜单作为下拉菜单添加到总菜单中，并且将命名为File
menubar.add_cascade(label="文件", menu=filemenu)


#再加一个编辑菜单
editmenu = Menu(menubar,tearoff = 0)

#向编辑菜单添加选项卡
editmenu.add_command(label="撤销", command=hello)
#创建下拉菜单的分割线
editmenu.add_separator()
editmenu.add_command(label="查找", command=hello)


#将编辑菜单添加到总菜单
menubar.add_cascade(label="编辑", menu=editmenu)


# 显示总菜单
root.config(menu=menubar)
root.mainloop()
'''
def select():
    result=tkinter.colorchooser.askcolor(title='选择你喜欢的颜色')
    print(result)
    btn['bg']=result[1]
btn=tkinter.Button(root,text='点击选择颜色',command =select)
btn.pack()

root.mainloop()
