import tkinter
from tkinter import *


def get_values():
    '''
    using .get() method, the values in the entries are stored in three different
    variables: zip , age and gender
    '''

    zip = float(zip_entry.get())
    age = float(age_entry.get())
    gender = float(gender_entry.get())
    #  place algorithm below the following is just a place holder algorithm
    Label(master, text=round(((zip - (age * (100 - zip) * 0.01)) / (gender * 0.01)), 2), height=2).grid(row=3,
                                                                                                        column=1), 2


master = tkinter.Tk()
master.title("HUB_HACK")

zip_entry = Entry(master)
age_entry = Entry(master)
gender_entry = Entry(master)

zip_code = Label(master, text="ZipCode", height=2).grid(row=0)
zip_entry.grid(row=0, column=1)

age = Label(master, text="Age", height=2).grid(row=1)
age_entry.grid(row=1, column=1)

gender = Label(master, text="Gender", height=2).grid(row=2)
gender_entry.grid(row=2, column=1)


b = Button(master, text="GO!", command=get_values).grid(row=4, column=1)

master.mainloop()
