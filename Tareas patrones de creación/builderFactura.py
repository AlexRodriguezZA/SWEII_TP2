#!/usr/python
#*--------------------------------------------------
#* singleton.py
#* excerpt from https://refactoring.guru/design-patterns/singleton/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):
    """
    La interfaz de Builder especifica métodos para crear las diferentes partes de
    los objetos Producto.
    """

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def produce_part_a(self) -> None:
        pass

    @abstractmethod
    def produce_part_b(self) -> None:
        pass

    @abstractmethod
    def produce_part_c(self) -> None:
        pass


class ConcreteBuilder1(Builder):
    """
    Las clases de Concrete Builder siguen la interfaz de Builder y proporcionan
    implementaciones específicas de los pasos de construcción. Su programa puede tener
    varias variaciones de Builders, implementadas de manera diferente.
    """

    def __init__(self) -> None:
        """
        Una nueva instancia del constructor debe contener un objeto de producto en blanco, que es
        utilizado en el montaje posterior.
        """
        self.reset()

    def reset(self) -> None:
        self._product = Product1()

    @property
    def product(self) -> Product1:
        """
        Se supone que los constructores de hormigón proporcionan sus propios métodos para
        recuperando resultados. Eso es porque varios tipos de constructores pueden crear
        productos completamente diferentes que no siguen la misma interfaz.
        Por lo tanto, dichos métodos no se pueden declarar en la interfaz base de Builder.
        (al menos en un lenguaje de programación tipado estáticamente).

        Por lo general, después de devolver el resultado final al cliente, un constructor
        se espera que la instancia esté lista para comenzar a producir otro producto.
        Es por eso que es una práctica habitual llamar al método de reinicio al final de
        el cuerpo del método `getProduct`. Sin embargo, este comportamiento no es obligatorio,
        y puede hacer que sus constructores esperen una llamada de reinicio explícita del
        código de cliente antes de desechar el resultado anterior.
        """
        product = self._product
        self.reset()
        return product

    def produce_part_a(self) -> None:
        self._product.add("Factura A")

    def produce_part_b(self) -> None:
        self._product.add("Factura B")

    def produce_part_c(self) -> None:
        self._product.add("Factura C")


class Product1():
    """
    Tiene sentido usar el patrón Builder solo cuando sus productos son bastante
    complejos y requieren una configuración extensa.

    A diferencia de otros patrones de creación, diferentes constructores de hormigón pueden producir
    productos no relacionados. En otras palabras, los resultados de varios constructores pueden no
    siempre sigue la misma interfaz.
    """

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        print(f"Product parts: {', '.join(self.parts)}", end="")


class Director:
    """
    El Director sólo es responsable de ejecutar los pasos de construcción en un
    secuencia determinada. Es útil cuando se fabrican productos de acuerdo con un
    orden o configuración específica. Estrictamente hablando, la clase Director es
    opcional, ya que el cliente puede controlar los constructores directamente.
    """

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        """
        El Director trabaja con cualquier instancia del constructor que pase el código del cliente
        lo. De esta forma, el código de cliente puede alterar el tipo final de la nueva
        producto ensamblado.
        """
        self._builder = builder

    """
    El Director puede construir varias variaciones de productos utilizando el mismo
    pasos de construcción.
    """

    def build_minimal_viable_product(self) -> None:
        self.builder.produce_part_a()

    def build_full_featured_product(self) -> None:
        self.builder.produce_part_a()
        self.builder.produce_part_b()
        self.builder.produce_part_c()


if __name__ == "__main__":
    """
    El código del cliente crea un objeto constructor, se lo pasa al director y luego
    inicia el proceso de construcción. El resultado final se recupera de la
    objeto constructor.
    """

   
    builder = ConcreteBuilder1();
    
    print("\n")

    #  Recuerde, el patrón Builder se puede usar sin una clase Director.
    print("Que tipo de factura desea generar?")
    print("1- Factura A")
    print("2- Factura B")
    print("3- Factura C")
    print("4- Todas")
    
    opcion = int(input())
    if opcion == 1:
        builder.produce_part_a()
        builder.product.list_parts()
    elif opcion == 2:
        builder.produce_part_b()
        builder.product.list_parts()
    elif opcion == 3:
        builder.produce_part_c()
        builder.product.list_parts()
    else:
        builder.produce_part_a()
        builder.produce_part_b()
        builder.produce_part_c()
        builder.product.list_parts()


    print("\n")
