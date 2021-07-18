import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox
r= tk.Tk()
r.geometry("400x300")
var=IntVar()
s=0
s0=0
s2=0
s1=0
s3=0
s4=0
task=""
Name1=StringVar()
Name2=StringVar()
Name3=StringVar()
Name01=StringVar()
Name02=StringVar()
Name03=StringVar()
name1=" "
name2=" "
name3=" "
name01=" "
name02=" "
name03=" "
label_1 = Label(r, text=" Enter Player1 Name   :",width=20,font=("bold", 10))
label_1.place(x=80,y=100)
entry_1 = Entry(r,textvar=Name1)
entry_1.place(x=240,y=100)
label_2 = Label(r , text="Enter Player2 Name   :",width=20,font=("bold", 10))
label_2.place(x=80,y=150)
entry_2 = Entry(r,textvar=Name2)
entry_2.place(x=240,y=150)
label_3=Label(r,text="")
entry_3=Entry(r)
label20=Label(r,text="WELCOME TO FUN GAME ",width=20,height=3)
label20.place(x=145,y=35)
def Select3():
  label20.config(text="WELCOME TO FUN GAME ",width=20,height=2)
  label20.place(x=140,y=0)
  label_1.config(text=" Enter Player1 Name   :",width=20,font=("bold", 10))
  label_1.place(x=80,y=50)
  entry_1.config(textvar=Name01)
  entry_1.place(x=240,y=50)
  label_2.config( text="Enter Player2 Name   :",width=20,font=("bold", 10))
  label_2.place(x=80,y=100)
  entry_2.config(textvar=Name02)
  entry_2.place(x=240,y=100)
  label_3.config( text="Enter Player3 Name   :",width=20,font=("bold", 10))
  label_3.place(x=80,y=150)
  entry_3.config(textvar=Name03)
  entry_3.place(x=240,y=150)
  Button15=Button(text="Player 2",bg="lightgreen",width=13,command=Select2,height=-2).place(x=120,y=200)
  Button16=Button(text="Player 3",bg="lightgreen",width=13,command=Select3).place(x=230,y=200)
  button0=Button(text="  Start  ",bg="lightgreen",width=13,command=Players3)
  button0.place(x=119,y=262)
  button0=tk.Button(text="   Fun Book  ",bg="lightgreen",width=13,command=Funbook)
  button0.place(x=230,y=262)
def Select2():
  label20.config( text=" WELCOME TO FUN GAME ",width=50,font=("bold", 10))
  label20.place(x=20,y=50)
  label_1.config(text=" Enter Player1 Name   :",width=20,font=("bold", 10))
  label_1.place(x=80,y=100)
  entry_1.config(textvar=Name1)
  entry_1.place(x=240,y=100)
  label_2.config(text="Enter Player2 Name   :",width=20,font=("bold", 10))
  label_2.place(x=80,y=150)
  entry_2.config(textvar=Name2)
  entry_2.place(x=240,y=150)
  button0=Button(r,text="  Start  ",bg="lightgreen",width=13,command=Players)
  button0.place(x=119,y=262)
  button0=tk.Button(text="   Fun Book  ",bg="lightgreen",width=13,command=Funbook)
  button0.place(x=230,y=262)
def Players():
   root= tk.Tk()
   root.geometry("400x300")
   resultLabel1 = Label(root, text = "")
   label6= Label(root,text="WELCOME TO FUN GAME ",width=20,height=10)
   label6.place(x=446,y=0)
   def random_computer_choice():
    return random.choice(['Sing a song','dance','frog voice','Lion voice','Nagin Dance','Joke'])
    return  random.choice()
   def result():
    global task
    task=random_computer_choice()
    print(task)
    resultLabel1.config(text="Fun Task : "+" "+task,font=("bold", 12))
    resultLabel1.place(x=440,y=350)
    button15 = Button(root,text="  Player1 Done  ",bg="skyblue",command=player1done)
    button15.place(x=410,y=400)
    button16 = Button(root,text="  Player2 Done  ",bg="skyblue",command=player2done)
    button16.place(x=520,y=400)
   def player1done():
    name1=Name1.get()
    global s
    s+=1
    details()
    button15 = Button(root,text="  Player1 Done  ",bg="skyblue",command=player1done,state="disabled")
    button15.place(x=410,y=400)
    #button15["state"]="disabled"
   def details():
    name1=Name1.get()
    text_area = tk.Text(master=root,height=5,width=25,bg="#FFFF99")
    text_area.place(x=410,y=450)
    if(name1==''):
     answer = "Yoo! {n} You Did it\nYour Task was:{t}\nYeah!You got {p} points".format(n="PLAYER1",t=task,p=s)
    else:
     answer = "Yoo! {n} You Did it\nYour Task was:{t}\nYeah!You got {p} points".format(n=name1,t=task,p=s)
    text_area.insert(tk.END,answer)
    resultLabel1.config(text=" ")
   def player2done():
    global s0
    name2=Name2.get()
    s0+=1
    details1()
    button16 = Button(root,text="  Player2 Done  ",bg="skyblue",command=player2done,state="disabled")
    button16.place(x=520,y=400)
   def details1():
    name2=Name2.get()
    text_area = tk.Text(master=root,height=5,width=25,bg="#FFFF99")
    text_area.place(x=410,y=450)
    if(name2==''):
       answer = "Yoo! {n} You Did it\nYour Task was:{t}\nYeah!You got {p} points".format(n="PLAYER2",t=task,p=s0)
    else:
       answer = "Yoo! {n} You Did it\nYour Task was:{t}\nYeah!You got {p} points".format(n=name2,t=task,p=s0)
    text_area.insert(tk.END,answer)
    resultLabel1.config(text=" ")
   def score():
    name1=Name1.get()
    name2=Name2.get()
    text_area = tk.Text(master=root,height=5,width=25,bg="#FFFF99")
    text_area.place(x=410,y=450)
    if s>s0:
     if(name1=='') and (name2==''):
      answer="{n1} score is {s1}\n{n2} score is {s2}\nCongrats! PLAYER1 WON ".format(n1="PLAYER1",s1=s,n2="PLAYER2",s2=s0,)
     else:
      answer="{n1} score is {s1}\n{n2} score is {s2}\nCongrats! {n1} WON ".format(n1=name1,s1=s,n2=name2,s2=s0)
    elif s0>s:
      if(name1=='') and (name2==''):
        answer="{n1} score is {s1}\n{n2} score is {s2}\nCongrats! PLAYER2 WON ".format(n1="PLAYER1",s1=s,n2="PLAYER2",s2=s0,)
      else:
        answer="{n1} score is {s1}\n{n2} score is {s2}\nCongrats! {n2} WON ".format(n1=name1,s1=s,n2=name2,s2=s0)
       
    else :
      if(name1=='') and (name2==''):
        answer="{n1} score is {s1}\n{n2} score is {s2}\nTie! Both Did Well ".format(n1="PLAYER1",s1=s,n2="PLAYER2",s2=s0,)
      else:
        answer="{n1} score is {s1}\n{n2} score is {s2}\nTie! Both Did Well ".format(n1=name1,s1=s,n2=name2,s2=s0)
    text_area.insert(tk.END,answer)
    return s,s0
   def quit1():
    s8=score()
    s8=0
    global s,s0
    s=s8
    s0=s8
    entry_1.delete(0,END)
    entry_2.delete(0,END)
    root.destroy()
   button1 = Button(root,text="     0    ",bg="skyblue",command=result)
   button1.place(x=430,y=100)
   button2 = Button(root,text="     1    ",bg="pink",command=result)
   button2.place(x=490,y=100)
   button3 = Button(root,text="     2    ",bg="lightgreen",command=result)
   button3.place(x=550,y=100)
   button4 = Button(root,text="     3    ",bg="skyblue",command=result)
   button4.place(x=430,y=150)
   button5 = Button(root,text="     4    ",bg="pink",command=result)
   button5.place(x=490,y=150)
   button6 = Button(root,text="     5    ",bg="lightgreen",command=result)
   button6.place(x=550,y=150)
   button7 = Button(root,text="     6    ",bg="skyblue",command=result)
   button7.place(x=430,y=200)
   button8 = Button(root,text="     7    ",bg="pink",command=result)
   button8.place(x=490,y=200)
   button9 = Button(root,text="     8    ",bg="lightgreen",command=result)
   button9.place(x=550,y=200)
   button10 = Button(root,text="     9    ",bg="skyblue",command=result)
   button10.place(x=430,y=250)
   button11 = Button(root,text="    10   ",bg="pink",command=result)
   button11.place(x=490,y=250)
   button12= Button(root,text="    11   ",bg="lightgreen",command=result)
   button12.place(x=550,y=250)
 
   button13=Button(root,text=" Score ",bg="RED",command=score)
   button13.place(x=452,y=300)
   button14=Button(root,text=" Quit ",bg="RED",command=quit1)
   button14.place(x=528,y=300)
   root.mainloop()
def Players3():
   root= tk.Tk()
   root.geometry("400x300")
   resultLabel1 = Label(root, text = "")
   label6= Label(root,text="WELCOME TO FUN GAME ",width=20,height=10)
   label6.place(x=440,y=0)
   def random_computer_choice():
    return random.choice(['Sing a song','dance','frog voice'])
    return  random.choice()
   def result():
    global task
    task=random_computer_choice()
    print(task)
    resultLabel1.config(text="Fun Task : "+" "+task,font=("bold", 12))
    resultLabel1.place(x=440,y=350)
    button15 = Button(root,text="  Player1 Done  ",bg="skyblue",command=player1done)
    button15.place(x=375,y=400)
    button16 = Button(root,text="  Player2 Done  ",bg="skyblue",command=player2done)
    button16.place(x=475,y=400)
    button17 = Button(root,text="  Player3 Done  ",bg="skyblue",command=player3done)
    button17.place(x=575,y=400)
   def player1done():
    name01=Name01.get()
    global s1
    s1+=1
    details()
    button15 = Button(root,text="  Player1 Done  ",bg="skyblue",command=player1done,state="disabled")
    button15.place(x=375,y=400)
   def details():
    name01=Name01.get()
    text_area = tk.Text(master=root,height=5,width=25,bg="#FFFF99")
    text_area.place(x=410,y=450)
    if(name1==''):
     answer = "Yoo! {n} You Did it\nYour Task was:{t}\nYeah!You got {p} points".format(n="PLAYER1",t=task,p=s1)
    else:
     answer = "Yoo! {n} You Did it\nYour Task was:{t}\nYeah!You got {p} points".format(n=name01,t=task,p=s1)
    text_area.insert(tk.END,answer)
    resultLabel1.config(text=" ")
    
   def player2done():
    
    name02=Name02.get()
    global s3
    s3+=1
    details1()
    button16 = Button(root,text="  Player2 Done  ",bg="skyblue",command=player2done,state="disabled")
    button16.place(x=475,y=400)
   def details1():
    name02=Name02.get()
    text_area = tk.Text(master=root,height=5,width=25,bg="#FFFF99")
    text_area.place(x=410,y=450)
    if(name02==''):
       answer = "Yoo! {n} You Did it\nYour Task was:{t}\nYeah!You got {p} points".format(n="PLAYER2",t=task,p=s3)
    else:
       answer = "Yoo! {n} You Did it\nYour Task was:{t}\nYeah!You got {p} points".format(n=name02,t=task,p=s3)
    text_area.insert(tk.END,answer)
    resultLabel1.config(text=" ")
   def player3done():
    name03=Name03.get()
    global s4
    s4+=1
    details2()
    button18 = Button(root,text="  Player3 Done  ",bg="skyblue",command=player3done,state="disabled")
    button18.place(x=575,y=400)
   def details2():
    name03=Name03.get()
    text_area = tk.Text(master=root,height=5,width=25,bg="#FFFF99")
    text_area.place(x=410,y=450)
    if(name3==''):
     answer = "Yoo! {n} You Did it\nYour Task was:{t}\nYeah!You got {p} points".format(n="PLAYER3",t=task,p=s4)
    else:
     answer = "Yoo! {n} You Did it\nYour Task was:{t}\nYeah!You got {p} points".format(n=name03,t=task,p=s4)
    text_area.insert(tk.END,answer)
    resultLabel1.config(text=" ")
   def score():
    name01=Name01.get()
    name02=Name02.get()
    name03=Name03.get()
    text_area = tk.Text(master=root,height=5,width=25,bg="#FFFF99")
    text_area.place(x=410,y=450)
    if s3<s1>s4:
     if(name01=='') and (name02=='') and (name03==''):
      answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!PLAYER1 WON ".format(n1="PLAYER1",s1=s1,n2="PLAYER2",s2=s3,n3="PLAYER3",s3=s4)
     else:
      answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!n1 WON ".format(n1=name01,s1=s1,n2=name02,s2=s3,n3=name03,s3=s4)
    elif s1<s3>s4:
      if(name01=='') and (name02=='')and (name03==''):
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!PLAYER2 WON ".format(n1="PLAYER1",s1=s1,n2="PLAYER2",s2=s3,n3="PLAYER3",s3=s4)
      else:
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!n2 WON ".format(n1=name01,s1=s1,n2=name02,s2=s3,n3=name03,s3=s4)
    elif s1<s4>s3:
      if(name01=='') and (name02=='')and (name03==''):
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!PLAYER3 WON ".format(n1="PLAYER1",s1=s1,n2="PLAYER2",s2=s3,n3="PLAYER3",s3=s4)
      else:
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!{n2} WON ".format(n1=name01,s1=s1,n2=name02,s2=s3,n3=name03,s3=s4)
    elif s1==s3>s4 :
      if(name01=='') and (name02=='')and (name03==''):
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!Player1 and Player2 Won ".format(n1="PLAYER1",s1=s1,n2="PLAYER2",s2=s3,n3="PLAYER3",s3=s4)
      else:
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!{n1} and {n2} WON ".format(n1=name01,s1=s1,n2=name02,s2=s3,n3=name03,s3=s4)
    elif s1==s4>s3 :
      if(name01=='') and (name02=='')and (name03==''):
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!Player1 and Player3 Won ".format(n1="PLAYER1",s1=s1,n2="PLAYER2",s2=s3,n3="PLAYER3",s3=s4)
      else:
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!{n1} and {n3} WON ".format(n1=name01,s1=s1,n2=name02,s2=s3,n3=name03,s3=s4)
    elif s3==s4>s1 :
      if(name01=='') and (name02=='')and (name03==''):
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!Player2 and Player3 No one Won ".format(n1="PLAYER1",s1=s1,n2="PLAYER2",s2=s3,n3="PLAYER3",s3=s4)
      else:
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!{n3} and {n4} WON ".format(n1=name01,s1=s1,n2=name02,s2=s3,n3=name03,s3=s4)
    elif s1==s3>s4 :
      if(name01=='') and (name02=='')and (name03==''):
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!Player1 and Player2 No one Won ".format(n1="PLAYER1",s1=s1,n2="PLAYER2",s2=s3,n3="PLAYER3",s3=s4)
      else:
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nCongrats!{n} and {n2} WON ".format(n1=name01,s1=s1,n2=name02,s2=s3,n3=name03,s3=s4)
 
    else:
      if(name01=='') and (name02=='')and (name03==''):
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nTie! All Did Well ".format(n1="PLAYER1",s1=s1,n2="PLAYER2",s2=s3,n3="PLAYER3",s3=s4)
      else:
        answer="{n1} score is {s1}\n{n2} score is {s2}\n{n3} score is {s3}\nTie! All Did Well ".format(n1=name01,s1=s1,n2=name02,s2=s3,n3=name03,s3=s4)
    text_area.insert(tk.END,answer)
    return s1,s3,s4
   def quit1():
     s5,s6,s7=score()
     print(s5,s6,s7)
     s5=0
     s6=0
     s7=0
     global s1,s3,s4
     s1=s5
     s3=s6
     s4=s7
     print(s1,s3,s4)
     entry_1.delete(0,END)
     entry_2.delete(0,END)
     entry_3.delete(0,END)
     root.destroy()
   button1 = Button(root,text="     0    ",bg="skyblue",command=result)
   button1.place(x=430,y=100)
   button2 = Button(root,text="     1    ",bg="pink",command=result)
   button2.place(x=490,y=100)
   button3 = Button(root,text="     2    ",bg="lightgreen",command=result)
   button3.place(x=550,y=100)
   button4 = Button(root,text="     3    ",bg="skyblue",command=result)
   button4.place(x=430,y=150)
   button5 = Button(root,text="     4    ",bg="pink",command=result)
   button5.place(x=490,y=150)
   button6 = Button(root,text="     5    ",bg="lightgreen",command=result)
   button6.place(x=550,y=150)
   button7 = Button(root,text="     6    ",bg="skyblue",command=result)
   button7.place(x=430,y=200)
   button8 = Button(root,text="     7    ",bg="pink",command=result)
   button8.place(x=490,y=200)
   button9 = Button(root,text="     8    ",bg="lightgreen",command=result)
   button9.place(x=550,y=200)
   button10 = Button(root,text="     9    ",bg="skyblue",command=result)
   button10.place(x=430,y=250)
   button11 = Button(root,text="    10   ",bg="pink",command=result)
   button11.place(x=490,y=250)
   button12= Button(root,text="    11   ",bg="lightgreen",command=result)
   button12.place(x=550,y=250)
   button13=Button(root,text=" Score ",bg="RED",command=score)
   button13.place(x=452,y=300)
   button14=Button(root,text=" Quit ",bg="RED",command=quit1)
   button14.place(x=528,y=300)
def Funbook():
   root1= tk.Tk()
   root1.geometry("400x300")
   label6= Label(root1,text="WELCOME TO FUN GAME ")
   label6.place(x=140,y=10)
   label0 =Label(root1,text="Hello Guys !")
   label0.place(x=60,y=40)
   label01=Label(root1,text="Welcome to Fun Game!..." )
   label01.place(x=60,y=80)
   label02=Label(root1,text=" Here Two or Three fun people can play, Select it...")
   label02.place(x=60,y=120)
   label03=Label(root1,text="Enter your Fun Names and Start Playing...")
   label03.place(x=60,y=160)
   label04=Label(root1,text="Select any Number, Play fun task you got, and score points...")
   label04.place(x=60,y=200)
   label05=Label(root1,text="View Score and Then to exit quit button...")
   label05.place(x=60,y=240)
   def back():
     root1.destroy()
   button0=Button(root1,text="   Back  ",bg="lightgreen",width=13,command=back)
   button0.place(x=150,y=280)

Button15=Button(r,text="Player 2",bg="lightgreen",width=13,command=Select2,height=-2).place(x=120,y=200)
Button16=Button(r,text="Player 3",bg="lightgreen",width=13,command=Select3).place(x=230,y=200)
button0=Button(r,text="  Start  ",bg="lightgreen",width=13,command=Players)
button0.place(x=119,y=262)
button0=tk.Button(text="   Fun Book  ",bg="lightgreen",width=13,command=Funbook)
button0.place(x=230,y=262)
r.mainloop()

