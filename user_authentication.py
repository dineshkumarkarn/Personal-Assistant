import speech_recognition as sr
import pyttsx3
import pickle
from collections import defaultdict

# Initialize the recognizer and the text-to-speech engine
recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Custom class to handle user profile default values
class UserProfile:
    def __init__(self):
        self.preferences = {}
        self.voice_print = None

# User Profiles
user_profiles = defaultdict(UserProfile)

# Function to save user profiles
def save_profiles(filename="profiles.pkl"):
    with open(filename, 'wb') as file:
        pickle.dump(user_profiles, file)

# Function to load user profiles
def load_profiles(filename="profiles.pkl"):
    global user_profiles
    try:
        with open(filename, 'rb') as file:
            user_profiles = pickle.load(file)
    except FileNotFoundError:
        print("Profile file not found, starting with an empty profile list.")

# Function to add or update user profile
def update_user_profile(user_name, voice_print, preferences=None):
    user_profiles[user_name].voice_print = voice_print
    if preferences:
        user_profiles[user_name].preferences.update(preferences)

# Function to recognize the user based on voice
def recognize_user(audio):
    for user_name, profile in user_profiles.items():
        if profile.voice_print and recognizer.recognize_google(audio) == profile.voice_print:
            return user_name
    return None

# Function to convert text to speech
def set_speech_rate(rate):
    tts_engine.setProperty('rate', rate)

def speek(text, user_name=None):
    voices = tts_engine.getProperty('voices')
    tts_engine.setProperty('voice', voices[2].id)
    tts_engine.setProperty('volume', 1.0)
    
    # Use user-specific preferences if available
    if user_name and user_name in user_profiles:
        rate = user_profiles[user_name].preferences.get("speech_rate", 150)
        tts_engine.setProperty('rate', rate)
    
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to listen to commands
def listen_command():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}")
            return command, audio
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None, audio
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None, audio

# Function to add a new user profile
def add_user_profile(user_name):
    print(f"Adding new user: {user_name}")
    speek(f"Please say your name for voice recognition, {user_name}")
    _, audio = listen_command()
    voice_print = recognizer.recognize_google(audio)
    print(f"Captured voice print for {user_name}: {voice_print}")
    
    preferences = {}
    speek("Do you have any speech preferences? For example, speek slower or faster.")
    command, _ = listen_command()
    if command:
        if "slow" in command:
            preferences["speech_rate"] = 100
        elif "fast" in command:
            preferences["speech_rate"] = 200
    
    update_user_profile(user_name, voice_print, preferences)
    save_profiles()
    speek(f"Profile for {user_name} has been saved.")
    
def update_existing_profile(user_name):
    if user_name in user_profiles:
        speek(f"Updating profile for {user_name}. Please say your new voice print.")
        _, audio = listen_command()
        voice_print = recognizer.recognize_google(audio)
        print(f"Captured new voice print for {user_name}: {voice_print}")
        
        preferences = {}
        speek("Do you have any new speech preferences? For example, speek slower or faster.")
        command, _ = listen_command()
        if command:
            if "slow" in command:
                preferences["speech_rate"] = 100
            elif "fast" in command:
                preferences["speech_rate"] = 200
        
        update_user_profile(user_name, voice_print, preferences)
        save_profiles()
        speek(f"Profile for {user_name} has been updated.")
    else:
        speek(f"Profile for {user_name} does not exist.")
    

      
# Example usage
def user_auth():
    load_profiles()
    
    # Uncomment the line below to add a new user
    
    speek("please tell you name for user verification  and if you are new so tell add users")
    command, audio = listen_command()
    
    if command:
        if "add new" in command:
            speek("tell me your name for adding you to the system")
            user=listen_command()
            add_user_profile(user)
        elif "update userid" in command:
            speek("tell me your name for updating your to the system")
            user=listen_command()
            add_user_profile(user)
            update_existing_profile(user)
        
        
