from Articulos.init import *

f = open ("./Resultados/eventos.csv", "w+")
for item in eventos:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()



