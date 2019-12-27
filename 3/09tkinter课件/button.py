import tkinter


root = tkinter.Tk()

root.minsize(400,400)

'''
#按钮组件

btn = tkinter.Button(root,text = '按钮')

btn.pack()
'''

'''

#按钮组件  bg背景色 fg前景色

btn = tkinter.Button(root,text = '按钮',bg = 'pink',fg = 'cyan')

btn.pack()
'''

'''
#bd 边框粗细
btn = tkinter.Button(root,text = '按钮',bd = 15)

btn.pack()
'''

'''
#command 命令属性

def func():
    print('点我就是点击！')

btn = tkinter.Button(root,text = '按钮',command = func)

btn.pack()
'''

'''
#font 字体设置  italic  斜体  bold  粗体  在字体大小之后 
btn = tkinter.Button(root,text = '按钮',font=('楷体',25,'italic','bold'))
btn.pack()
'''

'''
#宽高设置 width & height

btn = tkinter.Button(root,text = '按钮',width = 20,height = 5)
btn.pack()
'''

'''
#按钮状态 state  disabled 不可用  normal 正常

btn = tkinter.Button(root,text = '按钮',state='active')
btn.pack()
'''

#图片

img = tkinter.PhotoImage(file='./nb.gif')



btn = tkinter.Button(root,text = '按钮',image = img)
btn.pack(ipadx = 40,ipady = 20)








root.mainloop()
