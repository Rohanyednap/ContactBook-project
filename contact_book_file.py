# from multiprocessing import connection
# import queue
import tkinter as tk
import sqlite3
# from colorama import Cursor

db = "F:\\MCA\\Semester 2\\Winning Camp\\ContactBook Project\\contact_book\\contactBook.db"

def StoreFind():
    print("Numbar Saved !!!")
    connection = sqlite3.connect(db)
    Cursor = connection.cursor()
    Name = name_input.get("1.0",tk.END)
    Phone = Phone_input.get("1.0", tk.END)

    if len(Phone) < 2:
        query = "SELECT Phone from ContactBook_T where Name = '{n}'".format(n = Name)
        Cursor.execute(query)
        rows_found = Cursor.fetchall()
        phone_found = rows_found[0]
        Phone_input.insert("1.0", phone_found)


    else:
        query = "INSERT INTO ContactBook_T VALUES('{n}',{p})".format(n = Name, p = Phone)
        Cursor.execute(query)
        connection.commit()
        connection.close




root = tk.Tk()
root.geometry("400x300")

NameLabel = tk.Label(root, text ='Name')
NameLabel.place(x = 5, y = 20)

name_input = tk.Text(root)
name_input.place(x = 5, y = 50, height = 25, width = 200)

PhoneLabel = tk.Label(root, text ='Phone Number')
PhoneLabel.place(x = 5, y = 110)

Phone_input = tk.Text(root)
Phone_input.place(x = 5, y = 140, height = 25, width = 200)

StoreButton = tk.Button(root, text = "Save Contact", command = StoreFind)
StoreButton.place(x = 5, y = 220)

root.mainloop()
