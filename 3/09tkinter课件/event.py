import tkinter

root = tkinter.Tk()

root.minsize(300,300)


'''
#鼠标左键点击label变色

label = tkinter.Label(root,text = '因小失大',bg = 'red')
label.pack()

#事件绑定
def changebg(evt):
    #print(evt.__dict__)
    #修改组件属性
    evt.widget['bg'] = 'green'
    
label.bind('<Enter>',changebg)


def backbg(evt):
    #print(evt.__dict__)
    #修改组件属性
    evt.widget['bg'] = 'red'
    
label.bind('<Leave>',backbg)
'''



#键盘事件

uname = tkinter.StringVar()
uname.set('')


entry = tkinter.Entry(root,textvariable = uname)
entry.pack()

#添加label统计字数
label = tkinter.Label(root,text = '当前字数为:')
label.pack()
print(uname.get())

#事件绑定
'''
def countno(evt):
    #计算输入字符数
    l = len(uname.get())+1
    #改变label的显示
    label['text'] = '当前字数为:'+str(l)
    

entry.bind('<KeyPress>',countno)
'''

'''
entry = tkinter.Entry(root)
entry.pack()

#绑定事件
def changebg(evt):
    #输出键盘按下的键
    print(evt.char,evt.keycode)
    #改变操作
    evt.widget['bg'] = 'pink'
    
entry.bind('<KeyPress-B>',changebg)
'''
root.mainloop()
