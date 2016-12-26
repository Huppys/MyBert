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


def build_media_path(index):
	# index = f.index(vlc_player.get_media) + 1
	return vlc_instance.media_new_path(audioSourcePath + files_list[index])


# build a media list from folder
def build_media_list(list):
	# Create a new media list
	vlc_media_list = vlc_instance.media_list_new()
	# Iterate items in list
	for song in list:
		vlc_media_list.add_media(vlc_instance.media_new_path(audioSourcePath + song))
	print(vlc_media_list)
	return vlc_media_list


def wait_for_input():
	print('waiting for input')
	song = int(input('Next Song?: '))
	if vlc_player.get_state() is vlc.State.Playing:
		vlc_player.stop()
	vlc_player.set_media(build_media_path(song))
	print(vlc_player.get_media())
	vlc_player.play()


# wait_for_input()

def start_media_playlist():
	print('starting first song')
	starting = input('start?: ')
	print(vlc_player.is_playing())
	if vlc_player.is_playing() is 0:
		vlc_player.set_media_list(build_media_list(files_list))
	else:
		print('Playing next song')
		vlc_player.next()
	vlc_player.play()


start_media_playlist()

while True:
	print(vlc_player.get_state())
	start_media_playlist()
	pass
