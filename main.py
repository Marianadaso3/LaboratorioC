#Autor: Mariana David

#Importaciones
from yalex import * 
from arbol import *  
from utils import *

if __name__ == "__main__": 
    y = Yalex()  # Se crea una instancia de la clase Yalex
    y.leerYalex('ArchivosYalex/slr-4.yal', True)  # Se lee un archivo yalex y se carga en la instancia de Yalex
    #print(y.infix)
    #print (y.specialtoks)
    print("Infix:\n", ''.join(y.conversionspecialtoks(y.infix)))  # Se imprime la notación infix sin valores "dummies"
    postfix = Notaciones(y.infix).to_postfix()  # Se convierte la notación infix en postfix utilizando la clase Notations
    print()  # Se imprime una línea en blanco
    #print ("AQUIE"+postfix)
    print("Posfix:\n", ''.join(y.conversionspecialtoks(postfix)))  # Se imprime la notación postfix sin valores "dummies"
    generarGrafico = contruirArbol(y.conversionspecialtoks(postfix))  # Se construye un árbol a partir de la notación postfix sin valores "dummies"
    generarGrafico.dibujarArbol()  # Se genera un gráfico del árbol construido
 