#2. Implementar una cola utilizando una lista en Python. 
class Cola:
    def __init__(self):
        self.items = []

    def enqueue(self, elemento):
        self.items.append(elemento)

    def dequeue(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return "La cola está vacía"

    def front(self):
        if not self.esta_vacia():
            return self.items[0]
        else:
            return "La cola está vacía"

    def esta_vacia(self):
        return len(self.items) == 0

# Función para simular el proceso de atención en una fila
def simular_atencion(fila):
    while not fila.esta_vacia():
        print("\nAtendiendo a:", fila.dequeue())
        print("Elementos restantes en la fila:", len(fila.items))

# Crear una cola y agregar elementos a ella ingresados por el usuario
fila = Cola()  
print("\n****************BIENVENIDO USUARIO************\n")
num_p = int(input("Ingrese el número de personas en la fila: "))
for i in range(num_p):
    persona = input(f"Ingrese el nombre de la persona {i+1}: ")
    fila.enqueue(persona)

# Mostrar los elementos de la fila de forma ordenada
print("\nFila de espera:")
for i, persona in enumerate(fila.items, 1):
    print(f"{i}. {persona}")

# Simular el proceso de atención en la fila
print("\nProceso de atención:")
simular_atencion(fila)

print("\nMUCHAS GRACIAS POR ESPERAR")
print("\n************************************************")