# el patrón Strategy nos permite encapsular diferentes algoritmos o comportamientos en clases separadas,
# permitiendo que estos algoritmos sean intercambiables
#mi clas general de estrategias que tiene como metodo la ejecucion
class Strategy:
    def execute(self):
        pass

# Estrategia 1 que hereda de la clase Strategy e incluye su metodo ejecutar solo que ejecuta lineas diferentes
class ConcreteStrategyA(Strategy):
    def execute(self):
        return "Estrategia A"

# Estrategia 2
class ConcreteStrategyB(Strategy):
    def execute(self):
        return "Estrategia B"

# Contexto sirve para hacer un constructor de estrategias y me indique cual es el que le pedi ejecutar
class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def execute_strategy(self):
        return self._strategy.execute()

# Creo un objeto de la estrategia uno y se lo mando al contexto
#en el resultado guardo la ejecucion de mis estrategia creada segun la estrategia que elegi
strategy_a = ConcreteStrategyA()
context = Context(strategy_a)
result_a = context.execute_strategy()
print("Resultado de la estrategia A:", result_a)

strategy_b = ConcreteStrategyB()
context = Context(strategy_b)
result_b = context.execute_strategy()
print("Resultado de la estrategia B:", result_b)
