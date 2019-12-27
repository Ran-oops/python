'''
import tkinter
root=tkinter.Tk()
root.minsize(400,400)
btn=tkinter.Button(root,text='按钮',bg='pink',fg='black',bd=3)
btn.pack()
root.mainloop()
'''
#command命令属性
import tkinter
root=tkinter.Tk()
root.minsize(400,400)
'''
def func():
    print('点我就是点击！')
btn=tkinter.Button(root,text='按钮',command=func)
btn.pack()
'''
'''
#font字体设置  italic斜体  bold粗体 在字体大小之后
btn=tkinter.Button(root,text='按钮',width=20,height=5,state='disabled')
btn.pack()
'''


root.mainloop()
