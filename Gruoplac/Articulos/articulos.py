def artiextract():
    from main import my_url, name, RH, COD_PRODUCTO

    import Articulos.init, bs4, logging, sys, re, ssl
    global contarticulo
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
    

    # if a_tag:
        # td_tag = a_tag.find_parent("body")
        # if td_tag:
        #     nombre_td = td_tag.find("span")
        #     if nombre_td:
        #         siguiente_td = nombre_td.find_next_sibling("span")
        #         if siguiente_td:
        #             nombre = siguiente_td



    for a in range(0,len(containers)):
        buscaeventos = containers[a].td
        #print(buscaeventos)
        try:
            if buscaeventos.text == "Artículos publicados":
                all = a
                #print(buscaeventos)
                break
            
        except AttributeError:
            pass

    if all != 0:
        containerb = containers[all]
        #print(containerb)
        container = containerb.findAll("tr")
        # tipoart = containerb.findAll("td")

        for x in range(0, len(container)):
            cont = container[x]
            #tipoar = tipoart[x]
            #tipo = tipoar.text
            info_articulo = cont.text
            # Nombre Articulo
            # index1 = info_articulo.find('"')
            # index2 = info_articulo.rfind('"') + 1
            # NombreProducto = info_articulo[index1:index2]
       
            index1 = info_articulo.find('Publicado en revista especializada:') + 35
            index2 = info_articulo.find("\n", index1) - 1
            Titulo = info_articulo[index1:index2]
            # 
            index3 = info_articulo.find(",") 
            Pais = info_articulo[index2+18:index3]
            #ISSN
            index1 = info_articulo.find('ISSN: ') + 6
            ISSN = info_articulo[index1:index1 + 9]
            #AÑO
            index2 = info_articulo.find(',', index1) + 1
            ANIO = info_articulo[index2 : index2 + 5]
            #AUTORES
            index1 = info_articulo.find("Autores:") + 8
            index2 = info_articulo.find("\n", index1) - 1
            AUTORES = info_articulo[index1:index2]
 




            Articulos.init.articulos.append(RH+";"\
                                    + Grupo + ";"\
                                    + Titulo + ";" \
                                    + Pais + ";"\
                                    + ISSN + ";"\
                                    + ANIO + ";"\
                                    + AUTORES + ";"
                                    # + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
                                    # + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,]',r'',re.sub(' +',' ',Revista.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
                                    # + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,]',r'',re.sub(' +',' ',editorial.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
                                    # + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,-]', '', ISSN) + ";" \
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
    contarticulo = [COD_PRODUCTO]
