#相对定位布局
import tkinter

root = tkinter.Tk()
root.minsize(300,300)

btn1 = tkinter.Button(root,text = 'button1')
btn1.place(relx=0.05 ,rely=0.05,relwidth = 0.2)

btn2 = tkinter.Button(root,text = 'button2')
btn2.place(relx=0.3 ,rely=0.05,relwidth = 0.2)

btn3 = tkinter.Button(root,text = 'button3')
btn3.place(relx=0.55 ,rely=0.05,relwidth = 0.2)

btn4 = tkinter.Button(root,text = 'button4')
btn4.place(relx=0.05 ,rely=0.2,relwidth = 0.2)

btn5 = tkinter.Button(root,text = 'button5')
btn5.place(relx=0.3 ,rely=0.2,relwidth = 0.2)

btn6 = tkinter.Button(root,text = 'button6')
btn6.place(relx=0.55 ,rely=0.2,relwidth = 0.2)

btn0 = tkinter.Button(root,text = '0')
btn0.place(relx=0.05 ,rely=0.35,relwidth = 0.7)

btneq = tkinter.Button(root,text = '=')
btneq.place(relx=0.8 ,rely=0.05,relwidth = 0.2,relheight = 0.4)


root.mainloop()