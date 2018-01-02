#from django.shortcuts import render
from django.http import HttpResponse

from .models import Album, Artist, Contact, Booking

# Create your views here.
def index(request):
	"""Page d'accueil"""
	#On trie par date de création. On affiche que les trois derniers albums créés)
	albums = Album.objects.filter(available=True).order_by('-created_at')[:3]
	complete_message = (album.title for album in albums)
	message = """
	Voici la liste des derniers albums disponibles : 
	<ul>
		<li>
		{}
		</li>
	</ul>
	""".format("</li><li>".join(complete_message))
	return HttpResponse(message)

def store(request):
	message = 'Bienvenue sur la page store'
	return HttpResponse(message)

def listing(request):
	"""Affiche le listing des albums en base"""
	albums = Album.objects.filter(available=True).order_by('-created_at')
	message = """<ul><li>{}</li></ul>""".format('</li><li>'.join(album.title for album in albums))
	return HttpResponse(message)

def detail(request, album_id):
	"""Affiche le détail d'un album. Url attendue : store/{id}"""
	album = Album.objects.get(pk=album_id)
	artists = " ".join(artist.name for artist in album.artists.all())
	message = "Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
	return HttpResponse(message)

def search(request):
	#On récupère la valeur associée au paramètre query
	query = request.GET['query']
	#Si la query est vide, on renvoie tous les albums
	if not query:
		albums = Album.objects.all()
	else:
		#L'attribut icontains permet de matcher une partie du texte
		#Et rend le match insensible à la casse.
		albums = Album.objects.filter(title__icontains=query)

		#On vérifie s'il y a une occurrence
		if not albums.exists():
			#Si rien, on essaye de matcher les artistes
			albums = Album.objects.filter(artists__name__icontains=query)

		#Si tjours rien page d'erreur
		if not albums.exists():
			message = "Désolé nous n'avons trouvé aucun résultat"

		else:
			albums = [album.title for album in albums]
			message = """
			Voici les albums correspondant à votre recherche : 
			<ul>
				<li>
				{}
				</li>
			</ul>
			""".format("</li><li>".join(albums))


		#On génère une liste (de dictionnaires) des albums où les artistes de l'albums correspondent à la query.
		#albums = [album for album in ALBUMS
		#			if query in [artists['name'] for artists in album['artists']]]

		#Si aucun résultat
		#if len(albums) == 0:
		#	message = "Nous n'avons trouvé aucun album correspondant à votre recherche"
		#
		#else:
		#	#Dans le dictionnaire, on utilise seulement le nom de l'album
		#	albums = [album['name'] for album in albums]
		#	message = """
		#	Voici les albums correspondant à votre recherche : 
		#	<ul>
		#		<li>
		#		{}
		#		</li>
		#	</ul>
		#	""".format("</li><li>".join(albums))

	return HttpResponse(message)




