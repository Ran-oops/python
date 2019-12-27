#绑定所有组件

import tkinter

root = tkinter.Tk()
root.minsize(300,300)

#按钮
btn = tkinter.Button(root,text = '按钮')
btn.pack()

#标签
label = tkinter.Label(root,text = '标签')
label.pack()

#输入框
entry = tkinter.Entry(root)
entry.pack()


#事件函数
def changebg(evt):
    root['bg'] = 'blue'


#将所有组建都绑定一个事件
btn.bind_all('<Button-1>',changebg)

root.mainloop()