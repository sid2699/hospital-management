import os
import csv
import sys
import random
from tkinter import *
from tkinter import messagebox
def submit():
    
    
    with open("studentdb.csv",'a',newline='') as f:
        w =csv.writer(f)
        w.writerow([val_id.get(),val_name.get(),val_pointer.get(),val_city.get()])

def search():

      flag=0
      with open("studentdb.csv") as f:
          read=csv.reader(f)
          for row in read:
              if row[0]==val_searchid.get():
                  
                  did=Label(root,text="ID",bg='black',fg='yellow').place(x=300,y=450)
                  dname=Label(root,text="NAME",bg='black',fg='yellow').place(x=400,y=450)
                  dpointer=Label(root,text="POINTER",bg='black',fg='yellow').place(x=500,y=450)
                  dcity=Label(root,text="DEPARTMENT",bg='black',fg='yellow').place(x=650,y=450)
                  
                  
                  ldval_id=Label(root,text=row[0]).place(x=300,y=500)
                  ldval_name=Label(root,text=row[1]).place(x=400,y=500)
                  ldval_pointer=Label(root,text=row[2]).place(x=500,y=500)
                  ldval_city=Label(root,text=row[3]).place(x=650,y=500)

                  flag=1
          if flag==0:
              messagebox.showinfo("ERROR","RECORD NOT FOUND")
                            
                 


root=Tk()

val_id=StringVar()
val_name=StringVar()
val_pointer=StringVar()
val_city=StringVar()
val_searchid=StringVar()

root.geometry("900x900")
root.configure(bg='cyan')
root.title('BVCOE COE STUDENT DATABASE')
canvas=Canvas(root,width=900,height=900)
canvas.pack()
mimage=PhotoImage(file='bv.png')
canvas.create_image(0,0,anchor=NW,image=mimage)
name=Label(root,text="STUDENT DATABASE",bg='black',fg='lightgreen').place(x=400,y=0)
lid=Label(root,text="ENTER STUDENT ID :",bg='black',fg='yellow').place(x=200,y=50)
eid=Entry(root,textvariable=val_id,width=50,bd=5).place(x=350,y=50)
lname=Label(root,text="ENTER STUDENT NAME :",bg='black',fg='yellow').place(x=200,y=100)
ename=Entry(root,textvariable=val_name,width=50,bd=5).place(x=350,y=100)
lpointer=Label(root,text="ENTER STUDENT POINTER :",bg='black',fg='yellow').place(x=200,y=150)
epointer=Entry(root,textvariable=val_pointer,width=50,bd=5).place(x=350,y=150)
lcity=Label(root,text="ENTER DEPARTMENT :",bg='black',fg='yellow').place(x=200,y=200)
ecity=Entry(root,textvariable=val_city,width=50,bd=5).place(x=350,y=200)
bsubmit=Button(root,text="SUBMIT",bg='orange',fg='white',command=submit).place(x=420,y=250)
lsearchid=Label(root,text="ID :",bg='black',fg='yellow').place(x=300,y=350)
esearchid=Entry(root,textvariable=val_searchid,width=50,bd=5).place(x=350,y=350)
bsearch=Button(root,text="SEARCH",command=search,bg='orange',fg='white').place(x=420,y=400)


root.mainloop()


