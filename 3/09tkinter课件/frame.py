import tkinter

root = tkinter.Tk()
root.minsize(500,500)

frame1 = tkinter.Frame(root,bg = 'red',width = 200,height = 500)
frame1.pack(side = 'left')
btn1 = tkinter.Button(frame1,text = '左侧按钮').pack()

frame2 = tkinter.Frame(root,bg = 'green',width = 300,height = 200)
frame2.pack(side = 'top')

btn2 = tkinter.Button(frame2,text = '顶侧按钮').pack()

frame3 = tkinter.Frame(root,bg = 'blue',width = 300,height = 300)
frame3.pack(side = 'bottom')

btn1 = tkinter.Button(frame3,text = '底部按钮').pack()


root.mainloop()
