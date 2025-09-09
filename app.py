import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

# Function to convert text to speech    
def speak(text):
    voices = tts_engine.getProperty('voices')
    tts_engine.setProperty('voice', voices[2].id)
    tts_engine.setProperty('volume', 1.0)
    tts_engine.setProperty('rate', 150)
    tts_engine.say(text)
    tts_engine.runAndWait()

# Function to listen to commands
def listen_to_command():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak(f"Could not request results; {e}")
        except Exception as e:
            print(f"An error occurred; {e}")
            speak(f"An error occurred; {e}")

# Function to handle commands
def handle_command(command):
    if command is not None:
        if "hello" in command.lower():
            print("hello, nice to see you what i do now for you")
            speak("Hello! How can I assist you today?")
        elif "good bye" in command.lower():
            speak("Goodbye! Have a nice day!")
        elif 'play music' in command.lower():
            play_music()
        elif 'schedule' in command.lower():
            daily_shedules()
        elif 'turn on light' or 'turn off light' in command.lower():
            control_light()
            
        else:
            speak("Sorry, I can't do that yet.")
    else:
        speak("said, Louadly")
        
def play_music():
    from play_music import main,pygame,next_track,current_track_index,previous_track
    speak("i'm going to play music hope you enjoy ")
    if __name__=="__main__":
            main()
            while pygame.mixer.music.get_busy():
                for event in pygame.event.get():
                    if event.type == pygame.USEREVENT:  # Music finished playing
                        next_track()
                recognizer = sr.Recognizer()

                with sr.Microphone() as source:
                    print("Listening...")
                    audio = recognizer.listen(source)
                
                try:
                    command = recognizer.recognize_google(audio)
                    print("You said:", command)
                
                except Exception as e:
                    print(f"An error occurred; {e} with: {command}")
                    speak(f" {e}with: {command}")
                    
                try:
                    if "next" or "last" or "off music" or "stop"or"pause" in command.lower():
                        if "next" in command:  
                                next_track()
                        elif "last" in command: 
                                previous_track()  
                                
                        elif "stop"or"pause"or"off music" in command.lower():
                                pygame.mixer.music.stop()
                                break
                    else:
                        print(command)
                        print("said again")
                except:
                    print(command)  
                
                
    print("revisit again")

def daily_shedules():
    speak(f"this is your{command} schedule ")
    from dailly_schedule import main
    com=command
    main(com)
    
def control_light():
    from control_light import flashlight_on,flashlight_off,device_ip
    if "on" in command:
        flashlight_on(device_ip, turn_on=True)
    elif "off" in command:
        flashlight_off(device_ip, turn_on=False)
    else:
        
     speak("i'm , not able to this right now")


if __name__ == "__main__":
    from test_network import ensure_stable_connection
    ensure_stable_connection()
    while True:
        from user_authentication import  recognize_user,load_profiles,add_user_profile,update_existing_profile,listen_command,speek
        load_profiles()
        
        speak("please tell you name for user verification")
        cammand, audio = listen_command()
        if cammand:
            if "add new" in cammand:
                speak("tell me your name for adding you to the system")
                user=listen_to_command()
                add_user_profile(user)
                
            elif "update userid" in cammand:
                    speak("tell me your name for updating your to the system")
                    user=listen_to_command()
                    
                    update_existing_profile(user)
            
            
            user_name = recognize_user(audio)
            if user_name:
                print(f"Recognized user: {user_name}")
                speek(f"Hello, {user_name}! How can I assist you today?", user_name)
                command = listen_to_command()
                while True:
                    command = listen_to_command()
                    if command!='shutdown':
                        handle_command(command)
                    
                    elif command=='shutdown':
                        should_stop = True
                        speak(",Thank you, Have A nice day")
                        break
                    else:
                        break
                    speek(f"Hello,! How can I assist you today?")
                if should_stop:
                    break
            else:
                print("User not recognized.")
       
        
