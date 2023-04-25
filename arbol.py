#Importaciones
import graphviz  

class Nodo:
    def __init__(self, value, left=None, right=None):  # Se define el constructor de la clase, que recibe un valor y opcionalmente dos nodos hijos
        self.value = value  # Se asigna el valor al atributo 'value' del objeto
        self.left = left  # Se asigna el nodo izquierdo al atributo 'left' del objeto
        self.right = right  # Se asigna el nodo derecho al atributo 'right' del objeto

    def dibujarArbol(self):  # Se define el método para generar el gráfico del árbol
        dot = graphviz.Digraph()  # Se crea un objeto de la clase Digraph de la librería graphviz
        self.hacerArbol(dot, self)  # Se llama a la función privada hacerArbol con el objeto Dot y el nodo actual como argumentos
        dot.render("output/ArbolGenerado", format='png')  # Se guarda el gráfico generado en un archivo png con el nombre 'ArbolGenerado' en la carpeta 'output'
        return dot  # Se devuelve el objeto Digraph

    def hacerArbol(self, dot, node):  # Se define la función privada hacerArbol que recibe un objeto Digraph y un nodo
        if node is None:  # Si el nodo actual es None, se retorna
            return
        dot.node(str(node), str(node.value))  # Se agrega un nodo con la etiqueta del valor del nodo actual
        if node.left is not None:  # Si el nodo actual tiene un hijo izquierdo
            dot.edge(str(node), str(node.left))  # Se agrega un borde del nodo actual al nodo izquierdo
            self.hacerArbol(dot, node.left)  # Se llama recursivamente a hacerArbol con el objeto Digraph y el nodo izquierdo como argumentos
        if node.right is not None:  # Si el nodo actual tiene un hijo derecho
            dot.edge(str(node), str(node.right))  # Se agrega un borde del nodo actual al nodo derecho
            self.hacerArbol(dot, node.right)  # Se llama recursivamente a hacerArbol con el objeto Digraph y el nodo derecho como argumentos


# La función contruirArbol toma una expresión regular en notación postfix como entrada y construye un árbol de expresiones regulares.
def contruirArbol(postfix):
    try:
        pila = []  # Inicializa una pila vacía
        operadores = set('*•|+?♣')  # Crea un conjunto de operadores de expresiones regulares
        
        # Itera sobre cada carácter de la expresión regular
        for char in postfix:
            if char in operadores:  # Si el carácter es un operador de expresiones regulares
                right = pila.pop()  # Saca el último nodo de la pila y lo asigna como hijo derecho
                left = pila.pop() if pila else None  # Si no hay más nodos en la pila, asigna None como hijo izquierdo
                pila.append(Nodo(char, left, right))  # Agrega un nuevo nodo a la pila con el operador y sus dos hijos
            else:
                pila.append(Nodo(char))  # Si el carácter no es un operador, agrega un nuevo nodo con ese carácter a la pila
        
        return pila.pop()  # Retorna el último nodo de la pila, que corresponde al árbol completo
    except:
        print("ERROR: No se pudo generar el grafo, revise su sintaxis de yalex") #no identifca erres como tal
        exit()

