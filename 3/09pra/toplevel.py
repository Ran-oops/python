import tkinter

root=tkinter.Tk()
root.minsize(200,500)
root.title('feiQ')
def func():
    global tp

    tp=tkinter.Toplevel(width=300,height=300,bg='pink')
    #禁止调整大小
    tp.resizable(width=False,height=False)
    tp.title('对方正在输入')
    txt1=tkinter.Text(tp,width=20,height=8,state='disabled')
    txt1.pack()
    txt2=tkinter.Text(tp, width=20,height=5)
    txt2.pack()
btn=tkinter.Button(root,text='按钮',command=func)
btn.pack()
def hide():
    global tp
    tp.withdraw()
btn2=tkinter.Button(root,text='隐藏界面',command=hide)
btn2.pack()

root.mainloop()