import tkinter
root=tkinter.Tk()
root.minsize(300,300)
ent=tkinter.Text(root,bg='yellow',fg='green',bd=5,width=20,height=10,state='normal',selectbackground='red',selectforeground='white')
ent.pack()
root.mainloop()