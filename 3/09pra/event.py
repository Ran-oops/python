import tkinter
root=tkinter.Tk()
root.minsize(300,300)
'''
#添加label（鼠标事件）
label=tkinter.Label(root,text='点击鼠标变颜色')
label.pack()
def changeyellow(arg):
    label['bg']='yellow'
label.bind('<Button-1>',changeyellow)

def changecyan(arg):
    label['bg']='cyan'
label.bind('<Button-2>',changecyan)
'''
'''
#text组件
txt=tkinter.Text(root,width=30,height=5)
txt.pack()
def changeblue(arg):
    txt['bg']='blue'
txt.bind('<Enter>',changeblue)
def changewhite(arg):
    txt['bg']='white'
txt.bind('<Leave>',changewhite)
'''
'''
#entry每次输入统计文字个数
txt=tkinter.StringVar()
entry1=tkinter.Entry(root,textvariable=txt)
entry1.pack()

label=tkinter.Label(root,text='目前没有文字输入')
label.pack()
def countnum(arg):
    str1=txt.get()
    num=len(str1)
    label['text']='已经输入{}个文字'.format(num)

entry1.bind('<KeyRelease>',countnum)
'''
import tkinter.messagebox
txt=tkinter.StringVar()
txt.set('你猜我猜不猜呀')
entry=tkinter.Entry(root,textvariable=txt)
entry.pack()
def copytip(arg):
    tkinter.messagebox.showinfo(title='信息提示',message='你已成功复制了呢！')
entry.bind('<Control-KeyPress-c>',copytip)





root.mainloop()