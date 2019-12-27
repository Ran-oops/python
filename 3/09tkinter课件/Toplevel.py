import tkinter
import time

root = tkinter.Tk()
#设置图标
root.iconbitmap(bitmap = './ringtones.ico')

#设置主界面标题
root.title('主界面')

#设置宽高操作 最小
root.minsize(300,300)

#按钮点击弹出新的toplevel
def newwindow():
    #创建新的窗口
    one = tkinter.Toplevel()
    #添加标题
    one.title('新窗口')
    #设置大小  minsize  maxsize
    #one.minsize(300,300)
    #one.maxsize(300,300)
    #设置是否允许拉动（有没有拉动图标）
    one.resizable(False,False)
    #点击按钮关闭窗口
    tkinter.Button(one,text = '关闭',command = lambda : one.withdraw()).pack()
    
    

btn = tkinter.Button(root,text = '新界面',command = newwindow)
btn.pack()




root.mainloop()
