import tkinter
root=tkinter.Tk()
root.minsize(300,300)
'''
label=tkinter.Label(root,text='哈哈哈',bg='yellow',fg='black')
label.pack()
'''
'''
#bd边框宽度  看不见 本来就没有边
label=tkinter.Label(root,text='萌得不要不要的',bg='green',fg='black',width=8,height=5,font=['黑体',5,'bold'])
label.pack()
'''
'''
#justify对齐方式
label=tkinter.Label(root,text='hah你是一棵大白菜,\n你每天都在唱歌\n你每天都在等我\n你每天都很可爱',justify='right',bg='yellow',width=25,height=12)
label.pack()
'''
#label=tkinter.Label(root,text='一次一次没有好好的告别',font=['黑体',10,'bold'])
txt=tkinter.StringVar()
txt.set('别管以后将如何结束')
label=tkinter.Label(root,textvariable=txt)
label.pack()


root.mainloop()