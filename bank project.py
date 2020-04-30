from tkinter import *
import MySQLdb
from tkinter import messagebox
#exit
def exit():
    messagebox.showinfo(" Important Information", "Thankyou for using")
    t.destroy()
    t1.destroy()
#accountdetails1
def accountdetails1():
    cursor.execute("""select Name,AccountNumber,Email,PhoneNumber,Amount,Widthdraw from Employee where AccountNumber=%s and Password=%s""",(entry_l1.get(), entry_l2.get()))
    result = cursor.fetchall()
    print(result)
    label_a=Label(t5,text="Name",width=20, font=("bold", 10))
    label_a.place(x=80,y=130)
    label1 = Label(t5, text=result[0][0])
    label1.place(x=240,y=130)
    label_b=Label(t5,text="AccountNumber",width=20, font=("bold", 10))
    label_b.place(x=70,y=180)
    label2=Label(t5,text=result[0][1])
    label2.place(x=240,y=180)
    label_c=Label(t5,text="Email",width="20",font=("bold",10))
    label_c.place(x=60,y=230)
    label3=Label(t5,text=result[0][2])
    label3.place(x=240,y=230)
    label_d = Label(t5, text="Amount", width="20", font=("bold", 10))
    label_d.place(x=50, y=280)
    label4 = Label(t5, text=result[0][4])
    label4.place(x=240, y=280)
    label_e = Label(t5, text="Withdraw", width="20", font=("bold", 10))
    label_e.place(x=40, y=320)
    label5 = Label(t5, text=result[0][5])
    label5.place(x=240, y=320)
    button.config(state=DISABLED)
    t5.after(10000, t5.destroy)
#account details
def accountdetails():
    global t5
    global button
    t5 = Toplevel(t)
    t5.geometry("500x500")
    t5.title("simple application")
    button = Button(t5, text="Print account details", command=accountdetails1)
    button.pack()
    t5.mainloop()
#checkbalance1
def checkbalance1():
    cursor.execute("""select Amount from Employee where AccountNumber=%s and Password=%s""",
    (entry_l1.get(), entry_l2.get()))
    result = cursor.fetchall()
    label = Label(t4, text=result[0][0])
    label.pack()
    button.config(state=DISABLED)
    t4.after(1000,t4.destroy)
    #t4.destroy()
    #print(result[0][0])

#check balance
def checkbalance():
    global t4
    global c
    c=0
    global button
    t4=Toplevel(t)
    t4.geometry("500x500")
    t4.title("simple application")
    #cursor.execute("""select Amount from Employee where AccountNumber=%s and Password=%s""",
     #              (entry_l1.get(), entry_l2.get()))
    #result = cursor.fetchall()
    #print(result[0][0])
    button = Button(t4, text="Print balance", command=checkbalance1)
    button.pack()
    t4.mainloop()
#withdraw1
def withdraw1():
        if (entry_w1.get() == ""):
            messagebox.showinfo(" Important Information", "Please enter amount")
        elif (int(entry_w1.get()) < 0):
            messagebox.showinfo(" Important Information", "please enter +ve amount")
        else:
            cursor.execute("""
            UPDATE EMPLOYEE
            SET Widthdraw=%s
            WHERE AccountNumber=%s and Password=%s
            """, (entry_w1.get(), entry_l1.get(), entry_l2.get()))
            db.commit()
            cursor.execute("""select Amount from Employee where AccountNumber=%s and Password=%s""",(entry_l1.get(), entry_l2.get()))
            result = cursor.fetchall()
            c = int(result[0][0]) - int(entry_w1.get())
            cursor.execute("""
            UPDATE EMPLOYEE
            SET Amount=%s
            WHERE AccountNumber=%s and Password=%s
            """, (c, entry_l1.get(), entry_l2.get()))
            db.commit()
            messagebox.showinfo(" Important Information", "Amount withdraw")
            t3.destroy()
# WITHDRAW
def withdraw():
    global entry_w1
    global t3
    # t.destroy()
    t3 = Toplevel(t)
    t3.geometry("500x500")
    t3.title("simple application")
    lbl1 = Label(t3, text="WITHDRAW", bg="blue", fg="white")
    lbl1.config(anchor=CENTER)
    lbl1.pack()
    label_1 = Label(t3, text="Enter Amount To Withdraw:", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    entry_w1 = Entry(t3)
    entry_w1.place(x=250, y=130)
    Button(t3, text='withdraw', command=withdraw1, bg="blue", fg="white", width="15").place(x=130, y=180)
    t3.mainloop()


#deposit1()
def deposit1():
    if(entry_d1.get()==""):
        messagebox.showinfo(" Important Information", "Please enter amount")
    elif(int(entry_d1.get())<0):
        messagebox.showinfo(" Important Information", "please enter +ve amount")
    else:
        cursor.execute("""select Amount from Employee where AccountNumber=%s and Password=%s""", (entry_l1.get(),entry_l2.get()))
        result = cursor.fetchall()
        c=int(result[0][0])+int(entry_d1.get())
        cursor.execute("""
        UPDATE EMPLOYEE
        SET Amount=%s
        WHERE AccountNumber=%s and Password=%s
        """, (c, entry_l1.get(),entry_l2.get()))
        db.commit()
        messagebox.showinfo(" Important Information", "Amount deposited sucessfully")
        t2.destroy()

def deposit():
    global entry_d1
    global t2
    #t.destroy()
    t2=Toplevel(t)
    t2.geometry("500x500")
    t2.title("simple application")
    lbl1 = Label(t2, text="DEPOSIT", bg="blue", fg="white")
    lbl1.config(anchor=CENTER)
    lbl1.pack()
    label_1 = Label(t2, text="Enter Amount To Deposit:", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    entry_d1 = Entry(t2)
    entry_d1.place(x=250, y=130)
    Button(t2, text='DEPOSIT ', command=deposit1, bg="blue", fg="white", width="15").place(x=130,y=180)
    t2.mainloop()

# main()
def main():
    global t1
    t1=Tk()
    t1.geometry("500x500")
    #Button(root, text='Login', width=20, bg='brown', fg='white', command=t1.destroy).place(side="LEFT")
    Button(t1, text='DEPOSIT ', command=deposit, bg="pink", fg="black", width="15").pack(side=LEFT)
    Button(t1, text='WITHDRAW ', command=withdraw, bg="pink", fg="black", width="15").pack(side=RIGHT)
    Button(t1, text='CHECK BALANCE', command=checkbalance, bg="pink", fg="black", width="15").pack(side=TOP)
    Button(t1, text=' VIEW ACCOUNT DETAILS', command=accountdetails, bg="pink", fg="black", width="30").pack(side=BOTTOM)
    Button(t1, text=' EXIT', command=exit, bg="pink", fg="black", width="15").place(x=210,y=235)
    t1.mainloop()
# check()
def check():
    c=0
    sql1 = "select * from EMPLOYEE"
    cursor.execute(sql1)
    records = cursor.fetchall()
    a=str(entry_l1.get())
    b=str(entry_l2.get())
    if (entry_l1.get() == "" or entry_l2.get()==""):
        messagebox.showinfo(" Important Information", "Please Enter all Details")
        #root.after(10, root.destroy)
    else:
        #root.after(10, root.destroy)
        for i in records:
            if(a==str(i[1]) and b==str(i[2])):
                messagebox.showinfo(" Important Information", "LOGIN SUCESSFULLY")
                c=1
                main()
                #root.after(10,root.destroy)
        if(c==0):
            messagebox.showinfo(" Important Information", "LOGIN UNSUCESSFULLY")
        #root.destroy()


"""register function """
def register():
    global root
    if(entry_1.get()=="" or entry_2.get()=="" or entry_3.get()=="" or entry_4.get()=="" or entry_5.get()=="" ):
        messagebox.showinfo(" Important Information", "Please Enter all Details")
        #root.after(10, root.destroy)
    else:
        a=0
        w=0
        cursor.execute('INSERT INTO EMPLOYEE(Name,AccountNumber,Password,Email,PhoneNumber,Amount,Widthdraw) values(%s,%s,%s,%s,%s,%s,%s)',(entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),entry_5.get(),a,w))
        db.commit()
        messagebox.showinfo("Information","Your Account has been created sucessfully")
        #root.after(10,root.destroy)
        root.destroy()
#LOGIN METHOD
def login():
    global root
    root = Toplevel(t)
    root.geometry("500x500")
    global entry_l1
    global entry_l2
    label_0 = Label(root, text="Login", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)
    label_1 = Label(root, text="Account Number", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    entry_l1 = Entry(root)
    entry_l1.place(x=240, y=130)
    label_2 = Label(root, text="password", width=20, font=("bold", 10))
    label_2.place(x=68, y=180)
    entry_l2 = Entry(root,show="*")
    entry_l2.place(x=240, y=180)
    Button(root, text='Login', width=20, bg='brown', fg='white', command=check).place(x=70, y=230)
    root.mainloop()

"""SIGNUP """

def signup():
    global root
    root=Toplevel(t)
    root.geometry("500x500")
    global entry_1
    global entry_2
    global entry_3
    global entry_4
    global entry_5
    var1 = IntVar()
    label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
    label_0.place(x=90, y=53)
    label_1 = Label(root, text="Name", width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    entry_1 = Entry(root)
    entry_1.place(x=240, y=130)
    #ac = entry_1.get()
    label_2 = Label(root, text="Account Number", width=20, font=("bold", 10))
    label_2.place(x=70, y=180)
    entry_2 = Entry(root)
    entry_2.place(x=240, y=180)
    #e=entry_2.get()
    label_3 = Label(root, text="Password", width=20, font=("bold", 10))
    label_3.place(x=60, y=230)
    entry_3=Entry(root,show="*")
    entry_3.place(x=240,y=230)
    label_4=Label(root,text="Email",width=20,font=("bold",10))
    label_4.place(x=50,y=280)
    entry_4=Entry(root,)
    entry_4.place(x=240,y=280)
    label_5=Label(root,text="Phone Number",width=20,font=("bold",10))
    label_5.place(x=40,y=320)
    entry_5=Entry(root)
    entry_5.place(x=240,y=330)
    Button(root, text='Register', width=20, bg='brown', fg='white', command=register).place(x=180, y=380)
    root.mainloop()
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )
cursor = db.cursor()
#cursor.execute("IF EMPLOYEE2 EXISTS DROP TABLE EMPLOYEE2")
#cursor.execute("""CREATE TABLE EMPLOYEE (
 #      Name CHAR(20),
  #     AccountNumber INT,
   #      Password CHAR(20),
    #     Email CHAR(100),
     #    PhoneNumber INT,
      #   Amount INT,
       #  widthdraw INT)""")

t=Tk()
t.geometry("400x250")
t.title("simple application")
lbl1 = Label(t, text="WELCOME", bg="orange red", fg="white")
lbl1.config(anchor=CENTER)
lbl1.pack()
btn = Button(t, text = 'LOGIN ',command =login ,bg="pink",fg="black",width="15")
btn.pack(side=LEFT)
btn1=Button(t,text="CREATE ACCOUNT",command=signup,bg="pink",fg="black",width="15")
btn1.pack(side=RIGHT)
#btn.grid(row=0,column=5)
t.mainloop()