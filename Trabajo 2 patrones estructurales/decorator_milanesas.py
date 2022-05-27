#*--------------------------------------------------
#* decorator.py
#* excerpt from https://refactoring.guru/design-patterns/decorator/python/example
#*--------------------------------------------------

class Component():
    """
    The base Component interface defines operations that can be altered by
    decorators.
    """

    def operation(self) -> str:
        pass


class Milanesas(Component):
    """
    Concrete Components provide default implementations of the operations. There
    might be several variations of these classes.
    """

    def operation(self) -> str:
        return "solo Milanesas"


class Decorator(Component):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """

    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        """
        The Decorator delegates all work to the wrapped component.
        """

        return self._component

    def operation(self) -> str:
        return self._component.operation()


class Milanesas_papas_fritas(Decorator):
    """
    Concrete Decorators call the wrapped object and alter its result in some
    way.
    """

    def operation(self) -> str:
        """
        Decorators may call parent implementation of the operation, instead of
        calling the wrapped object directly. This approach simplifies extension
        of decorator classes.
        """
        return f"Al pedido de milanesas se le agrega un porcion de papas fritas"


class Milanesas_papas_fritas_bebida(Decorator):
    """
    Decorators can execute their behavior either before or after the call to a
    wrapped object.
    """

    def operation(self) -> str:
        return f"Al pedido de milanesas y papas fritas se la agrega una bebida"


def client_code(component: Component) -> None:
    """
    The client code works with all objects using the Component interface. This
    way it can stay independent of the concrete classes of components it works
    with.
    """

    # ...

    print(f"RESULT: {component.operation()}", end="")

    # ...


if __name__ == "__main__":

    #Pedido de plato de milanesas y los 'decoramos' con bebidas y porcion de papas

    #Pedido de solo milanesas
    simple_milanesas = Milanesas()
    print("EL cliente pide un plato simple de milanesas")
    client_code(simple_milanesas)
    print()

    #Al pedido de milanesas le agregamos porcion de papas
    decoramos_con_papas = Milanesas_papas_fritas(simple_milanesas)
    client_code(decoramos_con_papas)
    print()

    #Al pedido de milanesas con papas le agregamos bebidas
    decoramos_con_papas_bebidas = Milanesas_papas_fritas_bebida(decoramos_con_papas)
    client_code(decoramos_con_papas_bebidas)

    print("\n")
   
