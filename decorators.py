def decorador(function):
    def funcionCompleta(name):
        print("Antes de llamar a la función")
        function(name)
        print("Después de llamar a la función")
    return funcionCompleta

@decorador
def saludar(name):
    print(f"Hola, {name}")

saludar("david")

#Extra
#Crea un decorador que sea capaz de contabilizar cuantas veces se ha llamado a una función
#y aplicalo a una función de tu elección

def mi_decorador(function):
    
    def fullFunction():
        fullFunction.calls+=1
        print(f"Se ha llamado a la función {function.__name__} {str(fullFunction.calls)} veces")
        function()
    fullFunction.calls = 0
    return fullFunction

@mi_decorador
def Hola():
    pass
@mi_decorador
def hola():
    pass

Hola()
Hola()
Hola()
hola()
Hola()
Hola()
Hola()
