import tkinter

root = tkinter.Tk()
root.minsize(300,300)

'''
#ENTRY

ent =tkinter.Entry(root)
ent.pack()
'''
'''
#bg 背景色 fg 前景色
ent =tkinter.Entry(root,bg = 'yellow',fg = 'red')
ent.pack()
'''

'''
#bd 边框宽度
ent =tkinter.Entry(root,bd = 3)
ent.pack()
'''

'''
#font 字体效果
ent =tkinter.Entry(root,font = ('黑体',20))
ent.pack()
'''

'''
#width 宽度  没有高度

ent =tkinter.Entry(root,width = 40)
ent.pack()
'''

'''
#state 状态 normal 正常  disabeld 不可用 readonly 只读
ent =tkinter.Entry(root,state = 'readonly')
ent.pack()
'''

'''
#textvariable 文本变量

#三种变量  StringVar字符串 IntVar整型 FloatVar浮点型

#创建类型
txt = tkinter.StringVar()
#设置值
txt.set('请输入您的大名')

#获取值
#print(txt.get())

ent =tkinter.Entry(root,textvariable = txt)
ent.pack()

#设置函数
def gettxt():
    print(txt.get())

#点击按钮获取当前文本内容
btn=tkinter.Button(root,command = gettxt,text = '获取输入的内容')
btn.pack()

'''

'''
#selectbackground 选中内容的背景色      selectforeground选中内容的前景色

ent =tkinter.Entry(root,selectbackground = 'pink',selectforeground = 'blue')
ent.pack()
'''

#show 密码字符

ent =tkinter.Entry(root,show = '★')
ent.pack()
'''
txt=tkinter.StringVar()
txt.set("it's too bad")
print(txt.get())
ent1=tkinter.Entry(root,textvariable=txt)
ent1.pack()
btn7=tkinter.Button(root,command=lambda: txt.set('最好的我们'))
btn7.pack()
'''
'''#可以显示密码的操作
ent=tkinter.Entry(root,show='*')
ent.pack()
def showpwd():
    ent['show']=''
btn=tkinter.Button(root,text='显示密码',command=showpwd)
btn.pack()
'''

root.mainloop()
