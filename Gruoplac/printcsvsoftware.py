from Articulos.init import *

f = open ("./Resultados/software.csv", "w+")
for item in software:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()


