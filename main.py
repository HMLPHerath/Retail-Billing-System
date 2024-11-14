from tkinter import *


root = Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('icon.ico')

# Retail Billing System
headingLable = Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=10,relief=GROOVE)
headingLable.pack(fill=X)

# Customer Details
customer_deatails_labelFrame = LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=10,relief=GROOVE)
customer_deatails_labelFrame.pack(fill=X)

# Name
nameLabel = Label(customer_deatails_labelFrame,text='Name : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0, column=0,padx=20,pady=2)

nameEntry = Entry(customer_deatails_labelFrame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

# Phone Number
phoneLabel = Label(customer_deatails_labelFrame,text='Phone Number : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=20,pady=2)

phoneEntry = Entry(customer_deatails_labelFrame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=8)

# Bill Number
billLabel = Label(customer_deatails_labelFrame,text='Bill Number : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
billLabel.grid(row=0,column=4,padx=20,pady=2)

billEntry = Entry(customer_deatails_labelFrame,font=('arial',15),bd=7,width=18)
billEntry.grid(row=0,column=5,padx=8)

# Search Button
searchButton = Button(customer_deatails_labelFrame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10)
searchButton.grid(row=0,column=6,padx=20,pady=8)


# Product Frame
productFrame = Frame(root)
productFrame.pack()

# Cosmatic
cosmaticFrame = LabelFrame(productFrame,text='Cosmatic',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=10,relief=GROOVE)
cosmaticFrame.grid(row=0,column=0)

# Bath Soap
bathSoapLabel = Label(cosmaticFrame,text='Bath Sope : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bathSoapLabel.grid(row=0,column=0)

bathSoapEntry = Entry(cosmaticFrame,font=('arial',15),bd=7,width=10)
bathSoapEntry.grid(row=0,column=1)

# Face Creame
faceCreameLabel = Label(cosmaticFrame,text='Face Creame : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
faceCreameLabel.grid(row=1,column=0)

faceCreameEntry = Entry(cosmaticFrame,font=('arial',15),bd=7,width=10)
faceCreameEntry.grid(row=1,column=1)




root.mainloop()