from gmusicapi import Webclient
import os
import getpass

api = Webclient()

api.__init__()

while (api.login(raw_input('Email: '), getpass.getpass()) == False):
	print 'Error, try again'

i = 1
for playlist in api.get_all_playlist_ids()['user']:
	print str(i) + '. ' + playlist
	i += 1

while True:
	chosen_number = int(raw_input('Choose a playlist to export (enter the number): '))
	if chosen_number < i and chosen_number >= 0:
		break
	else:
		print 'Error, try again'

i = 1
for playlist in api.get_all_playlist_ids()['user']:
	if i == chosen_number:
		chosen_id = api.get_all_playlist_ids()['user'][playlist][0]
		chosen_name = playlist
		break
	else:
		i += 1

songs = []

for song in api.get_playlist_songs(chosen_id):
	songs.append(song['artist'] + ' - ' + song['album'] + ' - ' + song['name'])

songs.sort(key=lambda s: s.lower())

f = open(os.path.join(os.path.dirname(__file__), playlist + '.txt'), "w")
for song in songs:
 	f.write(song.encode("utf-8") + "\n")

api.logout()

raw_input('Success! Press enter to exit.')