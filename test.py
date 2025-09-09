# from datetime import datetime, timedelta
# import random


# tommarow_date=(datetime.now()+ timedelta(days=1)).strftime("%Y-%m-%d")
# print(tommarow_date)
# def generate_random_schedule():
#         tasks = ["Morning Exercise","Meeting","Meeting", "Breakfast", "Work on Project", "Work on Project", "Work on Project", "Lunch", "Meeting", "Afternoon Walk", "Dinner", "Reading", "Reading", "Reading", "Watch TV", "Sleep", "Sleep", "Sleep"]
#         start_date = datetime.now()
#         for i in range(3):
#             date = (start_date + timedelta(days=i)).strftime("%d-%B-%Y")
#             for hour in range(8, 22):  # From 8 AM to 10 PM
#                 time = f"{hour:02d}:00"
#                 task = random.choice(tasks)
                
#                 print(f"date: {date} time: {time} task:{task}")
#         #         self.add_task(date, time, task)
#         # self.speak("Random schedule for the week has been generated and saved.")
#         # self.save_schedule()
        
# generate_random_schedule()
# import pyttsx3

# # Initialize the TTS engine
# tts_engine = pyttsx3.init()

# # List available voices
# voices = tts_engine.getProperty('voices')
# print(voices)

# # Set the desired voice (e.g., first voice in the list)
# tts_engine.setProperty('voice', voices[2].id)  # You can change the index to use a different voice

# # Adjust the speech rate (words per minute)
# tts_engine.setProperty('rate', 150)  # Adjust the speech rate (default is usually 200)

# # Adjust the volume (0.0 to 1.0)
# tts_engine.setProperty('volume', 1.0)  # Set volume to maximum

# # Function to convert text to speech
# def text_to_speech(text):
#     tts_engine.say(text)
#     tts_engine.runAndWait()

# # Example usage
# text = "what, how can I assist you today?"
# text_to_speech(text)
# import socket
# import os
# def is_connected():
#     try:
#         socket.create_connection(("8.8.8.8", 53))
#         return True
#     except OSError:
#         return False

# def switch_to_wifi():
#     os.system("nmcli radio wifi on")
#     os.system("nmcli connection up id 'your_wifi_connection_name'")
#     print("Switched to Wi-Fi.")

# def switch_to_ethernet():
#     os.system("nmcli connection up id 'your_ethernet_connection_name'")
#     print("Switched to Ethernet.")

# def ensure_stable_connection():
#     if is_connected():
#         print("Connected to the internet.")
        
#     else:
#         print("No internet connection. Attempting to switch to Wi-Fi.")
        
#         switch_to_wifi()
# ensure_stable_connection()

# def is_connected():
#     try:
#         print("Checking internet connection...")
#         response = requests.get("http://www.google.com", timeout=5)
#         print("Response status code:", response.status_code)
#         return True
#     except requests.ConnectionError:
#         print("Connection error occurred.")
#         return False
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return False

# # Test the function
# if __name__ == "__main__":
#     if is_connected():
#         print("Connected to the internet.")
#     else:
#         print("Not connected to the internet.")

# import speech_recognition as sr
# import pyttsx3
# import pickle
# from collections import defaultdict

# # Initialize the recognizer and the text-to-speech engine
# recognizer = sr.Recognizer()
# tts_engine = pyttsx3.init()

# # Custom class to handle user profile default values
# class UserProfile:
#     def __init__(self):
#         self.preferences = {}
#         self.voice_print = None

# # User Profiles
# user_profiles = defaultdict(UserProfile)

# # Function to save user profiles
# def save_profiles(filename="profiles.pkl"):
#     with open(filename, 'wb') as file:
#         pickle.dump(user_profiles, file)

# # Function to load user profiles
# def load_profiles(filename="profiles.pkl"):
#     global user_profiles
#     try:
#         with open(filename, 'rb') as file:
#             user_profiles = pickle.load(file)
#     except FileNotFoundError:
#         print("Profile file not found, starting with an empty profile list.")

# # Function to add or update user profile
# def update_user_profile(user_name, voice_print, preferences=None):
#     user_profiles[user_name].voice_print = voice_print
#     if preferences:
#         user_profiles[user_name].preferences.update(preferences)

# # Function to recognize the user based on voice
# def recognize_user(audio):
#     for user_name, profile in user_profiles.items():
#         if profile.voice_print and recognizer.recognize_google(audio) == profile.voice_print:
#             return user_name
#     return None

# # Function to convert text to speech
# def set_speech_rate(rate):
#     tts_engine.setProperty('rate', rate)

# def speak(text, user_name=None):
#     voices = tts_engine.getProperty('voices')
#     tts_engine.setProperty('voice', voices[2].id)
#     tts_engine.setProperty('volume', 1.0)
    
#     # Use user-specific preferences if available
#     if user_name and user_name in user_profiles:
#         rate = user_profiles[user_name].preferences.get("speech_rate", 150)
#         tts_engine.setProperty('rate', rate)
    
#     tts_engine.say(text)
#     tts_engine.runAndWait()

# # Function to listen to commands
# def listen_to_command():
#     with sr.Microphone() as source:
#         print("Listening...")
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)
        
#         try:
#             command = recognizer.recognize_google(audio)
#             print(f"User said: {command}")
#             return command, audio
#         except sr.UnknownValueError:
#             print("Sorry, I did not understand that.")
#             return None, audio
#         except sr.RequestError:
#             print("Could not request results; check your network connection.")
#             return None, audio

# # Function to add a new user profile
# def add_user_profile(user_name):
#     print(f"Adding new user: {user_name}")
#     speak(f"Please say your name for voice recognition, {user_name}")
#     _, audio = listen_to_command()
#     voice_print = recognizer.recognize_google(audio)
#     print(f"Captured voice print for {user_name}: {voice_print}")
    
#     preferences = {}
#     speak("Do you have any speech preferences? For example, speak slower or faster.")
#     command, _ = listen_to_command()
#     if command:
#         if "slow" in command:
#             preferences["speech_rate"] = 100
#         elif "fast" in command:
#             preferences["speech_rate"] = 200
    
#     update_user_profile(user_name, voice_print, preferences)
#     save_profiles()
#     speak(f"Profile for {user_name} has been saved.")
    
# def update_existing_profile(user_name):
#     if user_name in user_profiles:
#         speak(f"Updating profile for {user_name}. Please say your new voice print.")
#         _, audio = listen_to_command()
#         voice_print = recognizer.recognize_google(audio)
#         print(f"Captured new voice print for {user_name}: {voice_print}")
        
#         preferences = {}
#         speak("Do you have any new speech preferences? For example, speak slower or faster.")
#         command, _ = listen_to_command()
#         if command:
#             if "slow" in command:
#                 preferences["speech_rate"] = 100
#             elif "fast" in command:
#                 preferences["speech_rate"] = 200
        
#         update_user_profile(user_name, voice_print, preferences)
#         save_profiles()
#         speak(f"Profile for {user_name} has been updated.")
#     else:
#         speak(f"Profile for {user_name} does not exist.")
        
# # Example usage
# if __name__ == "__main__":
#     load_profiles()
    
#     # Uncomment the line below to add a new user
    

#     command, audio = listen_to_command()
    
#     if command:
#         if "add new" in command:
#             speak("tell me your name for adding you to the system")
#             user=listen_to_command()
#             add_user_profile(user)
#         elif "update userid" in command:
#             speak("tell me your name for updating your to the system")
#             user=listen_to_command()
#             add_user_profile(user)
#             update_existing_profile(user)
#         user_name = recognize_user(audio)
#         if user_name:
#             print(f"Recognized user: {user_name}")
#             speak(f"Hello, {user_name}! How can I assist you today?", user_name)
#         else:
#             print("User not recognized.")
# import pyttsx3

# # Initialize the TTS engine
# tts_engine = pyttsx3.init()

# # Retrieve all available voices
# voices = tts_engine.getProperty('voices')

# # Display each voice's properties
# for index, voice in enumerate(voices):
#     print(f"Voice {index}:")
#     print(f" - Name: {voice.name}")
#     print(f" - ID: {voice.id}")
#     print(f" - Languages: {voice.languages}")
#     print(f" - Gender: {voice.gender}")
#     print("------")
