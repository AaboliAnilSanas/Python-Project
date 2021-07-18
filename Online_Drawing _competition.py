import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox 
from tkinter import filedialog
from PIL import Image,ImageTk
import os
from io import BytesIO
#Remember
#to create Tk indivisual(screen) so that you can call it anyting and also can destroy when needed
#to create global when it is to be used out of func
#We can create separated things b creating two func and what is needed to be used for all func can be displayed immediately after func
#This is to register participants
def register():
    #global screen1
    root.destroy()
    #screen1 = Toplevel(root)
    screen1=tk.Tk()
    screen1.title("Register")
    screen1.geometry("300x250")
    Name=StringVar()
    Address=StringVar()
    Email=StringVar()
    Contactno=IntVar()
    Age=IntVar()
    State=StringVar()
    Password=StringVar()
    var=StringVar()
    Labelphoto=Label(screen1)
    #This is to destroy register and start login
    def quit1():
      screen1.destroy()
      main_screen()
    #This is to take image from PC and ImageTk pil library to open select directory image and Photoimage to display on Label
    #ImageTk=
    #PhotoImage=
    #os.getcwd()=
    def showimage():
      global fln
      fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=(("JPG File","*.jpg"),("PNG file","*.png"),("All Files","*.*")))
      img=Image.open(fln)
      img.thumbnail((130,390))
      img=ImageTk.PhotoImage(img)
      Labelphoto.config(image=img)
      Labelphoto.image=img
    #This to store register data 
    def database():
     #to convert directory image into binary data so as to store in database 
     def convertToBinaryData(filename):
    #Convert digital data to binary format
      with open(filename, 'rb') as file:
        blobData = file.read()
      return blobData
     try:
       RName=Name.get()
       RAddress=Address.get()
       RGender=var.get()
       REmail=Email.get()
       RContactno=Contactno.get()
       RAge=Age.get()
       RState=State.get()
       RPassword=Password.get()
       #This is to convert number to string so as to use len function 
       c=str(RContactno)
       #Name,Gender,Password,Gmail,Rstate should not be empty so this.....
       if RName=="" or RGender=="" or RPassword=="" or REmail=="" or RState=="":
         messagebox.showinfo("Kindly!Enter Details first")
       #This is check contactno should be 10 len and age should not be 0
       elif len(c)!=10 or RAge==0:
         messagebox.showinfo("INVALID!")
       else:
       # 5 Steps
        #Step 1 To establish Connection with database("Register.db)
        sqliteConnection1 = sqlite3.connect('Register.db')
        cursor = sqliteConnection1.cursor()
        print("Connected to SQLite")
        #Step2 Create Databsae if not exists
        cursor.execute('CREATE TABLE IF NOT EXISTS participants ( RName TEXT,RAddress Text,RGender TEXT,REmail Text,RContactno Text,RAge Text,RState Text,RPassword Text, photo BLOB NOT NULL)')
        #This is to select Input Name with Database name 
        find_user = ('SELECT RName FROM participants WHERE RName = ?')
        c=cursor.execute(find_user,[(RName)])
        #This is to check whether Name Already exists
        if cursor.fetchall():
            messagebox.showerror('Error!','Username Taken Try a Diffrent One.')
        else:
            messagebox.showinfo('Successfully Registered!')
            #Step3 Insert Values
            sqlite_insert_blob_query = 'INSERT INTO participants(RName,RAddress,RGender,REmail,Rcontactno,RAge,RState,RPassword,photo) VALUES(?,?,?,?,?,?,?,?,?)'
            #Calling to convert image into binary and store in database
            empPhoto = convertToBinaryData(fln)
        # Convert data into tuple format=
            data_tuple = (RName,RAddress,RGender,REmail,RContactno, RAge,RState,RPassword,empPhoto)
            #step4 Execute Query
            cursor.execute(sqlite_insert_blob_query, data_tuple)
            #step5 Commit() Save Close
            sqliteConnection1.commit()
            print("Image and file inserted successfully as a BLOB into a table")
            cursor.close()
            readBlobData(Name.get())

     except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
     finally:
        if (sqliteConnection1):
            sqliteConnection1.close()
            print("the sqlite connection is closed")
    #This to Show Labels buttons on Tk screen1
    def reg():
      Labelreg=Label(screen1,text="Registration Form ",bg="Red",width=21,height=2)
      Labelname=Label(screen1,text="Enter  Name  :",bg="lightgreen",width=15)
      entryname=Entry(screen1,textvar=Name)
      Labeladdress=Label(screen1,text="Enter  Address  :",bg="lightgreen",width=15)
      entryaddress=Entry(screen1,textvar=Address)
      Labelgender=Label(screen1,text="Gender  :",bg="lightgreen",width=15)
      radiobuttonm=Radiobutton(screen1,text="Male",variable=var,value="Male")
      radiobuttonf=Radiobutton(screen1,text="Female",variable=var,value="Female")
      Labelemail=Label(screen1,text="Enter  Email  :",bg="lightgreen",width=15)
      entryemail=Entry(screen1,textvar=Email)
      Labelcontactno=Label(screen1,text="Enter  Contactno  :",bg="lightgreen",width=15)
      entrycontactno=Entry(screen1,textvar=Contactno)
      Labelage=Label(screen1,text="Enter  Age  :",bg="lightgreen",width=15)
      entryage=Entry(screen1,textvar=Age)
      Labelstate=Label(screen1,text="Enter  State  :",bg="lightgreen",width=15)
      entrystate=Entry(screen1,textvar=State)
      Labelpassword=Label(screen1,text="Enter  Password  :",bg="lightgreen",width=15)
      entrypassword=Entry(screen1,textvar=Password)
      LabelRdraw=Label(screen1,text="***Welcome to drawing Competition***",font=("",10,"bold"))
      LabelRdraw.place(x=403,y=10)
      buttonRregister=Button(screen1,text="Submit",bg="lightgreen",width=10,command=database)
      buttonRregister.place(x=453,y=615)
      buttonRlogin=Button(screen1,text="Login",bg="lightgreen",width=10,command=quit1)
      buttonRlogin.place(x=560,y=615)
      buttonupload=Button(screen1,text="Upload",bg="lightgreen",width=10,command=showimage)
      buttonupload.place(x=490,y=250)
      #Default image where user is going to upload his
      photo='C:/Users/ACER/Desktop/loginp.jpg'
      img=Image.open(photo)
      #This is to change size of image
      img.thumbnail((130,375))
      img=ImageTk.PhotoImage(img)
      Labelphoto.config(image=img)
      Labelphoto.image=img
      Labelphoto.place(x=464,y=80)
      Labelreg.place(x=454,y=30)
      Labelname.place(x=410,y=290)
      entryname.place(x=530,y=290)
      Labeladdress.place(x=410,y=330)
      entryaddress.place(x=530,y=330) 
      Labelgender.place(x=410,y=370)
      radiobuttonm.place(x=530,y=370)
      radiobuttonf.place(x=590,y=370)
      Labelemail.place(x=410,y=410)
      entryemail.place(x=530,y=410)
      Labelcontactno.place(x=410,y=450)
      entrycontactno.place(x=530,y=450)
      Labelage.place(x=410,y=490)
      entryage.place(x=530,y=490)
      Labelstate.place(x=410,y=530)
      entrystate.place(x=530,y=530)
      Labelpassword.place(x=410,y=570)
      entrypassword.place(x=530,y=570)
      screen1.mainloop()
    def writeTofile(data, filename):
# Convert binary data to proper format and write it on Hard Disk
     with open(filename, 'wb') as file:
        file.write(data)
     print("Stored blob data into: ", filename, "\n")
    def readBlobData(RName):
     try:
        sqliteConnection1 = sqlite3.connect('Register.db')
        cursor = sqliteConnection1.cursor()
        print("Connected to SQLite")
        sql_fetch_blob_query = """SELECT * from participants where RName = ?"""
        cursor.execute(sql_fetch_blob_query,[Name.get()])
        record = cursor.fetchall()
        #print( sql_fetch_blob_query)
        print(cursor.execute)
        for row in record:
            print("RName = ", row[0])
            name  = row[0]
            photo = row[8]
            print("Storing  image  on disk \n")
            photoPath = "C:/Users/ACER/Desktop/App Aaboli/Projects/Participants/" + name+ ".png"
            writeTofile(photo, photoPath)
            cursor.close()

     except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
     finally:
       if (sqliteConnection1):
            sqliteConnection1.close()
            print("sqlite connection is closed")
    reg()
#This is login what should be displayed when Program Start
def main_screen():
  #This is to destroy login,profile,rule func
  def quit1():
      #Here if select==1 means login func tk is active and if clicked on Home Button then destroy itself and default log login pg should appear
      #if select==2 means Profile tk pg is active destroy it when clicked on Home button
      #Similarly Rule tk is destroyed
         if(select==1):
            a.destroy()
         if(select==2):
            p.destroy()
         if(select==7):
           print("hii")
           d.destroy()
         if(select==5):
           print("hii")
           ad.destroy()
         if(select==8):
           print("hii")
           rootvo.destroy()
         if(select==3):
           root12.destroy()
      #This is to cal login pg    
         log()
  #This is to show active tk means select ==2 then destroy rule and login upload  tk simarly for others
  def quit2():
            if(select==3):
              print(destroy1)
              if(destroy1==2):
               print(destroy1)
               p.destroy()
              elif(destroy1==8):
               rootvo.destroy()
              elif(destroy1==7):
               d.destroy()
              elif(destroy1==5):
               ad.destroy()
              else:
               a.destroy()
            if(select==2):
              if(destroy1==3):
               root12.destroy()
              elif(destroy1==8):
               rootvo.destroy()
              elif(destroy1==7):
               d.destroy()
              elif(destroy1==5):
               ad.destroy()
              else:
                a.destroy()
            if(select==5):
              if(destroy1==2):
               print(destroy1)
               p.destroy()
              elif(destroy1==3):
               root12.destroy()
              elif(destroy1==8):
               rootvo.destroy()
              elif(destroy1==7):
               d.destroy()
              else:
                a.destroy()
            if(select==7):
              print(destroy1)
              if(destroy1==2):
               print(destroy1)
               p.destroy()
              elif(destroy1==5):
               ad.destroy()
              elif(destroy1==3):
               root12.destroy()
              elif(destroy1==8):
               rootvo.destroy()
              else:
                a.destroy()
            if(select==8):
              if(destroy1==2):
               print(destroy1)
               p.destroy()
              elif(destroy1==5):
               ad.destroy()
              elif(destroy1==7):
               d.destroy()
              elif(destroy1==3):
               root12.destroy()
              else:
               a.destroy()
            
               
  def home():
          if(select==2):
             p.destroy()
             login()
          if(select==3):
             root12.destroy()
             login()
          if(select==1):
             a.destroy()
             login()
          if(select==5):
             ad.destroy()
             login()

          if(select==7):
             d.destroy()
             login()
          if(select==8):
             rootvo.destroy()
             login()

  #This is to show database stored details about logined person       
  def profile():
            global select
            global p
            global destroy1
            select=2
            quit2()
            p=tk.Tk()
            p.geometry("300x250")
            destroy1=2
            print(destroy1)
            Dlabel1=Label(p,text="",bg="lightgreen",height=40,width=41)
            Dlabel1.place(x=440,y=72)
            poo='C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participants/'+name+'.png'
            img1=Image.open(poo)
            img1.thumbnail((130,370))
            img1=ImageTk.PhotoImage(img1)
            LabelDPhoto=Label(p,image=img1)
            LabelDPhoto.image=img1
            LabelDPhoto.place(x=514,y=79)
            Dlabel=Label(p,text="",bg="lightgreen",height=13,width=12)
            Dlabel.place(x=0,y=5)
            Dhome=Button(p,text="Home",width=10,height=2,command=home)
            Dhome.place(x=0,y=10)
            Dlogin=Button(p,text="Login",width=10,height=2,command=quit1)
            Dlogin.place(x=0,y=60)
            Dprofile=Button(p,text="Profile",command=profile,width=10,height=2)
            Dprofile.place(x=0,y=110)
            Drule=Button(p,text="Rules",width=10,height=2,command=Rule)
            Drule.place(x=0,y=160)
            LabelDName=Label(p,text="***Welcome"+" "+name+"***",bg="lightpink",height=2,width=20)
            LabelDName.place(x=505,y=14)
            LabelPname=Label(p,text="Full Name  :  ",height=2,width=13)
            LabelPname.place(x=463,y=220)
            LabelEname=Label(p,text= name,height=2,width=20)
            LabelEname.place(x=570,y=220)
            LabelPaddress=Label(p,text="Address  :  " ,height=2,width=13)
            LabelEaddress=Label(p,text=address,height=2,width=20)
            LabelEaddress.place(x=570,y=270)
            LabelPaddress.place(x=463,y=270)
            LabelPgender=Label(p,text="Gender   :  " ,height=2,width=13)
            LabelPgender.place(x=463,y=320)
            LabelEgender=Label(p,text=gender,height=2,width=20)
            LabelEgender.place(x=570,y=320)
            LabelPgmail=Label(p,text="Gmail  :  " ,height=2,width=13)
            LabelEgmail=Label(p,text=gmail,height=2,width=20)
            LabelEgmail.place(x=570,y=370)
            LabelPgmail.place(x=463,y=370)
            LabelPcontact=Label(p,text="Contactno : " ,height=2,width=13)
            LabelEcontact=Label(p,text=contactno,height=2,width=20)
            LabelEcontact.place(x=570,y=420)
            LabelPcontact.place(x=463,y=420)
            LabelPage=Label(p,text="Age  :  " ,height=2,width=13)
            LabelEage=Label(p,text=age,height=2,width=20)
            LabelEage.place(x=570,y=470)
            LabelPage.place(x=463,y=470)
            LabelPstate=Label(p,text="State : ",height=2,width=13)
            LabelEstate=Label(p,text=state,height=2,width=20)
            LabelEstate.place(x=570,y=520)
            LabelPstate.place(x=463,y=520)
            LabelPpassword=Label(p,text="Password :  ",height=2,width=13)
            LabelEpassword=Label(p,text=password,height=2,width=20)
            LabelEpassword.place(x=570,y=570)
            LabelPpassword.place(x=463,y=570)
            p.mainloop()
  #This is to show just intersection
  def Rule():
            global root12
            root12=tk.Tk()
            root12.geometry('800x800')
            root12.title("Registration Form")
            global destroy1
            global select
            select=3
            quit2()
            destroy1=3
            print(destroy1)
            Dlabel=Label(root12,text="",bg="lightgreen",height=13,width=12)
            Dlabel.place(x=0,y=5)
            Dhome=Button(root12,text="Home",width=10,height=2,command=home)
            Dhome.place(x=0,y=10)
            Dlogin=Button(root12,text="Login",width=10,height=2,command=quit1)
            Dlogin.place(x=0,y=60)
            Dprofile=Button(root12,text="Profile",command=profile,width=10,height=2)
            Dprofile.place(x=0,y=110)
            Drule=Button(root12,text="Rules",width=10,height=2,command=Rule)
            Drule.place(x=0,y=160)
            DRlabel=Label(root12,text="",bg="lightgreen",height=30,width=68)
            DRlabel.place(x=280,y=70)
            LabellRdraw=Label(root12,text="***Welcome to drawing Competition***",font=("",13,"bold"))
            LabellRdraw.place(x=373,y=90)
            Label1=Label(root12,text="This is a Drawing Competition......              ",font=("",10,""),height=2,width=35)
            Label2=Label(root12,text="You can upload your Drawing........              ",font=("",10,""),height=2,width=35)
            Label3=Label(root12,text=" Remember you can upload once ,you can't change it... ",font=("",10,""),height=2,width=43)
            Label4=Label(root12,text="Any Topic is accepted!!......                    ",font=("",10,""),height=2,width=35)
            Label5=Label(root12,text="All the best!! Show your creativity...           ",font=("",10,""),height=2,width=35)
            Label1.place(x=388,y=200)
            Label2.place(x=388,y=250)
            Label3.place(x=358,y=300)
            Label4.place(x=388,y=350)
            Label5.place(x=388,y=400)
  
  def pr1():
            global select
            global ad
            global poo
            global destroy1
            select=5
            quit2()
            ad=tk.Tk()
            ad.geometry("300x250")
            global LabelEname
            destroy1=5
            print(destroy1)
            global LabelEpassword
            global name12
            global password12
            name12=StringVar()
            password12=StringVar()
            def save():
                  global destroy1
                  destroy1=2
                  sqliteConnection1 = sqlite3.connect('Admin.db')
                  cursor = sqliteConnection1.cursor()
                  cursor.execute('CREATE TABLE IF NOT EXISTS admin(RName TEXT,RPassword TEXT,no TEXT)')
                  find_user=('Select RName,RPassword from admin WHERE RName= ? and RPassword= ?')
                  cursor.execute(find_user,[(LName.get()),(LPassword.get())])
                  result=cursor.fetchall()
                  print("result")
                  print(result)
                  print("name12")
                  print(name12.get())
                  print("password12")
                  print(password12.get())
                  print("Lname")
                  print(LName.get())
                  print("Lpassword")
                  print(LPassword.get())
                  for row in result:
                      global RName
                      global RPassword
                      RName=row[0]
                      RPassword=row[1]
                  print("RName")
                  print(RName)
                  print("RPassword")
                  print(RPassword)
                  find_user=('UPDATE admin SET RName= ?,RPassword= ?  WHERE RName= ? and RPassword= ?')
                  cursor.execute(find_user,[(name12.get()),(password12.get()),(LName.get()),(LPassword.get())])
                  record=cursor.fetchall()
                  print("record")
                  print(record)
                  sqliteConnection1.commit()
                  sqliteConnection1.close()
                  messagebox.showinfo("Done                   !!")
                  messagebox.showinfo("Login again            !!")
                  
            def edit():
                  LabelEname.destroy()
                  LabelEpassword.destroy()
                  LabelEname1=Entry(ad,textvar=name12)
                  LabelEpassword1=Entry(ad,textvar=password12)
                  LabelEname1.place(x=550,y=260)
                  LabelEpassword1.place(x=550,y=320)
                  buttone=Button(ad,text="Save",bg="red",width=10,height=1,command=save)
                  buttone.place(x=505,y=400)
              
            DRlabel=Label(ad,text="",bg="lightgreen",height=29,width=49)
            DRlabel.place(x=380,y=20)
            poo='C:/Users/ACER/Desktop/loginp.jpg'
            img1=Image.open(poo)
            img1.thumbnail((130,370))
            img1=ImageTk.PhotoImage(img1)
            LabelDPhoto=Label(ad,image=img1)
            LabelDPhoto.image=img1
            LabelDPhoto.place(x=480,y=79)
            Dlabel=Label(ad,text="",bg="lightgreen",height=17,width=12)
            Dlabel.place(x=0,y=5)
            Dhome=Button(ad,text="Home",width=10,height=2,command=home)
            Dhome.place(x=0,y=10)
            Dlogin=Button(ad,text="Login",width=10,height=2,command=quit1)
            Dlogin.place(x=0,y=60)
            Dprofile=Button(ad,text="Profile",width=10,height=2,command=pr1)
            Dprofile.place(x=0,y=110)
            Ddraw=Button(ad,text="Drawings",width=10,height=2,command=drawings)
            Ddraw.place(x=0,y=160)
            with sqlite3.connect('Register.db')as db:
              cursor=db.cursor()
            find_user=('Select Count(RName) from participants ')
            cursor.execute(find_user)
            record=cursor.fetchall()
            for row in record:
                    record1=row[0]
                    print("helllllo")
                    print(record1)
            db.close()
            sqliteConnection1 = sqlite3.connect('Admin.db')
            cursor = sqliteConnection1.cursor()
            cursor.execute('CREATE TABLE IF NOT EXISTS admin(RName TEXT,RPassword TEXT,no TEXT)')
            find_user=('Select no from admin ')
            cursor.execute(find_user)
            result=cursor.fetchall()
            for row in result:
                    no_of_participants=row[0]
            print("Helll participants")
            print(no_of_participants)
            cursor.close()
            aa=type(no_of_participants)
            cc=int(no_of_participants)
            bb=type(record1)
            print(aa)
            print(bb)
            print(type(cc))
            if (record1==int(no_of_participants)):
              DVoting=Button(ad,text="Voting",width=10,height=2,command=drawingsv)
            else:
              DVoting=Button(ad,text="Voting",width=10,height=2,state='disabled')  
            DVoting.place(x=0,y=210)
            LabellRdraw=Label(ad,text="***Welcome to drawing Competition***",font=("",13,"bold"))
            LabellRdraw.place(x=400,y=30)
            LabelPname=Label(ad,text="Full Name  :  ",height=2,width=14)
            LabelPname.place(x=428,y=260)
            LabelEname=Label(ad,text= name1,height=2,width=18)
            LabelEname.place(x=550,y=260)
            LabelPpassword=Label(ad,text="Password :  ",height=2,width=14)
            LabelEpassword=Label(ad,text=password1,height=2,width=18)
            LabelEpassword.place(x=550,y=320)
            LabelPpassword.place(x=428,y=320)
            buttone=Button(ad,text="Edit",bg="red",width=10,height=1,command=edit)
            buttone.place(x=505,y=400)
            ad.mainloop()
  #This is to show just intersection

  def drawings():
              global select
              global destroy1
              select=7
              quit2()
              global d
              d=tk.Tk()
              d.geometry('800x800')
              d.title("Registration Form")
              destroy1=7
              global n
              global photo
              global items_list 
              def resize_image(d,copy_of_image,label1):
                 new_height=500
                 new_width=600
                 image=copy_of_image.resize((new_width,new_height))
                 photo=ImageTk.PhotoImage(image)
                 label1.configure(image=photo)
                 label1.image=photo
                 label1.place(x=250,y=70)
              def prev():
                 global n
                 global items_list
                 global img1
                 n=n-1
                 img1=items_list[n]
                 print(img1)
                 image=Image.open('C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/'+img1)
                 copy_of_image=image.copy()
                 photo=ImageTk.PhotoImage(image)
                 label=Label(d,image=photo)
                 #b3=Button(d,text="Vote",width=10,height=2,bg='lightpink')
                 #b3.place(x=513,y=580)
                 label.bind('<configure>',resize_image(d,copy_of_image,label1))
    
              def next1():
                 global n
                 global items_list
                 global img1

                 n=n+1
                 img1=items_list[n]
                 print(img1)
                 print(items_list)
                 image=Image.open('C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/'+img1)
                 copy_of_image=image.copy()
                 photo=ImageTk.PhotoImage(image)
                 label=Label(d,image=photo)
                 #b3=Button(d,text="Vote",width=10,height=2,bg='lightpink')
                 #b3.place(x=513,y=580)
                 label.bind('<configure>',resize_image(d,copy_of_image,label1))
              n=0
              Dlabel=Label(d,text="",bg="lightgreen",height=17,width=12)
              Dlabel.place(x=0,y=5)
              Dhome=Button(d,text="Home",width=10,height=2,command=home)
              Dhome.place(x=0,y=10)
              Dlogin=Button(d,text="Login",width=10,height=2,command=quit1)
              Dlogin.place(x=0,y=60)
              Dprofile=Button(d,text="Profile",width=10,height=2,command=pr1)
              Dprofile.place(x=0,y=110)
              Ddraw=Button(d,text="Drawings",width=10,height=2,command=drawings)
              Ddraw.place(x=0,y=160)
              with sqlite3.connect('Register.db')as db:
                cursor=db.cursor()
              find_user=('Select Count(RName) from participants ')
              cursor.execute(find_user)
              record=cursor.fetchall()
              for row in record:
                    record1=row[0]
                    print("helllllo")
                    print(record1)
              db.close()
              sqliteConnection1 = sqlite3.connect('Admin.db')
              cursor = sqliteConnection1.cursor()
              cursor.execute('CREATE TABLE IF NOT EXISTS admin(RName TEXT,RPassword TEXT,no TEXT)')
              find_user=('Select no from admin ')
              cursor.execute(find_user)
              result=cursor.fetchall()
              for row in result:
                    no_of_participants=row[0]
              print("Helll participants")
              print(no_of_participants)
              cursor.close()
              aa=type(no_of_participants)
              cc=int(no_of_participants)
              bb=type(record1)
              print(aa)
              print(bb)
              print(type(cc))
              if (record1==int(no_of_participants)):
                DVoting=Button(d,text="Voting",width=10,height=2,command=drawingsv)
              else:
                DVoting=Button(d,text="Voting",width=10,height=2,state='disabled')  
              DVoting.place(x=0,y=210)
              LabelDName=Label(d,text="***Welcome"+" "+name1+"***",bg="lightpink",height=2,width=20)
              LabelDName.place(x=497,y=14)
              items_list=os.listdir('C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/')
              img1=items_list[n]
              print(img1)
              #b3=Button(d,text="Vote",width=10,height=2,bg='lightpink')
              #b3.place(x=513,y=580)
              image=Image.open('C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/'+img1)
              copy_of_image=image.copy()
              photo=ImageTk.PhotoImage(image)
              label1=Label(d,image=photo)
              label1.bind('<configure>',resize_image(d,copy_of_image,label1))
              label1.place(x=250,y=70)
              b1=Button(d,text=">>",width=4,height=10,command=next1,bg='lightblue')
              b1.place(x=856,y=238)
              b2=Button(d,text="<<",width=4,height=10,command=prev,bg='lightblue')
              b2.place(x=207,y=238)
              d.mainloop()
              #cursor.close()
  def drawingsv():
              global select
              select=8
              quit2()
              global rootvo
              rootvo=tk.Tk()
              rootvo.geometry('800x800')
              rootvo.title("Registration Form")
              global destroy1
              destroy1=8
              global n
              global items_list
              global image
              Dlabel=Label(rootvo,text="",bg="lightgreen",height=17,width=12)
              Dlabel.place(x=0,y=5)
              Dhome=Button(rootvo,text="Home",width=10,height=2,command=home)
              Dhome.place(x=0,y=10)
              Dlogin=Button(rootvo,text="Login",width=10,height=2,command=quit1)
              Dlogin.place(x=0,y=60)
              Dprofile=Button(rootvo,text="Profile",width=10,height=2,command=pr1)
              Dprofile.place(x=0,y=110)
              Ddraw=Button(rootvo,text="Drawings",width=10,height=2,command=drawings)
              Ddraw.place(x=0,y=160)
              with sqlite3.connect('Register.db')as db:
                 cursor=db.cursor()
              find_user=('Select Count(RName) from participants ')
              cursor.execute(find_user)
              record=cursor.fetchall()
              for row in record:
                    record1=row[0]
                    print("helllllo")
                    print(record1)
              db.close()
              sqliteConnection1 = sqlite3.connect('Admin.db')
              cursor = sqliteConnection1.cursor()
              cursor.execute('CREATE TABLE IF NOT EXISTS admin(RName TEXT,RPassword TEXT,no TEXT)')
              find_user=('Select no from admin ')
              cursor.execute(find_user)
              result=cursor.fetchall()
              for row in result:
                    no_of_participants=row[0]
              print("Helll participants")
              print(no_of_participants)
              cursor.close()
              aa=type(no_of_participants)
              cc=int(no_of_participants)
              bb=type(record1)
              print(aa)
              print(bb)
              print(type(cc))
              if (record1==int(no_of_participants)):
                DVoting=Button(rootvo,text="Voting",width=10,height=2,command=drawingsv)
              else:
                DVoting=Button(rootvo,text="Voting",width=10,height=2,state='disabled')  
              DVoting.place(x=0,y=210)
              LabelDName=Label(rootvo,text="***Welcome"+" "+ name1+"***",bg="lightpink",height=2,width=20)
              LabelDName.place(x=497,y=14)
              def resize_image(rootvo,copy_of_image,label1):
                 new_height=500
                 new_width=600
                 image=copy_of_image.resize((new_width,new_height))
                 photo=ImageTk.PhotoImage(image)
                 label1.configure(image=photo)
                 label1.image=photo
                 label1.place(x=250,y=70)
              def vote():
                 sqliteConnection12 = sqlite3.connect('Voting.db')
                 cursor = sqliteConnection12.cursor()
                 print("Connected to SQLite")
                 RName=LName.get()
                 print(RName)
                 Vote=img1
                 print(vote)
                 cursor.execute('CREATE TABLE IF NOT EXISTS voting ( RName TEXT,Vote TEXT)')
                 find_user=('Select * from voting Where RName = ?')
                 cursor.execute(find_user,[LName.get()])
                 record=cursor.fetchall()
                 print(record)
                 if record:
                  messagebox.showerror("Already Voted!             ")
                  messagebox.showerror("Wait for Result!              ")
                 else:
           #This is to check where logined name has uploaded image or not
                  sqlite_insert_blob_query = """ INSERT INTO voting (RName,Vote) VALUES(?,?)"""
                  data_tuple = (RName,Vote)
                  cursor.execute(sqlite_insert_blob_query, data_tuple)
                  messagebox.showinfo(img1+ " voted                        ")
                  sqliteConnection12.commit()
                  cursor.close()
              def prev():
                 global n
                 global items_list
                 global img1
                 n=n-1
                 img1=items_list[n]
                 print(img1)
                 image=Image.open('C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/'+img1)
                 copy_of_image=image.copy()
                 photo=ImageTk.PhotoImage(image)
                 label=Label(rootvo,image=photo)
                 b3=Button(rootvo,text="Vote",width=10,height=2,bg='lightpink',command=vote)
                 b3.place(x=513,y=580)
                 label.bind('<configure>',resize_image(rootvo,copy_of_image,label1))
    
              def next1():
                 global n
                 global items_list
                 global img1

                 n=n+1
                 img1=items_list[n]
                 print(img1)
                 print(items_list)
                 image=Image.open('C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/'+img1)
                 copy_of_image=image.copy()
                 photo=ImageTk.PhotoImage(image)
                 label=Label(rootvo,image=photo)
                 b3=Button(rootvo,text="Vote",width=10,height=2,bg='lightpink',command=vote)
                 b3.place(x=513,y=580)
                 label.bind('<configure>',resize_image(rootvo,copy_of_image,label1))
              global img1
              global items_list
              global image
              global photo
              n=0
              items_list=os.listdir('C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/')
              img1=items_list[n]
              print(img1)
              b3=Button(rootvo,text="Vote",width=10,height=2,bg='lightpink',command=vote)
              b3.place(x=513,y=580)
              image=Image.open('C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/'+img1)
              copy_of_image=image.copy()
              photo=ImageTk.PhotoImage(image)
              label1=Label(rootvo,image=photo)
              label1.bind('<configure>',resize_image(rootvo,copy_of_image,label1))
              label1.place(x=250,y=70)
              b1=Button(rootvo,text=">>",width=4,height=10,command=next1,bg='lightblue')
              b1.place(x=856,y=238)
              b2=Button(rootvo,text="<<",width=4,height=10,command=prev,bg='lightblue')
              b2.place(x=207,y=238)
              rootvo.mainloop()
              cursor.close()
  def writeTofile(data, filename):
# Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)
    print("Stored blob data into: ", filename, "\n")
  #This is to check where Name and password exists if exists then upload tk with Home,Profile,Rule and upload drawing for drawing competition

  def login():
    global selectroot
    global inserted
    global select
    global destroy1
    global no_of_participants
    no_of_participants=8
    inserted=0
    if(selectroot==1):
            print(selectroot)
            root.destroy()
            selectroot=0
    select=1
    quit2()
    destroy1=1
    def logadmin():
               global a
               a= tk.Tk()
               a.geometry("400x400")
               #This is to update change add the no of participants to be allowedfor competitions by admin
               def no():
                  global buttonsa
                  global no_of_participants
                  global no
                  #This is to get the entry field of "enter the no of participants" in homepg
                  no_of_participants=No.get()
                  sqliteConnection1 = sqlite3.connect('Admin.db')
                  cursor = sqliteConnection1.cursor()
                  cursor.execute('CREATE TABLE IF NOT EXISTS admin(RName TEXT,RPassword TEXT,no TEXT)')
                  find_user=('Select no from admin where RName=? and RPassword=?')
                  cursor.execute(find_user,[(LName.get()),(LPassword.get())])
                  result=cursor.fetchall()
                  print(result)
                  no=result[0]
                  print(no)
                  #This to update the no if admin want
                  find_user=('UPDATE admin SET no= ?  WHERE RName= ? and RPassword= ?')
                  cursor.execute(find_user,[(No.get()),(LName.get()),(LPassword.get())])
                  record=cursor.fetchall()
                  print(record)
                  sqliteConnection1.commit()
                  sqliteConnection1.close()
                  Buttons.configure(state="disabled")
               def change():
                  Buttons.configure(state="normal",command=no)
                  
               No=IntVar()
               Dlabel=Label(a,text="",bg="lightgreen",height=17,width=12)
               Dlabel.place(x=0,y=5)
               Dhome=Button(a,text="Home",width=10,height=2,command=home)
               Dhome.place(x=0,y=10)
               Dlogin=Button(a,text="Login",width=10,height=2,command=quit1)
               Dlogin.place(x=0,y=60)
               Dprofile=Button(a,text="Profile",width=10,height=2,command=pr1)
               Dprofile.place(x=0,y=110)
               Ddraw=Button(a,text="Drawings",width=10,height=2,command=drawings)
               Ddraw.place(x=0,y=160)
               with sqlite3.connect('Register.db')as db:
                 cursor=db.cursor()
               find_user=('Select Count(RName) from participants ')
               cursor.execute(find_user)
               record=cursor.fetchall()
               for row in record:
                    record1=row[0]
                    print("helllllo")
                    print(record1)
               db.close()
               sqliteConnection1 = sqlite3.connect('Admin.db')
               cursor = sqliteConnection1.cursor()
               cursor.execute('CREATE TABLE IF NOT EXISTS admin(RName TEXT,RPassword TEXT,no TEXT)')
               find_user=('Select no from admin ')
               cursor.execute(find_user)
               result=cursor.fetchall()
               for row in result:
                    no_of_participants=row[0]
               print("Helll participants")
               print(no_of_participants)
               cursor.close()
               aa=type(no_of_participants)
               cc=int(no_of_participants)
               bb=type(record1)
               print(aa)
               print(bb)
               print(type(cc))
               if (record1==int(no_of_participants)):
                 DVoting=Button(a,text="Voting",width=10,height=2,command=drawingsv)
                 DVoting.place(x=0,y=210)
               else:
                
                 DVoting=Button(a,text="Voting",width=10,height=2)
                 DVoting.config(state='disabled')
                 DVoting.place(x=0,y=210)
               DRlabel=Label(a,text="",bg="lightgreen",height=31,width=72)
               DRlabel.place(x=280,y=20)
               LabellRdraw=Label(a,text="***Welcome to drawing Competition***",font=("",13,"bold"))
               LabellRdraw.place(x=375,y=30)
               Label1=Label(a,text=" This is a Drawing Competition........",font=("",10,""),height=2,width=51)
               Label2=Label(a,text=" Hurahh! You are admin so you will have some extra features........    ",font=("",10,""),height=2,width=51)
               Label3=Label(a,text=" Also you can edit your already given Username and Password by us.... ",font=("",10,""),height=2,width=51)
               Label4=Label(a,text="  You can aslo increase the Number of Participants ......     ",font=("",10,""),height=2,width=51)
               Label5=Label(a,text=" You can see uploaded drawing also . You don't have to wait till voting!!...",font=("",10,""),height=2,width=51)
               Label6=Label(a,text=" Butt.. You can also vote for one drawing only!........",font=("",10,""),height=2,width=51)
               Label7=Label(a,text=" Hope!You have a great time...",font=("",10,""),height=2,width=51)
               DRlabel=Label(a,text="",bg="lightpink",height=8,width=72)
               DRlabel.place(x=280,y=470)
               Label8=Label(a,text="Enter the number of participants :",font=("",10,""))
               Entry1=Entry(a,textvar=No)
               if(buttonsa==0):
                 global buttons
                 Buttons=Button(a,text="Start Competition",width=13,height=1,command=no)
                 Buttons.place(x=440,y=540)
               else:
                 Buttons=Button(a,text="Start Competition",width=13,height=1,state='disabled')
                 Buttons.place(x=440,y=540)
               label9=Label(a,text="No of participants you decided"+"  "+no1,bg="lightpink")
               label9.place(x=438,y=475)
               Buttonc=Button(a,text=" Change ",width=13,height=1,command=change)
               Label1.place(x=330,y=80)
               Label2.place(x=330,y=140)
               Label3.place(x=330,y=200)
               Label4.place(x=330,y=260)
               Label5.place(x=330,y=320)
               Label6.place(x=330,y=380)
               Label7.place(x=330,y=440)
               Label8.place(x=342,y=500)
               Entry1.place(x=548,y=500)
            #Buttons.place(x=440,y=540)
               Buttonc.place(x=545,y=540)
    def vote1():
              global a
              a= tk.Tk()
              a.geometry("400x400")
              global n
              global items_list
              Dlabel=Label(a,text="",bg="lightgreen",height=13,width=12)
              Dlabel.place(x=0,y=5)
              Dhome=Button(a,text="Home",width=10,height=2,command=home)
              Dhome.place(x=0,y=10)
              Dlogin=Button(a,text="Login",width=10,height=2,command=quit1)
              Dlogin.place(x=0,y=60)
              Dprofile=Button(a,text="Profile",width=10,height=2,command=profile)
              Dprofile.place(x=0,y=110)
              Drule=Button(a,text="Rules",width=10,height=2,command=Rule)
              Drule.place(x=0,y=160)
              LabelDName=Label(a,text="***Welcome"+name+"***",bg="lightpink",height=1,width=20)
              LabelDName.place(x=497,y=14)
              LabelDName=Label(a,text="***Sorry !! "+" "+name+" only first "+" "+ no123+ " participants are accepted"+"***",bg="lightpink",height=1,width=80)
              LabelDName.place(x=278,y=42)
              def resize_image(a,copy_of_image,label1):
                 new_height=500
                 new_width=600
                 image=copy_of_image.resize((new_width,new_height))
                 photo=ImageTk.PhotoImage(image)
                 label1.configure(image=photo)
                 label1.image=photo
                 label1.place(x=250,y=70)
              def vote():
                 sqliteConnection12 = sqlite3.connect('Voting.db')
                 cursor = sqliteConnection12.cursor()
                 print("Connected to SQLite")
                 RName=LName.get()
                 print(RName)
                 Vote=img1
                 print(vote)
                 cursor.execute('CREATE TABLE IF NOT EXISTS voting ( RName TEXT,Vote TEXT)')
                 find_user=('Select * from voting Where RName = ?')
                 cursor.execute(find_user,[LName.get()])
                 record=cursor.fetchall()
                 print(record)
                 if record:
                  messagebox.showerror("Already Voted!             ")
                  messagebox.showerror("Wait for Result!              ")
                 else:
           #This is to check where logined name has uploaded image or not
                  sqlite_insert_blob_query = """ INSERT INTO voting (RName,Vote) VALUES(?,?)"""
                  data_tuple = (RName,Vote)
                  cursor.execute(sqlite_insert_blob_query, data_tuple)
                  messagebox.showinfo(img1+ " voted                        ")
                  sqliteConnection12.commit()
                  sqliteConnection12.close()
              def prev():
                 global n
                 global items_list
                 global img1
                 n=n-1
                 img1=items_list[n]
                 print(img1)
                 image=Image.open('C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/'+img1)
                 copy_of_image=image.copy()
                 photo=ImageTk.PhotoImage(image)
                 label=Label(v,image=photo)
                 b3=Button(a,text="Vote",width=10,height=2,bg='lightpink',command=vote)
                 b3.place(x=513,y=580)
                 label.bind('<configure>',resize_image(a,copy_of_image,label1))
    
              def next1():
                 global n
                 global items_list
                 global img1

                 n=n+1
                 img1=items_list[n]
                 print(img1)
                 print(items_list)
                 image=Image.open('C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/'+img1)
                 copy_of_image=image.copy()
                 photo=ImageTk.PhotoImage(image)
                 label=Label(a,image=photo)
                 b3=Button(a,text="Vote",width=10,height=2,bg='lightpink',command=vote)
                 b3.place(x=513,y=580)
                 label.bind('<configure>',resize_image(a,copy_of_image,label1))
              n=0
              items_list=os.listdir('C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/')
              img1=items_list[n]
              print(img1)
              b3=Button(a,text="Vote",width=10,height=2,bg='lightpink',command=vote)
              b3.place(x=513,y=580)
              image=Image.open('C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/'+img1)
              copy_of_image=image.copy()
              photo=ImageTk.PhotoImage(image)
              label1=Label(a,image=photo)
              label1.bind('<configure>',resize_image(a,copy_of_image,label1))
              label1.place(x=260,y=70)
              b1=Button(a,text=">>",width=4,height=10,command=next1,bg='lightblue')
              b1.place(x=873,y=238)
              b2=Button(a,text="<<",width=4,height=10,command=prev,bg='lightblue')
              b2.place(x=207,y=238)
              a.mainloop()
    def drawinginserted():
                def showp():
                 global inserted
                 sqliteConnection12 = sqlite3.connect('Drawing.db')
                 cursor = sqliteConnection12.cursor()
                 print("Connected to SQLite")
                 RName=LName.get()
                 print(RName)
                 cursor.execute('CREATE TABLE IF NOT EXISTS drawing ( RName TEXT,photo BLOB NOT NULL)')
                 #This is to check where logined name has uploaded image or not
                 find_user=('Select * from drawing Where RName = ?')
                 cursor.execute(find_user,[LName.get()])
                 record=cursor.fetchall()
                 if record:
                  inserted=1
                  name=LName.get()
                  p='C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/'+name+'.png'
                  img1=Image.open(p)
                  img1.thumbnail((660,580))
                  img1=ImageTk.PhotoImage(img1)
                  LabelDPhoto=Label(a,image=img1)
                  LabelDPhoto.image=img1
                  LabelDPhoto.place(x=230,y=79)
                  cursor.close()
                global a
                a=tk.Tk()
                a.geometry("300x250")
                showp()
                def convertToBinaryData(filename):
     #Convert digital data to binary format
                  with open(filename, 'rb') as file:
                    blobData = file.read()
                    return blobData
                def DUpload():
                  global fln
                  global photo1
                  #This daatabase is to store upload drawing and login name into Drawing.db
                  sqliteConnection12 = sqlite3.connect('Drawing.db')
                  cursor = sqliteConnection12.cursor()
                  print("Connected to SQLite")
                  RName=name
                  print(RName)
                  cursor.execute('CREATE TABLE IF NOT EXISTS drawing ( RName TEXT,photo BLOB NOT NULL)')
                  #This is to check where logined name has uploaded image or not
                  find_user=('Select * from drawing Where RName = ?')
                  cursor.execute(find_user,[LName.get()])
                  record=cursor.fetchall()
                  print(record)
                  if record:
                     messagebox.showerror("Already Uploaded!             ")
                     messagebox.showerror("Wait for Result!              ")
                  else:
                     fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=(("JPG File","*.jpg"),("PNG file","*.png"),("All Files","*.*")))
                     sqlite_insert_blob_query = """ INSERT INTO drawing (RName,photo) VALUES(?,?)"""
                     empPhoto = convertToBinaryData(fln)
                     data_tuple = (RName,empPhoto)
                     cursor.execute(sqlite_insert_blob_query, data_tuple)
                     sqliteConnection12.commit()
                     print("Image and file inserted successfully as a BLOB into a table")
                     img=Image.open(fln)
                     img.thumbnail((660,580))
                     img=ImageTk.PhotoImage(img)
                     LabelDPhoto.config(image=img)
                     LabelDPhoto.image=img
                     messagebox.showinfo('Done!ALL The Best!!          ')
                     sqliteConnection12
                     readBlobData(LName.get())
                Dlabel=Label(a,text="",bg="lightgreen",height=13,width=12)
                Dlabel.place(x=0,y=5)
                Dhome=Button(a,text="Home",width=10,height=2,command=home)
                Dhome.place(x=0,y=10)
                Dlogin=Button(a,text="Login",width=10,height=2,command=quit1)
                Dlogin.place(x=0,y=60)
                Dprofile=Button(a,text="Profile",command=profile,width=10,height=2)
                Dprofile.place(x=0,y=110)
                Drule=Button(a,text="Rules",width=10,height=2,command=Rule)
                Drule.place(x=0,y=160)
                LabelDName=Label(a,text="***Welcome"+" "+name+"***",bg="lightpink",height=2,width=20)
                LabelDName.place(x=497,y=14)
                if(inserted==1):
                    LabelD=Label(a,text="****** You  upload this drawing for competition******",height=2,width=50)
                    LabelD.place(x=400,y=42)
                    LabelDPhoto=Label(a,text="")
                else:
                    LabelD=Label(a,text="***Here you can upload your drawing for competition***",height=2,width=50)
                    LabelD.place(x=400,y=42)
                    photo='C:/Users/ACER/Desktop/Ql6iRu9.jpg'
                    img=Image.open(photo)
                    img.thumbnail((660,580))
                    img=ImageTk.PhotoImage(img)
                    LabelDPhoto=Label(a,image=img)
                    LabelDPhoto.image=img
                    LabelDPhoto.place(x=230,y=79)
                buttonDupload=Button(a,text="Upload Drawing",bg='lightpink',command=DUpload)
                buttonDupload.place(x=525,y=570)
                
    def check():
           #This are global variables
           #This are global variables in this registered details are taken.....
           global name
           global address
           global gender
           global gmail
           global contactno
           global age
           global state
           global password
           global photo
           #This is to is log() method is active or not so that when not actived it will not be destroyed..
           global selectroot
           #This is to get Labeled values...
           global LName
           global LPassword
           #
           global no_of_participants
           #This is to check what is their in admin table "no"(It has no of participants put by admin)
           global buttonsa
           #This is to take Admin table RNAME and RPASSWORD
           global name1
           global password1
           #
           global No
           #
           global no123
           #connection to Admin Table
           sqliteConnection1 = sqlite3.connect('Admin.db')
           cursor = sqliteConnection1.cursor()
           print(LName.get())
           print(LPassword.get())
           #Tablecreate if not exists..
           cursor.execute('CREATE TABLE IF NOT EXISTS admin(RName TEXT,RPassword TEXT,no TEXT)')
           #Select fetch RNAME AND RPASSWORD Where Login entered entry fields are similar....
           find_user=('Select RName,RPassword from admin where RName=? and RPassword=?')
           cursor.execute(find_user,[(LName.get()),(LPassword.get())])
           #if found saved in result...else result=[]....
           result=cursor.fetchall()
           print(result)
           #to check what is there in result if equal to login entered entr fields then
           if result==[(LName.get(), LPassword.get())]:
               # Acccording to row taking that data in one variable
               #Remeber in this way we can access each data, if for loop is not used then result will have only last stored thing...... 
               for row in result:
                   #taking first ,second row data
                  name1=row[0]
                  password1=row[1]
               
                  #This to check the data of no in Admin table
                  find_user=('Select no from admin where RName=? and RPassword=?')
                  cursor.execute(find_user,[(LName.get()),(LPassword.get())])
                  result=cursor.fetchall()
                  print(result)
                  if result==[('0')]:
                     buttonsa=0
                  else:
                    for row in result:
                      global no1
                      no1=row[0]
                      print(no1)
                      buttonsa=1
                      # this fuction is to provide differenet features for admin
                      logadmin()
               cursor.close()
           else:
             with sqlite3.connect('Register.db')as db:
               cursor=db.cursor()
             cursor.execute('CREATE TABLE IF NOT EXISTS participants(RName TEXT,RAddress Text,RGender TEXT,REmail Text,RContactno Text,RAge Text,RState Text,RPassword Text, photo BLOB NOT NULL)')
             find_user=('Select * from participants where RName=? and RPassword=?')
             cursor.execute(find_user,[(LName.get()),(LPassword.get())])
             result=cursor.fetchall()
             print(result)
             #To check result is empt or not
             if(result==[]):
               messagebox.showerror("Wrong Password      ")
               messagebox.showerror("Or Wrong Username   ")
               log()
               
             else:
        #If there is result taking databases into variables and displaying in profile 
               if result:
                for row in result:
                  print("RName = ", row[0], "RAddress = ", row[1],"RGender =",row[2],"REmail =",row[3],"Rcontactno =",row[4],"RAge =",row[5],"RState =",row[6],"RPassword =",row[7])
                  name  = row[0]
                  address =row[1]
                  gender= row[2]
                  gmail=row[3]
                  contactno=row[4]
                  age=row[5]
                  state=row[6]
                  password=row[7]
                  photo = row[8]
                  cursor.close()
                  with sqlite3.connect('Register.db')as db:
                    cursor=db.cursor()
                  find_user=('Select Count(RName) from participants ')
                  cursor.execute(find_user)
                  record=cursor.fetchall()
                  for row in record:
                    record1=row[0]
                    print("helllllo")
                    print(record1)
                  db.close()
                  sqliteConnection1 = sqlite3.connect('Admin.db')
                  cursor = sqliteConnection1.cursor()
                  cursor.execute('CREATE TABLE IF NOT EXISTS admin(RName TEXT,RPassword TEXT,no TEXT)')
                  find_user=('Select no from admin ')
                  cursor.execute(find_user)
                  result=cursor.fetchall()
                  for row in result:
                     no_of_participants=row[0]
                  print("Helll participants")
                  print(no_of_participants)
                  cursor.close()
                  aa=type(no_of_participants)
                  cc=int(no_of_participants)
                  bb=type(record1)
                  print(aa)
                  print(bb)
                  print(type(cc))
                  no123=no_of_participants
                  if (record1==int(no_of_participants)):
                    vote1()
                  else:
                    drawinginserted()
                    
                  
      #sqliteConnection12 = sqlite3.connect('Register.db')
      #cursor = sqliteConnection12.cursor()
      #print("Connected to SQLite")
      #cursor.execute('CREATE TABLE IF NOT EXISTS participants ( RName TEXT,photo BLOB NOT NULL)')
     #This is to check where logined name has uploaded image or not
    check()
  #This is to Store drawing and name of Drawing database into a file of Pc participants details
  def readBlobData(RName):
    try:
        sqliteConnection1 = sqlite3.connect('Drawing.db')
        cursor = sqliteConnection1.cursor()
        print("Connected to SQLite")
        sql_fetch_blob_query = """SELECT * from drawing where RName = ?"""
        cursor.execute(sql_fetch_blob_query,[LName.get()])
        record = cursor.fetchall()
        #print( sql_fetch_blob_query)
        print(cursor.execute)
        for row in record:
            print("RName = ", row[0])
            name  = row[0]
            photo = row[1]
            print("Storing  image  on disk \n")
            photoPath = "C:/Users/ACER/Desktop/App Aaboli/Projects/Drawing Competition/Participantsdetails/" + name+ ".png"
            writeTofile(photo, photoPath)
            cursor.close()

    except sqlite3.Error as error:
        print("Failed to read blob data from sqlite table", error)
    finally:
       if (sqliteConnection1):
            sqliteConnection1.close()
            print("sqlite connection is closed")
  #This is to display login page
  def log():
   global root
   root =tk.Tk()
   root.geometry("300x250")
   global selectroot
   selectroot=1
   global LName
   global LPassword
   LName=StringVar()
   LPassword=StringVar()
   Labeldraw=Label(root,text="***Welcome to drawing Competition***",font=("",13,"bold"))
   Labeldraw.place(x=400,y=90)
   Labellreg=Label(root,text="Login Form ",bg="Red",width=20,height=2)
   Labellreg.place(x=475,y=190)
   Labellname=Label(root,text="Enter Name :",bg="lightgreen",width=15)
   Labellname.place(x=420,y=260)
   entrylname=Entry(root,textvar=LName)
   entrylname.place(x=550,y=260)
   Labellpassword=Label(root,text="Enter Password : ",bg="lightgreen",width=15)
   Labellpassword.place(x=420,y=311)
   entrylpassword=Entry(root,textvar=LPassword)
   entrylpassword.place(x=550,y=311)
   buttonlogin=Button(root,text="Login",bg="lightgreen",width=10,command=login)
   buttonlogin.place(x=450,y=360)
   buttonregister=Button(root,text="Register",bg="lightgreen",width=10,command=register)
   buttonregister.place(x=563,y=360)
   root.mainloop()
  #caling login page
  log()
#Caling login and checking login and creating Drawing db and upload drawing toring data on desktop file...
main_screen()
