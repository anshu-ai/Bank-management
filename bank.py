#importing my sql connector & connecting the database
import mysql.connector as mysq
db=mysq.connect(host="localhost",user="root",password="beast_py12",database="bank")

#starting the code.....
#-----------------------------------------------------------------------------

#Defining a function to add a customer
def openAcc():
    n=input("Enter Name:")
    ac=input("Enter Account Number:")
    dob=input("Enter Date Of Birth:")
    ad=input("Enter Address:")
    p=input("Enter phone number:")
    ob=input("Enter Opening balance account:")
    data1=(n,ac,dob,ad,p,ob)
    data2=(n,ac,ob)
    sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amount values(%s,%s,%s)'
    c=db.cursor()
    c.execute(sql1,data1)
    c.execute(sql2,data2)
    db.commit()
    print('..............................................')
    print("-----------Data Entered Successfully----------")
    print('..............................................')
    main()


#Defining a function to Deposit amount 
def depoAmo():
    am=float(input("Enter Amount:"))
    ac=input("Enter Account Number:")
    a="select bal from amount where acno=%s"
    data=(ac,)
    c=db.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    total=myresult[0]+am
    sql="update amount set bal=%s where acno=%s"
    d=(total,ac)
    c.execute(sql,d)
    db.commit()
    print('.......................................................')
    print("-------------Amount entered successfully😊-------------")
    print('.......................................................')
    print('______________Thanks for using Atom Bank_______________')
    main()


#Defining a function to Withdraw amount
def witnam():
    am=float(input("Enter Amount:"))
    ac=input("Enter Account Number:")
    a="select bal from amount where acno=%s"
    data=(ac,)
    c=db.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    total=myresult[0] - am
    sql="update amount set bal=%s where acno=%s"
    d=(total,ac)
    c.execute(sql,d)
    db.commit()
    print('..................................................')
    print("-----------Amount debited successfully------------")
    print('..................................................')
    print('-------------------',am,'-------------------')
    main()


#Defining a function to check balance
def balance():
    ac=input("Enter Account Number:")
    a="select bal from amount where acno= %s"
    data=(ac,)
    c=db.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    print('........................................................')
    print('********************************************************')
    print("Balance For Account number:",ac,"is",myresult[0])
    print('********************************************************')
    print('........................................................')
    main()


#Defining a function to Display Details
def dispacc():
    ac=input("Enter Account Number:")
    a="select * from account where acno=%s"
    data=(ac,)
    c=db.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    for i in myresult:
        print(i, end=" ")
    print('........................................................')
    print('********************************************************')
    print('------------Data Displayed Successfully--------------')
    print('********************************************************')
    print('........................................................')
    main()


#Defining a function to close account
def closeac():
    ac=input("Enter Account Number:")
    sql1="delete from account where acno=%s"
    sql2="delete from amount where acno=%s"
    data=(ac,)
    c=db.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    db.commit()
    print('........................................................')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print("-------------------Account deleted 😀-------------------")
    print('_________Thank you for staying with Atom Bank____________')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('........................................................')
    main()
#Defining a function to update details
def updetail():
    print('---------------------------------')
    print('======Choose what to Update:=====')
    print('---------------------------------')
    print('''
    1.Your Name
    2.Phone number
    3.Address
    4.Date of Birth''')
    choice=input('Enter your choice:')
    if (choice=='1'):
        ac=input('Enter account number:')
        nme=input('Enter Your name:')
        sql1='update account set name=%s where acno=%s'
        sql2='update amount set name=%s where acno=%s'
        c=db.cursor()
        c.execute(sql1,ac)
        c.execute(sql2,ac)
        db.commit()
        print('*******************************')
        print('-------------------------------')
        print('...Data updated successfully...')
        print('-------------------------------')
        print('*******************************')
    elif (choice=='2'):
        ac=input('Enter account number:')
        ph=input('Enter phone number:')
        sql1='update account set phno=%s where acno=%s'
        c=db.cursor()
        c.execute(sql1,ac)
        db.commit()
        print('*******************************')
        print('-------------------------------')
        print('...Data updated successfully...')
        print('-------------------------------')
        print('*******************************')
    elif (choice=='3'):
        ac=input('Enter account number:')
        ad=input('Enter address:')
        sql1='update account set ad=%s where acno=%s'
        c=db.cursor()
        c.execute(sql1,ac)
        db.commit()
        print('*******************************')
        print('-------------------------------')
        print('...Data updated successfully...')
        print('-------------------------------')
        print('*******************************')
    elif (choice=='4'):
        ac=input('Enter account number:')
        dob=input('Enter Date of birth:')
        sql='update account set dob=%s where acno=%s'
        c=db.cursor()
        c.execute(sql,ac)
        db.commit()
        print('*******************************')
        print('-------------------------------')
        print('...Data updated successfully...')
        print('-------------------------------')
        print('*******************************')
    else:
        print('Enter correct choice!!!!')


#starting the page

#Defining the main page
def main():
    print("""
    _________________________________________________________
    _______________________Atom Bank_________________________
    *********************************************************
    Chunar branch                                     0011002
    *********************************************************
    ..........................................................
    ------------------1.OPEN NEW ACCOUNT---------------------
    ..........................................................
    ------------------2.DEPOSIT AMOUNT-----------------------
    ..........................................................
    ------------------3.WITHDRAW MONEY-----------------------
    ..........................................................
    ------------------4.BALANCE ENQUIRY----------------------
    ..........................................................
    ------------------5.DISPLAY CUSTOMER DETAILS-------------
    ..........................................................
    ------------------6.CLOSE AN ACCOUNT---------------------
    ..........................................................
    ------------------7.UPDATE DETAILS-----------------------
    ..........................................................
    **********************************************************
    __________________________________________________________
    """)
    choice=input("Enter Task No.")
    if(choice=="1"):
        openAcc()
    elif(choice=='2'):
        depoAmo()
    elif(choice=='3'):
        witnam()
    elif(choice=='4'):
        balance()
    elif(choice=='5'):
        dispacc()
    elif(choice=='6'):
        closeac()
    elif(choice=='7'):
        updetail()
    else:
        print("......Enter the correct choice😉🤞.....")
        main()


#Creating the login page

import tkinter
from tkinter import Tk
#-------------------------------------------------------------------------------
class Form(tkinter.Frame):

    def __init__(self,parent):

        tkinter.Frame.__init__(self,parent)
        self.parent = parent
        self.initialize_interface()

    def initialize_interface(self):

        self.parent.title("Atom Bank User_Login") # title of the form
        self.parent.config(background="lavender") # background color
        self.parent.geometry("350x150") 
        self.parent.resizable(False,False) 

        global username 
        global password 

        username = tkinter.StringVar() 
        password = tkinter.StringVar() 

        self.labelUser = tkinter.Label(self.parent,text="Username: ", background = "dark slate gray", foreground = "White", font="Arial 8 bold")
        self.labelUser.place(x=25,y=25)

        self.entryUser = tkinter.Entry(self.parent,textvariable=username)
        self.entryUser.place(x=100,y=25)

        self.labelPass = tkinter.Label(self.parent,text="Password: ", background = "dark slate gray", foreground = "White", font="Arial 8 bold")
        self.labelPass.place(x=25,y=50)

        self.entryPass = tkinter.Entry(self.parent,textvariable=password)
        self.entryPass.place(x=100,y=50)

        self.buttonLogin = tkinter.Button(self.parent,text="LOGIN", font = "Arial 8 bold",command=logs)
        self.buttonLogin.place(height=45,width=60 ,x=230,y=25)

def logs():
    mycursor = db.cursor()
    sql = "SELECT * FROM user_login WHERE BINARY username = '%s' AND BINARY password = '%s'" % (username.get(),password.get())

    mycursor.execute(sql)

    if mycursor.fetchone():
         main()
    else:
        print("Invalid Credentials")
    
def log():

    root = tkinter.Tk()
    b= Form(root)
    b.mainloop()
    
if __name__ == "__main__":
    log()




    

    


