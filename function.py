import tkMessageBox
def rearrange_data(data):
    count=0
    for ele in data:
        ele['No']=count;
        count+=1
    return data

def date_converter(date):
    '''simplified version of the date converter'''
    date=date.split('/')
    state=True
    if int(date[0])>12 or int(date[0])<1:
        state=False
    if int(date[0]) in range(1,10):
        date[0]=''.join('0'+int(date[0]))
    if int(date[1])<1 or int(date[1])>31:
        state=False
    return (state,date)


def amount_converter(amount):
    try:
        float(amount)
        return True
    except ValueError:
        return False


def datewarning():
    tkMessageBox.showinfo("Warning", "Date must follow the pattern:MM/DD/YY !!")


def amountwarning():
    tkMessageBox.showinfo('Warning','Amount must be numbers !!')
