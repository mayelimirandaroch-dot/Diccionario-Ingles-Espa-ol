class Nodo:
    """Clase que representa un nodo dentro del BST."""
    def __init__(self, espanol, ingles):
        self.espanol = espanol.lower()
        self.ingles = ingles.lower()
        self.izquierdo = None
        self.derecho = None

class ArbolBST:
    """Clase que implementa la lógica del BST para el diccionario."""
    def __init__(self):
        self.raiz = None

    def insertar(self, espanol, ingles):
        if self.raiz is None:
            self.raiz = Nodo(espanol, ingles)
        else:
            self._insertar_recursivo(self.raiz, espanol.lower(), ingles.lower())

    def _insertar_recursivo(self, nodo_actual, espanol, ingles):
        if espanol.lower() < nodo_actual.espanol.lower():
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = Nodo(espanol, ingles)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, espanol, ingles)
        elif espanol.lower() > nodo_actual.espanol.lower():
            if nodo_actual.derecho is None:
                nodo_actual.derecho = Nodo(espanol, ingles)
            else:
                self._insertar_recursivo(nodo_actual.derecho, espanol, ingles)
        else:
            nodo_actual.ingles = ingles

    def buscar(self, espanol):
        return self._buscar_recursivo(self.raiz, espanol.lower())

    def _buscar_recursivo(self, nodo_actual, espanol):
        if nodo_actual is None:
            return None
        if espanol == nodo_actual.espanol:
            return nodo_actual.ingles
        if espanol < nodo_actual.espanol:
            return self._buscar_recursivo(nodo_actual.izquierdo, espanol)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, espanol)

    def eliminar(self, nodo, espanol):
        if nodo is None:
            return None

        if espanol < nodo.espanol:
            nodo.izquierdo = self.eliminar(nodo.izquierdo, espanol)
        elif espanol > nodo.espanol:
            nodo.derecho = self.eliminar(nodo.derecho, espanol)
        else:
            if nodo.izquierdo is None:
                return nodo.derecho
            elif nodo.derecho is None:
                return nodo.izquierdo

            sucesor = self._minimo_valor_nodo(nodo.derecho)
            nodo.espanol = sucesor.espanol
            nodo.ingles = sucesor.ingles
            nodo.derecho = self.eliminar(nodo.derecho, sucesor.espanol)
        return nodo

    def _minimo_valor_nodo(self, nodo):
        actual = nodo
        while actual.izquierdo is not None:
            actual = actual.izquierdo
        return actual

    def obtener_inorden(self):
        lista = []
        self._inorden_recursivo(self.raiz, lista)
        return lista

    def _inorden_recursivo(self, nodo, lista):
        if nodo:
            self._inorden_recursivo(nodo.izquierdo, lista)
            lista.append({'espanol': nodo.espanol, 'ingles': nodo.ingles})
            self._inorden_recursivo(nodo.derecho, lista)