#Singleton: Garantiza que una clase tenga solo una instancia y proporciona un punto de acceso global a esa instancia.
class Mascota:
    perro = None

    def __new__(cls):
        if cls.perro is None:
            cls.perro = super().__new__(cls)
        return cls.perro

# Ejemplo de uso
s1 = Mascota()
s2 = Mascota()

print(s1 is s2)  # Debería imprimir True, ya que s1 y s2 son la misma instancia 

