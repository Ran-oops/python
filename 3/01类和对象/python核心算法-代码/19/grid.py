#网格布局
import tkinter

root = tkinter.Tk()
root.minsize(300,300)

#网格布局
btn1 = tkinter.Button(root,text = 'button1')
btn1.grid(row = 0,column =0)

btn2 = tkinter.Button(root,text = 'button2')
btn2.grid(row = 0,column =1)

btn3 = tkinter.Button(root,text = 'button3')
btn3.grid(row = 0,column =2)

btn4 = tkinter.Button(root,text = 'button4')
btn4.grid(row = 1,column =0)

btn5 = tkinter.Button(root,text = 'button5')
btn5.grid(row = 1,column =1)

btn6 = tkinter.Button(root,text = 'button6')
btn6.grid(row = 1,column =2)

#网格合并操作
#跨行设置
btneq = tkinter.Button(root,text = '=')
btneq.grid(row = 0,column = 3,rowspan = 2,ipady = 18)

#跨列设置
btn0 = tkinter.Button(root,text = '0')
btn0.grid(row = 2,column = 0,columnspan = 2,ipadx = 50)

root.mainloop()