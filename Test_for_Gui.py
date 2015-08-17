
from Tkinter import *
import tkMessageBox
import csv
from function import *

Person_selected="Dong Gao"
Shared_Status=True
Total_transaction=0
Save_status=True
Choosen_month="All year"
Data_read=[]
Data_show=[]



def addEntry () :
    global Total_transaction,Save_status
    date=date_converter(dateVar.get())
    if date[0] and amount_converter(AmountVar.get()):
        add_data={}
        add_data['Date']=date[1]
        add_data['Shared'] =SharedVar.get()
        add_data['Type'] = Type_get(TypeVar.get())
        add_data['Detail'] = DetailVar.get()
        add_data['Transaction']=AmountVar.get()
        Total_transaction+=1
        add_data['No']=Total_transaction
        Data_read.append (add_data)
        Save_status=False
        importbill()
        setSelect ()
    else:
        if not date[0]:
            datewarning()
        if not amount_converter(AmountVar.get()):
            amountwarning()

def updateEntry() :
    global Save_status
    add_data={}
    add_data['Date']=dateVar.get()
    add_data['Shared'] =SharedVar.get()
    add_data['Type'] = Type_get(TypeVar.get())
    add_data['Detail'] = DetailVar.get()
    add_data['Transaction']=AmountVar.get()
    Data_read[whichSelected()] = [add_data]
    Save_status=False
    importbill()
    setSelect ()

def deleteEntry() :
    global Save_status
    del Data_read[whichSelected()]
    Save_status=False
    importbill()
    setSelect ()

def loadEntry() :
    load_data = Data_read[whichSelected()]
    print "The loaed data"
    print load_data
    dateVar.set(load_data['Date'])
    AmountVar.set(load_data['Transaction'])
    TypeVar.set(Type_return(load_data['Type']))
    DetailVar.set(load_data['Detail'])
    SharedVar.set(load_data['Shared'])


def whichSelected () :
    place_in_date_show=int(select.curselection()[0])
    print "The place in date show is"+str(place_in_date_show)
    global Data_read,Data_show
    for ele in range(len(Data_read)):
        if Data_read[ele]['No'] == Data_show[place_in_date_show]['No']:
            return ele


def Export_bill_data():
    global Data_read
    if Person_selected == "Dong Gao":
        file=open("Dong_Gao_Bill_info.csv",'w')
    else:
        file=open("Chengwei_Li_Bill_info.csv",'w')
    fieldnames = []
    Data_read=rearrange_data(Data_read)
    for ele in Data_read[0]:
        fieldnames.append(ele)
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for ele in Data_read:
        writer.writerow(ele)

def Exit_program():
    if not Save_status:
        pass
    else:
        Export_bill_data();
        win.quit();

def Type_get(type):
    if type == 1 :
        return 'Housing'
    elif type == 2:
        return 'Transportation'
    elif type ==3:
        return 'Shopping'
    elif type == 4:
        return 'Entertaining'
    else:
        return 'Eating'

def Type_return(type):
    if type == 'Housing' :
        return 1
    elif type == 'Transportation':
        return 2
    elif type =='Shopping':
        return 3
    elif type == 'Entertaining':
        return 4
    else:
        return 5


def Load_bill_data():
    global Data_show,Data_read,Save_status,Total_transaction
    if Save_status:
        Data_read=[]
        '''Decide the person's bill to load'''
        if Person_selected == "Dong Gao":
            file=open("Dong_Gao_Bill_info.csv")
        else:
            file=open("Chengwei_Li_Bill_Info.csv")
        '''load the data'''
        print "Load "+""+Person_selected+" "+"Data"
        reader=csv.DictReader(file)
        for row in reader:
             Data_read.append(row)
        Total_transaction=int(Data_read[len(Data_read)-1]['No'])
        print Total_transaction
        '''decide the data to be shown on the listbox'''
        if Choosen_month.get() == "All year":
            for ele in Data_read:
                Data_show.append(ele)
        else:
            Data_show=show_monthly_data(Data_read)
        Save_status=False

    else:
        warning_window()
        button_release()


def Load_data_to_Listbox():
    global Data_show,Data_read
    Data_show=[]
    '''decide the data to be shown on the listbox'''
    if Choosen_month.get() == "All year":
        for ele in Data_read:
            Data_show.append(ele)
    else:
        Data_show=show_monthly_data(Data_read)

def importbill():
    month=Choosen_month.get()
    print month
    global Data_read,Data_show
    Data_show=[]
    Load_data_to_Listbox()
    setSelect()
    print "The show bill got the data to show is"
    print Data_show

def person_choose():
    global Person_selected,Save_status
    if Save_status:
        if PersonVar.get() == 1:
            Person_selected="Dong Gao"
        elif PersonVar.get() == 2:
            Person_selected="Chengwei Li"
        button_release()
        print Person_selected
    else:
        if PersonVar.get()==1 and Person_selected != 'Dong Gao':
            PersonVar.set(2)
        elif PersonVar.get() == 2 and Person_selected =='Dong Gao':
            PersonVar.set(1)
        print Person_selected
        warning_window()
def warning_window():
    tkMessageBox.showinfo("Warning", "please save your work before load another data")

def show_monthly_data(Data):
    monthly_data=[]
    global Choosen_month
    for ele in Data_read:
        a=get_month_from_date(ele['Date'])
        b=get_month(Choosen_month.get())
        if get_month_from_date(ele['Date']) == get_month(Choosen_month.get()):
            monthly_data.append(ele)
            print "appending montyly_data"
    return monthly_data

def get_month(button):
    dicts={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
    return dicts[button]
def get_month_from_date(date):
    date=date.split('/')
    return date[0]

def save():
    global Save_status
    Save_status=True
    Export_bill_data()

def button_release():
    global Load_data_Var
    Load_data_Var.set(0)

def Clear():
    global select
    select.delete(0,END)


def setSelect ():
    #sorted(Data_read, key = lambda user: (user['Date'], user['Transaction']))
    select.delete(0,END)
    for ele in Data_show :
        select.insert(END, str(ele['No'])+' | '+ele['Date']+' | '+ele['Transaction']+' | '+ele['Detail']+' | '+ele['Type']+" | "+str(ele['Shared']))


def compute_balance():
    global Month_total_Var,BalanceVar,Choosen_month,Save_status,Person_selected,Month_total_Var1,BalanceVar1
    if Save_status:
        data_read_Gao=[]
        data_read_Li=[]
        file1=open("Dong_Gao_Bill_info.csv")
        reader1=csv.DictReader(file1)
        for row in reader1:
             data_read_Gao.append(row)

        file2=open("Chengwei_Li_Bill_Info.csv")
        reader2=csv.DictReader(file2)
        for row in reader2:
             data_read_Li.append(row)

        total_li=0.0
        total_gao=0.0
        balance_li=0.0
        balance_gao=0.0

        if Choosen_month.get()!='All year':
            month=get_month(Choosen_month.get())
            for ele in data_read_Gao:
                if get_month_from_date(ele['Date'])==month:
                    total_gao+=float(ele['Transaction'])
            for ele in data_read_Li:
                if get_month_from_date(ele['Date'])==month:
                    total_li+=float(ele['Transaction'])
        else:
            for ele in data_read_Gao:
                total_gao+=float(ele['Transaction'])
            for ele in data_read_Li:
                total_li+=float(ele['Transaction'])

        Month_total_Var.set(total_gao)
        Month_total_Var1.set(total_li)
        '''Compute the balance'''

        if Choosen_month.get()!='All year':
            month=get_month(Choosen_month.get())
            for ele in data_read_Gao:
                print type(ele['Shared'])
                if get_month_from_date(ele['Date'])==month and ele['Shared']== '1':
                    balance_gao+=float(ele['Transaction'])
            for ele in data_read_Li:
                if get_month_from_date(ele['Date'])==month and ele['Shared'] == '1':
                    balance_li+=float(ele['Transaction'])


        BalanceVar.set(float(balance_gao+balance_li)/2-float(balance_gao))
        BalanceVar1.set(float(balance_gao+balance_li)/2-float(balance_li))
    else:
        warning_window()




def makeWindow () :
    global dateVar, AmountVar, DetailVar,TypeVar,SharedVar,select,Choosen_month,PersonVar,Save_status,Load_data_Var
    global Month_total_Var,BalanceVar,Month_total_Var1,BalanceVar1
    win = Tk()

    frame1 = Frame(win)
    frame1.pack()

    Label(frame1, text="Date").grid(row=0, column=0, sticky=W)
    dateVar = StringVar()
    date = Entry(frame1, textvariable=dateVar)
    date.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Amount").grid(row=1, column=0, sticky=W)
    AmountVar= StringVar()
    Amount= Entry(frame1, textvariable=AmountVar)
    Amount.grid(row=1, column=1, sticky=W)

    Label(frame1, text="Detail").grid(row=2, column=0, sticky=W)
    DetailVar= StringVar()
    Detail= Entry(frame1, textvariable=DetailVar)
    Detail.grid(row=2, column=1, sticky=W)


    frame5=Frame(win)
    frame5.pack()
    '''The type of the billing'''
    TypeVar = IntVar()
    a1=Radiobutton(frame5, text="Housing", variable=TypeVar, value=1).pack(side=LEFT)
    a2=Radiobutton(frame5, text="Transportation", variable=TypeVar, value=2).pack(side=LEFT)
    a3=Radiobutton(frame5, text="Shopping", variable=TypeVar, value=3).pack(side=LEFT)
    a4=Radiobutton(frame5, text="Entertaining", variable=TypeVar, value=4).pack(side=LEFT)
    a5=Radiobutton(frame5, text="Eating", variable=TypeVar, value=5).pack(side=LEFT)

    frame6=Frame(win)
    frame6.pack()
    '''The shared billing '''
    SharedVar = IntVar()
    c = Checkbutton(frame6, text="Shared Billing", variable=SharedVar)
    c.grid(row=1,column=1)
    c.pack()



    PersonVar = IntVar()
    r1 = Radiobutton(win, text="Dong Gao", variable=PersonVar, value=1,command=person_choose)
    r2 = Radiobutton(win, text="Chengwei Li", variable=PersonVar, value=2,command=person_choose)
    r1.config(indicatoron=0)
    r2.config(indicatoron=0)
    PersonVar.set(1)
    r1.pack()
    r2.pack()


    Load_data_Var = IntVar()
    l1 = Radiobutton(win, text="Load Bill", variable=Load_data_Var, value=1,command=Load_bill_data,height=5,width=10)
    l1.config(indicatoron=0)
    l1.pack()


    ######################################################################################
    '''setting up the buttons'''
    frame2 = Frame(win)       # Row of buttons
    frame2.pack()
    b1 = Button(frame2,text=" Add  ",command=addEntry)
    b2 = Button(frame2,text="Update",command=updateEntry)
    b3 = Button(frame2,text="Delete",command=deleteEntry)
    b4 = Button(frame2,text=" Load ",command=loadEntry)
    b5 = Button(frame2,text="Show Bill",command=importbill)
    b6 = Button(frame2, text ="Save",command=save,bg='RED')
    b1.pack(side=LEFT); b2.pack(side=LEFT)
    b3.pack(side=LEFT); b4.pack(side=LEFT)
    b5.pack(side=LEFT); b6.pack(side=RIGHT)

    '''select month'''
    Months = ["All year",
    "Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    Choosen_month = StringVar(win)
    Choosen_month.set(Months[0]) # default value
    w = apply(OptionMenu, (frame2, Choosen_month) + tuple(Months))
    w.pack(side=RIGHT)


    frame3 = Frame(win)       # select of names
    frame3.pack()
    scroll = Scrollbar(frame3, orient=VERTICAL)
    select = Listbox(frame3, yscrollcommand=scroll.set, height=6,width=50)
    scroll.config (command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH, expand=1)




    #######################################################################################
    '''Adding up the text to show the result down at the buttom'''
    frame4 = Frame(win)
    frame4.pack();
    X= Label(frame4, text="Dong's Monthly Total:", fg="red").grid(row=0, column=0, sticky=W)
    XE= Label(frame4, text="Dong's Monthly Balance:", fg="red").grid(row=1, column=0, sticky=W)

    Month_total_Var= StringVar()
    monTot= Entry(frame4, textvariable=Month_total_Var,width=10)
    monTot.grid(row=0, column=1, sticky=W)

    BalanceVar= StringVar()
    balance= Entry(frame4, textvariable=BalanceVar,width=10)
    balance.grid(row=1, column=1, sticky=W)


    X1= Label(frame4, text="Li's Monthly Total:", fg="red").grid(row=0, column=2, sticky=W)
    XE1= Label(frame4, text="Li's Monthly Balance:", fg="red").grid(row=1, column=2, sticky=W)

    Month_total_Var1= StringVar()
    monTot1= Entry(frame4, textvariable=Month_total_Var1,width=10)
    monTot1.grid(row=0, column=3, sticky=W)

    BalanceVar1= StringVar()
    balance1= Entry(frame4, textvariable=BalanceVar1,width=10)
    balance1.grid(row=1, column=3, sticky=W)


    ########################################################################################
    '''adding up the cascading menu for better utility'''
    menu = Menu(win)
    win.config(menu=menu)

    viewMenu = Menu(menu)
    menu.add_cascade(label="Menu", menu=viewMenu)
    viewMenu.add_command(label = "import", command=updateEntry)
    viewMenu.add_command(label = "export as... ", command=updateEntry)
    viewMenu.add_command(label = "Exit", command=Exit_program)

    edit=Menu(menu)
    edit.add_command(label = "Compute_balance",command=compute_balance)
    menu.add_cascade(label = "Edit",menu=edit)

    ########################################################################################
    '''Making the multi-column treectrl listbox'''



    return win

win = makeWindow()
Load_bill_data()
setSelect()
win.mainloop()

