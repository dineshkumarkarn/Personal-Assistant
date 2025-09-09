import socket
import os
def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        return False

def switch_to_wifi():
    os.system("nmcli radio wifi on")
    os.system("nmcli connection up id 'your_wifi_connection_name'")
    print("Switched to Wi-Fi.")

def switch_to_ethernet():
    os.system("nmcli connection up id 'your_ethernet_connection_name'")
    print("Switched to Ethernet.")

def ensure_stable_connection():
    if is_connected():
        print("Connected to the internet.")
        
    else:
        print("No internet connection. Attempting to switch to Wi-Fi.")
        
        switch_to_wifi()