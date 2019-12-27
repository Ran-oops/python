import tkinter
root=tkinter.Tk()
root.geometry('400x400')
'''
btn1=tkinter.Button(root,text='按钮1')
btn1.place(x=50,y=50,height=50,width=50)
btn2=tkinter.Button(root,text='按钮2')
btn2.place(x=100,y=50,width=50,height=50)
btn3=tkinter.Button(root,text='按钮3')
btn3.place(x=50,y=100,height=50,width=50)
btn4=tkinter.Button(root,text='按钮4')
btn4.place(x=100,y=100,height=50,width=50)
'''
btn1=tkinter.Button(root,text='按钮1')
btn1.place(relx=0.1,rely=0.1,relwidth=0.1,relheight=0.1)



root.mainloop()