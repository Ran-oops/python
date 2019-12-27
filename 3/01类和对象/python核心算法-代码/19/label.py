#标签组建
import tkinter

root = tkinter.Tk()
root.minsize(300,300)

#普通标签
label1 = tkinter.Label(root,text = '标签1')
label1.pack()

#bg  &fg 背景色 前景色
label2 = tkinter.Label(root,text = '孙悟空大尿天宫',fg = 'red',bg = 'pink')
label2.pack()

#borderwidth   边框宽度(不会显示，透明边框)
label3 = tkinter.Label(root,text = '孙悟空大尿天宫',borderwidth = 10,bg = 'blue')
label3.pack()

#width & height 宽度  高度
label4 = tkinter.Label(root,text = '清明上河图\n造血干细胞\n班长兼学委\n复方草珊瑚',bg = 'orange',width = 15,height =5)
label4.pack()

#font 字体
label5 = tkinter.Label(root,text = '孙悟空大尿天宫',font = ('楷体',12))
label5.pack()

#justify 设置label中文字的对其方式  left 左对齐  right 右对齐  center 剧中对其
label6 = tkinter.Label(root,text = '孙\n悟空\n大尿天\n宫',justify = 'right')
label6.pack()

#textvariable  设置标签的变量
txt = tkinter.StringVar()
txt.set( '南无阿弥陀佛')

label7 = tkinter.Label(root,textvariable = txt)
label7.pack()

root.mainloop()