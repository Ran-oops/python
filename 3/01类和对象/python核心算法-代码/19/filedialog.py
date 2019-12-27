#文件对话框
import tkinter
import tkinter.filedialog

root = tkinter.Tk()
root.minsize(300,300)



#定义点击菜单触发的方法

#打开一个文件（选择）
def openonefile():
    path = tkinter.filedialog.askopenfilename(title = "请选择一个文件",initialdir = '/',initialfile = '/home/itxdl/PycharmProjects/python04/myos.txt')
    print(path)

#打开多个文件
def openmorefile():
    path = tkinter.filedialog.askopenfilenames(title = "请选择多个文件",initialdir = '/',filetypes = [('python','*.py'),('文本文件','*.txt'),('allfile','*.*')])
    print(path)


#打开一个文件夹
def openonedir():
    path = tkinter.filedialog.askdirectory()
    print(path)

#保存文件的函数
def savefile():
    result = tkinter.filedialog.asksaveasfilename()
    print(result)




def hello():
    print("hello!")
#创建总菜单
menubar = tkinter.Menu(root)
# 创建一个下拉菜单，并且加入文件菜单
filemenu = tkinter.Menu(menubar,tearoff = 0)
#创建下来菜单的选项
filemenu.add_command(label="选择一个文件", command=openonefile)
filemenu.add_command(label="选择多个文件", command=openmorefile)
#创建下拉菜单的分割线
filemenu.add_separator()
#选择一个文件夹
filemenu.add_command(label="选择一个文件夹", command=openonedir)

#保存文件操作
filemenu.add_command(label="保存", command=savefile)
#创建下拉菜单的分割线
filemenu.add_separator()
filemenu.add_command(label="推出", command=root.quit)

#将文件菜单作为下拉菜单添加到总菜单中，并且将命名为File
menubar.add_cascade(label="文件", menu=filemenu)


# 显示总菜单
root.config(menu=menubar)


root.mainloop()