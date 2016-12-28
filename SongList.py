class SongList(object):
	sub_folder = ''
	song_list_files: list = []


	def get_sub_folder(self) -> str:
		return self.sub_folder


	def get_song_list_files(self) -> list:
		return self.song_list_files


	def set_sub_folder(self, folder_name: str):
		self.sub_folder = folder_name


	def set_song_list_files(self, liste: list):
		self.song_list_files = liste
