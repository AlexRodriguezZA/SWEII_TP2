#*--------------------------------------------------
#* adapter.py
#* excerpt from https://refactoring.guru/design-patterns/adapter/python/example
#*--------------------------------------------------

class Target:
    """
    El destino define la interfaz específica del dominio utilizada por el código del cliente.
    """

    def request(self) -> str:
        return "Objetivo: conectar el HW"


class Adaptee:
    """
    El Adaptee contiene algunos comportamientos útiles, pero su interfaz es incompatible
    con el código de cliente existente. El Adaptado necesita alguna adaptación antes de que el
    el código del cliente puede usarlo.
    """

    def specific_request(self) -> str:
        return "Impresora no conectada"
    def specific_request2(self) -> str:
        return "mouse no conectado"
    def specific_request3(self) -> str:
        return "Teclado no conectado"


class Adapter(Target, Adaptee):
    """
    El adaptador hace que la interfaz del Adaptee sea compatible con la del Target
    Interfaz a través de herencia múltiple.
    """

    def request(self) -> str:
        return f"Dispositivos conectados"


def client_code(target: "Target") -> None:
    """
    El código del cliente admite todas las clases que siguen la interfaz de Target.
    """

    print(target.request(), end="")


if __name__ == "__main__":
    print("Desea conectar los dispositivo:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Cliente: ")
    print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")
    print(f"Adaptee: {adaptee.specific_request2()}", end="\n\n")
    print(f"Adaptee: {adaptee.specific_request3()}", end="\n\n")

    print("Cliente: conectar dispositivos:")
    adapter = Adapter()
    client_code(adapter)
