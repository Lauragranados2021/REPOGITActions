# mi_modulo.py
#give
def ingresar_numero():
    try:
        numero = int(input("Por favor ingresa un número: "))
        return numero
    except ValueError:
        print("Error: Por favor ingresa un número válido.")
        return None
ingresar_numero()