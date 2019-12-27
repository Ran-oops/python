#顶部界面组建（操作适用于root主界面）

import tkinter

root = tkinter.Tk()
root.minsize(200,500)
root.title('FEIQ')

#新建顶级窗口
def newwindow():
    global tp
    #相当于主界面
    tp = tkinter.Toplevel(width= 300,height = 300,bg = 'pink')
    #禁止调整大小
    tp.resizable(width = False ,height =False)
    #定义标题
    tp.title('王饼环正在偷人')

    #消息记录
    txt1 = tkinter.Text(tp,width = 30,height =10,state = 'disabled')
    txt1.pack()
    #发送信息
    txt2 = tkinter.Text(tp,width = 30,height = 5)
    txt2.pack()


btn1 = tkinter.Button(root,text = '打开新界面',command = newwindow)
btn1.pack()


def hidewindow():
    global tp
    tp.withdraw()

btn2 = tkinter.Button(root,text= '隐藏界面',command = hidewindow)
btn2.pack()

root.mainloop()