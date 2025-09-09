# this need premium acount for play
# 
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth

# # Set up your credentials
# client_id = 'b4366c50d6004c7e8151d33296349b91'
# client_secret = '1510ba2b7c424923910e132de5b1f0f8'
# redirect_uri = 'http://localhost:8888/callback'

# scope = 'user-library-read user-modify-playback-state user-read-playback-state'

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
#                                                 client_secret=client_secret,
#                                                 redirect_uri=redirect_uri,
#                                                 scope=scope))

#     # Search for a track
# track_name = 'Shape of You'  # Replace with your desired track name
# results = sp.search(q=track_name, limit=1, type='track')
# # results = sp.current_user_saved_tracks()
# track_id = results['tracks']['items'][0]['id']

# # for idx, item in enumerate(results['items']):
# #     track = item['track']
# #     print(f"{idx + 1}. {track['artists'][0]['name']} – {track['name']}")
    
    
# #     # Get the available devices
# devices = sp.devices()
# print(devices)


# if devices['devices']:
#     for device in devices['devices']:
#         print(f"Device Name: {device['name']}, Device Type: {device['type']}, Device ID: {device['id']}")
#     device_id = devices['devices'][0]['id']  # Choose the first available device

#         # Play the track on the selected device
#     sp.start_playback(device_id=device_id, uris=[f'spotify:track:{track_id}'])
#     print(f'Playing {track_name} on {devices["devices"][0]["name"]}')
# else:
#         print('No available devices found.')


# deezer api not awaible in india
# import requests

# url = "https://deezerdevs-deezer.p.rapidapi.com/infos"

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

# # Deezer API credentials
# rapidapi_key = "0fedadc180msh92c390c5f0693dfp1307dajsnbf283b6ad5d6"

# # Define the headers for the API request
# headers = {
#     "x-rapidapi-key": rapidapi_key,
#     "x-rapidapi-host": "deezerdevs-deezer.p.rapidapi.com"
# }

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

# # Your API key
# api_key = "Q7xqw_kCmgH9wub06HUqs"

# # Define the API endpoint
# graphql_url = f"https://osdb-api.confidence.sh/graphql/{api_key}/"

# # Define the GraphQL query
# query = """
# query {
#   searchSong(input: {query: "do you know", limit: 3}) {
#     id
#     name
#     duration
#   }
#   song(id: "5eab924441b68077f13207ad") {
#     id
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

# # Replace with your Mixcloud username
# username = "Dineshkumarkarn"

# # URL for the Mixcloud API endpoint
# url = f"https://api.mixcloud.com/{username}/uploads/"

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
    
        
    

    


    
