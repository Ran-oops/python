import tkinter

root = tkinter.Tk()
root.minsize(300,300)
'''
#label
label = tkinter.Label(root,text = '掉个没完没了')
label.pack()
'''

'''
#background    bg        设置标签的背景色foreground      fg      设置标签的前景色

label = tkinter.Label(root,text = '掉个没完没了',bg = 'yellow',fg = 'red')
label.pack()
'''


# bd 边框宽度  看不见 本来就没有边
label = tkinter.Label(root,text = '掉个没完没了',bd = 20)
label.pack()


'''
#width 宽度  height 高度

label = tkinter.Label(root,text = '掉个没完没了\n掉个没完没了\n掉个没完没了\n掉个没完没了\n',bg = 'yellow',width = 20,height = 10)
label.pack()

root.mainloop()
'''

'''
#font 字体

label = tkinter.Label(root,text = '掉个没完没了',font = ('黑体',16))
label.pack()
'''

'''
#image 图片
img = tkinter.PhotoImage(file = './nb.gif')

label = tkinter.Label(root,image = img)
label.pack()
'''


#justify 对齐方式  left  right center

label = tkinter.Label(root,text = '鹅鹅鹅，\n曲项向天歌，\n白毛浮绿水，\n红掌拨清波',justify ='right')
label.pack()

'''

#textvariable 变量

txt = tkinter.StringVar()
txt.set('吃饭不积极，思想有问题！')

label = tkinter.Label(root,textvariable = txt)
label.pack()

'''
root.mainloop()