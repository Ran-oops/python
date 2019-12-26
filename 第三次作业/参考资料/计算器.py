
import tkinter
import random
import math
import re

root=tkinter.Tk()
root.minsize(320,500)

#创建变量
num=tkinter.StringVar()
num.set(0)

#创建显示框
#用来显示运算过程
lb=tkinter.Label(root,textvariable=num,bg='white',fg='black',font=('黑体',20),anchor='e')
lb.place(x=20,y=20,width=280,height=25)

#创建两个变量判断
isxiaoshu=False  #初始条件，表示输入小数点

#数字函数
def shuzi(no):
    #判断界面原始数字是否为0
    app=num.get()
    #判断界面否为0
    if app=='0':
        num.set(no)
    else:
        num.set(app+no)
#符号函数
def fuhao(no1):
    global isxiaoshu
    app=num.get()
    #只有按下了数字键且没有按下小数点才可以按下符号键
    if app[-1] in '0123456789':
        #将输入的字符加入到界面中
        num.set(num.get()+no1)
        #当按下符号键后可以使用小数点
        isxiaoshu=False
    #没有按下数字键
    else:
        num.set(num.get())
#删除函数
def del1():
    global isxiaoshu
    #获取界面的字符串
    app=num.get()
    #1.判断元素个数是否大于1
    if len(app)>1:
        #1.如果最后一个元素为数字，直接删除
        if app[-1] in '0123456789':
            app1=app[:-1]
            num.set(app1)
        #2.如果最后一个元素为小数点
        elif app[-1]=='.':
            app1=app[:-1]
            num.set(app1)
            #设置为小数点没有操作
            isxiaoshu=False
        #3.如果最后一个元素为运算符
        elif app[-1] in '+-/*':
            app1=app[:-1]
            num.set(app1)
            #设置运算符没有按下
            isxiaoshu=False
    #2.元素个数等于1个，那么就直接设置为0
    else:
        num.set(0)
        
#清空键函数
def clear():
    #直接设置界面为0
    num.set(0)
    #重置所有按钮
    isxiaoshu=False
    
#正负号函数
def zhenfu():
    app=num.get()
    #在最前面添加正负号
    #1.如果界面只有0，则无法添加
    if app=='0':
        num.set(0)
    #2.如果界面不为0
    else:
        #2.1.如果最前面有个负号，则消除
        if app[0]=='-':
            num.set(app[1:])
        else:
            num.set('-'+app)
                
#求和函数
def dengyu():
    global isxiaoshu
    #1.如果界面只有一个字符，那么设置界面就为当前值
    app=num.get()
    if len(app)==1:
        num.set(app)
    #2.如果界面超过一个字符，进行条件再判断
    elif len(app)>1:
        #2.1 如果最后一个字符为数字，那么直接求和
        if app[-1] in '0123456789':
            app1=eval(''.join(app))
            #2.1.1 如果为整型（10.0）
            if app1==int(app1):
                num.set(int(app1))
                #可以使用小数点
                isxiaoshu=False
            #2.1.2 如果为小数（10.2）
            else:
                num.set(app1)
                #不能使用小数点
                isxiaoshu=True
        #2.2 如果最后一个字符不是数字，那么去掉最后一个符号，求和
        else:
            app1=eval(''.join(app[0:-1]))
            #2.2.1 如果为整型（10.0）
            if app1==int(app1):
                num.set(int(app1))
                #可以使用小数点
                isxiaoshu=False
            #2.2.2 如果为小数（10.2）
            else:
                num.set(app1)
                #不能使用小数点
                isxiaoshu=True
            
#小数点函数
def xiaoshu():
    global isxiaoshu
    app=num.get()
    #判断界面最后一个元素是否为数字
    if app[-1] in '0123456789' and isxiaoshu==False:
        num.set(app+'.')
        isxiaoshu=True
    else:
        num.set(app)
#开平方函数
def kpf():
    pass

#分数函数
def fenshu():
    pass

def baifenbi():
    pass
        
#创建按钮显示名字(第1排)
xq=tkinter.Button(root,text='MC')  
xq.place(x=20,y=140,width=40,height=40)

zf=tkinter.Button(root,text='MR')   
zf.place(x=80,y=140,width=40,height=40)

gy=tkinter.Button(root,text='MS')  
gy.place(x=140,y=140,width=40,height=40)

sq=tkinter.Button(root,text='M+') 
sq.place(x=200,y=140,width=40,height=40)

xh=tkinter.Button(root,text='M-')  
xh.place(x=260,y=140,width=40,height=40)

#创建按钮显示名字(第2排)
xq=tkinter.Button(root,text='<-',command=del1)
xq.place(x=20,y=200,width=40,height=40)

zf=tkinter.Button(root,text='CE',command=clear) 
zf.place(x=80,y=200,width=40,height=40)

gy=tkinter.Button(root,text='C',command=clear)
gy.place(x=140,y=200,width=40,height=40)

sq=tkinter.Button(root,text='±',command=zhenfu)
sq.place(x=200,y=200,width=40,height=40)

xh=tkinter.Button(root,text='√',command=kpf)
xh.place(x=260,y=200,width=40,height=40)

#创建按钮显示名字(第3排)
xq=tkinter.Button(root,text='7',command=lambda:shuzi('7'))
xq.place(x=20,y=260,width=40,height=40)

zf=tkinter.Button(root,text='8',command=lambda:shuzi('8'))
zf.place(x=80,y=260,width=40,height=40)

gy=tkinter.Button(root,text='9',command=lambda:shuzi('9'))
gy.place(x=140,y=260,width=40,height=40)

sq=tkinter.Button(root,text='/',command=lambda:fuhao('/'))
sq.place(x=200,y=260,width=40,height=40)

xh=tkinter.Button(root,text='%',command=baifenbi)
xh.place(x=260,y=260,width=40,height=40)

#创建按钮显示名字(第4排)
xq=tkinter.Button(root,text='4',command=lambda:shuzi('4'))
xq.place(x=20,y=320,width=40,height=40)

zf=tkinter.Button(root,text='5',command=lambda:shuzi('5'))
zf.place(x=80,y=320,width=40,height=40)

gy=tkinter.Button(root,text='6',command=lambda:shuzi('6'))
gy.place(x=140,y=320,width=40,height=40)

sq=tkinter.Button(root,text='*',command=lambda:fuhao('*'))
sq.place(x=200,y=320,width=40,height=40)

xh=tkinter.Button(root,text='1/x',command=fenshu)
xh.place(x=260,y=320,width=40,height=40)

#创建按钮显示名字(第5排)
xq=tkinter.Button(root,text='1',command=lambda:shuzi('1'))
xq.place(x=20,y=380,width=40,height=40)

zf=tkinter.Button(root,text='2',command=lambda:shuzi('2'))
zf.place(x=80,y=380,width=40,height=40)

gy=tkinter.Button(root,text='3',command=lambda:shuzi('3'))
gy.place(x=140,y=380,width=40,height=40)

sq=tkinter.Button(root,text='-',command=lambda:fuhao('-'))
sq.place(x=200,y=380,width=40,height=40)

xh=tkinter.Button(root,text='=',command=dengyu)
xh.place(x=260,y=380,width=40,height=100)

#创建按钮显示名字(第6排)
xq=tkinter.Button(root,text='0',command=lambda:shuzi('0'))
xq.place(x=20,y=440,width=100,height=40)

zf=tkinter.Button(root,text='.',command=xiaoshu)
zf.place(x=140,y=440,width=40,height=40)

gy=tkinter.Button(root,text='+',command=lambda:fuhao('+'))
gy.place(x=200,y=440,width=40,height=40)


root.mainloop()
