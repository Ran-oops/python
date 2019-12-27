import tkinter

root = tkinter.Tk()

root.minsize(300,300)

label1 = tkinter.Label(root,text = '标签1',bg = 'green')
label1.pack()

label2 = tkinter.Label(root,text = '标签2',bg = 'green')
label2.pack()

label3 = tkinter.Label(root,text = '标签3',bg = 'green')
label3.pack()

label4 = tkinter.Label(root,text = '标签4',bg = 'green')
label4.pack()

#改变背景的方法
def chbg(evt):
    
    evt.widget['bg'] = 'yellow'


'''
#为标签1绑定事件
label1.bind('<Enter>',chbg)

#为标签2绑定事件
label2.bind('<Enter>',chbg)

#为标签3绑定事件
label3.bind('<Enter>',chbg)

#为标签4绑定事件
label4.bind('<Enter>',chbg)
'''


#一次绑定所有同类组件
label1.bind_class('Label','<Enter>',chbg)

root.mainloop()
