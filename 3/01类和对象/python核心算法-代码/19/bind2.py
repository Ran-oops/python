#事件对象
import tkinter

root = tkinter.Tk()
root.minsize(300,300)


'''
#按钮
btn1 = tkinter.Button(root,text = '按钮1')
btn1.pack()

#事件函数
def changecolor(arg):
    print(arg.__dict__)
    arg.widget['bg'] = 'yellow'

#事件绑定
btn1.bind('<Button-1>',changecolor)
'''
'''
#entry输入框
entry = tkinter.Entry(root)
entry.pack()

#事件函数
def changecolor(arg):
    print(arg.__dict__)

#事件绑定
entry.bind('<KeyPress>',changecolor)

'''

root.mainloop()