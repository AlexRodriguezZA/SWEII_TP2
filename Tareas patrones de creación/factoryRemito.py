#!/usr/bin/python3.7
#*--------------------------------------------------
#* factory.py
#* excerpt from https://refactoring.guru/design-patterns/factory/python/example
#*--------------------------------------------------
from __future__ import annotations
from abc import ABC, abstractmethod


class Product(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """
    # operaciones que debe implementar todos los productos concretos
    @abstractmethod
    def operation(self) -> str: 
        pass


class Creator(ABC):
    """
    La clase Creator declara el método de fábrica que se supone que devolverá un
    objeto de una clase de Producto. Las subclases de Creator suelen proporcionar la
    implementación de este método.
    """

    @abstractmethod
    def factory_method(self):
        """
        tenga en cuenta que el Creador también puede proporcionar alguna implementación predeterminada de
        el método de fábrica.
        """
        pass

    def operacionEnviarRemito(self) -> str:
        LugarEnvio = self.factory_method()
        MesajeEnviado = f"El medio por el cual se envio el remito es {LugarEnvio.operation()}\n"

        return MesajeEnviado


"""
Concrete Creators anula el método de fábrica para cambiar el resultado
tipo de producto.
"""

class Creator_correo(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductCorreo()


class Creator_Mesajeria(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductMesajeria()

class Creator_Portal(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductPortal()



"""
Concrete Products provide various implementations of the Product interface.
"""


class ConcreteProductCorreo(Product):
    def operation(self) -> str:
        return "{Correo}"


class ConcreteProductMesajeria(Product):
    def operation(self) -> str:
        return "{mensajeria}"

class ConcreteProductPortal(Product):
    def operation(self) -> str:
        return "{del portal de ventas}"




if __name__ == "__main__":


    correo = Creator_correo()
    mensajeria = Creator_Mesajeria()
    portalVentas = Creator_Portal()

    print("Indique por donde quiere enviar el remito al cliente")
    print
    print("1- Enviar a traves de correo")
    print("2- Enviar a traves de Mensajeria")
    print("3- Enviar a traves del portal de ventas")
    opcion = int(input())
    if opcion == 1:
        print(correo.operacionEnviarRemito())
    elif opcion == 2:
        print(mensajeria.operacionEnviarRemito())
    else:
        print(portalVentas.operacionEnviarRemito())
        
        
