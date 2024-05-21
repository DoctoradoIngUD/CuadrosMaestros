def artiextract():
    from main5 import my_url, name, RH, COD_PRODUCTO

    import Articulos.init, bs4, logging, sys, re, ssl
    global contarCapitulo
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
    nombre = None
    a_tag = page_soup.find("a", {"name": "datos_generales"})
    if a_tag:
        td_tag = a_tag.find_parent("td")
        if td_tag:
            nombre_td = td_tag.find("td", text="Nombre")
            if nombre_td:
                siguiente_td = nombre_td.find_next_sibling("td")
                if siguiente_td:
                    nombre = siguiente_td.text.strip()
                    print(nombre)



    for a in range(0,len(containers)):
        buscaeventos = containers[a].h3
        #print(buscaeventos)
        try:
            if buscaeventos.text == "Capitulos de libro":
                all = a
                #print(all)
                break
            
        except AttributeError:
            pass
 
    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("blockquote")
        tipoart = containerb.findAll("")
        for x in range(0, len(container)):
            cont = container[x]
            # tipoar = tipoart[x]
            # tipo = tipoar.text
            info_capitulo = cont.text
            
            #TITULO
            index1 = info_capitulo.find('"')
            index2 = info_capitulo.find('"',index1+10) 
            titulo = info_capitulo[index1:index2]
            
            #LIBRO
            index3 = info_capitulo.find('.',index2) 
            libro = info_capitulo[index2:index3]
         
            #Año
            index1 =  info_capitulo.find('p.') 
            index2 = info_capitulo.find(',',index1) + 1
            fecha = info_capitulo[index2: index2 + 5]

            #Paginas
            paginas = info_capitulo[index1:index2 - 1]

            #Sitio
            index1 = info_capitulo.rfind("En: ") + 4   
            index2 = info_capitulo.find('ISBN', index1) 
            lugar = info_capitulo[index1:index2]
        
            #ISBN

            index3 = info_capitulo.find("ed:",index2)
            isbn = info_capitulo[index2 + 5:index3]
            # #Producto y tipo producto
            # index1 = info_evento.find("Nombre del producto:")
            # if (info_evento[index1 : index1 + 20] == "Nombre del producto:"):
            #     index2 = info_evento.find("Tipo de producto:",index1)
            #     producto = info_evento[index1 + 20:index2]
            #     index3 = info_evento.find("\n",index2)
            #     tipo = info_evento[index2 + 16 : index3]
            # else:
            #     producto = ""
            #     tipo = ""
  

            Articulos.init.capitulosLibros.append(RH+";"\
                                    + nombre +";"\
                                    + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,]',r'',re.sub(' +',' ',titulo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
                                    + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,()]',r'',re.sub(' +',' ',libro.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"
                                    + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,]',r'',re.sub(' +',' ',fecha.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
                                    + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,]',r'',re.sub(' +',' ',isbn.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
                                    + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó òÁÉÍÓÚ,]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
                                    + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,.-]',r'',re.sub(' +',' ',paginas.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
                                    # + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,]',r'',re.sub(' +',' ',tipo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
                                    # + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,-]', '', ISBN) + ";" \
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
    contarCapitulo = [COD_PRODUCTO]
