import tkinter
import tkinter.simpledialog
import tkinter.filedialog
import tkinter.colorchooser
import tkinter

root = tkinter.Tk()

root.minsize(300,300)

"""
#简单对话框
def simple():
    #弹出简单对话框
    '''
    #字符串
    result = tkinter.simpledialog.askstring('信息收集','请输入姓名',initialvalue = '匿名用户')
    print(result)
    '''
    '''
    #整型
    result = tkinter.simpledialog.askinteger('信息收集','请输入年龄',initialvalue = 0)
    print(result)
    '''

    #浮点型
    result = tkinter.simpledialog.askfloat('信息收集','请输入体重',initialvalue = 50)
    print(result)

tkinter.Button(root,text = '简单对话框',command = simple).pack()
"""


#文件选择框
'''
def file():
    #选择一个文件
    #result = tkinter.filedialog.askopenfilename(title = '请打开课本',filetypes = [('python','*.py'),('文本文件','*.txt'),('allfile','*.*')])
    #print(result)
    
    #选择多个文件
    result = tkinter.filedialog.askopenfilenames(title = '请打开课本',filetypes = [('python','*.py'),('文本文件','*.txt'),('allfile','*.*')])
    print(result)

    
tkinter.Button(root,text = '打开文件对话框',command = file).pack()
'''

'''
def mydir():
    
    #选择一个文件夹
    result = tkinter.filedialog.askdirectory(title = '请打开指定文件夹')
    print(result)

    
tkinter.Button(root,text = '打开文件对话框',command = mydir).pack()
'''

'''
def mysave():
    
    #选择一个文件夹
    result = tkinter.filedialog.asksaveasfilename(title = '保存文件',filetypes = [('python','*.py'),('文本文件','*.txt'),('allfile','*.*')])
    print(result)

    
tkinter.Button(root,text = '打开文件对话框',command = mysave).pack()

'''


#使用颜色选择框
def color():
    result = tkinter.colorchooser.askcolor(title = '请选择内裤颜色',initialcolor = 'pink')
    print(result)


btn=tkinter.Button(root,text = '选择颜色',command = color)\
btn.pack()



root.mainloop()
