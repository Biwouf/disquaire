#from django.shortcuts import render
from django.http import HttpResponse

from .models import ALBUMS, ARTISTS

# Create your views here.
def index(request):
	message = 'Salut tout le monde'
	return HttpResponse(message)

def store(request):
	message = 'Bienvenue sur la page store'
	return HttpResponse(message)

def listing(request):
	"""Affiche le listing des albums en base"""
	albums = ['<li>{}</li>'.format(album['name']) for album in ALBUMS]
	message = """<ul>{}</ul>""".format('\n'.join(albums))
	return HttpResponse(message)

def detail(request, album_id):
	"""Affiche le détail d'un album. Url attendue : store/{id}"""
	id = int(album_id)
	album = ALBUMS[id]
	artists = " ".join([artist['name'] for artist in album['artists']])
	message = "Le nom de l'album est {}. Il a été écrit par {}".format(album['name'], artists)
	return HttpResponse(message)

def search(request):
	"""Vue qui gère une recherche avec un paramètre query qui s'attend à avoir un artist"""
	query = request.GET.get('query')
	#message = "Propriété GET {} et la requête est {}".format(obj, query)

	if not query:
		message = "Utilisez le paramètre query"
	else:
		#albums = [album for album in ALBUMS
		#			if query in " ".join(artist['name'] for artist in album['artists'])]

		albums = []
		albums_def = []
		for album in ALBUMS:
			albums.append(album)

		#for artist in albums['artists']:
		#	print(artist)

	return HttpResponse(albums)




