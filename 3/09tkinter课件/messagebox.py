import tkinter
import tkinter.messagebox

root = tkinter.Tk()

root.minsize(300,300)

'''
#showinfo（）
#显示成功操作
def info():
    tkinter.messagebox.showinfo('提示框','恭喜 操作成功！')


btn = tkinter.Button(root,text = '显示信息',command = info)
btn.pack()
'''

'''
#showwarning()
#显示成功操作
def warn():
    tkinter.messagebox.showwarning('FBI','Warning')


btn = tkinter.Button(root,text = '警告信息',command = warn)
btn.pack()
'''

'''
#showerror()
#显示成功操作
def err():
    tkinter.messagebox.showerror('请注意','程序出现错误')


btn = tkinter.Button(root,text = '错误信息',command = err)
btn.pack()
'''

'''
#askquestion()
#显示问题操作
def ques():
    result = tkinter.messagebox.askquestion('请注意','程序出现错误')
    print(result)


btn = tkinter.Button(root,text = '错误信息',command = ques)
btn.pack()
'''

'''
#askokcancel()
#显示问题操作
def ok():
    result = tkinter.messagebox.askokcancel('请注意','程序出现错误')
    print(result)


btn = tkinter.Button(root,text = '确定取消',command = ok)
btn.pack()
'''

'''
#askyesno()
#显示问题操作
def yes():
    result = tkinter.messagebox.askyesno('请回答','你是爷们 吗？')
    print(result)


btn = tkinter.Button(root,text = '是不是',command = yes)
btn.pack()
'''


#askyesno()
#显示问题操作
def cs():
    result = tkinter.messagebox.askretrycancel('请回答','程序出现问题，是否重试')
    print(result)


btn = tkinter.Button(root,text = '是不是',command = cs)
btn.pack()


root.mainloop()
