import tkinter

root = tkinter.Tk()

root.minsize(400,400)

#按钮1
btn1 = tkinter.Button(root,text = '1')

btn1.grid(row = 0,column = 0,ipadx = 20,ipady = 10,padx = 10,pady = 10)

#按钮2
btn2 = tkinter.Button(root,text = '2')

btn2.grid(row = 0,column = 1,ipadx = 20,ipady = 10,padx = 10,pady = 10)

#按钮3
btn3 = tkinter.Button(root,text = '3')

btn3.grid(row = 1,column = 0,ipadx = 20,ipady = 10,padx = 10,pady = 10)


#按钮4
btn4 = tkinter.Button(root,text = '4')

btn4.grid(row = 1,column = 1,ipadx = 20,ipady = 10,padx = 10,pady = 10)

#按钮=
btneq = tkinter.Button(root,text = '=')
btneq.grid(row = 0 ,column =2,rowspan = '2',ipadx = 20,ipady =45)

#按钮0
btn0 = tkinter.Button(root,text = '0')

btn0.grid(row = 2,column = 0,columnspan = 2,ipady = 10,ipadx = 60)



root.mainloop()
