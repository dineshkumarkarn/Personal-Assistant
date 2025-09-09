# this need premium acount for play
# 
#

# if devices['devices']:
#     for device in devices['devices']:
#         print(f"Device Name: {device['name']}, Device Type: {device['type']}, Device ID: {device['id']}")
#     device_id = devices['devices'][0]['id']  # Choose the first available device


# headers = {
# 	"x-rapidapi-key": "0fedadc180msh92c390c5f0693dfp1307dajsnbf283b6ad5d6",
# 	"x-rapidapi-host": "deezerdevs-deezer.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())

# import requests
# import requests
# import deezer
# import vlc
# import time


# # Function to search for a track
# def search_track(track_name):
#     search_url = "https://deezerdevs-deezer.p.rapidapi.com/search"
#     querystring = {"q": track_name}

#     response = requests.get(search_url, headers=headers, params=querystring)
#     return response.json()

# # Example usage
# track_name = "do you know"  # Replace with your desired track name
# track_info = search_track(track_name)

# # Print track details
# if track_info['data']:
#     track = track_info['data'][0]
#     print(f"Track ID: {track['id']}")
#     print(f"Track Name: {track['title']}")
#     print(f"Track URL: {track['link']}")
# else:
#     print("Track not found")
    
# web_url=track['link']
# player = vlc.MediaPlayer(web_url)
# player.play()

# # Keep the script running to listen to the music
# while True:
#     time.sleep(1)



# open song database give only data not able to play

# import requests

#

# # Define the GraphQL query
# query = """
# query {
#   searchSong(input: {query: "do you know", limit: 3}) {
#     id
#     name
#     duration
#   }
#   song(id
#     name
#     duration
    
#   }
# }
# """

# # Define the headers for the API request
# headers = {
#     "Content-Type": "application/json"
# }

# # Make the API request
# response = requests.post(graphql_url, headers=headers, json={'query': query})

# # Print the response text (for debugging purposes)
# print("Response Text:", response.json())

# # Check the status code and process the response
# if response.status_code == 200:
#     try:
#         data = response.json()
#         if 'data' in data and 'searchSong' in data['data']:
#             track = data['data']['searchSong'][0]
#             print(f"Track ID: {track['id']}")
#             print(f"Track Name: {track['name']}")
#             print(f"Track Duration: {track['duration']} seconds")
#             # print(f"Track URL: {track['link']}")
#         else:
#             print("Track not found")
#     except ValueError:
#         print("Invalid JSON response")
# else:
#     print(f"Error: {response.status_code}")
#     print("Response Headers:", response.headers)
#     print("Response Content:", response.content)


# #mixclud
# import requests





# # Send a GET request to the API endpoint
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     data = response.json()
#     print("Uploads:")
#     for item in data["data"]:
#         print(f"- {item['name']}: {item['url']}")
# else:
#     print(f"Failed to retrieve data: {response.status_code}")




import pygame
import os

# Initialize pygame
pygame.init()

# Path to the folder containing music files
music_folder = "/Users/dines/OneDrive/Desktop/ingen dynamics/Aido personal assistant/music"

# Get a list of all music files in the folder
playlist = [os.path.join(music_folder, file) for file in os.listdir(music_folder) if file.endswith(".mp3")]

# Current track index
current_track_index = 0

def play_music(track_index):
    pygame.mixer.music.load(playlist[track_index])
    pygame.mixer.music.play()
    pygame.mixer.music.set_endevent(pygame.USEREVENT)

def next_track():
    global current_track_index
    current_track_index += 1
    if current_track_index >= len(playlist):
        current_track_index = 0
    play_music(current_track_index)

def previous_track():
    global current_track_index
    current_track_index -= 1
    if current_track_index < 0:
        current_track_index = len(playlist) - 1
    play_music(current_track_index)
    
def main():
    play_music(current_track_index)
    
        
    

    


    
