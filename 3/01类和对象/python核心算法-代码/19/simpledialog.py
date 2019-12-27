#简单对话弹窗
import tkinter
import tkinter.simpledialog


root = tkinter.Tk()
root.minsize(300,300)

#添加按钮  （获取用户输入字符串的弹窗）
def dialog():
    result = tkinter.simpledialog.askstring(title = '请输入用户名',prompt = '用户名必须为中文',initialvalue = '匿名用户')
    print('用户名：',result)

btn1 = tkinter.Button(root,text = '字符串弹窗',command = dialog)
btn1.pack()


#添加按钮  （获取用户输入整形的弹窗）
def dialog():
    result = tkinter.simpledialog.askinteger(title = '请输入年龄',prompt = '年龄必须为正整数',initialvalue = '0')
    print('年龄：',result)

btn1 = tkinter.Button(root,text = '整形弹窗',command = dialog)
btn1.pack()

#添加按钮  （获取用户输入浮点型的弹窗）
def dialog():
    result = tkinter.simpledialog.askfloat(title = '请输入身高',prompt = '身高单位为：米',initialvalue = '0')
    print('身高：',result,'米')

btn1 = tkinter.Button(root,text = '浮点型弹窗',command = dialog)
btn1.pack()

root.mainloop()