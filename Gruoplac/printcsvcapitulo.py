from Articulos.init import *

f = open ("./Resultados/capitulos.csv", "w+")
for item in capitulos:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()


