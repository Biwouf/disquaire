from django.db import models

# Create your models here.

class Artist(models.Model):
	name = models.CharField(unique=True, max_length=200)

class Contact(models.Model):
	email = models.EmailField(max_length=100)
	name = models.CharField(max_length=200)

class Album(models.Model):
	reference = models.IntegerField(null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	available = models.BooleanField(default=True)
	title = models.CharField(max_length=200)
	picture = models.URLField
	artists = models.ManyToManyField(Artist, related_name=albums, blank=True)

class Booking(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	contacted = models.BooleanField(default=False)
	contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
	album = models.OneToOneField(Album)

#ARTISTS = {
 # 'francis-cabrel': {'name': 'Francis Cabrel'},
  #'lej': {'name': 'Elijay'},
  #'rosana': {'name': 'Rosana'},
  #'maria-dolores-pradera': {'name': 'María Dolores Pradera'},
#}


#ALBUMS = [
  #{'name': 'Sarbacane', 'artists': [ARTISTS['francis-cabrel']]},
  #{'name': 'In extremis', 'artists': [ARTISTS['francis-cabrel']]},
  #{'name': 'La Dalle', 'artists': [ARTISTS['lej']]},
  #{'name': 'Luna Nueva', 'artists': [ARTISTS['rosana'], ARTISTS['maria-dolores-pradera']]}
#]