import time
import tkinter
from tkinter import *
import random
from tkinter import filedialog, messagebox
import pyttsx3
# pyttsx3 for text to speak.


m = Tk()
m.geometry("1000x900")

m.title("STEAKY STAKES RESTAURANT")
l = Label(m)
l.place(x=0, y=0, relwidth=1, relheight=1)

Photo_list=[]
for i in range(3):
    Photo_list.append(f"RES_{i}")

# initialisation the engine var to speak soething
engine = pyttsx3.init()


say = ['WELCOME TO STEAKY STAKES RESTAURANT','We are providing best quality meat, delicious and mouthwatering steaks',"Let's order"]


for j in range(3):


    # testing : engine mein values ko add karane ke liye.

    try:
        x = Photo_list[j]
  
        bg = PhotoImage(file = f"{x}.png")
        l.config(image=bg)
        m.update()
        engine.say(say[j])
        engine.runAndWait()


        time.sleep(1)
    except RuntimeError as e:
        pass
try:
    m.destroy()
except tkinter.TclError as e:
    pass




root = Tk()

def reset():
    e1.set(0)
    e2.set(0)
    e3.set(0)
    e4.set(0)
    e5.set(0)
    e6.set(0)
    e7.set(0)
    e8.set(0)
    e9.set(0)
    e10.set(0)
    e11.set(0)
    e12.set(0)
    e13.set(0)


    cost_of_steak_var.set('')
    ser_tax_var.set('')
    total_cost_var.set('')

    var_1.set(0)
    var_2.set(0)
    var_3.set(0)
    var_4.set(0)
    var_5.set(0)
    var_6.set(0)
    var_7.set(0)
    var_8.set(0)
    var_9.set(0)
    var_10.set(0)
    var_11.set(0)
    var_12.set(0)
    var_13.set(0)
    var_14.set(0)

    e = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e1, state=DISABLED).place(x=250, y=40)
    num_of_BEEF_sizling_STEAK = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e2,state=DISABLED).place(x=275, y=75)
    num_of_BEEF_steaky_STEAK = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e3, state=DISABLED).place(x=340, y=110)
    num_of_BEEF_sizling_steaky_STEAK = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e4,state=DISABLED).place(x=370, y=150)
    num_of_CHICKEN_STEAK = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e5, state=DISABLED).place(x=250, y=185)
    num_of_CHICKEN_STEAKY_special = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e6,state=DISABLED).place(x=300, y=220)
    num_of_CHICKEN_sizzling = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e7, state=DISABLED).place(x=290, y=255)
    num_of_grilled_steak = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e8, state=DISABLED).place(x=235, y=290)
    num_of_grilled_steak_caperherb = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e9,state=DISABLED).place(x=340, y=330)
    num_of_special_fries = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e10, state=DISABLED).place(x=300, y=365)
    num_of_sandwich = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e11, state=DISABLED).place(x=320,y=400)
    num_of_sandwich_steaky_special = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e12,state=DISABLED).place(x=322, y=435)
    num_of_deal = Entry(R_frame,font="Halvetica 10 bold",bd=7,textvariable=e13,state=DISABLED).place(x=470,y=30)

def quit():
    exit()

def change():   # If check button is on then entry becomes enabled.
    global e
    if var_1.get() == 1:
        e = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e1, state=NORMAL).place(x=250, y=40)
    else:
        e = Entry(menu_frame, font="Halvetica 13 bold", bd=7, textvariable=e1, state=DISABLED).place(x=250, y=40)
        e1.set(0)
        e1.focus.get()
def change_1():
    if var_2.get() == 1:
        num_of_BEEF_sizling_STEAK = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e2,state=NORMAL).place(x=275,y=75)
    else:
        num_of_BEEF_sizling_STEAK = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e2,state=DISABLED).place(x=275,y=75)
        e2.set(0)

def change_2():
    if var_3.get() == 1:
        num_of_BEEF_steaky_STEAK = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e3,state=NORMAL).place(x=340,y=110)
    else:
        num_of_BEEF_steaky_STEAK = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e3,state=DISABLED).place(x=340,y=110)
        e3.set(0)



def change_3():
    if var_4.get() == 1:
        num_of_BEEF_sizling_steaky_STEAK = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e4,state=NORMAL).place(x=370,y=150)
    else:
        num_of_BEEF_sizling_steaky_STEAK = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e4,state=DISABLED).place(x=370,y=150)
        e4.set(0)

def change_4():
    if var_5.get() == 1:
        num_of_CHICKEN_STEAK = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e5,state=NORMAL).place(x=250,y=185)
    else:
        num_of_CHICKEN_STEAK = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e5,state=DISABLED).place(x=250,y=185)
        e5.set(0)

def change_5():
    if var_6.get() == 1:
        num_of_CHICKEN_STEAKY_special = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e6,state=NORMAL).place(x=300,y=220)
    else:
        num_of_CHICKEN_STEAKY_special = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e6,state=DISABLED).place(x=300,y=220)
        e6.set(0)

def change_6():
    if var_7.get() == 1:
        num_of_CHICKEN_sizzling = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e7,state=NORMAL).place(x=290,y=255)
    else:
        num_of_CHICKEN_sizzling = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e7,state=DISABLED).place(x=290,y=255)
        e7.set(0)
def change_7():
    if var_8.get() == 1:
        num_of_grilled_steak = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e8,state=NORMAL).place(x=235,y=290)
    else:
        num_of_grilled_steak = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e8,state=DISABLED).place(x=235,y=290)
        e8.set(0)
def change_8():
    if var_9.get() == 1:
        num_of_grilled_steak_caperherb = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e9,state=NORMAL).place(x=340,y=330)
    else:
        num_of_grilled_steak_caperherb = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e9,state=DISABLED).place(x=340,y=330)
        e9.set(0)
def change_9():
    if var_10.get() == 1:
        num_of_special_fries = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e10,state=NORMAL).place(x=300,y=365)
    else:
        num_of_special_fries = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e10,state=DISABLED).place(x=300,y=365)
        e10.set(0)
def change_10():
    if var_11.get() == 1:
        num_of_sandwich = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e11,state=NORMAL).place(x=320,y=400)
    else:

        num_of_sandwich = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e11,state=DISABLED).place(x=320,y=400)
        e11.set(0)

def change_11():
    if var_13.get() == 1:
        num_of_sandwich_steaky_special = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e12,state=NORMAL).place(x=322,y=435)
    else:

        num_of_sandwich_steaky_special = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e12,state=DISABLED).place(x=322,y=435)
        e12.set(0)


def change_12():
    if var_14.get() == 1:
        num_of_deal = Entry(R_frame,font="Halvetica 10 bold",bd=7,textvariable=e13,state=NORMAL).place(x=470,y=30)

    else:

        num_of_deal = Entry(R_frame,font="Halvetica 10 bold",bd=7,textvariable=e13,state=DISABLED).place(x=470,y=30)
        e13.set(0)








def save_receipt():
    global j
    if e1.get() != 0:
        b0 = f"\t\t\tBEEF STEAK \t\t\t{str(e1.get())} \t\t\tRs{str(int(e1.get())*600)}"
    else:
        b0 = ''

    if e2.get() != 0:
        b1 = f"\t\t\tBEEF SIZZLING STEAK \t\t{str(e2.get())} \t\t\tRs{str(int(e2.get())*800)}"
    else:
        b1 = ''

    if e3.get() != 0:
        b2 = f"\t\t\tSTEAKY SPECIAL BEEF \t\t{str(e3.get())} \t\t\tRs{str(int(e3.get())*1000)}"
    else:
        b2 = ''

    if e4.get() != 0:
        b3 = f"\t\t\tBEEF SIZZLING STEAKY SPECIAL    {str(e4.get())} \t\t\tRs{str(int(e4.get())*1400)}"
    else:
        b3 = ''

    if e5.get() != 0:
        b4 = f"\t\t\tCHICKEN STEAK \t\t\t{str(e5.get())} \t\t\tRs{str(int(e5.get())*650)}"
    else:
        b4 = ''

    if e6.get() != 0:
        b5 = f"\t\t\tCHICKEN STEAKY SPECIAL \t\t{str(e6.get())} \t\t\tRs{str(int(e6.get())*1200)}"
    else:
        b5 = ''

    if e7.get() != 0:
        b6 = f"\t\t\tCHICKEN SIZZLING STEAK \t\t{str(e7.get())} \t\t\tRs{str(int(e7.get())*1100)}"
    else:
        b6 = ''

    if e8.get() != 0:
        b7 = f"\t\t\tGRILLED STEAK \t\t\t{str(e8.get())} \t\t\tRs{str(int(e8.get())*1000)}"
    else:
        b7 = ''

    if e9.get() != 0:
        b8 = f"\t\t\tGRILLED STEAK & CAPERHERB \t{str(e9.get())} \t\t\tRs{str(int(e9.get())*1600)}"
    else:
        b8 = ''

    if e10.get() != 0:
        b9 = f"\t\t\tSTEAKY SPECIAL FRIES \t\t{str(e10.get())} \t\t\tRs{str(int(e10.get())*800)}"
    else:
        b9 = ''

    if e11.get() != 0:
        b10 = f"\t\t\tGRILLED STEAK SANDWICH \t\t{str(e11.get())} \t\t\tRs{str(int(e11.get())*700)}"
    else:
        b10 = ''

    if e12.get() != 0:
        b11 = f"\t\t\tSTEAKY SPECIAL SANDWICH \t{str(e12.get())} \t\t\tRs{str(int(e12.get())*1000)}"
    else:
        b11 = ''

    if e13.get() != 0:
        b12 = f"\t\t\tSTEAKY SPECIAL DEAL \t\t{str(e13.get())} \t\t\tRs{str(int(e13.get())*4500)}"
    else:
        b12 = ''



    b = [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12]
    d = ''
    for k in range(13):
        if b[k] != '':
            d = d + b[k] + '\n'




    items1 = int(e1.get())

    items2 = int(e2.get())

    items3 = int(e3.get())

    items4 = int(e4.get())

    items5 = int(e5.get())

    items6 = int(e6.get())

    items7 = int(e7.get())

    items8 = int(e8.get())

    items9 = int(e9.get())

    items10 = int(e10.get())

    items11 = int(e11.get())

    items12 = int(e12.get())

    items13 = int(e13.get())

    total_cost = (items1 * 600) + (items2 * 800) + (items3 * 1000) + (items4 * 1400) + (items5 * 650) + (items6 * 1200) + (items7 * 1100) + (items8 * 1000) + (items9 * 1600) + (items10 * 800) + (items11 * 700) + (items12 * 1000) + (items13 * 4500)
    t = f"Rs{str(total_cost)}"
    cost_of_steak_var.set(str(t))

    gst = (10 / 100) * total_cost
    service_tax_p = f"Rs{str(gst)}"
    ser_tax_var.set(service_tax_p)

    tot_cost = int(total_cost) + gst

    t_cost = f"Rs{str(tot_cost)}"
    total_cost_var.set(str(t_cost))

    x = random.randint(0,10000)
    bill_no = f"BILL NO.{str(x)}"
    date = time.strftime('%d/%m/%Y')
    m = f"Receipt no:   {bill_no}   {str(date)}"

    kh = f"Receipt number {bill_no}" #Initializing this as file name of the bill.

    c = "ITEMS \t\t QUANTITY \t\t        PRICE"
    bill_data = f"{m} \n\n ***********************STEAKY STAKE RESTAURANT************** \n \
                            {c} \n {d}\
                            \n\n\t\t\t\tCost of STEAKS : {t} \n\n\t\t\t\t General Slaes Tax : {service_tax_p} \n\n\t\t\t\t TOTAL COST : {t_cost}\n\n\t\t  \
                            ENJOY YOUR MEAL.THANKS FOR COMING."




    if t == 'Rs0': # If nothing is selected.
        messagebox.showinfo('STEAKY STAKE RESTAURANT BILL INFO','No Items Selected.')
    else: # If items were selected.
        url = filedialog.asksaveasfile(initialdir=r"D:\RESTAURANT MANAGEMENT BILLS",initialfile=kh,title="BILL",mode="w", defaultextension='.txt')

        if url == None: # If cancel is clicked and you don't want to save the bill
            pass
        else: # When the bill is going to save in a file
            url.write(bill_data)
            url.close()
            messagebox.showinfo("STEAKY STEAK RESTAURANT BILL INFO", 'The bill have been saved successfully')




    j += 1 #for incrementing the value of j on every new bill appending to the manager.
    data_for_manager =f"*****************************{m}****************************** \nSERIAL NO.{j}\n \
                            {c} \n {d}\
                            \n\n\t\t\t\tCost of STEAKS : {t} \n\n\t\t\t\t General Slaes Tax : {service_tax_p} \n\n\t \
                            TOTAL COST : {t_cost}\n\n\t\t  "
    f = open(r"D:\RESTAURANT MANAGER\BILLING DETAILS", 'a')
    f.write(data_for_manager)
    f.close()



def total_cost():

    items1 = int(e1.get())

    items2 = int(e2.get())

    items3 = int(e3.get())

    items4 = int(e4.get())

    items5 = int(e5.get())

    items6 = int(e6.get())

    items7 = int(e7.get())

    items8 = int(e8.get())

    items9 = int(e9.get())

    items10 = int(e10.get())

    items11 = int(e11.get())

    items12 = int(e12.get())

    items13 = int(e13.get())


    total_cost = (items1*600)+(items2*800)+(items3*1000)+(items4*1400)+(items5*650)+(items6*1200)+(items7*1100)+(items8*1000)+(items9*1600)+(items10*800)+(items11*700)+(items12*1000)+(items13*4500)
    t = f"Rs{str(total_cost)}"
    cost_of_steak_var.set(str(t))

    gst = (10/100)*total_cost
    service_tax_p = f"Rs{str(gst)}"
    ser_tax_var.set(service_tax_p)

    tot_cost = int(total_cost) + gst

    t_cost = f"Rs{str(tot_cost)}"
    total_cost_var.set(str(t_cost))


root.title("RESTAURANT MANAGEMENT SYSTEM PROJECT")
root.config(background="bisque")

mainframe = Frame(root,bd=10, relief=RIDGE).place()

Label_rest_name = Label(mainframe, text="STEAKY STAKES \n We are providing best quality meat, mouthwatering and delicious steaks",
                        font="conicsansms 19 bold",relief=RIDGE,bd=8,pady=5,fg="firebrick",bg="alice blue")
Label_rest_name.pack(side=TOP, fill=X)

# FRAMES
# Left Frame with steaks menu and cost frame
menu_frame = Frame(root,bd=10,relief=RIDGE,bg="lemon chiffon",width=1200)
menu_frame.pack(side=LEFT,anchor="nw")



cost_frame = Frame(menu_frame,bd=4,relief=RIDGE)
cost_frame.pack(side=BOTTOM)



drinks_frame = LabelFrame(menu_frame,text="DRINKS",font="Halvetica 14 bold",bd=7,relief=RIDGE).pack(side=LEFT)

# RIght Frame With Receipt and calculator
R_frame = Frame(root, bd=10, relief=RIDGE, bg='mint cream',padx=50)
R_frame.pack(side=LEFT,anchor=W,fill=X)




# VARIABLES
var_1=IntVar()
var_2=IntVar()
var_3=IntVar()
var_4=IntVar()
var_5=IntVar()
var_6=IntVar()
var_7=IntVar()
var_8=IntVar()
var_9=IntVar()
var_10=IntVar()
var_11=IntVar()
var_12=IntVar()
var_13=IntVar()
var_14=IntVar()
var_15=IntVar()

e1 = IntVar()
e2 = IntVar()
e3 = IntVar()
e4 = IntVar()
e5 = IntVar()
e6 = IntVar()
e7 = IntVar()
e8 = IntVar()
e9 = IntVar()
e10 = IntVar()
e11 = IntVar()
e12 = IntVar()
e13 = IntVar()



# Setting the value initially to be zero
e1.set(0)
e2.set(0)
e3.set(0)
e4.set(0)
e5.set(0)
e6.set(0)
e7.set(0)
e8.set(0)
e9.set(0)
e10.set(0)
e11.set(0)
e12.set(0)
e13.set(0)

deal = Checkbutton(R_frame,text="STEAKY SPECIAL DEAL\n2SPECIAL STAKES AND 1 SPECIAL SANDWICH",font="Halvetica 15 bold",onvalue=1,offvalue=0,variable=var_14,command=change_12,relief=RIDGE).pack(anchor="nw",pady=20)
num_of_deal = Entry(R_frame,font="Halvetica 10 bold",bd=7,textvariable=e13,state=DISABLED).place(x=470,y=30)

# STEAKS MENU
l = Label(menu_frame,text="MENU OF STEAKY STAKES :BEST STEAKS ",font="comicsansms 20 bold").pack(side=TOP,anchor="nw")
beef_steak_normal = Checkbutton(menu_frame,text="BEEF STEAK",font="Halvetica 15 bold",onvalue=1,offvalue=0,variable=var_1,command=change).pack(anchor="nw")
beef_sizzling_stake= Checkbutton(menu_frame,text="BEEF SIZZLING STEAK",font="Halvetica 15 bold",onvalue=1,offvalue=0,variable=var_2,command=change_1).pack(anchor="nw")
beef_steaky_special= Checkbutton(menu_frame,text="STEAKY SPECIAL BEEF STEAK",font="Halvetica 15 bold",onvalue=1,offvalue=0,variable=var_3,command=change_2).pack(anchor="nw")
beef_sizzling_steaky= Checkbutton(menu_frame,text="BEEF SIZZLING STEAKY SPECIAL",font="Halvetica 15 bold",onvalue=1,offvalue=0,variable=var_4,command=change_3).pack(anchor="nw")
chicken_steak = Checkbutton(menu_frame,text="CHICKEN STEAK",font="Halvetica 15 bold",onvalue=1,offvalue=0,variable=var_5,command=change_4).pack(anchor="nw")
steaky_chicken = Checkbutton(menu_frame,text="CHICKEN STEAKY SPECIAL",font="Halvetica 15 bold",onvalue=1,offvalue=0,variable=var_6,command=change_5).pack(anchor="nw")
sizzling_chicken = Checkbutton(menu_frame,text="CHICKEN SIZZLING STEAK",font="Halvetica 15 bold",onvalue=1,offvalue=0,variable=var_7,command=change_6).pack(anchor="nw")
grilled_chicken = Checkbutton(menu_frame,text="GRILLED STEAK",font="Halvetica 15 bold",onvalue=1,offvalue=0,variable=var_8,command=change_7).pack(anchor="nw")
grilled_with_caper_chicken = Checkbutton(menu_frame,text="GRILLED STEAK & CAPERHERB",font="Halvetica 15 bold",onvalue=1,offvalue=0,variable=var_9,command=change_8).pack(anchor="nw")

steaky_special_fies = Checkbutton(menu_frame,text="STEAKY SPECIAL FRIES",font="Halvetica 15 bold",onvalue=1,offvalue=0,variable=var_10,command=change_9).pack(anchor="nw")
grilled_sandwich = Checkbutton(menu_frame,text="GRILLED STEAK SANDWICH",font="Halvetica 15 bold",onvalue=1,offvalue=0,variable=var_11,command=change_10).pack(anchor="nw")

steaky_special_sand = Checkbutton(menu_frame,text="STEAKY SPECIAL SANDWICH",font="Halvetica 15 bold",onvalue=1,offvalue=0,variable=var_13,command=change_11).pack(anchor="nw")



# Entry Fields For Items
e= Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e1,state=DISABLED).place(x=250,y=40)
num_of_BEEF_sizling_STEAK = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e2,state=DISABLED).place(x=275,y=75)
num_of_BEEF_steaky_STEAK = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e3,state=DISABLED).place(x=340,y=110)
num_of_BEEF_sizling_steaky_STEAK = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e4,state=DISABLED).place(x=370,y=150)
num_of_CHICKEN_STEAK = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e5,state=DISABLED).place(x=250,y=185)
num_of_CHICKEN_STEAKY_special = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e6,state=DISABLED).place(x=300,y=220)
num_of_CHICKEN_sizzling = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e7,state=DISABLED).place(x=290,y=255)
num_of_grilled_steak = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e8,state=DISABLED).place(x=235,y=290)
num_of_grilled_steak_caperherb = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e9,state=DISABLED).place(x=340,y=330)
num_of_special_fries = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e10,state=DISABLED).place(x=300,y=365)
num_of_sandwich = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e11,state=DISABLED).place(x=320,y=400)
num_of_sandwich_steaky_special = Entry(menu_frame,font="Halvetica 13 bold",bd=7,textvariable=e12,state=DISABLED).place(x=322,y=435)


cost_of_steak_var = StringVar()
ser_tax_var = StringVar()
total_cost_var = StringVar()

cost_steak = Label(menu_frame, text="Cost Of Steaks", bd=3, fg="white", bg="firebrick4", font="comicsansms 10 bold").pack(side=LEFT,anchor=NW,pady=2)
cost_of_steak = Entry(menu_frame,textvariable=cost_of_steak_var, state='readonly',font="comicsansms 10 bold", bd=5).pack(anchor=NW)

service_tax = Label(menu_frame,text="GST", bd=3, fg="white", bg="firebrick4", font="comicsansms 10 bold").pack(side=LEFT,anchor=NW)
service_tax_text = Entry(menu_frame,textvariable=ser_tax_var,state='readonly', font="comicsansms 10 bold", bd=5).pack(anchor=NW)

Total_cost = Label(menu_frame, text="TOTAL COST", bd=3, fg="white", bg="firebrick4", font="comicsansms 10 bold").pack(side=LEFT,anchor=NW,pady=2)

Total_cost_text = Entry(menu_frame,textvariable=total_cost_var, state='readonly', font="comicsansms 15 bold", bd=5).pack(anchor=NW)

# BUTTONS
button_total = Button(R_frame,text="TOTAL",command=total_cost,font="Halvetica 10 bold",fg="white", bg="red4", bd=5, padx=30).pack(side=LEFT,anchor=NW)

button_order = Button(R_frame,text="SAVE_BILL",command=save_receipt,font="Halvetica 10 bold",fg="white", bg="red4", bd=5, padx=30).pack(side=LEFT,anchor=NW,padx=25)

button_reset = Button(R_frame,text="Reset",font="Halvetica 10 bold",fg="white", bg="red4", bd=5, padx=30, command=reset).pack(side=LEFT, anchor=NW, padx=25)

button_quit = Button(R_frame,text="Exit",font="Halvetica 10 bold", fg='white',bg='red4',bd=5,padx=25,command=quit).pack(side=LEFT,anchor=SE,padx=25)

j = 0 # For serial number of receipt.


root.mainloop()
