import tkinter
import tkinter.messagebox
root=tkinter.Tk()
root.minsize(300,300)
'''
#showinfo()
#显示成功操作
def info():
    tkinter.messagebox.showinfo('提示框','恭喜 操作成功！')

btn=tkinter.Button(root,text='显示信息',command=info)
btn.pack()
'''
'''
#showwarning()
#提示警告对话框
def warn():
    tkinter.messagebox.showwarning('FBI','warnning')


btn=tkinter.Button(root,text='警告信息',command=warn)
btn.pack()
'''
'''
def error():
    tkinter.messagebox.showerror('注意','这里有错误')


btn=tkinter.Button(root,text='错误信息',command=error)
btn.pack()
'''

#askquestion()
#显示问题操作
def que():
    tkinter.messagebox.askyesno('请注意','程序出现错误')

btn=tkinter.Button(root,text='错误信息',command=que)
btn.pack()



root.mainloop()