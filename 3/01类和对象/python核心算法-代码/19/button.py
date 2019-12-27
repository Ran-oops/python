#按钮组件

import tkinter

root = tkinter.Tk()
#初始化界面大小
root.geometry('300x400')

#普通按钮
btn1 = tkinter.Button(root,text = 'button1')
btn1.pack()

#bg 背景色  fg 前景色（字的颜色）
btn2 = tkinter.Button(root,text = 'button2',bg = 'yellow',fg = 'red')
btn2.pack()

#borderwidth  边框宽度
btn3 = tkinter.Button(root,text = 'button3',borderwidth = 3)
btn3.pack()

#command 设置命令属性
def myfunc():
    print('按钮呗点击了')

btn4 = tkinter.Button(root,text = 'button4',command = myfunc)
btn4.pack()

#font 设置字体 (字体类型,大小,粗体,斜体)

btn5 = tkinter.Button(root,text = '按钮5',font = ('楷体',20,'italic','bold'))
btn5.pack()


#width 宽度 height高度  单位是字符个数而不是像素！！！
btn6 = tkinter.Button(root,text = 'button6',width = 20,height = 3)
btn6.pack()

#state  设置按钮的状态disabled 不可用  active 激活状态 normal 正常状态（ 默认值）
btn7 = tkinter.Button(root,text= 'button7',state = 'normal')
btn7.pack()





root.mainloop()