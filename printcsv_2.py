from Articulos.init import *

f = open ("./Resultados/libros.csv", "w+")
for item in libros:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()



