import tkinter

root = tkinter.Tk()

root.minsize(400,400)


#place 布局(绝对布局)

btn1 = tkinter.Button(root,text = '按钮1')
btn1.place(x= 50,y = 50,width = 50,height =50)

btn2 = tkinter.Button(root,text = '按钮2')
btn2.place(x= 100,y = 50,width = 50,height = 50)

btn3 = tkinter.Button(root,text = '按钮3')
btn3.place(x= 50,y = 100,width = 50,height = 50)

btn4 = tkinter.Button(root,text = '按钮4')
btn4.place(x= 100,y = 100,width = 50,height = 50)
'''


#place(相对布局)

btn1 = tkinter.Button(root,text = '按钮1')
btn1.place(relx = 0.05,rely = 0.1,relwidth = 0.2,relheight = 0.2)

btn2 = tkinter.Button(root,text = '按钮2')
btn2.place(relx = 0.3,rely = 0.3,relwidth = 0.2,relheight = 0.2)
'''

root.mainloop()
