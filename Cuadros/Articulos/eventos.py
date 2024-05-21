def artiextract():
    from main4 import my_url, name, RH, COD_PRODUCTO

    import Articulos.init, bs4, logging, sys, re, ssl
    global contarEvento
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
            if buscaeventos.text == "Eventos científicos":
                all = a
                #print(all)
                break
            
        except AttributeError:
            pass
 
    if all != 0:
        containerb = containers[all]
        container = containerb.findAll("table")
        tipoart = containerb.findAll("td")
        for x in range(0, len(container)):
            cont = container[x]
            tipoar = tipoart[x]
            tipo = tipoar.text
            info_evento = cont.text
            
            #PARTICIPANTE
            index1 = info_evento.find('Participantes') + 20
            index2 = info_evento.find('Rol',index1) - 1
            participante = info_evento[index1 :index2]
            
            #evento
            index1 =  info_evento.find('Nombre del evento: ') + 25
            index2 = info_evento.find('\n',index1) 
            evento = info_evento[index1:index2]
         
            #Año
            index1 =  info_evento.find('Realizado el:') 
            # index2 = info_libro.find('2',index1) 
            fecha = info_evento[index1 + 13 : index1 +17]
           
            #Sitio
            index0 = info_evento.rfind(":00.0")   
            index1 = info_evento.find('en ', index0)
            index2 = info_evento.find("-", index1) 
            lugar = info_evento[index1 + 3:index2]
        
            

            #Producto y tipo producto
            index1 = info_evento.find("Nombre del producto:")
            if (info_evento[index1 : index1 + 20] == "Nombre del producto:"):
                index2 = info_evento.find("Tipo de producto:",index1)
                producto = info_evento[index1 + 20:index2]
                index3 = info_evento.find("\n",index2)
                tipo = info_evento[index2 + 16 : index3]
            else:
                producto = ""
                tipo = ""
            # print(info_evento[index1 : index1 +20])


            Articulos.init.eventos.append(RH+";"\
                                    + nombre +";"\
                                    # + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,]',r'',re.sub(' +',' ',participante.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
                                    + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,]',r'',re.sub(' +',' ',evento.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"
                                    + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,]',r'',re.sub(' +',' ',fecha.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
                                    + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó òÁÉÍÓÚ,]',r'',re.sub(' +',' ',lugar.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
                                    + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,]',r'',re.sub(' +',' ',producto.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
                                    + re.sub(r'[^A-Za-z0-9éèáàéñèíìúùó ò,]',r'',re.sub(' +',' ',tipo.replace('"',"").replace("'","").strip().replace(";" , "|").replace("\r\n","").replace("\n","").replace("\r",""))) + ";"\
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
    contarEvento = [COD_PRODUCTO]
