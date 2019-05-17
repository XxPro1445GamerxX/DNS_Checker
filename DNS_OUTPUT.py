import socket
import schedule 
import pyttsx3
import time 
import sys
import threading
from threading import Thread
from tkinter import *
print('Finding the IP of google, if successful, you have a connetion to the wifi\nChecking...\n')

def button():
    root = Tk()
        
    equalButton = Button(root, text="Press")
    equalButton.bind('<Button-1>', entire1)
    equalButton.pack()

    sumEntry = Entry(root)
    sumEntry.pack()

    root.mainloop()
def entire():
    print('This wil check every 30 seconds\nPress Ctrl C to exit')
    while True:

        def check():
            try:
                addr1 = socket.gethostbyname('google.com')
                print(addr1)
                e = pyttsx3.init()
                e.setProperty('rate', 150)
                e.setProperty('volume', 0.9)
                e.say('success, printing out IP')
                e.runAndWait()
            except:
                print("Error")
                e = pyttsx3.init()
                e.setProperty('rate', 150)
                e.setProperty('volume', 0.9)
                e.say('Failed')
                e.runAndWait()

        def other_check():

            if fuct1_thread.isAlive:
                e = pyttsx3.init()
                e.setProperty('rate', 150)
                e.setProperty('volume', 0.9)
                e.say('Scanning')
                e.runAndWait()
                check()
            
        fuct1_thread = Thread(target = check)

        schedule.every().minute.at(":30").do(other_check)
        schedule.every().minute.at(":00").do(other_check)
        while True:
            schedule.run_pending()
            time.sleep(1)

def entire1(event):

    def check():
        try:
            addr1 = socket.gethostbyname('google.com')
            print(addr1)
            e = pyttsx3.init()
            e.setProperty('rate', 150)
            e.setProperty('volume', 0.9)
            e.say('success, printing out IP')
            e.runAndWait()
        except:
            print("Error")
            e = pyttsx3.init()
            e.setProperty('rate', 150)
            e.setProperty('volume', 0.9)
            e.say('Failed')
            e.runAndWait()

    def other_check():
        if fuct1_thread.isAlive:
            e = pyttsx3.init()
            e.setProperty('rate', 150)
            e.setProperty('volume', 0.9)
            e.say('Scanning')
            e.runAndWait()
            check()
            
    fuct1_thread = Thread(target = check)
    other_check()
def elses():
    over = input('Do want to do it automatically(a) or manually(m): ').lower()
    score = 0
    if over == 'm' or over == 'a':
        score = 1
    while score == 0:
        print('Thats not one of them! (M or A)')
        over = input('Do want to do it automatically(a) or manually(m): ').lower()
        if over == 'm':
            button()
        elif over == 'a':
            entire()
over = input('Do want to do it automatically(a) or manually(m): ').lower()
if over == 'm':
    button()
elif over == 'a':
    entire()
else:
    elses()
