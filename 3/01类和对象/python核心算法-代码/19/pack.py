import tkinter

root = tkinter.Tk()

#设置主界面的大小
root.minsize(300,300)


#添加按钮
btn1 = tkinter.Button(root,text = '按钮1')
btn1.pack(side = 'left')


btn2 = tkinter.Button(root,text= '按钮2')
btn2.pack(side = 'top')

btn3 = tkinter.Button(root,text = '按钮3')
btn3.pack(side = 'right')

btn4 = tkinter.Button(root,text = '按钮4')
btn4.pack(side = 'bottom')

root.mainloop()