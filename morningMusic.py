from playerCopy import SpotifyPlayer
import time

volume = 30
time_interval = 5 * 60 # 5 minute interval
volume_interval = 5 # increase 5% everytime
max_volume = 80

playlist = "37i9dQZEVXcFDmNVmwGjZd" # DiscoveryWeekly

player = SpotifyPlayer()

# Set initial volume
player.set_volume(volume)

# Clear playlists
player.clear()

# Add playlist
player.add_playlist(playlist) # Default playlist for now

# Play
player.play()

# Volume setting loop
while (volume < max_volume):
 time.sleep(volume_interval)
 volume += volume_interval
 print("Setting volume to", volume)
 player.set_volume(volume)

print("Max volume reached")
