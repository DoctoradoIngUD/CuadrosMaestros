from Articulos.init import *

f = open ("./Resultados/proyectos.csv", "w+")
for item in proyectos:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()



