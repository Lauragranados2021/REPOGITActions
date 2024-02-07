# Decorator: Permite agregar funcionalidades adicionales a un objeto dinámicamente, sin alterar su estructura básica.
#cramos la clase cafe y le creamos un metodo a si mimso de 5
class Coffee:
    def cost(self):
        return 5

# Decorador base
#aqui heredamos el metodo de costo y creamos el primer cafe normal lo que significa un constrcutor self se refiere a la instancia enviada
class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

# Se le agrega funcionalidad heredad del anterior se le aumenta dos pesos al anterior
class Milk(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

# instancia del mismos cafe pero con azucar
class Sugar(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

# Ejemplo de uso
coffee = Coffee()
print("Costo del café simple:", coffee.cost())

coffee_with_milk = Milk(coffee)
print("Costo del café con leche:", coffee_with_milk.cost())

coffee_with_milk_and_sugar = Sugar(coffee_with_milk)
print("Costo del café con leche y azúcar:", coffee_with_milk_and_sugar.cost())
