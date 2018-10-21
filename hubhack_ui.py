import tkinter
from tkinter import *

from identifier import *


def get_values():
    '''
    using .get() method, the values in the entries are stored in three different
    variables: zip , age and gender
    '''

    zip = float(zip_entry.get())
    age = float(age_entry.get())
    gender = float(gender_entry.get())
    #  place algorithm below the following is just a place holder algorithm
    d = [int(2018-age+10), int(2018-age-10), int(gender)]
    writeIndDataToCSV(d,'0'+str(int(zip)),csv_files)
    
    Label(master, text="Check the directory for a new CSV", height=2).grid(row=3,column=1)


master = tkinter.Tk()
master.title("HUB_HACK")

zip_entry = Entry(master)
age_entry = Entry(master)
gender_entry = Entry(master)

zip_code = Label(master, text="Zip Code", height=2).grid(row=0)
zip_entry.grid(row=0, column=1)

age = Label(master, text="Age", height=2).grid(row=1)
age_entry.grid(row=1, column=1)

gender = Label(master, text="Gender (1 or 2)", height=2).grid(row=2)
gender_entry.grid(row=2, column=1)


b = Button(master, text="GO!", command=get_values).grid(row=4, column=1)

master.mainloop()