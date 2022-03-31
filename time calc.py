from tkinter import *
from tkinter.ttk import Combobox
from datetime import date


def calcDate(d2=tuple):
    d1 = date.today()
    d2 = date(int(yearCombo.get()), months[monthCombo.get()], int(dayCombo.get()))
    delta = d1 - d2 
    print(delta.days)


#Makes the months with their respecting days(Leap years will be modulated)
months = {  
            'Jan' : [i for i in range(31)],
            'Feb' : [i for i in range(28)], 
            'Mar' : [i for i in range(31)], 
            'Apr' : [i for i in range(30)], 
            'May' : [i for i in range(31)], 
            'Jun' : [i for i in range(30)], 
            'Jul' : [i for i in range(31)], 
            'Aug' : [i for i in range(31)], 
            'Sep' : [i for i in range(30)], 
            'Oct' : [i for i in range(31)], 
            'Nov' : [i for i in range(30)], 
            'Dec' : [i for i in range(31)]
        }

#Initializes the window
window = Tk()
window.configure(bg='white')
window.geometry('400x200')
window.resizable(0,0)


#Initializes the label
dateLabel = Label(window, text='Date', font=(30), bg='white')
dateLabel.pack()
dateLabel.place(relwidth=0.3, relx=0.35, rely=0, relheight=0.1)

#Initializes the combo boxes for the days and months, and the entry for the year
dayCombo = Combobox(window, values=[i for i in range(31)])
dayCombo.current(0)
dayCombo.pack()
dayCombo.place(relwidth=0.2, relx=0.1, rely=0.5, relheight=0.1)

monthCombo = Combobox(window, values=[i for i in months.keys()])
monthCombo.current(0)
monthCombo.pack()
monthCombo.place(relwidth=0.2, relx=0.4, rely=0.5, relheight=0.1)

year = StringVar(window, '2022')
yearCombo = Entry(window, textvariable=year)
yearCombo.pack()
yearCombo.place(relwidth=0.2, relx=0.7, rely=0.5, relheight=0.1)

goBtn = Button(window, text='Go', command=calcDate )
goBtn.pack()
goBtn.place(relwidth=0.1, relx=0.5, rely=0.8, relheight=0.1)



window.mainloop()