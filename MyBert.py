from os import walk
from vlc import vlc
from SongList import SongList

print('This is MyBert playing some songs')

audio_source_path: str = 'audio/'
audio_sub_folder: str = ''

# Create a new vlc player instance
vlc_instance = vlc.Instance()
# Create a new media list player
vlc_player = vlc_instance.media_list_player_new()


def get_files_in_folder(index: int) -> SongList:
	song_list = SongList  # Create new SongList object to store songs in list with a subfolder path
	for (dirpath, dirnames, filenames) in walk(audio_source_path):  # iterate over all folders in './audio'
		# print('initial dir:', dirpath)
		# print('initial dir contains those folders:', dirnames)
		if len(dirnames) <= index:
			index %= len(dirnames)
		for (dir_path, dir_names, file_names) in walk(audio_source_path + dirnames[index] + '/'):
			print('selected dir_path: ', dir_path)
			song_list.set_sub_folder(song_list, dir_path)
			for file in file_names:  # filter for files with extension '.mp3'
				if '.mp3' not in file:
					file_names.remove(file)
			song_list.set_song_list_files(song_list, file_names)
			return song_list


# build a media list from folder
def build_media_list(song_list: SongList) -> vlc.MediaList:
	# Create a new media list
	vlc_media_list = vlc_instance.media_list_new()
	# Iterate items in list
	for song in song_list.song_list_files:
		# print(song_list.sub_folder + song)
		vlc_media_list.add_media(vlc_instance.media_new_path(song_list.sub_folder + song))
	# print(vlc_media_list)
	return vlc_media_list


def start_media_playlist():
	user_input = input('Make your input: ')
	if user_input is '':
		user_input = -1
	# print(vlc_player.is_playing())
	if vlc_player.is_playing() is 0 and user_input is -1:
		vlc_player.set_media_list(build_media_list(get_files_in_folder(0)))
		print('Initializing song list')
	elif vlc_player.is_playing() is not 0 and int(user_input) >= 0 and int(user_input) <= 9:
		vlc_player.stop()
		vlc_player.set_media_list(build_media_list(get_files_in_folder(int(user_input))))
	else:
		print('Playing next song')
		vlc_player.next()
	vlc_player.play()


start_media_playlist()

while True:
	# print(vlc_player.get_state())
	start_media_playlist()
	pass
