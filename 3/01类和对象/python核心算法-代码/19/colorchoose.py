#颜色选择对话框
import tkinter
import tkinter.colorchooser

root = tkinter.Tk()
root.minsize(300,300)

#添加颜色选择按钮
def select():
    #打开颜色选择器
    result = tkinter.colorchooser.askcolor(title = '内裤颜色种类',initialcolor = 'purple')
    print(result)
    #改变按钮颜色
    btn1['bg'] = result[1]

btn1 = tkinter.Button(root,text = '请选择你的内裤颜色',command = select)
btn1.pack()




root.mainloop()