import tkinter

#定义数字被按下的额函数
def num(num):
    global bj
    print(num)
    if bj == True:
        val.set('0')
        bj = False
    #判断面板里的值是否为初始值‘0’
    if val.get() == '0':
        val.set(num)
    else:
      val.set(val.get()+num)

#==================================
#定义空列表存储，上一次的值
lists=[]
#定义标志位
bj = False
#定义一个运算符被按下的函数
def ys(ys):
    global bj
    print(ys)
    print(val.get())
    lists.append(val.get())
    lists.append(ys)
    print(lists)
    bj = True

#等于号被按下的函数
def equal():
    global lists
    #添加当前面板的值到lists中
    lists.append(val.get())
    print(lists)
    #将列表转换为字符串
    result = ''.join(lists)
    print(result)
    result = eval(result)
    val.set(result)

root = tkinter.Tk()
root.minsize(300,450)

val = tkinter.StringVar()
val.set('0')
#显示面板
label1 = tkinter.Label(root,bg = '#fff',textvariable = val,font = ('黑体',30),width = 15,anchor = 'e',borderwidth = 10).grid(row = 0 ,column = 0,columnspan=2)
#数字
btn3 = tkinter.Button(root,text= 3,width = 4,height = 2,command =lambda :num('3')).grid(row = 1,column = 0,pady = 20)
btn5 = tkinter.Button(root,text= 5,width = 4,height = 2,command = lambda :num('5')).grid(row = 1,column = 1)
#运算符
add = tkinter.Button(root,text= '+',width = 4,height = 2,command = lambda :ys('+')).grid(row = 2,column = 0)
equal = tkinter.Button(root,text= '=',width = 4,height = 2,command = equal).grid(row = 2,column = 1)
root.mainloop()