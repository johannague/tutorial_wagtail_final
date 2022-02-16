'''
crear canciones

ejecutar:

python manage.py shell < datos/crear_canciones.py
'''

from canciones.models import Cancion
import json
import os

# borrar canciones
for p in Cancion.objects.all():
    p.delete()

#lista de canciones del json
if os.path.exists("datos/datos_cancion.json"):
    canciones = json.load(open("datos/datos_cancion.json"))
else:
    canciones = json.load(open("datos_cancion.json"))


'''
{
        "img": "https://m.media-amazon.com/images/M/MV5BMDFkYTc0MGEtZmNhMC00ZDIzLWFmNTEtODM1ZmRlYWMwMWFmXkEyXkFqcGdeQXVyMTMxODk2OTU@._V1_UY67_CR0,0,45,67_AL_.jpg",
        "url": "/title/tt0111161/",
        "cast": "Frank Darabont (dir.), Tim Robbins, Morgan Freeman",
        "titulo": "Cadena perpetua",
        "year": "1994"
    },
'''

for p1 in Cancion:
    p = Cancion()
    p.title = p1["titulo"]
    p.rating = 0 # p1["rating"]
    p.link = "https://www.elportaldemusica.es/" + p1["url"]
    p.place = 0 #p1["place"]
    p.imagen = p1["img"]
    p.singer = p1['singer']
    p.save()

