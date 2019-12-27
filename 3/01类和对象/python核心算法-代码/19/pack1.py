import tkinter

root = tkinter.Tk()
root.minsize(300,300)

'''
#padx,pady 设置组建摆放时候和其他组建的间距
#ipad,ipady 设置组建内部内容和组建边框之间的间距，可以让组建变大
btn1 = tkinter.Button(root,text = '按钮1')
btn1.pack(pady = 10,ipadx = 10,ipady = 10)

btn2 = tkinter.Button(root,text = '按钮2')
btn2.pack(pady = 10)
'''

#fill 填充剩余共建
#如果side = top或者butuom  只能横向填充x    如果side = left或者right 只能纵向填充y
#btn1 = tkinter.Button(root,text = '按钮1')
#btn1.pack(fill = 'x')

#btn2 = tkinter.Button(root,text = '按钮2')
#btn2.pack(side = 'left',fill = 'y')

#填满所有剩余空间
#btn3 = tkinter.Button(root,text = 'button')
#btn3.pack(expand = 'yes',fill = 'both')


#方位anchor
btn1 = tkinter.Button(root,text = '按钮1')
#btn1.pack(anchor = 'w')

btn2 = tkinter.Button(root,text = '按钮2')
#btn2.pack(anchor = 'e')

btn3 = tkinter.Button(root,text = '按钮1')
btn3.pack(side = 'left',anchor = 'n')

root.mainloop()