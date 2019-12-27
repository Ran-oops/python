#多行文本输入框
import tkinter

root = tkinter.Tk()
root.minsize(300,400)

#普通的多行文本
#text = tkinter.Text(root)
#text.pack()

#width & height  宽度和高度
text1 = tkinter.Text(root,width = 25,height = 5)
text1.pack()

#bg & fg 背景色 前景色
text2 = tkinter.Text(root,width = 25,height = 5,bg = 'gray',fg = 'yellow')
text2.pack()

#borderwidth 边框宽度
text3 = tkinter.Text(root,width = 25,height = 5,borderwidth = 3)
text3.pack()

#font 字体
text4 = tkinter.Text(root,width = 25,height = 5,font = ('楷体',15,'bold','italic'))
text4.pack()

#state  状态  normal正常（默认值）  disabled 禁止使用
text5 = tkinter.Text(root,width = 25,height = 5,state = 'normal')
text5.pack()

#selectbackground   选中内容的背景色  selectforeground   选中内容的前景色
text6 = tkinter.Text(root,width = 25,height = 5,selectbackground = 'pink',selectforeground = '#ff9900')
text6.pack()

#textvariable    添加内容的变量
txt = tkinter.StringVar()
txt.set('3.141592653')



root.mainloop()