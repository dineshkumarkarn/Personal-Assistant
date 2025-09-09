# import speech_recognition as sr
# import socket

# def listen_for_command():
#     recognizer = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening for command...")
#         audio = recognizer.listen(source)

#     try:
#         command = recognizer.recognize_google(audio).lower()
#         print(f"Command received: {command}")
#         return command
#     except sr.UnknownValueError:
#         print("Sorry, I did not understand the command.")
#         return None
#     except sr.RequestError:
#         print("Could not request results; check your network connection.")
#         return None

# def send_command_to_mobile(command):
#     host = "192.0.0.4"
#     port = 12345

    

#     try:
#         with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#             s.connect((host, port))
#             s.sendall(command.encode())
#             s.close()
#     except ConnectionRefusedError:
#         print(f"Connection refused. Ensure the server is running on {host}:{port}.")
#     except socket.error as err:
#         print(f"Socket error: {err}")


# if __name__ == '__main__':
#     while True:
#         command = listen_for_command()
#         if command:
#             if "on" in command:
#                 send_command_to_mobile("on")
#             elif "off" in command:
#                 send_command_to_mobile("off")

import os
import time
import os

def is_screen_on(device_ip):
    os.system(f'adb connect {device_ip}:5555')
    result = os.popen(f'adb -s {device_ip}:5555 shell dumpsys display').read()
    
    # Check for various display states that indicate the screen is on
    is_on = 'mState=ON' in result or 'mScreenState=ON' in result
    
    return is_on

# Example usage
device_ip = '192.0.0.4'
screen_on = is_screen_on(device_ip)
print(f'Screen is on: {screen_on}')

def flashlight_on(device_ip, turn_on=True):
    os.system(f'adb connect {device_ip}:5555')
    os.system(f'adb -s {device_ip}:5555 shell am broadcast -a com.android.systemui.torch.TOGGLE')
    
    if screen_on==False:
            print("turning on the light")
        # os.system(f'adb connect {device_ip}:5555')
            os.system(f'adb -s {device_ip}:5555 shell input keyevent 224')
            # Input the passkey
            os.system(f'adb -s {device_ip}:5555 shell input text {5825}')
            # Press Enter to unlock
            os.system(f'adb -s {device_ip}:5555 shell input keyevent 66')
    elif screen_on==True:
        os.system(f'adb -s {device_ip}:5555 shell input text {5825}')
        time.sleep(2)
        # Turn on the flashlight using chemara
        # os.system(f'adb -s {device_ip}:5555 shell am start -a android.media.action.STILL_IMAGE_CAMERA')
       

        # os.system(f'adb -s {device_ip}:5555 shell input keyevent 26')
        os.system(f'adb -s {device_ip}:5555 shell input swipe 1000 100 500 500')
        time.sleep(1)
        os.system(f'adb -s {device_ip}:5555 shell input tap 500 1000')

def flashlight_off(device_ip, turn_on=False):
        # Turn off the flashlight
        if screen_on==False:
            print("turning off the light")
        # os.system(f'adb connect {device_ip}:5555')
            os.system(f'adb -s {device_ip}:5555 shell input keyevent 224')
            # Input the passkey
            os.system(f'adb -s {device_ip}:5555 shell input text {5825}')
            # Press Enter to unlock
            os.system(f'adb -s {device_ip}:5555 shell input keyevent 66')
        elif screen_on==True:
            os.system(f'adb -s {device_ip}:5555 shell input text {5825}')
        time.sleep(2)
        os.system(f'adb -s {device_ip}:5555 shell input swipe 1000 100 500 500')
        time.sleep(1)
        os.system(f'adb -s {device_ip}:5555 shell input tap 500 1000')
        # os.system(f'adb -s {device_ip}:5555 shell input keyevent KEYCODE_BACK')
        os.system(f'adb -s {device_ip}:5555 shell input keyevent 26')

# Replace with your device's IP address
device_ip = '192.0.0.4'  # Replace with the actual IP address

# Turn on the flashlight
# toggle_flashlight(device_ip, turn_on=True)

# Wait for 10 seconds before turning it off (adjust as needed)
# import time
# time.sleep(10)
flashlight_on(device_ip, turn_on=True)
time.sleep(10)
flashlight_off(device_ip, turn_on=False)

# toggle_flashlight(device_ip, turn_on=False)



