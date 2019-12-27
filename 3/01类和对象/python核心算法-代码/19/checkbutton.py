#复选框  选择框

import tkinter

root = tkinter.Tk()
root.minsize(300,300)

#普通
check1 = tkinter.Checkbutton(root,text = '同意本协议')
check1.pack()

#font,bg,fg,bd,font,width,height 通用的


#command  命令属性
#设置是否同意的变量
agree = tkinter.StringVar()

btn1 = tkinter.Button(root,text = 'next>>',state = 'disabled')
btn1.pack()

def func():
    #print(agree.get())

    if agree.get() == 'yes':
        #修改按钮的状态
        btn1['state'] = 'normal'
    else:
        btn1['state'] = 'disabled'

check2 = tkinter.Checkbutton(root,text = '同意本协议',command = func,onvalue = 'yes',offvalue = 'no',variable = agree)
check2.pack()


root.mainloop()