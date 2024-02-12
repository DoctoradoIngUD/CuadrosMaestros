from Articulos.init import *

f = open ("./Resultados/articulos.csv", "w+")
for item in articulos:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()


