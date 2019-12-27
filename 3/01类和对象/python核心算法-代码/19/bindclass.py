#按类别绑定组件
import tkinter

root = tkinter.Tk()
root.minsize(300,300)

#按钮1
btn1 = tkinter.Button(root,text = '按钮1')
btn1.pack()

#按钮2
btn2 = tkinter.Button(root,text = '按钮2')
btn2.pack()

#按钮3
btn3 = tkinter.Button(root,text = '按钮3')
btn3.pack()

#按钮4
btn4 = tkinter.Button(root,text = '按钮4')
btn4.pack()

#按钮5
btn5 = tkinter.Button(root,text = '按钮5')
btn5.pack()

#事件函数
def changecolor(evt):
    #print(evt.__dict__)
    #通过事件对象查找触发事件的组件
    evt.widget['bg'] = 'pink'


#一次绑定一个类别的组建
btn1.bind_class('Button','<Button-1>',changecolor)




root.mainloop()