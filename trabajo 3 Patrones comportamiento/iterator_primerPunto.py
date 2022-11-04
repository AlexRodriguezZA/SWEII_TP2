from __future__ import annotations
from collections.abc import Iterable, Iterator
from typing import Any, List


"""
Para crear un iterador en Python, hay dos clases abstractas del código integrado.
en el módulo `colecciones` - Iterable, Iterator. Necesitamos implementar la
método `__iter__()` en el objeto iterado (colección), y `__next__ ()`
método en theiterator.
"""


class ListaDeInvitados(Iterator):
    """
    Los iteradores concretos implementan varios algoritmos transversales. estas clases
    almacenar la posición transversal actual en todo momento.
    """

    """
    El atributo `_position` almacena la posición transversal actual. Un iterador puede
    tiene muchos otros campos para almacenar el estado de iteración, especialmente cuando
    se supone que funciona con un tipo particular de colección.
    """
    _position: int = None

    """
    Este atributo indica la dirección transversal.
    """
    _reverse: bool = False

    def __init__(self, collection: ColeccionDePersonas, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        """
       El método __next__() debe devolver el siguiente elemento de la secuencia. En
        llegando al final, y en llamadas posteriores, debe levantar StopIteration.
        """
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()

        return value


class ColeccionDePersonas(Iterable):
    """
    Colecciones concretas proporcionan uno o varios métodos para recuperar nuevos
    instancias de iterador, compatibles con la clase de colección.
    """

    def __init__(self, collection: List[Any] = []) -> None:
        self._collection = collection

    def __iter__(self) -> ListaDeInvitados:
        """
        El método __iter__() devuelve el propio objeto iterador, por defecto
        devuelve el iterador en orden ascendente.
        """
        return ListaDeInvitados(self._collection)

    def get_reverse_iterator(self) -> ListaDeInvitados:
        return ListaDeInvitados(self._collection, True)

    def add_item(self, item: Any):
        self._collection.append(item)


if __name__ == "__main__":
   # El código del cliente puede o no saber sobre el iterador concreto o
    # Clases de colección, según el nivel de direccionamiento indirecto que desee mantener
    # en su programa.
    collection = ColeccionDePersonas()
    listaDepersonas = ["mario","juan","marcos","gabriel"]
    for persona in listaDepersonas:
        collection.add_item(persona)

    print("Listado de personas")
    print("\n".join(collection))
 