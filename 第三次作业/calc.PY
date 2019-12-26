import tkinter
root=tkinter.Tk()
root.minsize(370,495)
root.title('计算器')
isys=False#是否按下了运算符
yslists=[]#操作序列
#起始显示的数据
n=tkinter.StringVar()
n.set(0)
#用label创建一个显示框
show=tkinter.Label(root,textvariable=n,bg='white',fg='black',font=('楷体',20,'bold'),anchor='e')
show.place(x=20,y=20,width=330,height=35)
#数字及小数点
def change(no):
    global isys
    if isys==False:
        if n.get()=='0':
            n.set('')
            n.set(no)
        else:
            n.set(n.get()+no)
    else:
        n.set(no)
        isys=False
def operation(sign):
    global isys
    global yslists
    isys=True
    yslists.append(n.get())
    if sign=='+':
        yslists.append('+')
    elif sign=='-':
        yslists.append('-')
    elif sign=='*':
        yslists.append('*')
    elif sign=='/':
        yslists.append('/')
    print(yslists)
def equal():
    global yslists
    #获取当前界面的数值准备计算
    yslists.append(n.get())
    print(yslists)
    #组成运算字符串
    yslistsstr=''.join(yslists)
    #检测最后一位是否是运算符，是就删去
    if yslistsstr[-1] in '+-*/':
        yslistsstr=yslistsstr[0:-1]
    #运算操作
    result=eval(yslistsstr)
    n.set(result)
    yslists.clear()
def delete():
    if n.get()=='' or n.get()=='0':
        n.set('0')
        return
    else:
        no=len(n.get())
        if no>1:
            strnum=n.get()
            strnum=strnum[0:no-1]
        else:
            n.set('0')
def clear():

    global yslists
    yslists=[]
    #直接设置界面为0
    n.set('0')
    #重置所有按钮
    isys=False
def zhengfu ():
    num=n.get()
    #在最前面加负号
    if num=='0':
        n.set(0)
    else:
        if num[0]=='-':
            n.set(num[1:])
        else:
            n.set('-'+num)
#开平方函数
def kpf():
    pass
#分数函数
def fenshu():
    pass
def baifenshu():
    pass
def percent():
    pass
def daoshu():
    pass





#创建第一排按钮
btn1=tkinter.Button(root,text='MC')
btn1.place(x=20,y=75,height=40,width=40)

btn2=tkinter.Button(root,text='MR')
btn2.place(x=90,y=75,height=40,width=40)

btn3=tkinter.Button(root,text='MS')
btn3.place(x=160,y=75,height=40,width=40)

btn4=tkinter.Button(root,text='M+')
btn4.place(x=230,y=75,height=40,width=40)

btn5=tkinter.Button(root,text='M-')
btn5.place(x=300,y=75,height=40,width=40)
#第二排按钮
btn6=tkinter.Button(root,text='<-',command=delete)
btn6.place(x=20,y=145,height=40,width=40)

btn7=tkinter.Button(root,text='CE')
btn7.place(x=90,y=145,height=40,width=40)

btn8=tkinter.Button(root,text='C',command=clear)
btn8.place(x=160,y=145,height=40,width=40)

btn9=tkinter.Button(root,text='±',command=zhengfu)
btn9.place(x=230,y=145,height=40,width=40)

btn10=tkinter.Button(root,text='√',command=kpf)
btn10.place(x=300,y=145,height=40,width=40)

#第三排
btn11=tkinter.Button(root,text='7',command=lambda:change('7'))
btn11.place(x=20,y=215,height=40,width=40)

btn12=tkinter.Button(root,text='8',command=lambda:change('8'))
btn12.place(x=90,y=215,height=40,width=40)

btn13=tkinter.Button(root,text='9',command=lambda:change('9'))
btn13.place(x=160,y=215,height=40,width=40)

btn14=tkinter.Button(root,text='/',command=lambda:operation('/'))
btn14.place(x=230,y=215,height=40,width=40)

btn15=tkinter.Button(root,text='%',command=percent)
btn15.place(x=300,y=215,height=40,width=40)
#第四排
btn16=tkinter.Button(root,text='4',command=lambda:change('4'))
btn16.place(x=20,y=285,height=40,width=40)

btn17=tkinter.Button(root,text='5',command=lambda:change('5'))
btn17.place(x=90,y=285,height=40,width=40)

btn18=tkinter.Button(root,text='6',command=lambda:change('6'))
btn18.place(x=160,y=285,height=40,width=40)

btn19=tkinter.Button(root,text='*',command=lambda:operation('*'))
btn19.place(x=230,y=285,height=40,width=40)

btn20=tkinter.Button(root,text='1/x',command=daoshu)
btn20.place(x=300,y=285,height=40,width=40)
#第五排
btn21=tkinter.Button(root,text='1',command=lambda:change('1'))
btn21.place(x=20,y=355,height=40,width=40)

btn22=tkinter.Button(root,text='2',command=lambda:change('2'))
btn22.place(x=90,y=355,height=40,width=40)

btn23=tkinter.Button(root,text='3',command=lambda:change('3'))
btn23.place(x=160,y=355,height=40,width=40)

btn24=tkinter.Button(root,text='-',command=lambda:operation('-'))
btn24.place(x=230,y=355,height=40,width=40)

btn25=tkinter.Button(root,text='=',command=equal)
btn25.place(x=300,y=355,height=110,width=40)
#第六排
btn26=tkinter.Button(root,text='0',command=lambda:change('0'))
btn26.place(x=20,y=425,height=40,width=110)

btn27=tkinter.Button(root,text='.',command=lambda:change('.'))
btn27.place(x=160,y=425,height=40,width=40)

btn28=tkinter.Button(root,text='+',command=lambda:operation('+'))
btn28.place(x=230,y=425,height=40,width=40)



root.mainloop()
