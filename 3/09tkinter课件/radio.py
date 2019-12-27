import tkinter

root = tkinter.Tk()

root.minsize(300,300)

#创建单选按钮
sex = tkinter.StringVar()
sex.set('性别')

'''
#text 显示内容  value 被选中时接收的值  variable  将多个按钮分到同一个组别 必须同一个变量
#男
rbtn = tkinter.Radiobutton(root,text = '男',variable = sex,value = 'man')
rbtn.pack()
#女
rbtn = tkinter.Radiobutton(root,text = '女',variable = sex,value = 'woman')
rbtn.pack()
'''

'''
#bg 背景色 fg 前景色
rbtn = tkinter.Radiobutton(root,text = '男',variable = sex,value = 'man',bg = 'red',fg = 'yellow')
rbtn.pack()
#女
rbtn = tkinter.Radiobutton(root,text = '女',variable = sex,value = 'woman')s
rbtn.pack()
'''

'''
#width 宽度 anchor 组件对齐
rbtn = tkinter.Radiobutton(root,text = '男',variable = sex,value = 'man',width = 20,bg = 'red',anchor = 'w')
rbtn.pack()
#女
rbtn = tkinter.Radiobutton(root,text = '女',variable = sex,value = 'woman',bg = 'green')
rbtn.pack()
'''

'''
#justify 文字对齐
rbtn = tkinter.Radiobutton(root,text = '男\ndi大物博',variable = sex,value = 'man',width = 20,justify = 'left')
rbtn.pack()
#女
rbtn = tkinter.Radiobutton(root,text = '女',variable = sex,value = 'woman',bg = 'green')
rbtn.pack()
'''

#command  指定操作
def show():
    print('选中性别')

rbtn = tkinter.Radiobutton(root,text = '男',variable = sex,value = 'man',command = show)
rbtn.pack()
#女
rbtn = tkinter.Radiobutton(root,text = '女',variable = sex,value = 'woman')
rbtn.pack()

root.mainloop()
