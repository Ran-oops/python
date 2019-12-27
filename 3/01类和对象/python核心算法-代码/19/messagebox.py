#消息弹窗组建

import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.minsize(300,300)

#添加按钮，点击出现弹窗（信息弹窗）
def msgbox1():

    tkinter.messagebox.showinfo(title = '信息提示',message = '您啦的shi已经顺利冲走了！')

btn1 = tkinter.Button(root,text = '信息弹窗',command = msgbox1)
btn1.pack()


#添加按钮，点击出现弹窗（警告弹窗）
def msgbox2():

    tkinter.messagebox.showwarning(title = 'FBI Warnning',message = '18岁以下禁止观看！！')

btn1 = tkinter.Button(root,text = '警告弹窗',command = msgbox2)
btn1.pack()

#添加按钮，点击出现弹窗（错误弹窗）
def msgbox3():

    tkinter.messagebox.showerror(title = '出现错误',message = '对不起，您的便便堵住了厕所！！')

btn1 = tkinter.Button(root,text = '错误弹窗',command = msgbox3)
btn1.pack()


#问题对话框
def msgbox4():

    result = tkinter.messagebox.askquestion(title = '提问',message = ' 你妈逼你结婚了没有！')
    print(result)

btn1 = tkinter.Button(root,text = '提问弹窗',command = msgbox4)
btn1.pack()


#确定还是取消对话框
def msgbox5():

    result = tkinter.messagebox.askokcancel(title = '提问',message = '你是否确定要和你媳妇离婚')
    print(result)

btn1 = tkinter.Button(root,text = '提问弹窗',command = msgbox5)
btn1.pack()




#是不是对话框
def msgbox6():

    result = tkinter.messagebox.askyesno(title = '提问',message = '你是爷们么？')
    print(result)

btn1 = tkinter.Button(root,text = '提问弹窗',command = msgbox6)
btn1.pack()


#重试或者取消对话框
def msgbox7():

    result = tkinter.messagebox.askretrycancel(title = '请选择',message = '自宫失败，是否重新尝试！')
    print(result)

btn1 = tkinter.Button(root,text = '重试弹窗',command = msgbox7)
btn1.pack()

root.mainloop()