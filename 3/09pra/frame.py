import tkinter
root=tkinter.Tk()
root.minsize(500,500)
frame1=tkinter.Frame(root,bg='yellow',width=200,height=500)
frame1.pack(side='left')
btn1=tkinter.Button(frame1,text='按钮1')
btn1.pack(side='top')

root.mainloop()