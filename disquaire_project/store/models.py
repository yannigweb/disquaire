from django.db import models

# Create your models here.
ARTISTS = {
    'francis-cabrel':{'name':'Francis Cabrel'},
    'lej':{'name':'Elijay'},
    'rosana':{'name':'Rosana'},
    'renaud':{'name':'Renaud Sechan'},
}

ALBUMS = [
    {'name':'Sarbacane', 'artists':[ARTISTS['francis-cabrel']]},
    {'name':'La Dalle','artists':[ARTISTS['lej']]},
    {'name':'Marchand de cailloux','artists':[ARTISTS['renaud']]}
]
