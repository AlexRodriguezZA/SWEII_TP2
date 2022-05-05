class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class SingletonCUIT(metaclass=SingletonMeta):
    def getCUIT(self):
        return "20-42070594-9"

if __name__ == "__main__":

    cuit = SingletonCUIT()
    validador = input("Desea conocer el cuit? y/n")
    if (validador=="y"):
        print("El cuit de la empresa es: ")
        print(cuit.getCUIT())



