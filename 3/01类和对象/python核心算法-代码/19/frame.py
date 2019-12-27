#框架组建  配合pack布局方式使用
import tkinter

root = tkinter.Tk()
root.minsize(300,300)

#划分顶部取余
frametop = tkinter.Frame(root,bg = 'red',width = 300,height = 100)
frametop.pack()

#顶部取余添加组建
btn1 = tkinter.Button(frametop,text = '顶部按钮')
btn1.pack()

#划分左侧区域
frameleft = tkinter.Frame(root,bg = 'pink',width = 100,height = 200)
frameleft.pack(side = 'left')

#左侧取余添加组建
btn2 = tkinter.Button(frameleft,text = '左侧按钮')
btn2.pack()



#划分右侧取余
frameright = tkinter.Frame(root,bg = 'blue',width= 200,height = 200)
frameright.pack(side = 'right')

#右侧取余添加组建
btn1 = tkinter.Button(frameright,text = '右侧按钮')
btn1.pack()

root.mainloop()