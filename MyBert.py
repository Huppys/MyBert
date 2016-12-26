from os import walk
from vlc import vlc

print('This is MyBert playing some songs')

files_list = []
audioSourcePath = 'audio/'
for (dirpath, dirnames, filenames) in walk(audioSourcePath):
	for file in filenames: # filter for files with extension '.mp3'
		if '.mp3' not in file:
			filenames.remove(file)
	files_list.extend(filenames)
	break

print(files_list)

# Create a new vlc player instance
vlc_instance = vlc.Instance()
# Create a new media list player
vlc_player = vlc_instance.media_list_player_new()


# build a media list from folder
def build_media_list(list):
	# Create a new media list
	vlc_media_list = vlc_instance.media_list_new()
	# Iterate items in list
	for song in list:
		vlc_media_list.add_media(vlc_instance.media_new_path(audioSourcePath + song))
	# print(vlc_media_list)
	return vlc_media_list


def start_media_playlist():
	user_input = input('Make your input: ')
	# print(vlc_player.is_playing())
	if vlc_player.is_playing() is 0:
		vlc_player.set_media_list(build_media_list(files_list))
		print('Initializing song list')
	else:
		print('Playing next song')
		vlc_player.next()
	vlc_player.play()


start_media_playlist()

while True:
	# print(vlc_player.get_state())
	start_media_playlist()
	pass
