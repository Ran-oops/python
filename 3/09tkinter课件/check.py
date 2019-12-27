import tkinter

root = tkinter.Tk()

root.minsize(300,300)

#创建单选按钮
sex = tkinter.StringVar()
sex.set('协议')

'''
#声明一个下一步的按钮
btn = tkinter.Button(root,text = '下一步',state = 'disabled')
btn.pack()


#定义函数
def nextbtn():
    #将按钮设置为正常状态
    btn['state'] = 'normal'


#text 显示内容  value 被选中时接收的值  variable  将多个按钮分到同一个组别 必须同一个变量
#男
rbtn = tkinter.Checkbutton(root,text = '同意协议',variable = sex,onvalue = '1',offvalue = '0',command = nextbtn)
rbtn.pack()
'''

'''
#bg 背景色 fg 前景色
rbtn = tkinter.Checkbutton(root,text = '同意',variable = sex,onvalue = '1',offvalue = '0',bg = 'red',fg = 'yellow')
rbtn.pack()
'''

''' 
#width 宽度 anchor 组件对齐
rbtn = tkinter.Checkbutton(root,text = '同意',variable = sex,onvalue = '1',offvalue = '0',width = 20,bg = 'red',anchor = 'w')
rbtn.pack()
'''

'''
#justify 文字对齐
rbtn = tkinter.Checkbutton(root,text = '男\ndi大物博',variable = sex,onvalue = '1',offvalue = '0',width = 20,justify = 'right')
rbtn.pack()
'''

'''
import tkinter
root=tkinter.Tk()
root.minsize(300,300)

check1=tkinter.Checkbutton(root,text='不同意该协议')
check1.pack()
agree=tkinter.StringVar()

btn=tkinter.Button(root,text='next>>',state='disabled')
btn.pack()

#agree.set('协议')

def nextfunc():
    if agree.get() == 'yes':
        btn['state'] = 'normal'
    else:
        btn['state']='disabled'

check2=tkinter.Checkbutton(root,text='同意该协议',variable=agree,onvalue='yes',offvalue='no',command=nextfunc)
check2.pack()

root.mainloop()

'''



