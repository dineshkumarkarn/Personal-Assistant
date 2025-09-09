import csv
import speech_recognition as sr
import pyttsx3
import pandas as pd
from datetime import datetime, timedelta
import random

class HomeAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.tts = pyttsx3.init()
        self.schedule = {}
        self.filename = "schedule.csv"
        self.load_schedule()
        
    def get_today_date(self):
        today_date = datetime.now().strftime("%d-%B-%Y")
        return today_date
    
    def speak(self, message):
        self.tts.say(message)
        self.tts.runAndWait()
        
    def get_tommarow_date():
        tomorrow_date=(datetime.now()+ timedelta(days=1)).strftime("%d-%B-%Y")
        return tomorrow_date
    
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
                print(f"You said: {command}")
                return command.lower()
            except sr.UnknownValueError:
                self.speak("Sorry, I did not understand that.")
                return None
            except sr.RequestError:
                self.speak("Sorry, my speech service is down.")
                return None
    
    def add_task(self, date, time, task):
        if date not in self.schedule:
            self.schedule[date] = {}
        self.schedule[date][time] = task
        message = f"Task '{task}' added on {date} at {time}."
        self.speak(message)
        print(message)
        self.save_schedule()
        self.speak("your task is saved in the csv file ")
    
    def view_schedule(self,cmd):
        tomorrow_date=(datetime.now()+ timedelta(days=1)).strftime("%d-%B-%Y")
        today_date=datetime.now().strftime("%d-%B-%Y")
        
        if "today schedule" in cmd:
            if today_date in self.schedule:
                self.speak(f"Here is your schedule for {today_date}:")
                print(f"Your Schedule for today {today_date}:")
                for time, task in self.schedule[today_date].items():
                    self.speak(f"At {time}, you have {task}.")
                    print(f"  {time}: {task}")
            else:
                print(f"there is no schedule for{today_date} ")
                       
        elif "tomorrow schedule" in cmd :
            if tomorrow_date in self.schedule:
                self.speak(f"Here is your schedule for {tomorrow_date}:")
                print(f"Your Schedule for tomorrow {tomorrow_date}:")
                for time, task in self.schedule[tomorrow_date].items():
                    self.speak(f"At {time}, you have {task}.")
                    print(f"  {time}: {task}")
            else:
                print(f"there is no schedule for{tomorrow_date} ")
                
        elif "all schedule" in cmd:
            self.speak("Here is your schedule:")
            print("Your Schedule:")
            for date, tasks in self.schedule.items():
                self.speak(f"Date: {date}")
                print(f"Date: {date}")
                for time, task in tasks.items():
                    self.speak(f"At {time}, you have {task}.")
                    print(f"  {time}: {task}")
        else:
            self.speak("Your schedule is empty.")
            print("Your schedule is empty.")
            
    def search_schedule(self, date, time):
        if date in self.schedule and time in self.schedule[date]:
            task = self.schedule[date][time]
            self.speak(f"On {date} at {time}, you have: {task}.")
            print(f"On {date} at {time}, you have: {task}.")
        else:
            self.speak("No task found at the specified date and time.")
            print("No task found at the specified date and time.")
            
    def load_schedule(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    date = row['Date']
                    time = row['Time']
                    task = row['Task']
                    if date not in self.schedule:
                        self.schedule[date] = {}
                    self.schedule[date][time] = task
            
            print("Schedule loaded from file.")
        except FileNotFoundError:
            self.speak("Schedule file not found.")
            print("Schedule file not found.")
    
    def save_schedule(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Time", "Task"])
            for date, tasks in self.schedule.items():
                for time, task in tasks.items():
                    writer.writerow([date, time, task])
        message = f"Schedule saved to {self.filename}."
        self.speak(message)
        print(message)
        

        

        
   
    
        
        
assistant = HomeAssistant()
def main(com):
        
        while True:
            command = com
            if command:
                if "add" in command:
                    assistant.speak("Please specify the date for the task.")
                    date = assistant.listen()
                    if date == "today":
                        date = assistant.get_today_date()
                        
                    elif date=="tomorrow":
                        date== assistant.get_tommarow_date()
                    assistant.speak("Please specify the time for the task.")
                    
                    time = assistant.listen()
                    assistant.speak("Please specify the task.")
                    
                    task = assistant.listen()
                    if date and time and task:
                        assistant.add_task(date, time, task)
                        
                elif "search" in command:
                    assistant.speak("Please specify the date to search.")
                    date = assistant.listen() or input("Enter the date: ").lower()
                    if date == "today":
                        date = assistant.get_today_date()
                    assistant.speak("Please specify the time to search.")
                    time = assistant.listen() or input("Enter the time: ")
                    assistant.search_schedule(date, time)
                    break
                    
                    
                        
                elif "schedule" in command: 
                    cmd=command
                    assistant.view_schedule(cmd)
                    break
                    
                
                
                else:
                    assistant.speak("Sorry, I did not understand that command.")

