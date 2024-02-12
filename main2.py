import openpyxl, time

#Bin
import Articulos.libros, Articulos.init

def get_maximum_rows(*, sheet_object):
    rows = 0
    for max_row, row in enumerate(sheet_object, 1):
        if not all(col.value is None for col in row):
            rows += 1
    return rows

start_time = time.time()

print ("Lectura de registros")
wb = openpyxl.load_workbook('./Input/Base.xlsx')
sheet = wb['Sheet1']
total = get_maximum_rows(sheet_object=sheet)
COD_PRODUCTO = 1
print("Los CvLAC han sido cargados, Estado: " + str(1/(total-1)*100) + "%")
Articulos.init.inicio()
for q in range(2,total+1):
    name = sheet['B'+str(q)].value
    my_url = sheet['C'+str(q)].value
    index1 = my_url.find("cod_rh=") + 7
    index2 = len(my_url)
    RH = my_url[index1:index2]

    if my_url != '-':
        Articulos.libros.artiextract()
        COD_PRODUCTO = int("".join(str(x) for x in Articulos.libros.contarlibro))
        print(""+name + " ha sido procesado, Estado: " + str(q/(total-1)*100) + "%")
        print("-----------------------------------------------------------------------------------------------")
        print("")
        print("------> ¡Extracción Exitosa!")
        print("------> La información se encuentra en la carpeta: Resultados.")
        print("------> Tiempo de ejecución: %s Minutos." % ((time.time() - start_time)/60))
        print("")
        print("***********************************************************************************************")
    
import printcsv_2