from tkinter import *
from PIL import ImageTk
import sqlite3
import os
from tktimepicker import AnalogPicker, AnalogThemes


class Hotel_Management:
    def __init__(self, root):
        self.root = root
        self.root.title("HOTEL MANAGEMENT SYSTEM")
        self.root.geometry("1000x650")
        scroll_bar = Scrollbar(self.root)
        scroll_bar.place(x=0,y=0)

        def createDB():
            # CONNECT TO SQLITE
            conn = sqlite3.connect("hotelDB.db")
            c = conn.cursor()

            # CREATE OUT DATABASE HERE
            c.execute("""CREATE TABLE customer(
                firstname TEXT, 
                lastname TEXT,
                phone TEXT, 
                customer_location TEXT, 
                room_number TEXT,
                gender TEXT
            )""")
            conn.commit()
            conn.close()

            print("DB created Successfully")

        # EXIT APPLICATION
        def exitApplication():
            pass

        # CLEAR APPLICATION

        def clearData():
            pass

        # SAVE DATA

        def saveData():
            pass

        # TEXTVARIABLE
        firstnameVariable = StringVar()
        lastnameVariable = StringVar()
        phoneVariable = StringVar()
        locationVariable = StringVar()
        RoomNumberVariable = StringVar()
        clicked = StringVar()
        clicked.set("SELECT GENDER")
        OPTIONS = ["MALE", "FEMALE"]

        # TITLE
        labelTitle = Label(self.root, text="HOTEL MANAGEMENT SYSTEM", font=(
            "Arial", 35, "bold"), fg="white", bg="#f17c37", width=50)
        labelTitle.place(x=0, y=0,)

        # DISPLAY USER FRAME
        userFrame = Frame(self.root, width=490, height=500, bg="#E7E6E6",)
        userFrame.place(x=500, y=100)

        # USERNAME
        firstnameLabel = Label(self.root, text="FIRSTNAME", font=(
            "Gloudy old style", 15,), bg="white")
        firstnameLabel.place(x=45, y=100)

        # FIRSTNAME ENTRY
        firstnameEntry = Entry(
            self.root, textvariable=firstnameVariable, bg="#E7E6E6", width=35,)
        firstnameEntry.place(x=50, y=120)

        # LASTNAME LABEL
        lastnameLabel = Label(self.root, text="LASTNAME", font=(
            "Gloudy old style", 15,), bg="white")
        lastnameLabel.place(x=45, y=160)
        lastnameEntry = Entry(
            self.root, textvariable=lastnameVariable, bg="#E7E6E6", width=35,)
        lastnameEntry.place(x=50, y=180)

        # PHONE NUMBER
        phoneNumberLabel = Label(self.root, text="PHONE NUMBER", font=(
            "Gloudy old style", 15,), bg="white")
        phoneNumberLabel.place(x=45, y=220)
        phoneNumberEntry = Entry(
            self.root, textvariable=phoneVariable, bg="#E7E6E6", width=35,)
        phoneNumberEntry.place(x=50, y=240)

        # LOCATION
        locationLabel = Label(self.root, text="LOCATION", font=(
            "Gloudy old style", 15,), bg="white")
        locationLabel.place(x=45, y=280)
        locationEntry = Entry(
            self.root, textvariable=locationVariable, bg="#E7E6E6", width=35,)
        locationEntry.place(x=50, y=300)

        # ROOM NUMBER
        roomLabel = Label(self.root, text="ROOM NUMBER",
                          font=("Gloudy old style", 15,), bg="white")
        roomLabel.place(x=45, y=340)
        roomEntry = Entry(
            self.root, textvariable=RoomNumberVariable, bg="#E7E6E6", width=35,)
        roomEntry.place(x=50, y=360)

        # GENDER
        genderLabel = Label(self.root, text="GENDER", font=(
            "Gloudy old style", 15,), bg="white")
        genderLabel.place(x=45, y=390)
        genderEntry = OptionMenu(self.root, clicked, *OPTIONS, )
        genderEntry.place(x=50, y=410)

        # TIME PICKER LABEK
        timeLabel = Label(self.root, text="PICK TIME", font=(
            "Gouldy old style", 15), bg="white")
        timeLabel.place(x=45, y=450)

        # PICK DATE TIME
        timePicker = AnalogPicker(self.root)
        timePicker.place(x=50, y=500)


        # # BUTTONS
        # saveBtn = Button(self.root, text="SAVE", width=15,
        #                  height=2, command=saveData, )
        # saveBtn.place(x=50, y=450)
        # # CLEAR DATA
        # saveBtn = Button(self.root, text="CLEAR", width=15,
        #                  height=2, command=saveData)
        # saveBtn.place(x=200, y=450)
root = Tk()
obj = Hotel_Management(root)
root.mainloop()
