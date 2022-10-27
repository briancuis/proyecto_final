from mi_app.models import familiares, futbolista

familiares(nombre="brian", direccion="aaa 123", edad=17).save()
familiares(nombre="juan", direccion="aaa 124", edad=22).save()
familiares(nombre="silvia", direccion="aaa 125", edad=30).save()

futbolista(nombre="Lionel Messi", edad=35, equipo="Paris Saint Germain")
futbolista(nombre="Rodrigo De Paul", edad=28, equipo="Atletico de Madrid")
futbolista(nombre="Leandro Paredes", edad=28, equipo="Juventus")


print("se cargo exitosamente")