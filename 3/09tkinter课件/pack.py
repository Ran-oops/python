import tkinter

root = tkinter.Tk()
#设置界面大小
root.minsize(400,400)

#添加按钮并且摆放
btn1 = tkinter.Button(root,text = '按钮1')

'''
#side  设置摆放的方位
#摆放按钮
btn1.pack(side = 'left')

#添加按钮并且摆放
btn2 = tkinter.Button(root,text = '按钮2')

#摆放按钮
btn2.pack(side = 'right')

#添加按钮并且摆放
btn3 = tkinter.Button(root,text = '按钮3')

#摆放按钮
btn3.pack(side = 'top')

#添加按钮并且摆放
btn4 = tkinter.Button(root,text = '按钮4')

#摆放按钮
btn4.pack(side = 'bottom')
'''

'''
#fill 组件填充  
btn1 = tkinter.Button(root,text = '按钮1')
#横向摆放 允许横向填满
#btn1.pack(fill = 'x')

#纵向摆放 允许纵向填满
#btn1.pack(side='left',fill = 'y')

#任意摆放，全部填满可用空间 expand 必须设置yes才能用
#btn1.pack(expand = 'yes',fill= 'both', anchor = 'n')
'''

'''
#anchor 方位设置

btn1 = tkinter.Button(root,text = '按钮1')

btn1.pack(expand = 'yes',anchor = 'se')
'''

'''
#ipadx  ipady  设置自身间距

btn1 = tkinter.Button(root,text= '按钮')
btn1.pack(ipadx = 20,ipady = 10)
'''

'''
#padx  pady 设置组件之间间距

btn1 = tkinter.Button(root,text = '按钮1')

btn1.pack(pady = 20)

btn2 = tkinter.Button(root,text = '按钮2')

btn2.pack()
'''


root.mainloop()
