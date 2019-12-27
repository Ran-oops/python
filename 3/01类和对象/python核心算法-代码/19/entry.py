#单行文本输入框
import tkinter

root = tkinter.Tk()
root.minsize(300,300)


#单行输入框
entry1 = tkinter.Entry(root)
entry1.pack()

#bg 背景色  fg 前景色
entry2 = tkinter.Entry(root,bg = 'orange',fg = 'purple')
entry2.pack()

#borderwidth 边框宽度
entry3 = tkinter.Entry(root,borderwidth = 3)
entry3.pack()

#font 字体
entry4 = tkinter.Entry(root,font = ('黑体',15))
entry4.pack()

#width 宽度
entry5 = tkinter.Entry(root,width = 40)
entry5.pack()

#state 设置文本输入框的状态 disabled 禁用 normal 正常  readonly
entry6 = tkinter.Entry(root,state = 'disabled')
entry6.pack()

#textvariable   设置输入框的内容
txt = tkinter.StringVar()#创建tkinter专用的字符串变量
txt.set('')#设置值

entry7 = tkinter.Entry(root,textvariable = txt)
entry7.pack()

btn7 = tkinter.Button(root,text= '添加文字',command = lambda :txt.set("小伟不小"))
btn7.pack()

#获取值
print(txt.get())


#selectbackground  选中内容的背景色    selectforeground   选中内容的前景色
entry8 = tkinter.Entry(root,selectbackground = 'pink',selectforeground = 'blue')
entry8.pack()

#show 设置内容显示的符号 一般用于输入密码
entry9 = tkinter.Entry(root,show = '*')
entry9.pack()

def showpwd():
    entry9['show'] = ''

btn9 = tkinter.Button(root,text = '显示密码' ,command = showpwd)
btn9.pack()

root.mainloop()