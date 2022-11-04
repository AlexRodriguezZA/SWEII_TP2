from abc import ABC, abstractmethod


class AbstractClass(ABC):
    """
    La clase abstracta define un método de plantilla que contiene un esqueleto de
    algún algoritmo, compuesto de llamadas a (generalmente) primitivas abstractas
    operaciones.

    Las subclases concretas deberían implementar estas operaciones, pero dejar el
    método de plantilla en sí intacto.
    """

    def template_method(self) -> None:
        """
        El método de plantilla define el esqueleto de un algoritmo.        """

        self.vistaPrincipal()
        self.required_operations1()
        self.required_operations2()

    # Estas operaciones ya tienen implementaciones.
    def vistaPrincipal(self) -> None:
        print("vista principal dice: iniciando vista ")
    
    

    # Estas operaciones deben implementarse en subclases.

    @abstractmethod
    def required_operations1(self) -> None:
        pass

    @abstractmethod
    def required_operations2(self) -> None:
        pass

   # Estos son "ganchos". Las subclases pueden anularlas, pero no es obligatorio
    # ya que los ganchos ya tienen una implementación predeterminada (pero vacía). Manos
    # proporcionar puntos de extensión adicionales en algunos lugares cruciales del
    #algoritmo.

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


class vista1(AbstractClass):
    """
    Las clases concretas tienen que implementar todas las operaciones abstractas de la base.
    clase. También pueden anular algunas operaciones con una implementación predeterminada.
    """

    def required_operations1(self) -> None:
        print("Vista 1 dice: vista 1 iniciada")

    def required_operations2(self) -> None:
        pass


class vista2(AbstractClass):
    """
    Por lo general, las clases concretas anulan solo una fracción de la clase base.
    operaciones.
    """

    def required_operations1(self) -> None:
        print("Vista 2 dice: vista 2 iniciada")

    def required_operations2(self) -> None:
        pass

    def hook1(self) -> None:
        pass

class vista3(AbstractClass):
    """
    Por lo general, las clases concretas anulan solo una fracción de la clase base.
    operaciones.
    """

    def required_operations1(self) -> None:
        print("Vista 3 dice: vista 3 iniciada")

    def required_operations2(self) -> None:
        pass

    def hook1(self) -> None:
        pass

def client_code(abstract_class: AbstractClass) -> None:
    """
    El código del cliente llama al método de plantilla para ejecutar el algoritmo. Cliente
    código no tiene que saber la clase concreta de un objeto con el que trabaja, como
    siempre que trabaje con objetos a través de la interfaz de su clase base.
    """

    # ...
    abstract_class.template_method()
    # ...


if __name__ == "__main__":
    print("El mismo código de cliente puede funcionar con diferentes subclases:")
    client_code(vista1())
    print("")

    print("El mismo código de cliente puede funcionar con diferentes subclases:")
    client_code(vista2())
    print("")

    print("El mismo código de cliente puede funcionar con diferentes subclases:")
    client_code(vista3())
    print("")
