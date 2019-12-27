import tkinter

root = tkinter.Tk()
root.minsize(300,300)

#组件1
btn = tkinter.Button(root,text = '按钮')
btn.pack()

#组件2
label = tkinter.Label(root,text = '标签')
label.pack()

#组件3
entry = tkinter.Entry(root)
entry.pack()

#函数
def chbg(evt):
    entry['bg'] = 'blue'
    
    

btn.bind_all('<Button-1>',chbg)


root.mainloop()
