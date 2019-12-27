from tkinter import *
root=Tk()
def hello():
    print('hello!')

menubar=Menu(root)
filememu=Menu(menubar,tearoff=0)
filemenu.add_command(label='打开',command=hello)
filemenu.add_command(label='保存',command=hello)