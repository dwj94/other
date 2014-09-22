# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 13:44:26 2014

@author: Dan
"""

from Tkinter import *   #import tkinter for app
import csv, xlwt        #import csv and xlwt for csv to excel conversion
import pandas as pd

root = Tk()
root.title("Budget")   #title for window
df = pd.read_csv('C:/Users/Dan/Documents/Budget/budget.csv', header = 0)
df = df.dropna()
count = -2
for row in df['Bills']:
    count +=2
print df
info = [0,0,0,df['Bills'][count],0]  #empty list for adding info in that will go to excel sheet
def Button1():  
    text_contents = text.get() #gets the text entered when the button is pressed
    info[0] = text.get() #append the lsit with this text
    listbox.insert(END, "Entered Date:")  #text to displayt after button is pressed
    listbox.insert(END, text_contents)#display the entered text also
    text.delete(0, END)  #clear the text box

def Button2():  #button2
    text_contents = text.get()
    info[1] = float(text.get())
    listbox.insert(END, "Entered Spend:")
    listbox.insert(END, text_contents)
    text.delete(0, END)

def Button3():  #button3
    text_contents = text.get()
    info[2] = float(text.get())
    listbox.insert(END, "Entered Earnings:")
    listbox.insert(END, text_contents)
    text.delete(0, END)

bilist = [0]

def Button4():   #button4
    bill = float(text.get())
    bilist[0] = bill
    count = -2
    for row in df['Bills']:
        count+=2
    bills = df['Bills'][count] - float(text.get())
    info[3] = bills
    listbox.insert(END, "Bills Payed")
    listbox.insert(END, text.get())
    text.delete(0,END)

def Button5():
    count = -2
    for row in df['Bills']:
        count+=2
    number = float(df['Balance'][count]) + info[2] - info[1] - bilist[0]
    info[4] = number
    csv_out = open('C:/Users/Dan/Documents/Budget/budget.csv', 'a')  #open the database in appendable form
    mywriter = csv.writer(csv_out) 
    mywriter.writerow(info) #write the info list to the database
    csv_out.close() 
    f=open('C:/Users/Dan/Documents/Budget/budget.csv', 'rb')  #open the csv in readable form
    g = csv.reader(f)
    wbk= xlwt.Workbook()
    sheet = wbk.add_sheet("Sheet 1")  #add a sheet to the empty workbook
    for rowi, row in enumerate(g):
        for coli, value in enumerate(row):
            sheet.write(rowi,coli,value)  #wrtie the values to the excel sheet in the correct row/column form
    wbk.save('C:/Users/Dan/Documents/Budget/budget.csv' + '.xls')  #save the workbook
    listbox.insert(END, 'Exported')  #tell the user the data has been exported


def Button6(): #button to delete the list and start again (clears the text box)
    del info[:]
    count = 0
    if count < 5:
        count += 1
        info.append(0)
    listbox.delete(0,END)

def Button7():
    listbox.insert(END, 'Balance...') #search function
    count = -2
    for row in df['Bills']:
        count +=2
    listbox.insert(END, df['Balance'][count])
    listbox.insert(END, 'With Bills of')
    listbox.insert(END, df['Bills'][count])

def Button8():
    listbox.insert(END, 'Added Bill of')
    listbox.insert(END, text.get())
    count = -2
    for row in df['Bills']:
        count +=2
    info[3] = float(df['Bills'][count]) + float(text.get())
    
    
    
textframe = Frame(root)
listframe = Frame(root)

button1 = Button(textframe, text = "Date", command = Button1)  #calls the buttons and names them with colour if required
button2 = Button(textframe, text = "Spent", command = Button2)
button3 = Button(textframe, text= "Earnt", command = Button3)
button4 = Button(textframe, text="Pay Bills", command = Button4)
button5 = Button(textframe, text="Export", command = Button5, background = 'green')
button6 = Button(textframe,text="Restart", command = Button6, background = 'red')
button7 = Button(textframe, text = 'Balance', command = Button7, background = 'blue')
button8 = Button(textframe, text = 'Add Bill', command = Button8)
text = Entry(textframe)

scrollbar = Scrollbar(root, orient = VERTICAL)  #adds a vertical scrollbar
listbox = Listbox(root, yscrollcomman=scrollbar.set)
scrollbar.configure(command = listbox.yview)


text.pack(side=LEFT, fill = X, expand = 1)  #positions all the widgets
button1.pack(side = LEFT)
button2.pack(side = LEFT)
button3.pack(side = LEFT)
button4.pack(side = LEFT)
button8.pack(side = LEFT)
button5.pack(side=BOTTOM, fill = X, expand = 1)
button6.pack(side = BOTTOM, fill = X, expand = 1)
button7.pack(side=BOTTOM, fill =X, expand = 1)
listbox.pack(side = LEFT, fill = BOTH, expand = 1)
scrollbar.pack(side = RIGHT, fill = Y)
textframe.pack(fill=X)
listframe.pack(fill = BOTH, expand = 1)

root.geometry("700x150")  #size of the window upon opening
root.mainloop()  #complete the programme to open window