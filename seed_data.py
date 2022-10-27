from mi_app.models import familiares, futbolistas

familiares(nombre="brian", direccion="aaa 123", edad=17).save()
familiares(nombre="juan", direccion="aaa 124", edad=22).save()
familiares(nombre="silvia", direccion="aaa 125", edad=30).save()

futbolistas(nombre="Lionel Messi", edad=35, equipo="Paris Saint Germain").save()
futbolistas(nombre="Rodrigo de Paul", edad=28, equipo="Real Madrid").save()
futbolistas(nombre="Leandro Paredes", edad=28, equipo="Juventus").save()

print("se cargo exitosamente")