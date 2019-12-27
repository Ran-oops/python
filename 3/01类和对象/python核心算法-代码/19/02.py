#导入tkinter模块
import tkinter

#主界面
root = tkinter.Tk()

#加入一个按钮（在内存中创建）
btn = tkinter.Button(root,text = '点击')
#将按钮添加到主界面
btn.pack()

#加入一个标签（内存中）
label = tkinter.Label(root,text = '欣欣向荣')
label.pack()

#加入消息循环
root.mainloop()