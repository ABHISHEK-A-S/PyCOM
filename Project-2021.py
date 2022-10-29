import random
from tkinter import *
from tkinter import messagebox
import mysql.connector
from os import system
from prettytable import PrettyTable
from tqdm import tqdm
import datetime


mycon=mysql.connector.connect(host="localhost",user="root",passwd="ueztjk7rtb",database='project')
cursor=mycon.cursor()
'''Admin='create table project2021(PhNo varchar(20) primary key not null,Name varchar(20),Processor varchar(50),Ram varchar(30),MotherBoard varchar(50),Graphics_Card varchar(50),HardDisk varchar(50),Cpu_Case varchar(50),Monitor varchar(50),Total_price int);'
cursor.execute(Admin)'''
print()


v=datetime.date.today()
print(v)


def Hverify():
    text=['DOGGY','ZZ98nbTu','AQ3vTk','MaAk3Ri']
    window=Tk()
    window.title("Human Verification")
    window.geometry('350x100')
    captcha=StringVar()
    user_input=StringVar()
    

    def set_captcha():
        s=random.choices(text)
        captcha.set(" ".join(s))

    def check():
        if captcha.get()==user_input.get():
            print("You Are A Human...Verified!!!.....CLOSE THE VERIFICATION PAGE TO PROCEED")
        

        else:
            messagebox.showerror("Sorry","Incorrect")
            #print("The Commmand Is Wrong")
        set_captcha()

    Label(window,textvariable=captcha,
          font="Flubber 30 bold underline ").pack()
    Entry(window,textvariable=user_input,
          font='Arail 10 bold').pack(ipady=5)
    Button(window,command=check,text='Verify',
           font='Arial 10').pack()
    Button(window,command=check,text='Quit',
           font='Arial 10').pack()

    set_captcha()
    window.mainloop()
    



def linebar():
    loop=tqdm(total=5000,position=0,leave=False)
    for k in range(5000):
        loop.set_description("Loading Nessecary details....".format(k))
        loop.update(1)
    loop.close()
linebar()

def linebar4():
    
    loop=tqdm(total=5000,position=0,leave=False)
    for k in range(5000):
        loop.set_description("Verifiying Your Phone Number.......".format(k))
        loop.update(1)
    loop.close()

def linebar5():
    
    loop=tqdm(total=5000,position=0,leave=False)
    for k in range(5000):
        loop.set_description("Tracking Your Global Position.......".format(k))
        loop.update(1)
    loop.close()

def linebar6():
    
    loop=tqdm(total=5000,position=0,leave=False)
    for k in range(5000):
        loop.set_description("TroubleShooting tracking failure......".format(k))
        loop.update(1)
    loop.close()
print()

print('................................................................HELLO.....WELCOME TO THE MEGA PC BUILD EMPORIUM...............................................................')
print()
print()
Pprice=0
y=0
Tprice=0
nme=''
fone=''
I=''
p=''
Gen=''
CJ=''

x=''
m=''
mp=0
g=''
gp=0
h=''
hp=0
c=''
cp=0
s=''
sp=0

def name():
    global nme
    nme=input('Please Enter your Name::-')
    u=input("Do You Have Any Correction?[Y/N]")
    if u=='Y' or u=='y':
        name()
        
    else:
        print()
        Hverify()
        print("Name saved succesfully")
        print()
        cl=input("Press any key to continue...")
        system("cls")
    
def phone():
    global fone
    fone=int(input('Enter Your Phone Number::-'))
    linebar4()
    linebar5()
    print("Server Down Error")
    linebar6()
    print("Sorry....Could'nt track ...Error With The GPS system")
    
    u=input("Do You Have Any Correction in your phone number?[Y/N]")
    if u=='Y' or u=='y':
        phone()
        
    else:
        print()
        print("Phone Number saved succesfully")
        print()
        cl=input("Press any key to continue...")
        system("cls")

    
name()
print()
print()
print()
phone()
print()
print()
print()
print()




def GB():
    o=input('Do You Like To Buld GAMING or BUSINESS PURPOSE pc??[B/G]')
    if o=='B' or o=='b':
        print()
        print('OK...You have selected BUSINESS PURPOSE')
        print()
        print()
    elif o=='G' or o=='g':
        print()
        print('OK...You have selected GAMING PURPOSE')
        print()
        print()
    else:
        print()
        print('Sir/Madam.....You cannot move forward without giving appropriate choice')
        GB()
        print()
        cl=input("Press any key to continue...")
        system("cls")

GB()
def linebar1():
    
    loop=tqdm(total=5000,position=0,leave=False)
    for k in range(5000):
        loop.set_description("Please wait while we rummage around the StoreRoom".format(k))
        loop.update(1)
    loop.close()
linebar1()





def procc():
    print("These are all the processors available here::")
    print("1. INTEL")
    print("2. AMD")
    print()
    pro=input("Sir/Madam...Please select your required processor varient:: ")
    print()

    if pro=='1':
        def corepro():
            
            
            global I
            global p
            global Gen
            global CJ
            
            I='Intel'
            print("You have selected intel as your processor")
            print()

            print("The variety of intel processors are given below:")
            print()

            print("1. Core i3")
            print("2. Core i5")
            print("3. Core i7") 
            print("4. Core i9")
            print()
            
        
            pri=input("Enter your required processor varient:")
            global Pprice
            if pri=='1':
                p='Core i3'
                print()
                print("You have selected Core i3")
                Cprice=10000
            elif pri=="2":
                print()
                print("You have selected Core i5")
                p='Core i5'
                Cprice=20000
            elif pri=='3':
                print()
                print("You have selected Core i7")
                p='Core i7'
                Cprice=30000
            elif pri=='4':
                print()
                print("You have selected Core i9")
                p='Core i9'
                Cprice=40000
                print()
                print()
            else:
                print()
                print('Oops...Out of choice')
                corepro()
        
                
            print()
            Gen=input('Enter Your Required Gen[Currently available Gens are 8/9/10]:')
            if Gen=='8':
                print()
                print("You have selected 8th Gen")
                Gprice=1000
            elif Gen=='9':
                print()
                print("You have selected 9th Gen")
                Gprice=2000
            elif Gen=='10':
                print()
                print("You have selected 10th Gen")
                Gprice=3000
            else:
                print()
                print("Oops...Out of choice")
                corepro()
            print()
            print("So...My dear customer...Your processor selection is",I,p,Gen,'Th Gen')
            Pprice=Cprice+Gprice
            print()
            print('PRICE OF PROCESSOR ONLY ₹',Pprice)
            
            print()
            CJ=I+' '+p+' '+Gen
            
            corr=input('Do you have any correction?[Y/N]')
            if corr=='Y' or corr=='y':
                corepro()
            else:
                print()
                print()
                print()
                cl=input("Press any key to continue...")
                system("cls")

        corepro()
                
        print()
        print()
        

        
        
    elif pro=='2':
        def amd():
            global CJ
            global Pprice
            print ("You have selected AMD as your processor")
            print()
            print("The variety of AMD processors are given below:")
            print("1. AMD Ryzen")
            print("2. AMD Athlon")
            print()
            print()

            Apri=input("Enter your required processor varient:")
            
            if Apri=='1':
                p='AMD Ryzen™'
                print()
                print("You have selected AMD Ryzen")
                Cprice=9000
                print()
                print()
            elif Apri=="2":
                print()
                print("You have selected AMD Athlon")
                p='AMD Athlon™'
                Cprice=18000
                print()
            else:
                print()
                print('Oops...Out of choice')
                amd()
           

            Gen=input('Enter Your Required Gen[Currently available Gens are 3200G/3500G/4000G]:')
            if Gen=='3200G':
                print()
                print("You have selected 3200G")
                Gprice=900
                print()
            elif Gen=='3500G':
                print()
                print("You have selected 3500G")
                Gprice=1700
                print()
            elif Gen=='4000G':
                print()
                print("You have selected 4000G")
                Gprice=2000
                print()
            else:
                print()
                print('Oops...Out of choice')
                amd()
            
            print()
            print("So...Dear customer...Your processor selection is",p,Gen)
            Pprice=Cprice+Gprice
            print()
            print('Price Of Processor Only is ₹',Pprice)
            CJ=p+' '+Gen
            print()
            corr=input('Do you have any correction?[Y/N]')
            if corr=='Y' or corr=='y':
                amd()
            else:
                print()
                print()
                cl=input("Press any key to continue...")
                system("cls")

                

        
        amd()
        
    
    else:
        print('Sir/Madam.....You cannot move forward without giving appropriate choice')
        procc()
        print()
        cl=input("Press any key to continue...")
        system("cls")

procc()










def RAM():
    print()
    global x
    global y
    print('Here are the available RAM variants::-')
    print('1. 4Gb')
    print('2. 8Gb')
    print('3. 16Gb')
    print('4. 32Gb')
    print()
    k=input("Sir/Madam...Please select your required ram varient::-")
    if k=='1':
        print()
        print('You have seleted 4gb ram varient')
        x='4Gb'
        y=1500
    elif k=='2':
        print()
        print('You have seleted 8gb ram varient')
        x='8Gb'
        y=2500
    elif k=='3':
        print()
        print('You have seleted 16gb ram varient')
        x='16Gb'
        y=5500
        
    elif k=='4':
        print()
        print('You have seleted 32gb ram varient')
        x='32Gb'
        y=7500
   
    else:
        print()
        print('Sir/Madam.....You cannot move forward without giving appropriate choice')
        RAM()
    print()
    print('Price of selected RAM varient is only ₹',y)
    print()
    corr=input('Do you have any correction?[Y/N]')
    if corr=='Y' or corr=='y':
                RAM()
    else:
        print()
        print()
        cl=input("Press any key to continue...")
        system("cls")

RAM()



def MB():
    global m
    global mp
    print()
    print('Here are the available MotherBoards varients :-')
    print('1. Asus ROG Strix')
    print('2. Gigabyte Technology')
    print('3. MSI B450 GAMING PLUS MAX AM4 ATX')
    print('4. Aorus Gaming')
    print()
    print()
    mb=input("Sir/Madam...Please select your required MotherBoard varient :-")
    if mb=='1':
        print()
        print('You have seleted Asus ROG Strix  MotherBoard varient ')
        m='Asus ROG Strix'
        mp=26000
    elif mb=='2':
        print()
        print('You have seleted Gigabyte Technology ')
        m='Gigabyte Technology'
        mp=6000
    elif mb=='3':
        print()
        print('You have seleted MSI B450 GAMING PLUS MAX AM4 ATX  MotherBoard varient ')
        m='MSI B450 GAMING PLUS MAX AM4 ATX'
        mp=17000
        
    elif mb=='4':
        print()
        print('You have seleted Aorus Gaming MotherBoard varient')
        m='Aorus Gaming'
        mp=22000
    else:
        print()
        print('Sir/Madam.....You cannot move forward without giving appropriate choice')
        MB()
    print()
    print()
    print('Price of selected MotherBoard varient only is ₹',mp)
    print()
    corr=input('Do you have any correction?[Y/N]')
    print()
    if corr=='Y' or corr=='y':
                MB()
    else:
        print()
        print()
        cl=input("Press any key to continue...")
        system("cls")
MB()      



def GPU():
    
    print()
    print()
    global g
    global gp
    print('Here are the available Graphics card varients')
    print('1. Nvidia GEFORCE GTX 1050 Ti (4Gb/DDR4)')
    print('2. Nvidia GEFORCE GTX 1070 Super (6Gb/DDR5)')
    print('3. Nvidia Titan (8Gb/DDR5)')
    print('4. Nvidia GEFORCE RTX 2080 Ti (10Gb/DDR6)')
    print('5. Nvidia GEFORCE RTX 3090 Ti (24Gb/GDDR6X)')
    print()
    print()
    gpu=input("Sir/Madam...Please select your required Graphics Card varient :-")
    if gpu=='1':
        print()
        print('You have seleted Nvidia GEFORCE GTX 1050 Ti (4Gb/DDR4) varient ')
        g='Nvidia GEFORCE GTX 1050 Ti (4Gb/DDR4)'
        gp=20000
    elif gpu=='2':
        print()
        print('You have seleted Nvidia GEFORCE GTX 1070 Super (6Gb/DDR5) ')
        g='Nvidia GEFORCE GTX 1070 Super (6Gb/DDR5)'
        gp=36000
    elif gpu=='3':
        print()
        print('You have seleted Nvidia Titan (8Gb/DDR5) varient ')
        g='Nvidia Titan (8Gb/DDR5)'
        gp=184963
        
    elif gpu=='4':
        print()
        print('You have seleted Nvidia GEFORCE RTX 2080 Ti (10Gb/DDR6) varient')
        g='Nvidia GEFORCE RTX 2080 Ti (10Gb/DDR6)'
        gp=99000
    elif gpu=='5':
        print()
        print('You have seleted Nvidia GEFORCE RTX 3090 Ti (24Gb/GDDR6X) varient')
        g='Nvidia GEFORCE RTX 3090 Ti (24Gb/GDDR6X)'
        gp=152000
    else:
        print()
        print('Sir/Madam.....You cannot move forward without giving appropriate choice')
        GPU()
    print()
    print()
    print('Price of selected Graphics card varient only is ₹',gp)
    print()
    corr=input('Do you have any correction?[Y/N]')
    if corr=='Y' or corr=='y':
                GPU()
    else:
        print()
        print()
        cl=input("Press any key to continue...")
        system("cls")

print()
print()
gpuneed=input("Does Your PC Need Graphics card?[Y/N]::-")
if gpuneed=='Y' or gpuneed=='y':
    print()
    GPU()
else:
    print()
    print("You have not not selected Graphics Card for Your PC ")

print()
print()
def HDD():
    print()
    print()
    global h
    global hp
    print('Here are the available HardDisk varients')
    print('1. Kingston 1Tb')
    print('2. Kingston 2Tb')
    print()
    print()
    hdd=input("Sir/Madam...Please select your required HardDisk varient :-")
    if hdd=='1':
        print()
        print('You have seleted Kingston 1Tb varient ')
        h='Kingston 1Tb'
        hp=3000
    elif hdd=='2':
        print()
        print('You have seleted Kingston 2Tb ')
        h='Kingston 2Tb'
        hp=5500
    else:
        print()
        print('Sir/Madam.....You cannot move forward without giving appropriate choice')
        HDD()
    print()
    print()
    print('Price of selected HardDisk varient only is ₹',hp)
    print()
    corr=input('Do you have any correction?[Y/N]')
    if corr=='Y' or corr=='y':
                HDD()
    else:
        print()
        print()
        cl=input("Press any key to continue...")
        system("cls")
HDD()
print()
print()
def CASE():
    print()
    print()
    global c
    global cp
    print('Here are the available CPU case varients')
    print('1. Corsair iCUE 465X RGB ')
    print('2. Corsair iCUE 4000X RGB')
    print()
    print()
    case=input("Sir/Madam...Please select your required CPU case varient :-")
    if case=='1':
        print()
        print('You have seleted Corsair iCUE 465X RGB varient ')
        c='Corsair iCUE 465X RGB'
        cp=8000
    elif case=='2':
        print()
        print('You have seleted Corsair iCUE 4000X RGB ')
        c='Corsair iCUE 4000X RGB'
        cp=12000
    else:
        print()
        print('Sir/Madam.....You cannot move forward without giving appropriate choice')
        CASE()
    print()
    print('Price of selected CPU case varient only is ₹',cp)
    print()
    corr=input('Do you have any correction?[Y/N]')
    if corr=='Y' or corr=='y':
                CASE()
    else:
        print()
        print()
        cl=input("Press any key to continue...")
        system("cls")
CASE()

print()
print()

def MONI():
    print()
    print()
    global s
    global sp
    print('Here are the available Monitor varients')
    print('1. Samsung 23.5 inch Curved 75Hz ')
    print('2. LG 27 inch 4K-UHD Monitor 120Hz ')
    print('3. BenQ 27 Inch QHD 1440p IPS 144Hz')
    print()
    moni=input("Sir/Madam...Please select your required Monitor varient :-")
    if moni=='1':
        print()
        print('You have seleted Samsung 23.5 inch Curved 75Hz varient ')
        s='Samsung 23.5 inch Curved 75Hz'
        sp=14000
    elif moni=='2':
        print()
        print('You have seleted LG 27 inch 4K-UHD Monitor 120Hz ')
        s='LG 27 inch 4K-UHD Monitor 120Hz'
        sp=30000
    elif moni=='3':
        print()
        print('You have seleted BenQ 27 Inch QHD 1440p IPS 144Hz ')
        s='BenQ 27 Inch QHD 1440p IPS 144Hz'
        sp=42000
    else:
        print()
        print('Sir/Madam.....You cannot move forward without giving appropriate choice')
        MONI()
    print()
    print('Price of selected Monitor varient only is ₹',sp)
    print()
    corr=input('Do you have any correction?[Y/N]')
    print()
    if corr=='Y' or corr=='y':
                MONI()
    else:
        print()
        print()
        cl=input("Press any key to continue...")
        system("cls")
MONI()

print()
print()

def linebar2():
    
    loop=tqdm(total=15000,position=0,leave=False)
    for k in range(15000):
        loop.set_description("Please wait while Load the Bill...".format(k))
        loop.update(1)
    loop.close()
linebar2()
def linebar3():
    
    loop=tqdm(total=8000,position=0,leave=False)
    for k in range(8000):
        loop.set_description("Please wait while Load the  Final Bill...".format(k))
        loop.update(1)
    loop.close()

    
def DispAll():
    cursor=mycon.cursor()
    sql='select * from project2021 ;'
    cursor.execute(sql)
    data=cursor.fetchall()
    t=PrettyTable(['Phone Number','Name',"Processor",'RAM','MotherBoard','Graphics Card','HardDisk','Cpu Case','Monitor','Total'])
    for rec in data:
        t.add_row(list(rec))
    print(t.get_string(title='Final Billings'))
    mycon.commit()

print()


Tprice=Pprice+y+mp+gp+hp+cp+sp
val=(fone,nme,CJ,x,m,g,h,c,s,Tprice)
Admin='insert into project2021 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
cursor.execute(Admin,val)

DispAll()

  
print()
print()
def Modify():
    global Tprice
    Tprice=Tprice-gp
    cursor=mycon.cursor()
    print()
    Fon=int(input('Enter Phone Number to be changed:-'))
    
    GPU()
    sql='update project2021 set Graphics_Card=%s,Total_price=%s where PhNo=%s;'
    val=(g,gp+Tprice,Fon)
    cursor.execute(sql,val)
    mycon.commit()
    
print()
print()

pmodi=input('Do You Need To Modify The Graphics Card[Y/N]::-')
if pmodi=='y' or pmodi=='Y':
    Modify()
    iy=input("Do You Have To See Your Renewed Bill?[Y/N]")
    print()
    cl=input("Press any key to continue...")
    system("cls")
    

    if iy=='Y' or iy=='y':
        linebar3()
        DispAll()
    else:
        print()
        print('ThankYou Dear Customer......Poyi kidann urangada mone!!!')
else:
    print()
    print()
    print("TOTAL PRICE INCLUDING TAX==₹",Tprice)

  
print()
print()
print()
print()
print("CONGRAGULATIONS !!!! YOU ARE AWARDED A GAMING MOUSE+KEYBOARD FOR ABSOLUTELY FREE.....")
print()
print()

    
mycon.close()
print()
jum=input("Enter any key to continue::")
