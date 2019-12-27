import tkinter
root=tkinter.Tk()
root.minsize(300,300)
#ent=tkinter.Entry(root)
#ent.pack()
#ent=tkinter.Entry(root,bg='yellow',fg='blue',bd=8,font=['黑体',20],width=5)
#ent=tkinter.Entry(root,state='normal')
#textvariable 文本变量
#三种变量 StringVar字符串 IntVar整形  FloatVar浮点型
'''
txt=tkinter.StringVar()
txt.set("it's too bad")
print(txt.get())
ent1=tkinter.Entry(root,textvariable=txt)
ent1.pack()
btn7=tkinter.Button(root,command=lambda: txt.set('最好的我们'))
btn7.pack()
root.mainloop()
'''
#selectbackground选中内容的背景色
#selectforeground

# ent=tkinter.Entry(root,selectbackground='pink',selectforeground='cyan')
ent=tkinter.Entry(root,show='*')
ent.pack()
def showpwd():
    ent['show']=''
btn=tkinter.Button(root,text='显示密码',command=showpwd)
btn.pack()


root.mainloop()