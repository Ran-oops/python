import tkinter

root = tkinter.Tk()
root.minsize(300,300)

'''
#ENTRY

ent =tkinter.Text(root)
ent.pack()
'''

'''
#bg 背景色 fg 前景色
ent =tkinter.Text(root,bg = 'yellow',fg = 'red')
ent.pack()
'''

'''
#bd 边框宽度
ent =tkinter.Text(root,bd = 10)
ent.pack()
'''

'''
#font 字体效果
ent =tkinter.Text(root,font = ('黑体',20))
ent.pack()

'''

'''
#width 宽度  height高度

ent =tkinter.Text(root,width = 20,height = 10)
ent.pack()
'''

'''
#state 状态 normal 正常  disabled 不可用 readonly 只读
ent =tkinter.Text(root,state = 'disabled')
ent.pack()
'''

'''
#selectbackground 选中内容的背景色      selectforeground选中内容的前景色

ent =tkinter.Text(root,selectbackground = 'pink',selectforeground = 'blue')
ent.pack()

'''



root.mainloop()
