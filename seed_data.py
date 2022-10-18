from mi_app.models import familiares

familiares(nombre="brian", direccion="aaa 123", edad=17).save()
familiares(nombre="juan", direccion="aaa 124", edad=22).save()
familiares(nombre="silvia", direccion="aaa 125", edad=30).save()


print("se cargo exitosamente")