import tkinter
root=tkinter.Tk()
root.minsize(300,300)
sex=tkinter.StringVar()
sex.set('性别')
def show():
    print('选中性别')
radio1=tkinter.Radiobutton(root,text='男\n我是爷们',variable=sex,value=0,command =show,width='20',anchor='w',bg='blue')
radio1.pack()
radio2=tkinter.Radiobutton(root,text='女\n我是娘们',variable=sex,value=1,justify='right',width='20',bg='pink')
radio2.pack()


root.mainloop()