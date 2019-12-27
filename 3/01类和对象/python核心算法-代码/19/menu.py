#菜单组建
import tkinter

root = tkinter.Tk()
root.minsize(300,300)

#定义点击菜单触发的方法
def hello():
    print("hello!")
#创建总菜单
menubar = tkinter.Menu(root)
# 创建一个下拉菜单，并且加入文件菜单
filemenu = tkinter.Menu(menubar,tearoff = 0)
#创建下来菜单的选项
filemenu.add_command(label="打开", command=hello)
#创建下拉菜单的分割线
filemenu.add_separator()
filemenu.add_command(label="保存", command=hello)
#创建下拉菜单的分割线
filemenu.add_separator()
filemenu.add_command(label="推出", command=root.quit)

#将文件菜单作为下拉菜单添加到总菜单中，并且将命名为File
menubar.add_cascade(label="文件", menu=filemenu)


# 创建一个下拉菜单，并且加入编辑菜单
editmenu = tkinter.Menu(menubar,tearoff = 0)
#创建下来菜单的选项
editmenu.add_command(label="撤销", command=hello)
editmenu.add_command(label="前进", command=hello)
editmenu.add_command(label="前进", command=hello)
editmenu.add_command(label="前进", command=hello)
editmenu.add_command(label="前进", command=hello)
editmenu.add_command(label="前进", command=hello)
editmenu.add_command(label="前进", command=hello)
#创建下拉菜单的分割线
editmenu.add_separator()
editmenu.add_command(label="查找", command=hello)

#将文件菜单作为下拉菜单添加到总菜单中，并且将命名为File
menubar.add_cascade(label="编辑", menu=editmenu)



# 显示总菜单
root.config(menu=menubar)

root.mainloop()