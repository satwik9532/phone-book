import splash
from Tkinter import *
from tkMessageBox import *
import time
import sqlite3
con=sqlite3.Connection('Phone book')
cur=con.cursor()
cur.execute('create table if not exists phone(contactid number primary key,first_name varchar(20),last_name varchar(20),company varchar(20),address varchar(20),city varchar(20),pin number,website varchar(20),dob date)')
cur.execute('create table if not exists phoneno(contactid number ,contact_type varchar(8),phone_num number(10), primary key(contactid,phone_num),foreign key(contactid) references phone (contactid) on delete cascade);')
cur.execute('create table if not exists email(contactid number,email_type varchar(10),emailid varchar(30), primary key(contactid,emailid),foreign key(contactid) references phone (contactid) on delete cascade)')
cur.execute('create table if not exists recent(recent_search varchar(30))')
#cur.execute('drop table phoneno')


#cur.execute("insert into phoneno values(1,'Home',7141171477)")

#cur.execute('delete from phone where contactid=1')
#li=['piyush','rachit','kartike','mayank','satwik','akshray','pic']
#li.sort()
#print li

def main1():
   # cur.execute('drop table recent')
    
    
    root=Tk()
    root.wm_iconbitmap('pb.bmp')
    lastname=StringVar()
    firstname=StringVar()
    Company=StringVar()
    Address=StringVar()
    City=StringVar()
    Pin=StringVar()
    URL=StringVar()
    DOB=StringVar()
    var1=StringVar()
    var=StringVar()
    NUM=IntVar()
    var1=StringVar()
    EM=StringVar()
    getinfo=StringVar()
    deletefirt=StringVar()
    deleteno=StringVar()
    
    
    
    root.geometry('650x520')
    root.maxsize(width=800,height=800)
    root.title('Phone Book')

    
    def abc1():
    
        f2=Frame(root,bg='powder blue',width='500',height=200,borderwidth=3,relief=SUNKEN)
        f2.pack(side=LEFT,pady=2,fill='y')
        Label(f2,text='                                            ',font='Times 20 bold',pady=1,bg='cadet blue').place(x=100,y=100)
        search=Entry(f2,width=30)
        search.pack(pady=10)

        Button(f2,text='search',command=abc).pack()
        scorollbar1=Scrollbar(f2)
        scorollbar1.pack(side=RIGHT,fill='y')

        listbox1=Listbox(f2,height=40,width=50,yscrollcommand=scorollbar1.set)
        scorollbar1.config(command=listbox1.yview)
        listbox1.pack(pady=2)
        return
    
       
    def delete1():
           
        cls=askyesno('Confirm','Do you really what to delete')
        if cls==True:
            cur.execute('select contactid from phone where first_name="'+str(getinfo.get())+'"')
            p=cur.fetchall()
            cur.execute('delete from phone where first_name="'+str(getinfo.get()+'"'))
            cur.execute('delete from phoneno where contactid='+str(p[0][0]))
            cur.execute('delete from email where contactid='+str(p[0][0]))
      #     cur.execute('delete from phoneno where con
           # cur.execute('delete from phoneno where first_name="'+str(
        #--querey----
            a=showinfo('delete','contact delete sucessfully')
            if a=='ok':
                root.destroy()
                main1()

            






  #  cur.execute('delete from email where contactid=1')
    #cur.execute('select *from phoneno')
    #m=cur.fetchall()
    #print m
    
    #o=cur.fetchall()
    #print o

    def abc():
        p=getinfo.get()
        p1=p.split(' ')
        print p1
        o=(getinfo.get(),)
        po=[]
        po.append(o)
        print p,o,po
        cur.executemany('insert into recent values(?)',po)
        
        cur.execute("select *from phone where first_name='"+str(p)+"'")
        d=cur.fetchall()
        cur.execute('select *from phoneno')
        j=cur.fetchall()
        cur.execute('select *from email')
        j_1=cur.fetchall()
        
        #print d
        #c=search.get()
        #if c=='qwe':
        f2.pack_forget()
        f5=Frame(root,bg='powder blue',width=500,height=200,borderwidth=3,relief=SUNKEN)
        f5.pack(side=LEFT,pady=2,fill='y')
        Label(f5,text='First Name:'+str(d[0][1]),fg='black',font=' 10 ',bg='powder blue').place(x=5,y=10)
        Label(f5,text='Last Name:'+str(d[0][2]),fg='black',font=' 10 ',bg='powder blue').place(x=5,y=30)
        Label(f5,text='Company:'+str(d[0][3]),fg='black',font=' 10 ',bg='powder blue').place(x=5,y=50)
        Label(f5,text='Address:'+str(d[0][4]),fg='black',font=' 10 ',bg='powder blue').place(x=5,y=70)
        Label(f5,text='City:'+str(d[0][5]),fg='black',font=' 10 ',bg='powder blue').place(x=5,y=90)
        Label(f5,text='Pin Code:  '+str(d[0][6]),fg='black',font=' 10 ',bg='powder blue').place(x=5,y=110)
        Label(f5,text='Website URL: '+str(d[0][7]),fg='black',font=' 10 ',bg='powder blue').place(x=5,y=130)
        Label(f5,text='Date of Birth: '+str(d[0][8]),fg='black',font=' 10 ',bg='powder blue').place(x=5,y=150)
        Label(f5,text='phone Detail..: '+str(j[0][2]),fg='black',font=' 10 ',bg='powder blue').place(x=5,y=170)
        Label(f5,text='Phone type: '+str(j[0][1]),fg='black',font=' 10 ',bg='powder blue').place(x=5,y=190)
        Label(f5,text='Email Addresses: '+str(j_1[0][2]),fg='black',font=' 10 ',bg='powder blue').place(x=5,y=210)
        Label(f5,text='email type: '+str(j_1[0][1]),fg='black',font=' 10 ',bg='powder blue').place(x=5,y=230)
        Label(f5,text='Press Home button on right side:',fg='black',font=' 10 ',bg='powder blue').place(x=15,y=270)
        Button(f5,text='Delete',command=delete1).place(x=100,y=300)
            
            
            
            
          #  k=Button(root,text='press',command=abc1)
           # k.pack(side=RIGHT)
        return
#------------------------------------------------frame1----------------------------
    f1=Frame(root,bg="grey",borderwidth=8,relief=SUNKEN)
    f1.pack(side=LEFT,fill='y')

    Label(f1,text='Recent Search',font="Times 15 bold",pady=10,bg='grey').pack()
    scrollbar=Scrollbar(f1)
    scrollbar.pack(side=RIGHT,fill='y')
    listbox=Listbox(f1,height=50,yscrollcommand=scrollbar.set)
    cur.execute('select *from recent')
    oops=cur.fetchall()
   # listbox.delete(,END)
    print oops
    len1=len(oops)
    while len1>=0:
        
        listbox.insert(END,oops[len1-1])
        len1+=-1
    
    listbox.pack(fill='y')




#-----------------------------frame2--------------------------------

    f2=Frame(root,bg='powder blue',width=500,height=200,borderwidth=3,relief=SUNKEN)
    f2.pack(side=LEFT,pady=2,fill='y')
    Label(f2,text='                                            ',font='Times 20 bold',pady=1,bg='cadet blue').pack()
    scrollbar.config(command=listbox.yview)



    #lishow=''    
    def lisort(event):
        lishow=search.get()
       # lishow=lishow+t.get()
        listbox1.delete(0,END)
        cur.execute("select first_name,last_name from phone where first_name like'"+str(search.get())+"%'")
        y=cur.fetchall()
        for i in y: 
            listbox1.insert(END,i)
        a=[]
        #a.append(search.get())
        #listbox1.delete(0,END)
        #fr i in li:
         #   if i[0]==search.get():
          #      listbox1.insert(END,i)


    search=Entry(f2,width=30,textvariable=getinfo)

    search.pack(pady=10)

    t=Button(f2,text='search',command=abc)
    t.place(x=260,y=45)
    root.bind('<KeyPress>',lisort)
    scorollbar1=Scrollbar(f2)
    scorollbar1.pack(side=RIGHT,fill='y')

    listbox1=Listbox(f2,height=40,width=50,yscrollcommand=scorollbar1.set)
    scorollbar1.config(command=listbox1.yview)
    listbox1.pack(pady=2)
    cur.execute('select first_name,last_name from phone')
    sea=cur.fetchall()
    sea1=[]

    for i in sea:
        sea1.append(i[0]+" "+i[1])
    sea1.sort()
    for i in sea1:
        listbox1.insert(END,i)
    
                    

    



    
   

    
   





#---------------------------------------------frame3---------------------------------

    f3=Frame(root,bg='grey',height=200,width=250,borderwidth=3,relief=SUNKEN)
    f3.pack(side=RIGHT,pady=2,fill='y')
    



#-------------save_function----
    def save_contact():
        cur.execute('select max(contactid) from phone')
        c=cur.fetchall()
        if c[0][0]==None:
            c=1
        else:
            c=int(c[0][0])+1
        

        
        l=(c,firstname.get(),lastname.get(),Company.get(),Address.get(),City.get(),Pin.get(),URL.get(),DOB.get())
        L=[]
        L.append(l)
        
        
        
        cur.executemany('insert into phone values(?,?,?,?,?,?,?,?,?)',L)
        l_1=(c,var.get(),NUM.get())
        L1=[]
        L1.append(l_1)
        cur.executemany('insert into phoneno values(?,?,?)',L1)
        l_2=(c,var1.get(),EM.get())
        L2=[]
        L2.append(l_2)
        cur.executemany('insert into email values(?,?,?)',L2)
        
        #print l,type(NUM.get())
        a=showinfo("Save",'Contact Save Sucessfully')
        if a=='ok':
            root.destroy()
            main1()
        
        






    

#--------function_f3----------
    def create():
        
        f2.pack_forget()
        f4=Frame(root,bg='powder blue',width=500,height=200,borderwidth=3,relief=SUNKEN)
        f4.pack(side=LEFT,pady=2,fill='y')
        Label(f4,text='First Name:                                                  ',bg='powder blue').place(x=2,y=15)
      #  Label(f4,text='enter data                                                                                         ').place(x=2,y=15)
        first_name=Entry(f4,textvariable=firstname)
        first_name.place(x=100,y=15)
        Label(f4,text='Last Name:').place(x=5,y=50)
        last_name = Entry(f4,textvariable=lastname)
        last_name.place(x=100,y=50)
        Label(f4,text='Company Name').place(x=5,y=85)
        company=Entry(f4,textvariable=Company)
        company.place(x=100,y=85)
        Label(f4,text='Address').place(x=5,y=120)
        address=Entry(f4,textvariable=Address)
        address.place(x=100,y=120)
        Label(f4,text='City:',bg='powder blue',font='  bold').place(x=5,y=150)
        city=Entry(f4,textvariable=City)
        city.place(x=100,y=150)
        Label(f4,text='Pin code:',bg='powder blue',font='  bold').place(x=5,y=185)
        pin=Entry(f4,textvariable=Pin).place(x=100,y=180)
        Label(f4,text='Website Url:',bg='powder blue',font='  bold').place(x=5,y=215)
        url=Entry(f4,textvariable=URL)
        url.place(x=110,y=215)
        Label(f4,text='DoB:',bg='powder blue',font='  bold').place(x=5,y=250)
        dob=Entry(f4,textvariable=DOB)
        dob.place(x=90,y=250)
        Label(f4,text='Select Phone Type:',fg='blue',bg='powder blue',font='  bold').place(x=5,y=285)
        
    

        radio=Radiobutton(f4,text='office',bg='powder blue',variable=var,value='office',tristatevalue=0).place(x=140,y=285)
        radio=Radiobutton(f4,text='Home',bg='powder blue',variable=var,value='Home',tristatevalue=0).place(x=200,y=285)
        radio=Radiobutton(f4,text='Mobile',bg='powder blue',variable=var,value='Mobile',tristatevalue=0).place(x=270,y=285)
        Label(f4,text='Phone Number',bg='powder blue').place(x=5,y=315)
    


        Label(f4,text='Select Email Type',bg='powder blue',font='  bold').place(x=5,y=350)
        number=Entry(f4,textvariable=NUM)
        number.place(x=90,y=320)

        
    #var1.set()
        radio1=Radiobutton(f4,text='Offce',bg='powder blue',variable=var1,value='Office',tristatevalue=0).place(x=150,y=350)
        radio1=Radiobutton(f4,text='Personal',bg='powder blue',variable=var1,value='personal',tristatevalue=0).place(x=210,y=350)
        Label(f4,text='Email id',bg='powder blue',font='  bold').place(x=10,y=380)
        email=Entry(f4,textvariable=EM)
        email.place(x=150,y=380)
        Button(f4,text='+',font='  bold').place(x=280,y=375)
        Button(f4,text='Save',command=save_contact).place(x=150,y=410)
       # enter_data=(first_name.get(),last_name.get(),company.get(),address.get(),city.get(),pin.get(),url.get(),dob.get())
        #print enter_data
       
        



    





    def home():
        root.destroy()
        main1()
        
    
    
    def close():
        cls=askyesno('Confirm','Do you really what to exit')
        
        if cls==True:
            root.destroy()
       # else:
           # main1()
        
    def delete_2():
    
        cls=askyesno('Confirm','Do you really what to delete')
        if cls==True:
            cur.execute('select contactid from phone where first_name="'+str(deletefirt.get())+'"')
            p=cur.fetchall()
            cur.execute('delete from phone where first_name="'+str(deletefirt.get()+'"'))
            cur.execute('delete from phoneno where contactid='+str(p[0][0]))
            cur.execute('delete from email where contactid='+str(p[0][0]))
            a=showinfo('delete','contact delete sucessfully')
            if a=='ok':
                root.destroy()
                main1()
      #     cur.execute('delete from phoneno where con
            

    def delete():
        f2.pack_forget()
        f6=Frame(root,bg='powder blue',width=500,height=200,borderwidth=3,relief=SUNKEN)
        f6.pack(side=LEFT,pady=2,fill='y')
        Label(f6,text='Enter the first name ',bg='powder blue',font='  bold').place(x=100,y=100)
        df=Entry(f6,textvariable=deletefirt)
        df.place(x=100,y=130)
        Label(f6,text='Enter Phone no',bg='powder blue',font='  bold').place(x=100,y=160)
        df_1=Entry(f6,textvariable=deleteno)
        df_1.place(x=100,y=190)
        Button(f6,text='Delete',command=delete_2).place(x=100,y=240)


   




#--------------button_f3--------
    Button(f3,text='         add contact           ',command=create).pack(pady=10,padx=5)
    Button(f3,text='         Edit contact          ').pack(padx=5,pady=10)
    Button(f3,text='         Delete contact        ',command=delete).pack(padx=5,pady=10)
    Button(f3,text='             Home              ',command=home).pack(padx=5,pady=10)
    Button(f3,text='           Close                ',command=close).pack(padx=5,pady=10)










    root.mainloop()

main1()
con.commit()

