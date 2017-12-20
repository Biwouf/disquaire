#from django.shortcuts import render
from django.http import HttpResponse

#from .models import ALBUMS, ARTISTS

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
	#On récupère la valeur associée au paramètre query
	query = request.GET['query']
	#Si la query est vide
	if not query:
		message = "Vous devez utilisez le paramètre query pour passer votre recherche"
	else:
		#On génère une liste (de dictionnaires) des albums où les artistes de l'albums correspondent à la query.
		albums = [album for album in ALBUMS
					if query in [artists['name'] for artists in album['artists']]]

		#Si aucun résultat
		if len(albums) == 0:
			message = "Nous n'avons trouvé aucun album correspondant à votre recherche"
		#
		else:
			#Dans le dictionnaire, on utilise seulement le nom de l'album
			albums = [album['name'] for album in albums]
			message = """
			Voici les albums correspondant à votre recherche : 
			<ul>
				<li>
				{}
				</li>
			</ul>
			""".format("</li><li>".join(albums))

	return HttpResponse(message)




