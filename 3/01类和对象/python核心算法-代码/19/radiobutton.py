#单选框
import tkinter

root = tkinter.Tk()
root.minsize(300,300)

#单选框
sex = tkinter.StringVar()

radio1 = tkinter.Radiobutton(root,text = '男',variable = sex,value = 'man')
radio1.pack()

radio2 = tkinter.Radiobutton(root,text = '女',variable = sex,value = 'woman')
radio2.pack()


#bg  & fg 背景色  & 前景色
sex1 = tkinter.StringVar()
radio1 = tkinter.Radiobutton(root,text = '男',variable = sex1,value = 'man',bg = 'blue',fg = 'red')
radio1.pack()

radio2 = tkinter.Radiobutton(root,text = '女',variable = sex1,value = 'woman',bg = 'pink',fg = 'red')
radio2.pack()

#borderwidth n边框宽度  (别用)
sex2 = tkinter.StringVar()
radio1 = tkinter.Radiobutton(root,text = '男',variable = sex2,value = 'man',bd = 10)
radio1.pack()

radio2 = tkinter.Radiobutton(root,text = '女',variable = sex2,value = 'woman',bd = 10)
radio2.pack()

#font 字体属性
sex3 = tkinter.StringVar()
radio1 = tkinter.Radiobutton(root,text = '男',variable = sex3,value = 'man',font = ('楷体',20))
radio1.pack()

radio2 = tkinter.Radiobutton(root,text = '女',variable = sex3,value = 'woman',font = ('楷体',20))
radio2.pack()

#width & height 宽度和高度
sex4 = tkinter.StringVar()
radio1 = tkinter.Radiobutton(root,text = '男',variable = sex4,value = 'man',width = 15,height = 3,bg = 'pink')
radio1.pack()

radio2 = tkinter.Radiobutton(root,text = '女',variable = sex4,value = 'woman',width = 15,height = 3,bg = 'pink')
radio2.pack()

#anchor 设置方位
sex5 = tkinter.StringVar()
radio1 = tkinter.Radiobutton(root,text = '男',variable = sex5,value = 'man',width = 15,height = 3,bg = 'pink',anchor = 'w')
radio1.pack()

radio2 = tkinter.Radiobutton(root,text = '女',variable = sex5,value = 'woman',width = 15,height = 3,bg = 'pink',anchor = 'w')
radio2.pack()

#
sex6 = tkinter.StringVar()
radio1 = tkinter.Radiobutton(root,text = '男\n我是爷们',variable = sex6,value = 'man',width = 15,height = 3,bg = 'pink',justify = 'right')
radio1.pack()

radio2 = tkinter.Radiobutton(root,text = '女\n我是娘们',variable = sex6,value = 'woman',width = 15,height = 3,bg = 'pink',justify = 'right')
radio2.pack()






root.mainloop()