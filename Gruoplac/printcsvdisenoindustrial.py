from Articulos.init import *

f = open ("./Resultados/disenoIndustrial.csv", "w+")
for item in diseno:
    try:
        f.write(item)
    except UnicodeEncodeError:
        pass
f.close()


