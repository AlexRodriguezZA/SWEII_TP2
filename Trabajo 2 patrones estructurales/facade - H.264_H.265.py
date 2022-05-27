#*--------------------------------------------------
#* facade.py
#* excerpt from https://refactoring.guru/design-patterns/facade/python/example
#*--------------------------------------------------

from __future__ import annotations


class Facade:
    """
    La clase Fachada proporciona una interfaz simple a la lógica compleja de uno o
    varios subsistemas. La Fachada delega las solicitudes del cliente al
    objetos apropiados dentro del subsistema. La Fachada también es responsable de
    gestionando su ciclo de vida. Todo esto blinda al cliente de lo no deseado.
    complejidad del subsistema.
    """

    def __init__(self, Formato_264: formato_h_264, Formato_265: formato_h_265) -> None:
        """
        Dependiendo de las necesidades de su aplicación, puede proporcionar a Facade
        objetos de subsistema existentes o forzar a Facade a crearlos en su
        propio.
        """

        self._subsystem1 = Formato_264 or formato_h_264()
        self._subsystem2 = Formato_265 or formato_h_265()

    def compresion_video(self) -> str:
        """
        Los métodos de The Facade son atajos convenientes para el sofisticado
        funcionalidad de los subsistemas. Sin embargo, los clientes obtienen solo una fracción
        de las capacidades de un subsistema.
        """

        results = []
        values = input("¿desea comprimir a formato H.264? y/n")
        if values == "y":
            results.append(self._subsystem1.operation1())
            results.append(self._subsystem1.operation_n())
        else:
            results.append(self._subsystem1.operationCancelar())
        values2 = input("¿desea comprimir a formato H.265? y/n")
        if values2 == "y":
            results.append(self._subsystem2.operation1())
            results.append(self._subsystem2.operation_z())
        else:
            results.append(self._subsystem2.operationCancelar())
        return "\n".join(results)


class formato_h_264:
    """
    El Subsistema puede aceptar solicitudes ya sea de la fachada o del cliente directamente.
    En todo caso, para el Subsistema, la Fachada es un cliente más, y es
    no es parte del Subsistema.
    """

    def operation1(self) -> str:
        return "comprimiendo a formato H.264..."

    # ...

    def operation_n(self) -> str:
        return "H.264: compresion realizada!"

    def operationCancelar(self) -> str:
        return "H.264: compresion CANCELADA!"

class formato_h_265:
    """
    Algunas fachadas pueden trabajar con múltiples subsistemas al mismo tiempo.
    """

    def operation1(self) -> str:
        return "comprimiendo a formato H.265..."

    # ...

    def operation_z(self) -> str:
        return "H.265: compresion realizada!"
    
    def operationCancelar(self) -> str:
        return "H.265: compresion CANCELADA!"


def client_code(facade: Facade) -> None:
    """
    El código del cliente trabaja con subsistemas complejos a través de una interfaz simple
    proporcionada por la Fachada. Cuando una fachada gestiona el ciclo de vida del
    subsistema, es posible que el cliente ni siquiera sepa acerca de la existencia del
    subsistema. Este enfoque le permite mantener la complejidad bajo control.
    """

    print(facade.compresion_video(), end="")


if __name__ == "__main__":
    # El código del cliente puede tener algunos de los objetos del subsistema ya creados.
    # En este caso, podría valer la pena inicializar el Facade con estos
    # objetos en lugar de dejar que Facade cree nuevas instancias.
    formato_264 = formato_h_264()
    formato_265 = formato_h_265()
    facade = Facade(formato_264, formato_265)
    client_code(facade)
    print("\n")
