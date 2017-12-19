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
	#obj = str(request.GET)
	#query = request.GET['query']
	#message = "Propriété GET {} et la requête est {}".format(obj, query)
	#return HttpResponse(message)
	query = request.GET['query']
	if not query:
		message = "Vous devez utilisez le paramètre query pour passer votre recherche"
	else:
		albums = [album for album in ALBUMS
					if query in [artists['name'] for artists in album['artists']]]

		if len(albums) == 0:
			message = "Nous n'avons trouvé aucun album correspondant à votre recherche"
		else:
			albums = ["<li>{}</li>".format(album['name'] for album in albums)]
			print(albums)
			message = """
			Voici les albums correspondant à votre recherche : 
			<ul>{}</ul>
			""".format("</li><li>".join(albums))

	return HttpResponse(message)




