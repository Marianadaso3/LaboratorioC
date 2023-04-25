class Notaciones:
    def __init__(self, infix):
        self.infix = infix # Se guarda la expresión regular en notación infix
        self.precedencia = {  # Diccionario que contiene la precedencia de cada operador
            '*': 3,
            '+': 3,
            '?': 3,
            '♣': 3,
            '•': 1,
            '|': 2,
            '(': 0,
            ')': 0,
            '': 0
        }

    def to_postfix(self):
        infix = self.concatenacion() # Se asigna la expresión infix con la concatenación explícita a la variable infix
        #print ("aqui:" + infix)
        postfix = "" # Se crea una cadena vacía para almacenar la expresión postfix
        pila = [] # Se crea una pila vacía para almacenar los operadores
        skip_op = False # Se inicializa un indicador de si se deben omitir los operadores

        for chr in infix: # Se itera sobre cada caracter en la expresión infix
            if (chr == '(') and not skip_op: # Si el caracter es un paréntesis izquierdo y no se deben omitir operadores:
                pila += chr # Se añade el paréntesis izquierdo a la pila
            elif (chr == ')') and not skip_op: # Si el caracter es un paréntesis derecho y no se deben omitir operadores:
                while (not (len(pila) < 1) and pila[-1] != '('): # Se desapilan los operadores hasta encontrar el paréntesis izquierdo correspondiente
                    postfix += pila.pop() # Y se añaden a la expresión postfix
                pila.pop() # Se elimina el paréntesis izquierdo de la pila
            elif (chr in ['*', '•', '|', '+', '?', '♣']) and not skip_op: # Si el caracter es un operador y no se deben omitir operadores:
                while (not len(pila) < 1): # Se itera mientras la pila no esté vacía
                    if self.precedencia[pila[-1]] >= self.precedencia[chr]: # Si la precedencia del operador en el tope de la pila es mayor o igual a la del operador actual:
                        postfix += pila.pop() # Se desapila el operador y se añade a la expresión postfix
                    else:
                        break # En caso contrario se sale del bucle
                pila.append(chr) # Se añade el operador actual a la pila
            elif chr == "'": # Si el caracter es una comilla simple:
                skip_op = not skip_op # Se cambia el indicador de omitir operadores
            else: # Si el caracter es un operando:
                if skip_op: # Si se deben omitir los operadores:
                    postfix += f"'{chr}'" # Se añade el operando con comillas simples a la expresión postfix
                else:
                    postfix += chr # Si no se deben omitir operadores, se añade el operando tal cual a la expresión postfix

        while (not (len(pila) < 1)): # Se desapilan los operadores restantes en la pila
            postfix += pila.pop() # Y se añaden a la expresión posfiX

        return postfix # Se retorna la expresión postfix resultante
    

    #Función que agrega el operador de concatenación explícito "." donde sea necesario
    def concatenacion(self):
        infix = "" # Inicializar una cadena vacía para almacenar la cadena infix con operadores de concatenación explícitos agregados
        for i in range(len(self.infix)): # Iterar sobre la cadena infix original
            chr = self.infix[i]  # Obtener el carácter actual en la cadena infix
            infix += chr # Agregar el carácter a la nueva cadena infix
            #print ("VER ANTES DE CONCATENACION--" + infix)
            if i < (len(self.infix) - 1): # Verificar si se necesita agregar un operador de concatenación explícito después del carácter actual
                if (
                    ((chr in ')*+?') or (chr not in "?+()*•|\\'")) # Verificar si el carácter actual es un operador o un carácter válido
                    and (self.infix[i + 1] not in "+*?|)'") # Verificar si el siguiente carácter es un operador
                ):
                    infix += '•' # Agregar el operador de concatenación explícito a la nueva cadena infix
        #print ("VER CONCATENACION"+ infix)
        return infix # Devolver la cadena infix con los operadores de concatenación explícitos agregados

