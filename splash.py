from Tkinter import *
root=Tk()
root.title('phonebook')
root.configure(background='orange3')
root.geometry('400x500')
Label(root,text='PYTHON AND DBMS PROJECT',pady=20,bg='orange3',fg='white',font='Arial 10 bold').pack()
a=PhotoImage(file='phonebook.gif')
Label(root,image=a,pady=60).pack()
Label(root,text='Project Developed  By: SATWIK MISHRA (181B183)',bg='orange3',fg='white',font='Arial 10 bold',pady=40).pack()
Label(root,text='---------------------------------------------',bg='orange3',fg='red').pack()
Label(root,text='move mouse to close window',bg='orange3',fg='white',font='Arial 10 bold').pack()
def close(e=1):
    root.destroy()
root.bind('<Motion>',close)
root.mainloop()
