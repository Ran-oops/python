#事件绑定1

import tkinter

root = tkinter.Tk()
root.minsize(300,300)

'''
#添加label（鼠标事件）
label = tkinter.Label(root,text = '点击鼠标变颜色')
label.pack()

#声明一个函数（点击左键，背景颜色便黄）
def changeyellow(arg):
    label['bg'] = 'yellow'

#事件绑定操作
label.bind('<Button-1>',changeyellow)


#声明一个函数（点击左键，背景颜色变为青色）
def changecyan(arg):
    label['bg'] = 'cyan'

#事件绑定操作
label.bind('<Button-3>',changecyan)
'''


'''
#text 组建
txt = tkinter.Text(root,width = 30,height = 5)
txt.pack()

#鼠标进入变为蓝色
def changeblue(arg):
    txt['bg'] = 'blue'

#事件绑定
txt.bind('<Enter>',changeblue)

#鼠标离开变为白色
def changewhite(arg):
    txt['bg'] = 'white'

#鼠标离开
txt.bind('<Leave>',changewhite)
'''

'''
#enrty 每次输入统计文字个数
txt = tkinter.StringVar()

entry = tkinter.Entry(root,textvariable = txt)
entry.pack()

#添加label显示输入字符
label = tkinter.Label(root,text = '目前没有文字输入')
label.pack()

#统计字数的函数
def countnum(arg):
    #获取输入框中的文字
    allstr = txt.get()
    #统计大小
    num = len(allstr)
    #将数量设置到label中显示
    label['text'] = '已经输入{}个文字'.format(num)


#事件绑定
entry.bind('<KeyRelease>',countnum)
'''

#键盘复制事件 ctrl + c
import tkinter.messagebox

data = tkinter.StringVar()
data.set('用于复制的内容')

entry = tkinter.Entry(root, textvariable = data)
entry.pack()

#复制提示函数
def copytip(arg):
    tkinter.messagebox.showinfo(title= '复制提示',message= '您已经复制内容')

#事件绑定
entry.bind('<Control-KeyPress-c>',copytip)



root.mainloop()