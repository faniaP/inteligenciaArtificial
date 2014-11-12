#! /usr/bin/python
# -*- coding: utf-8 _*_

import xml.etree.ElementTree as ET

###########################################
# Por medio de este modulo es que podemos #
# generar un parser para un archivo xml   #
# y cargar la grafica de nuestro          #
# territorio de juego.                    #
# Fernando Abigail Galicia Mendoza        #
# Estefania Prieto Larios                 #
# Antonio Galvan                          #
###########################################

def loadXML():
    '''
    Metodo encargado de generar el arbol que 
    se encuentra definido en el archivo .xml
    '''
    territorio = ET.parse('Territorio.xml')
    arbol = territorio.getroot()
    
    for node in arbol:
        ids = [x.text for x in node.findall('id')]
        continente = [x.text for x in node.findall('continente')]
        tropas = [x.text for x in node.findall('tropas')]
        salida = [node[0].text]+ids+continente+tropas
        print [node.attrib]+[x.text for x in node]
        

    


loadXML()
