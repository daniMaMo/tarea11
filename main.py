# Ejemplo1: uso de dumps, el cual retorna una resresentaciín string a una data pickled, es decir
# únicamente serializa objetos.
import pickle
from pickle import dumps
from pickle import loads

colores_arcoiris = ['rojo', 'naranja', 'amarillo', 'verde', 'azul', 'indigo', 'violeta']
dctstring = dumps(colores_arcoiris)
print('lista de colores serializada', dumps(dctstring))
print('lista de colores recuperadas con loads', loads(dctstring))

# Ejemplo2: uso de dumps, además de serializar un objeto, lo guardara en un archivo abierto para escritura
# tipo binario

file = open('colores_pickled', 'wb')
pickle.dump(colores_arcoiris, file)
file.close()

file = open('colores_pickled', 'rb')
print(file.read())
file.close()

file = open('colores_pickled', 'rb')
print(pickle.load(file))
file.close()
