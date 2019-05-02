import socket
import schedule 
import pyttsx3
import time 
import sys
import threading
from threading import Thread
print('Finding the IP of google, if successful, you have a connetion to the wifi\nChecking...\n')
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
    if fuct1_thread.isAlive is False:
        schedule.every().minute.at(":30").do(check)

    while True:
        schedule.run_pending()
        time.sleep(1)
