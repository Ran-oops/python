import tkinter
root=tkinter.Tk()
root.minsize(300,300)

check1=tkinter.Checkbutton(root,text='不同意该协议')
check1.pack()



agree=tkinter.StringVar()
#agree.set('协议')

def nextfunc():
    if agree.get() == 'yes':
        btn['state'] = 'normal'
    else:
        btn['state']='disabled'

check2=tkinter.Checkbutton(root,text='同意该协议',variable=agree,onvalue='yes',offvalue='no',command=nextfunc)
check2.pack()
btn=tkinter.Button(root,text='next>>',state='disabled')
btn.pack()

root.mainloop()
