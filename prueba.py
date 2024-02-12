def artiextract():
    from main import my_url, name, RH, COD_PRODUCTO

    import Bin.init, bs4, logging, sys, re
    global contarticulo
    from urllib.request import urlopen as uReq
    from bs4 import BeautifulSoup as soup
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
    '''Obtener nombre a quien pertenece el CvLAC
    nombre = "NN"
    a_tag = page_soup.find("a", {"name": "datos_generales"})
    if a_tag:
        td_tag = a_tag.find_parent("td")
        if td_tag:
            nombre_td = td_tag.find("td", text="Nombre")
            if nombre_td:
                siguiente_td = nombre_td.find_next_sibling("td")
                if siguiente_td:
                    nombre = siguiente_td.text.strip()
                    print(nombre)'''



    for a in range(0,len(containers)):
        buscaeventos = containers[a].h3
        #print(buscaeventos)
        try:
            if buscaeventos.text == "Artículos":
                all = a
                #print(all)
                break
            
        except AttributeError:
            pass
 
    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("blockquote")
        tipoart = containerb.findAll("li")
        for x in range(0, len(container)):
            cont = container[x]
            tipoar = tipoart[x]
            tipo = tipoar.text
            info_articulo = cont.text
            #Nombre Articulo
            index1 = info_articulo.find('"')
            index2 = info_articulo.rfind('"') + 1
            NombreProducto = info_articulo[index1:index2]
            #print(NombreProducto)
            if tipo.strip() == "Producción bibliográfica - Artículo - Publicado en revista especializada":
                tipo = "8"
            elif tipo.strip() == "Producción bibliográfica - Artículo - Corto (Resumen)":
                tipo = "9"
            elif tipo.strip() == "Producción bibliográfica - Artículo - Revisión (Survey)":
                tipo = "10"
            elif tipo.strip() == "Producción bibliográfica - Artículo - Caso clínico":
                tipo = "11"
            else:
                logging.critical('Añadir: ' + tipo)
                print ("ALERTA: Revisar el archivo Artículos.log")
            #autores
            index1 = 0
            index2 = info_articulo.find('"')
            #autores_aux = info_articulo[index1:index2]
            #autores = info_articulo[index1:index2-1]
            '''Asignar variables para imprimir en el archivo CSV'''
            #autores = nombre
            #autores_aux = list(map(str.rstrip, autores_aux))
            #print(autores_aux)
            #autores = "".join(map(str, autores_aux))
            #print(autores)
            #Lugar
            index1 = info_articulo.find('En: ') +4
            index2 = info_articulo.find('ISSN:')
            lugar_aux = info_articulo[index1:index2]
            lugar= lugar_aux[:lugar_aux.find("\n")]
            #print(lugar)
            #Editorial
            index1 = info_articulo.find("\xa0\r\n                    ed:\xa0") + 27
            index2 = info_articulo.find("v.",index1,len(info_articulo))
            editorial = info_articulo[index1:index2]
            #DOI
            index1 = info_articulo.find("\xa0DOI:\xa0") + 6
            index2 = info_articulo.find("\n",index1,len(info_articulo))
            doi = info_articulo[index1:index2]
            #ISSN
            index1 = info_articulo.find("ISSN:") + 6
            index2 = index1 + 9
            ISSN = info_articulo[index1:index2]
            #Nombre Revista
            index1 = info_articulo.find("\xa0\r\n                    ") + 23
            index2 = info_articulo.find("\xa0\r\n                    ISSN:")
            Revista = info_articulo[index1:index2]
            #Año
            index1 = info_articulo.find("fasc.")
            index2 = info_articulo.find("DOI:")
            AnoEvento = info_articulo[index1:index2]
            AnoEvento = AnoEvento.strip()
            AnoEvento = AnoEvento[-5:-1]
            #print(AnoEvento)
            #Volumen
            index1 = info_articulo.find("\nv.") + 3
            index2 = info_articulo.find("fasc.")
            Volumen = info_articulo[index1:index2]
            #Fasciculo
            index1 = info_articulo.find("fasc.") + 5
            index2 = info_articulo.find("p.")
            fasciculo = info_articulo[index1:index2]
            #Páginas
            index1 = info_articulo.find("\r\n                    p.") + 24
            index2 = info_articulo.find("\r\n                    ",index1,len(info_articulo))
            Pagini = info_articulo[index1:index2]
            index1 = info_articulo.find("\r\n                    p.") + 24
            index1 = info_articulo.find("\r\n                    -",index1,len(info_articulo)) + 24
            index2 = info_articulo.find("\r\n                    ,",index1,len(info_articulo))
            Pagfin = info_articulo[index1:index2]

            Bin.init.articulos.append(RH+";"\
                                      +"NN"+";"\
                                    +NombreProducto + ";"\
                                    + AnoEvento + ";"
                                    + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";" + "\n"
                                    )
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
    contarticulo = [COD_PRODUCTO]