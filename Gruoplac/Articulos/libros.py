def artiextract():
    from mainLibros import my_url, name, RH, COD_PRODUCTO

    import Articulos.init, bs4, logging, sys, re, ssl
    global contarlibros
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
    ssl._create_default_https_context = ssl._create_unverified_context
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    all = 0
    a = 0
    x = 0
    y = 0
    page_soup = soup(page_html,"html.parser")
    containers = page_soup.findAll("table")
    
    '''Imprimir en archivo HTML el CVLAC en el directorio raiz
    # Obtener el contenido HTML formateado
    html = page_soup.prettify()
    # Escribir el contenido en un archivo HTML
    with open("cvlac.html", "w") as file:
        file.write(html)'''
    '''Imprimir segmento de código en archivo HTML en el directorio raiz
    # Abrir el archivo de salida en modo escritura
    with open("containers.html", "w") as file:
        # Escribir la etiqueta de apertura de la página
        file.write("<html><head><title>Containers</title></head><body>")
        # Iterar sobre cada container
        for container in containers:
            # Agregar el contenido del container al archivo de salida
            file.write(str(container))
        # Escribir la etiqueta de cierre de la página
        file.write("</body></html>")'''
    '''Obtener nombre a quien pertenece el CvLAC'''
    Grupo = None
    a_tag = page_soup.find("span", {"class": "celdaEncabezado"})
    Grupo =  a_tag.text.strip()  




    for a in range(0,len(containers)):
        buscaeventos = containers[a].td
        #print(buscaeventos)
        try:
            if buscaeventos.text == " Libros publicados ":
                all = a

                break
            
        except AttributeError:
            pass

    if all != 0:
        containerb = containers[all]
        #print(containerb)
        container = containerb.findAll("tr")
        #tipoart = containerb.findAll("td")

        for x in range(0, len(container)):
            cont = container[x]
            #tipoar = tipoart[x]
            #tipo = tipoar.text
            info_libro = cont.text
            # print(info_libro)

            # Nombre Libro      
            index1 = info_libro.find("Libro resultado de investigación") + 35
            index2 = info_libro.find("\n", index1) - 1
            Titulo = info_libro[index1:index2]      
            #Pais 
            index3 = info_libro.find(",",index2 + 18)
            Pais = info_libro[index2+18:index3]
            #AÑO 
            index4 = info_libro.find("\n",index3)
            index5 = info_libro.find(",",index4)
            ANIO = info_libro[index5 - 4 : index5 ]
            #ISBN
            index1 = info_libro.find('ISBN: ') + 6
            index2 = info_libro.find(",",index1)
            ISBN = info_libro[index1:index2]
            #AUTORES
            index1 = info_libro.find("Autores:") + 8
            index2 = info_libro.find("\n", index1) - 1
            AUTORES = info_libro[index1:index2]
    


            Articulos.init.libros.append(RH+";"\
                                    + Grupo + ";"\
                                    + Titulo + ";" \
                                    + Pais + ";"\
                                    + ISBN + ";"\
                                    + ANIO + ";"\
                                    + AUTORES + ";"
                                    + "\n")
            

            """
            Bin.init.rel_persona_producto_colciencias.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',tipo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',NombreProducto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "0" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',AnoEvento.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',coautores.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',editorial.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Volumen.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',doi.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" \
            + "\n")
            Bin.init.colciencias_prod_bibliografica.append(RH + ";"\
            + str(COD_PRODUCTO) + ";"\
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Revista.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',ISSN.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + "" + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',fasciculo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagini.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò]',r'',re.sub(' +',' ',Pagfin.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" \
            + "\n")"""
            COD_PRODUCTO = COD_PRODUCTO + 1
    contarlibros = [COD_PRODUCTO]
