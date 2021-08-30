# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 11:11:57 2021

@author: SHIVAANSH
"""

import tkinter as tK
from tkinter import messagebox
import sqlite3

root=tK.Tk()
root.title("Registration Information")
root.geometry("800x280")
root.configure(bg="light grey")

#REGISTRATION FORM
v1=tK.IntVar()
v2=tK.IntVar()
v3=tK.IntVar()
v4=tK.IntVar()
v5=tK.IntVar()
v6=tK.IntVar()
v7=tK.IntVar()
v8=tK.IntVar()
v9=tK.IntVar()
v10=tK.IntVar()
v11=tK.IntVar()
v12=tK.IntVar()
v13=tK.IntVar()
v14=tK.IntVar()
#ADDITIONAL FORM
v15=tK.IntVar()
v16=tK.IntVar()

#REGISTRATION FORM
ent1=tK.StringVar()
ent2=tK.StringVar()
ent3=tK.StringVar()
ent4=tK.StringVar()
#OWNER FORM
ent5=tK.StringVar()
ent6=tK.StringVar()
ent7=tK.StringVar()
ent8=tK.StringVar()
ent9=tK.StringVar()
ent10=tK.StringVar()
ent11=tK.StringVar()
ent12=tK.StringVar()
ent13=tK.StringVar()
ent14=tK.StringVar()
ent15=tK.StringVar()
ent16=tK.StringVar()
ent17=tK.StringVar()
ent18=tK.StringVar()
ent19=tK.StringVar()
ent20=tK.StringVar()
ent21=tK.StringVar()
#ADDITIONAL FORM
ent22=tK.StringVar()
ent23=tK.StringVar()
ent24=tK.StringVar()
ent25=tK.StringVar()
ent26=tK.StringVar()
ent27=tK.StringVar()


#REGISTRATION FORM
op1=tK.StringVar()
op2=tK.StringVar()
op3=tK.StringVar()
op4=tK.StringVar()
op5=tK.StringVar()
op6=tK.StringVar()
op7=tK.StringVar()
op8=tK.StringVar()
op9=tK.StringVar()
op10=tK.StringVar()
op11=tK.StringVar()
op12=tK.StringVar()
op13=tK.StringVar()
#OWNER FORM
op15=tK.StringVar()
op14=tK.StringVar()
op16=tK.StringVar()
op17=tK.StringVar()
op18=tK.StringVar()
op19=tK.StringVar()
op20=tK.StringVar()
op21=tK.StringVar()
op22=tK.StringVar()
op23=tK.StringVar()
op24=tK.StringVar()
op25=tK.StringVar()
op26=tK.StringVar()
op27=tK.StringVar()
op28=tK.StringVar()
op29=tK.StringVar()
op30=tK.StringVar()
#ADDITIONAL FORM
op31=tK.StringVar()
op32=tK.StringVar()
op33=tK.StringVar()
op34=tK.StringVar()
op35=tK.StringVar()
op36=tK.StringVar()
op37=tK.StringVar()



conn=sqlite3.connect('car.db')
conn.execute("CREATE TABLE IF NOT EXISTS REGISTRATION\
(PERIOD VARCHAR,\
TYPE VARCHAR,\
REISSUE VARCHAR,\
RENTAL VARCHAR,\
TRANSFER VARCHAR,\
PLATE INTEGER,\
HIRE VARCHAR,\
RIDE VARCHAR,\
SEATING INTEGER,\
AMATEUR VARCHAR,\
LETTER VARCHAR,\
OTHER VARCHAR,\
SPECIFY VARCHAR);")

conn.execute("CREATE TABLE IF NOT EXISTS OWNER\
(ONAME VARCHAR,\
OPHONE VARCHAR,\
ODMV VARCHAR,\
CONAME VARCHAR,\
COPHONE VARCHAR,\
CODMV VARCHAR,\
RESIDENCE VARCHAR,\
ORESIDENCE VARCHAR,\
OCITY VARCHAR,\
OSTATE VARCHAR,\
OZIP VARCHAR,\
CORESIDENCE VARCHAR,\
COCITY VARCHAR,\
COSTATE VARCHAR,\
COZIP VARCHAR,\
OEMAIL VARCHAR,\
COEMAIL VARCHAR);")

conn.execute("CREATE TABLE IF NOT EXISTS ADDITIONAL\
(LOCATION VARCHAR,\
DATE VARCHAR,\
MILITARY SERVICE VARCHAR,\
REGISTER ADDRESS VARCHAR,\
CITY VARCHAR,\
STATE VARCHAR,\
ZIP VARCHAR);")

def registration():
    if(v1.get()==1):
        op1.set("One year")
        v2.set(0)
        v3.set(0)
    if(v2.get()==1):
        op1.set("Two years")
        v1.set(0)
        v3.set(0)
    if(v3.get()==1):
        op1.set("Three years")
        v1.set(0)
        v2.set(0)
    if(v4.get()==1):
        op2.set("Original")
        v5.set(0)
        v6.set(0)
        v7.set(0)
    if(v5.get()==1):
        op2.set("Renewal")
        v4.set(0)
        v6.set(0)
        v7.set(0)
    if(v6.get()==1):
        op2.set("Private")
        v4.set(0)
        v5.set(0)
        v7.set(0)
    if(v7.get()==1):
        op3.set("Reissue")
        v4.set(0)
        v5.set(0)
        v6.set(0)
    if(v8.get()==1):
        op3.set("Yes")
    else:
        op3.set("No")
        
    if(v9.get()==1):
        op4.set("Yes")
    else:
        op4.set("No")
        
    if(v10.get()==1):
        op5.set("Yes")
        op6.set(ent1.get())
    else:
        op5.set("No")
        op6.set("NULL")
    
    if(v11.get()==1):
        op7.set("Yes")
    else:
        op7.set("No")
        
    if(v12.get()==1):
        op8.set("Yes")
        op9.set(ent2.get())
    else:
        op8.set("No")
        op9.set("NULL")
        
    if(v13.get()==1):
        op10.set("Yes")
        op11.set(ent3.get())
    else:
        op10.set("No")
        op11.set("NULL")
    
    if(v14.get()==1):
        op12.set("Yes")
        op13.set(ent4.get())
    else:
        op12.set("No")
        op13.set("NULL")
        
    conn.execute("INSERT INTO REGISTRATION VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?);",(op1.get(),op2.get(),op3.get(),\
                                                                                op4.get(),op5.get(),op6.get(),op7.get(),\
                                                                                op8.get(),op9.get(),op10.get(),\
                                                                                op11.get(),op12.get(),op13.get()))
    conn.commit()
    
    
def owner():
    op14.set(ent5.get())
    op15.set(ent6.get())
    op16.set(ent7.get())
    op17.set(ent8.get())
    op18.set(ent9.get())
    op19.set(ent10.get())
    op20.set(ent11.get())
    op21.set(ent12.get())
    op22.set(ent13.get())
    op23.set(ent14.get())
    op24.set(ent15.get())
    op25.set(ent16.get())
    op26.set(ent17.get())
    op27.set(ent18.get())
    op28.set(ent19.get())
    op29.set(ent20.get())
    op30.set(ent21.get())
    
    conn.execute("INSERT INTO OWNER VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",\
                 (op14.get(),op15.get(),op16.get(),op17.get(),op18.get(),op19.get(),op20.get(),op21.get(),op22.get(),op23.get(),\
                  op24.get(),op25.get(),op26.get(),op27.get(),op28.get(),op29.get(),op30.get()))
    conn.commit()
    
def additional():
    op31.set(ent22.get())
    op32.set(ent23.get())
    if(v15.get()==1):
        op33.set("Yes")
        v16.set(0)
    else:
        op33.set("No")
        v16.set(0)
    op34.set(ent24.get())
    op35.set(ent25.get())
    op36.set(ent26.get())
    op37.set(ent27.get())
    
    conn.execute("INSERT INTO ADDITIONAL VALUES(?,?,?,?,?,?,?)",(op31.get(),op32.get(),op33.get(),\
                                                                 op34.get(),op35.get(),op36.get(),op37.get()))
    conn.commit()
    
    
frame1=tK.Frame(root,bg="grey")
frame2=tK.Frame(root,bg="light grey")
label1=tK.Label(frame1,text="REGISTRATION INFORMATION",bg="grey",fg="white").grid(padx=330)
frame1.pack(fill="x")
label2=tK.Label(frame2,text="Registration Period:(check one) ",bg="light blue")
label2.grid(row=0,column=0,pady=(20,0))
ch1=tK.Checkbutton(frame2,text="One Year",variable=v1,onvalue=1,offvalue=0,bg="light grey")
ch2=tK.Checkbutton(frame2,text="Two Years($2 discount)",variable=v2,onvalue=1,offvalue=0,bg="light grey")
ch3=tK.Checkbutton(frame2,text="Three Years($3 discount)",variable=v3,onvalue=1,offvalue=0,bg="light grey")
ch1.grid(row=0,column=1,pady=(20,0))
ch2.grid(row=0,column=2,pady=(20,0))
ch3.grid(row=0,column=3,pady=(20,0))
label3=tK.Label(frame2,text="Registration Type:(check one)",bg="light blue")
label3.grid(row=1,column=0)
ch4=tK.Checkbutton(frame2,text="Original",variable=v4,onvalue=1,offvalue=0,bg="light grey")
ch5=tK.Checkbutton(frame2,text="Renewal",variable=v5,onvalue=1,offvalue=0,bg="light grey")
ch6=tK.Checkbutton(frame2,text="Private",variable=v6,onvalue=1,offvalue=0,bg="light grey")
ch7=tK.Checkbutton(frame2,text="Reissue",variable=v7,onvalue=1,offvalue=0,bg="light grey")
ch4.grid(row=1,column=1)
ch5.grid(row=1,column=2)
ch6.grid(row=1,column=3)
ch7.grid(row=1,column=4)
ch8=tK.Checkbutton(frame2,text="Reissue",variable=v8,onvalue=1,offvalue=0,bg="light grey")
ch9=tK.Checkbutton(frame2,text="Rental Vehicle",variable=v9,onvalue=1,offvalue=0,bg="light grey")
ch10=tK.Checkbutton(frame2,text="Transfer Plate Number",variable=v10,onvalue=1,offvalue=0,bg="light grey")
en1=tK.Entry(frame2,textvariable=ent1)
ch8.grid(row=3,column=0)
ch9.grid(row=3,column=1)
ch10.grid(row=3,column=2)
en1.grid(row=3,column=3,sticky="W")
label4=tK.Label(frame2,text="Enter plate NUM",bg="light blue")
label4.grid(row=4,column=3,sticky="W")
ch11=tK.Checkbutton(frame2,text="For Hire",variable=v11,onvalue=1,offvalue=0,bg="light grey")
ch12=tK.Checkbutton(frame2,text="Ride Sharing",variable=v12,onvalue=1,offvalue=0,bg="light grey")
label5=tK.Label(frame2,text="Seating Capacity",bg="light blue")
en2=tK.Entry(frame2,textvariable=ent2)
ch11.grid(row=5,column=0)
ch12.grid(row=5,column=1)
label5.grid(row=5,column=2,sticky="E")
en2.grid(row=5,column=3,sticky="W")
ch13=tK.Checkbutton(frame2,text="Amateur Radio Operator Call Letter-Specify Letters:",variable=v13,onvalue=1,offvalue=0,bg="light grey")
en3=tK.Entry(frame2,textvariable=ent3)
ch13.grid(row=6,column=0,columnspan=2,sticky="E")
en3.grid(row=6,column=2,sticky="W")
ch14=tK.Checkbutton(frame2,text="Other:",variable=v14,onvalue=1,offvalue=0,bg="light grey")
en4=tK.Entry(frame2,textvariable=ent4)
ch14.grid(row=6,column=3,sticky="E")
en4.grid(row=6,column=4,sticky="W")
label6=tK.Label(frame2,text="SPECIFY",bg="light blue")
label6.grid(row=7,column=4)

#ADDITIONAL INFORMATION FORM

def newwindow2():
    root3=tK.Toplevel(root)
    root3.title("Additional Information")
    root3.geometry("1000x280")
    root3.configure(bg="light grey")
    frame1=tK.Frame(root3,bg="grey")
    frame2=tK.Frame(root3,bg="light grey")
    label26=tK.Label(frame1,text="ADDITIONAL INFORMATION",bg="grey",fg="white").grid(padx=430)
    frame1.pack(fill="x")
    label27=tK.Label(frame2,text="Location where Vehicle is Principally Parked",bg="light blue")
    label28=tK.Label(frame2,text="If New Location Enter Date Changed",bg="light blue")
    label29=tK.Label(frame2,text="Are any of the Owners/Leesses on active military duty?",bg="light blue")
    label27.grid(row=0,column=0,columnspan=2,padx=20,pady=(20,0))
    label28.grid(row=0,column=2,columnspan=2,padx=20,pady=(20,0))
    label29.grid(row=0,column=4,columnspan=2,padx=(20,0),pady=(20,0))
    en22=tK.Entry(frame2,textvariable=ent22)
    en23=tK.Entry(frame2,textvariable=ent23)
    ch15=tK.Checkbutton(frame2,text="Yes",variable=v15,bg="light grey")
    ch16=tK.Checkbutton(frame2,text="No",variable=v16,bg="light grey")
    en22.grid(row=1,column=0,columnspan=2,padx=20)
    en23.grid(row=1,column=2,columnspan=2,padx=20)
    ch15.grid(row=1,column=4,sticky="W",padx=140)
    ch16.grid(row=1,column=4,sticky="E")
    label30=tK.Label(frame2,text="If you would like your registration renewals sent to an address other than your residence/business address, enter it below.",bg="yellow")
    label30.grid(row=2,column=0,columnspan=5,padx=60,pady=(20,0))
    label31=tK.Label(frame2,text="Registration Mailing Address-Optional",bg="light blue")
    label32=tK.Label(frame2,text="City",bg="light blue")
    label33=tK.Label(frame2,text="State",bg="light blue")
    label34=tK.Label(frame2,text="ZIP Code",bg="light blue")
    label31.grid(row=3,column=0,columnspan=2,padx=20,pady=(20,0))
    label32.grid(row=3,column=2,columnspan=2,padx=20,pady=(20,0))
    label33.grid(row=3,column=4,padx=20,pady=(20,0))
    label34.grid(row=3,column=5,padx=20,pady=(20,0))
    en24=tK.Entry(frame2,textvariable=ent24).grid(row=4,column=0,columnspan=2,padx=20)
    en25=tK.Entry(frame2,textvariable=ent25).grid(row=4,column=2,columnspan=2,padx=20)
    en26=tK.Entry(frame2,textvariable=ent26).grid(row=4,column=4,padx=20)
    en27=tK.Entry(frame2,textvariable=ent27).grid(row=4,column=5,padx=20)
    b3=tK.Button(frame2,text="Close.",command=root.destroy,bg="light grey")
    b3.grid(row=6,column=4,pady=10,sticky="w")
    b30=tK.Button(frame2,text="Submit",command=additional,bg="lightgrey").grid(row=5,column=4,pady=10,sticky="w")
    frame2.pack()
    
#OWNER INFORMATION FORM

def newwindow():
    root2=tK.Toplevel(root)
    root2.title("Owner Information")
    root2.geometry("1100x500")
    root2.configure(bg="light grey")
    frame1=tK.Frame(root2,bg="grey")
    frame2=tK.Frame(root2,bg="light grey")
    label7=tK.Label(frame1,text="OWNER INFORMATION",bg="grey",fg="white").grid(padx=500)
    frame1.pack(fill="x")
    label8=tK.Label(frame2,text="Owner's Full Legal Name or Business Name",bg="light blue")
    label9=tK.Label(frame2,text="Telephone Number",bg="light blue")
    label10=tK.Label(frame2,text="DMV Customer Number/FEIN/SSN",bg="light blue")
    label8.grid(row=0,column=0,columnspan=3,pady=(20,0))
    label9.grid(row=0,column=3,columnspan=3,pady=(20,0))
    label10.grid(row=0,column=6,columnspan=3,pady=(20,0))
    en5=tK.Entry(frame2,textvariable=ent5)
    en6=tK.Entry(frame2,textvariable=ent6)
    en7=tK.Entry(frame2,textvariable=ent7)
    en5.grid(row=1,column=0,columnspan=3,padx=40)
    en6.grid(row=1,column=3,columnspan=3,padx=40)
    en7.grid(row=1,column=6,columnspan=3,padx=40)
    label11=tK.Label(frame2,text="Co-Owner's Full Legal Name or Business Name",bg="light blue")
    label12=tK.Label(frame2,text="Telephone Number",bg="light blue")
    label13=tK.Label(frame2,text="DMV Customer Number/FEIN/SSN",bg="light blue")
    label11.grid(row=2,column=0,columnspan=3,padx=40,pady=(20,0))
    label12.grid(row=2,column=3,columnspan=3,padx=40,pady=(20,0))
    label13.grid(row=2,column=6,columnspan=3,padx=40,pady=(20,0))
    en8=tK.Entry(frame2,textvariable=ent8)
    en9=tK.Entry(frame2,textvariable=ent9)
    en10=tK.Entry(frame2,textvariable=ent10)
    en8.grid(row=3,column=0,columnspan=3)
    en9.grid(row=3,column=3,columnspan=3)
    en10.grid(row=3,column=6,columnspan=3)
    label14=tK.Label(frame2,text="Note:Owners(and Lessees) if applicable Must provide their residence/home/business address where requested,this address \n can not be a PO Box. You must complete form ISD-01 if you would like your address updated",bg="yellow")
    label15=tK.Label(frame2,text="Residence/Business Jurisdiction",bg="light blue")
    label14.grid(row=4,column=0,columnspan=6,padx=40,pady=(20,0))
    label15.grid(row=4,column=6,columnspan=3,padx=40,pady=(20,0))
    en11=tK.Entry(frame2,textvariable=ent11)
    en11.grid(row=5,column=6,columnspan=3,padx=40)
    label16=tK.Label(frame2,text="Owner's residence/home/business Address",bg="light blue")
    label17=tK.Label(frame2,text="QITY",bg="light blue")
    label18=tK.Label(frame2,text="State",bg="light blue")
    label19=tK.Label(frame2,text="ZIP Code",bg="light blue")
    label16.grid(row=6,column=0,columnspan=3,padx=20,pady=(20,0))
    label17.grid(row=6,column=3,columnspan=3,padx=20,pady=(20,0))
    label18.grid(row=6,column=6,columnspan=2,padx=20,pady=(20,0))
    label19.grid(row=6,column=8,columnspan=2,padx=20,pady=(20,0))
    en12=tK.Entry(frame2,textvariable=ent12)
    en13=tK.Entry(frame2,textvariable=ent13)
    en14=tK.Entry(frame2,textvariable=ent14)
    en15=tK.Entry(frame2,textvariable=ent15)
    en12.grid(row=7,column=0,columnspan=3,padx=20)
    en13.grid(row=7,column=3,columnspan=3,padx=20)
    en14.grid(row=7,column=6,columnspan=2,padx=20)
    en15.grid(row=7,column=8,columnspan=2,padx=20)
    label20=tK.Label(frame2,text="Co-Owner's residence/home/business Address",bg="light blue")
    label21=tK.Label(frame2,text="QITY",bg="light blue")
    label22=tK.Label(frame2,text="State",bg="light blue")
    label23=tK.Label(frame2,text="ZIP Code",bg="light blue")
    label20.grid(row=8,column=0,columnspan=3,padx=20,pady=(20,0))
    label21.grid(row=8,column=3,columnspan=3,padx=20,pady=(20,0))
    label22.grid(row=8,column=6,columnspan=2,padx=20,pady=(20,0))
    label23.grid(row=8,column=8,columnspan=2,padx=20,pady=(20,0))
    en16=tK.Entry(frame2,textvariable=ent16)
    en17=tK.Entry(frame2,textvariable=ent17)
    en18=tK.Entry(frame2,textvariable=ent18)
    en19=tK.Entry(frame2,textvariable=ent19)
    en16.grid(row=9,column=0,columnspan=3,padx=20)
    en17.grid(row=9,column=3,columnspan=3,padx=20)
    en18.grid(row=9,column=6,columnspan=2,padx=20)
    en19.grid(row=9,column=8,columnspan=2,padx=20)
    label24=tK.Label(frame2,text="Owner's Email Address",bg="light blue")
    label25=tK.Label(frame2,text="Co-Owner's Email Address",bg="light blue")
    label24.grid(row=10,column=0,columnspan=4,padx=20,pady=(20,0),sticky="e")
    label25.grid(row=10,column=4,columnspan=3,padx=20,pady=(20,0),sticky="e")
    en20=tK.Entry(frame2,textvariable=ent20)
    en21=tK.Entry(frame2,textvariable=ent21)
    en20.grid(row=11,column=0,columnspan=4,padx=20,sticky="e")
    en21.grid(row=11,column=4,columnspan=3,padx=20,sticky="e")
    b2=tK.Button(frame2,text="Go to Additional Information",command=newwindow2,bg="light grey")
    b2.grid(row=13,column=4,pady=10)
    b20=tK.Button(frame2,text="Submit",command=owner,bg="lightgrey").grid(row=12,column=4,pady=10)
    frame2.pack()
    
    
b1=tK.Button(frame2,text="Go to Owner Information",command=newwindow,bg="light grey")
b1.grid(row=9,column=2,pady=10)
b10=tK.Button(frame2,text="Submit",command=registration,bg="lightgrey")
b10.grid(row=8,column=2)
frame2.pack()
root.mainloop()