from tkinter import *

def total():
    # Cosmatic Price
    bathShopPrice = int(bathSoapEntry.get())*50
    faceCreamePrice = int(faceCreameEntry.get())*100
    faceWashPrice = int(faceWashEntry.get())*200
    hairSprayPrice = int(hairSprayEntry.get())*175
    hairGelPrice = int(hairGelEntry.get())*80
    bodyLotionPrice = int(bodyLotionEntry.get())*500

    totalCosmaticPrice = bathShopPrice+faceCreamePrice+faceWashPrice+hairSprayPrice+hairGelPrice+bodyLotionPrice
    cosmaticPriceEntry.delete(0,END)
    cosmaticPriceEntry.insert(0,f'Rs.{totalCosmaticPrice}')

    # Cosmatic Tax
    cosmaticTax = totalCosmaticPrice*0.12
    cosmaticTaxEntry.delete(0,END)
    cosmaticTaxEntry.insert(0,f'Rs.{cosmaticTax}')


    # Grocery Price
    ricePrice = int(riceEntry.get())*275
    oilPrice = int(oileEntry.get())*100
    dallPrice = int(dallEntry.get())*80
    wheatPrice = int(wheatEntry.get())*100
    sugerPrice = int(sugerEntry.get())*120
    teaPrice = int(teaEntry.get())*30

    totalGroceryPrice = ricePrice+oilPrice+dallPrice+wheatPrice+sugerPrice+teaPrice
    groceryPriceEntry.delete(0,END)
    groceryPriceEntry.insert(0,f'Rs.{totalGroceryPrice}')

    # Grocery Tax
    groceryTax = totalGroceryPrice*0.05
    groceryTaxEntry.delete(0,END)
    groceryTaxEntry.insert(0,f'Rs.{groceryTax}')

    # Cold Drink Price
    maazaPrice = int(maazaEntry.get())*100
    pepsiPrice = int(pepsiEntry.get())*150
    spritePrice = int(spriteEntry.get())*80
    dewPrice = int(dewEntry.get())*140
    frootiPrice = int(frootiEntry.get())*120
    cocaColaPrice = int(cocaColaEntry.get())*130

    totalColdDrinksPrice = maazaPrice+pepsiPrice+spritePrice+dewPrice+frootiPrice+cocaColaPrice
    coldDrinksPriceEntry.delete(0,END)
    coldDrinksPriceEntry.insert(0,f'Rs.{totalColdDrinksPrice}')

    # Cold Drink Tax
    coldDrinksTax = totalColdDrinksPrice*0.08
    coldDrinksTaxEntry.delete(0,END)
    coldDrinksTaxEntry.insert(0,f'Rs.{coldDrinksTax}')


    


root = Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('icon.ico')
root.configure(bg='gray20')

# Retail Billing System
headingLable = Label(root,text='Retail Billing System',font=('times new roman',30,'bold'),bg='gray20',fg='gold',bd=10,pady=10,relief=GROOVE)
headingLable.pack(fill=X)

# Customer Details
customer_deatails_labelFrame = LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=10,relief=GROOVE)
customer_deatails_labelFrame.pack(fill=X,pady=7)

# Name
nameLabel = Label(customer_deatails_labelFrame,text='Name : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
nameLabel.grid(row=0, column=0,padx=(20,10),pady=2)

nameEntry = Entry(customer_deatails_labelFrame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=(0,8))

# Phone Number
phoneLabel = Label(customer_deatails_labelFrame,text='Phone Number : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
phoneLabel.grid(row=0,column=2,padx=(20,10),pady=2)

phoneEntry = Entry(customer_deatails_labelFrame,font=('arial',15),bd=7,width=18)
phoneEntry.grid(row=0,column=3,padx=(0,8))

# Bill Number
billLabel = Label(customer_deatails_labelFrame,text='Bill Number : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
billLabel.grid(row=0,column=4,padx=(20,10),pady=2)

billEntry = Entry(customer_deatails_labelFrame,font=('arial',15),bd=7,width=18)
billEntry.grid(row=0,column=5,padx=(0,8))

# Search Button
searchButton = Button(customer_deatails_labelFrame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10)
searchButton.grid(row=0,column=6,padx=50,pady=8)



# Product Frame
productFrame = Frame(root,bg='gray20')
productFrame.pack(fill=X,)



# Cosmatic
cosmaticFrame = LabelFrame(productFrame,text='Cosmatic',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=10,relief=GROOVE)
cosmaticFrame.grid(row=0,column=0,padx=10)

# Bath Soap
bathSoapLabel = Label(cosmaticFrame,text='Bath Sope : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bathSoapLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

bathSoapEntry = Entry(cosmaticFrame,font=('arial',15),bd=7,width=10)
bathSoapEntry.grid(row=0,column=1,pady=9,padx=10)
bathSoapEntry.insert(0,0)

# Face Creame
faceCreameLabel = Label(cosmaticFrame,text='Face Creame : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
faceCreameLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

faceCreameEntry = Entry(cosmaticFrame,font=('arial',15),bd=7,width=10)
faceCreameEntry.grid(row=1,column=1,pady=9,padx=10)
faceCreameEntry.insert(0,0)

# Face Wash
faceWashLable1 = Label(cosmaticFrame,text='Face Wash : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
faceWashLable1.grid(row=2,column=0,pady=9,padx=10,sticky='w')

faceWashEntry = Entry(cosmaticFrame,font=('arial',15),bd=7,width=10)
faceWashEntry.grid(row=2,column=1,pady=9,padx=10)
faceWashEntry.insert(0,0)

# Hair Spray
hairSprayLabel = Label(cosmaticFrame,text='Hair Spray : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairSprayLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

hairSprayEntry = Entry(cosmaticFrame,font=('arial',15),bd=7,width=10)
hairSprayEntry.grid(row=3,column=1,pady=9,padx=10)
hairSprayEntry.insert(0,0)

# Hair Gel
hairGelLabel = Label(cosmaticFrame,text='Hair Gel : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
hairGelLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

hairGelEntry = Entry(cosmaticFrame,font=('arial',15),bd=7,width=10)
hairGelEntry.grid(row=4,column=1,pady=9,padx=10)
hairGelEntry.insert(0,0)

# Body Lotion
bodyLotionLabel = Label(cosmaticFrame,text='Body Lotion : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
bodyLotionLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

bodyLotionEntry = Entry(cosmaticFrame,font=('arial',15),bd=7,width=10)
bodyLotionEntry.grid(row=5,column=1,pady=9,padx=10)
bodyLotionEntry.insert(0,0)



# Grocery Frame
groceryFrame = LabelFrame(productFrame,text='Grocery',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=10,relief=GROOVE)
groceryFrame.grid(row=0,column=1,padx=10)

# Rice
riceLabel = Label(groceryFrame,text='Rice : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
riceLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

riceEntry = Entry(groceryFrame,font=('arial',15),bd=7,width=10)
riceEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
riceEntry.insert(0,0)

# Oil
oileLabel = Label(groceryFrame,text='Oil : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
oileLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

oileEntry = Entry(groceryFrame,font=('arial',15),bd=7,width=10)
oileEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
oileEntry.insert(0,0)

# Dall
dallLabel = Label(groceryFrame,text='Dall : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
dallLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

dallEntry = Entry(groceryFrame,font=('arial',15),bd=7,width=10)
dallEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
dallEntry.insert(0,0)

# Wheat
wheatLabel = Label(groceryFrame,text='Wheat : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
wheatLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

wheatEntry = Entry(groceryFrame,font=('arial',15),bd=7,width=10)
wheatEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
wheatEntry.insert(0,0)

# Suger
sugerLabel = Label(groceryFrame,text='Suger : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
sugerLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

sugerEntry = Entry(groceryFrame,font=('arial',15),bd=7,width=10)
sugerEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
sugerEntry.insert(0,0)

# Tea
teaLabel = Label(groceryFrame,text='Tea : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
teaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

teaEntry = Entry(groceryFrame,font=('arial',15),bd=7,width=10)
teaEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
teaEntry.insert(0,0)


# Cold Drinks Frame
coldDrinksFrame = LabelFrame(productFrame,text='Cold Drinks',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=10,relief=GROOVE)
coldDrinksFrame.grid(row=0,column=2,padx=10)


# Maaza
maazaLabel = Label(coldDrinksFrame,text='Maaza : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
maazaLabel.grid(row=0,column=0,pady=9,padx=10,sticky='w')

maazaEntry = Entry(coldDrinksFrame,font=('arial',15),bd=7,width=10)
maazaEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')
maazaEntry.insert(0,0)

# Pepsi
pepsiLabel = Label(coldDrinksFrame,text='Pepsi : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
pepsiLabel.grid(row=1,column=0,pady=9,padx=10,sticky='w')

pepsiEntry = Entry(coldDrinksFrame,font=('arial',15),bd=7,width=10)
pepsiEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')
pepsiEntry.insert(0,0)

# Sprite
spriteLabel = Label(coldDrinksFrame,text='Sprite : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
spriteLabel.grid(row=2,column=0,pady=9,padx=10,sticky='w')

spriteEntry = Entry(coldDrinksFrame,font=('arial',15),bd=7,width=10)
spriteEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')
spriteEntry.insert(0,0)

# Dew
dewLabel = Label(coldDrinksFrame,text='Dew : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
dewLabel.grid(row=3,column=0,pady=9,padx=10,sticky='w')

dewEntry = Entry(coldDrinksFrame,font=('arial',15),bd=7,width=10)
dewEntry.grid(row=3,column=1,pady=9,padx=10,sticky='w')
dewEntry.insert(0,0)

# Frooti
frootiLabel = Label(coldDrinksFrame,text='Frooti : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
frootiLabel.grid(row=4,column=0,pady=9,padx=10,sticky='w')

frootiEntry = Entry(coldDrinksFrame,font=('arial',15),bd=7,width=10)
frootiEntry.grid(row=4,column=1,pady=9,padx=10,sticky='w')
frootiEntry.insert(0,0)

# Coca Cola
cocaColaLabel = Label(coldDrinksFrame,text='Coca Cola : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
cocaColaLabel.grid(row=5,column=0,pady=9,padx=10,sticky='w')

cocaColaEntry = Entry(coldDrinksFrame,font=('arial',15),bd=7,width=10)
cocaColaEntry.grid(row=5,column=1,pady=9,padx=10,sticky='w')
cocaColaEntry.insert(0,0)


# Bill Area
billFrame = Frame(productFrame,bd=8,relief=GROOVE)
billFrame.grid(row=0,column=3,padx=50,pady=7)

scrollbar = Scrollbar(billFrame,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)

billLabel = Label(billFrame,text='Bill Area',font=('times new roman',15,'bold'),bd=7,relief=GROOVE)
billLabel.pack(fill=X)

billText = Text(billFrame,width=55,height=20,yscrollcommand=scrollbar.set)
billText.pack()


scrollbar.config(command=billText.yview)


# Bill Menu
billMenuLabelFrame = LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),bg='gray20',fg='gold',bd=10,relief=GROOVE)
billMenuLabelFrame.pack(fill=X)

# Cosmaic Price
cosmaticPriceLabel = Label(billMenuLabelFrame,text='Cosmaic Price : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
cosmaticPriceLabel.grid(row=0,column=0,pady=9,padx=(20,10),sticky='w')

cosmaticPriceEntry = Entry(billMenuLabelFrame,font=('arial',15),bd=7,width=10)
cosmaticPriceEntry.grid(row=0,column=1,pady=9,padx=10,sticky='w')

# Grocery Price
groceryPriceLabel = Label(billMenuLabelFrame,text='Grocery Price : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
groceryPriceLabel.grid(row=1,column=0,pady=9,padx=(20,10),sticky='w')

groceryPriceEntry = Entry(billMenuLabelFrame,font=('arial',15),bd=7,width=10)
groceryPriceEntry.grid(row=1,column=1,pady=9,padx=10,sticky='w')

# Cold Drinks Price
coldDrinksPriceLabel = Label(billMenuLabelFrame,text='Cold Drinks Price : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
coldDrinksPriceLabel.grid(row=2,column=0,pady=9,padx=(20,10),sticky='w')

coldDrinksPriceEntry = Entry(billMenuLabelFrame,font=('arial',15),bd=7,width=10)
coldDrinksPriceEntry.grid(row=2,column=1,pady=9,padx=10,sticky='w')

# Cosmatic Tax
cosmaticTaxLabel = Label(billMenuLabelFrame,text='Cosmatic Tax : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
cosmaticTaxLabel.grid(row=0,column=2,pady=9,padx=(20,10),sticky='w')

cosmaticTaxEntry = Entry(billMenuLabelFrame,font=('arial',15),bd=7,width=10)
cosmaticTaxEntry.grid(row=0,column=3,pady=9,padx=10,sticky='w')

# Grocery Tax
groceryTaxLabel = Label(billMenuLabelFrame,text='Grocery Tax : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
groceryTaxLabel.grid(row=1,column=2,pady=9,padx=(20,10),sticky='w')

groceryTaxEntry = Entry(billMenuLabelFrame,font=('arial',15),bd=7,width=10)
groceryTaxEntry.grid(row=1,column=3,pady=9,padx=10,sticky='w')

# Cold Drinks Tax
coldDrinksTaxLabel = Label(billMenuLabelFrame,text='Cold Drinks Tax : ',font=('times new roman',15,'bold'),bg='gray20',fg='white')
coldDrinksTaxLabel.grid(row=2,column=2,pady=9,padx=(20,10),sticky='w')

coldDrinksTaxEntry = Entry(billMenuLabelFrame,font=('arial',15),bd=7,width=10)
coldDrinksTaxEntry.grid(row=2,column=3,pady=9,padx=10,sticky='w')



# Buttons
buttonFrame = Frame(billMenuLabelFrame,bd=8,relief=GROOVE)
buttonFrame.grid(row=0,column=4,rowspan=3,padx=60)

# Total Button
totalButton = Button(buttonFrame,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8,command=total)
totalButton.grid(row=0,column=0,padx=5,pady=20)

# Bill Button
billButton = Button(buttonFrame,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8)
billButton.grid(row=0,column=1,padx=5,pady=20)

# Email Button
emailButton = Button(buttonFrame,text='Email',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8)
emailButton.grid(row=0,column=2,padx=5,pady=20)

# Print Button
printButton = Button(buttonFrame,text='Print',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8)
printButton.grid(row=0,column=3,padx=5,pady=20)

# Clear Button
clearButton = Button(buttonFrame,text='Clear',font=('arial',16,'bold'),bg='gray20',fg='white',bd=5,width=8)
clearButton.grid(row=0,column=4,padx=5,pady=20)



root.mainloop()