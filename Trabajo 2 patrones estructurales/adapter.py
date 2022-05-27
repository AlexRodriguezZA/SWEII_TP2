#*--------------------------------------------------
#* adapter.py
#* excerpt from https://refactoring.guru/design-patterns/adapter/python/example
#*--------------------------------------------------




class Target:
    """
    El destino define la interfaz específica del dominio utilizada por el código del cliente.
    """

    def request(self) -> str:
        return "Objetivo: adaptar a puerto serie"
    


class Adaptee:
    
    """
    El Adaptee contiene algunos comportamientos útiles, pero su interfaz es incompatible
    con el código de cliente existente. El Adaptado necesita alguna adaptación antes de que el
    el código del cliente puede usarlo.
    """

    def specific_request(self) -> str:
        return "puerto serie conectado" 
    


class Adapter(Target, Adaptee):
    """
    El adaptador hace que la interfaz del Adaptee sea compatible con la del Target
    Interfaz a través de herencia múltiple.
    """

    def request(self) -> str:
        return f"Adapter: Puerto conectado"
    
    def abrir(self) -> int:
            return "puerto serie abierto"

    def enviar(self) -> str:
        return "enviando datos" 
    
    def cerrar(self) -> str:
        return "cerrar puerto serie"





if __name__ == "__main__":
    target = Target()
    print(target.request())

    adapter = Adapter()
    print(adapter.abrir())
    print(adapter.enviar())
    print(adapter.cerrar())
