'''
import tkinter
root=tkinter.Tk()
root.minsize(250,250)
btn1=tkinter.Button(root,text='按钮1')
btn1.pack(side='left')
btn2=tkinter.Button(root,text='按钮2')
btn2.pack(side='right')
btn3=tkinter.Button(root,text='按钮3')
btn3.pack(side='top')
btn4=tkinter.Button(root,text='按钮4')
btn4.pack(side='bottom')
root.mainloop()
'''
import tkinter
root=tkinter.Tk()
root.minsize(270,270)
root.maxsize(270,270)
'''
btn1=tkinter.Button(root,text='按钮1')
btn1.pack(fill='x')
btn2=tkinter.Button(root,text='按钮2')
btn2.pack(side='right',fill='y')
#全部填满
btn4=tkinter.Button(root,text='按钮4')
btn4.pack(expand='yes',fill='both',anchor='n')
'''
'''
#anchor方位设置
btn1=tkinter.Button(root,text='按钮1')
btn1.pack(expand='yes',anchor='se')
'''
'''
#padx  pady设置组件之间的间距
btn1=tkinter.Button(root,text='按钮1')
btn1.pack(pady=20)
btn2=tkinter.Button(root,text='按钮2')
btn2.pack()

'''
#ipadx  ipady  设置自身间距
btn1=tkinter.Button(root,text='按钮1')
btn1.pack(ipadx=20, ipady=10)


root.mainloop()














