#事件对象
import tkinter
root=tkinter.Tk()
root.minsize(300,300)
#按钮
btn1=tkinter.Button(root,text='按钮1')
btn1.pack()
def changecolor(arg):
    print(arg.__dict__)
    arg.widget['bg']='yellow'
btn1.bind('<Button-1>',changecolor)





root.mainloop()