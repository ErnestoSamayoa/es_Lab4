#2. Implementar una cola utilizando una lista en Python. 
##Definir funciones para las operaciones básicas de una cola: enqueue (añadir elemento), dequeue (eliminar elemento) y front (ver el primer elemento sin eliminarlo).
#Escribir un programa que simule el proceso de atención en una fila, donde los elementos son atendidos en el orden en que llegan.

class Cola:
    def __init__(self):
        # Inicializa una lista vacía para almacenar los elementos de la cola
        self.items = []

    def enqueue(self, elemento):
        # Agrega un elemento al final de la cola
        self.items.append(elemento)

    def dequeue(self):
        # Elimina y devuelve el elemento al frente de la cola
        if not self.esta_vacia():
            return self.items.pop(0)  # Utiliza pop(0) para eliminar el primer elemento de la lista (FIFO)
        else:
            return "La cola está vacía"

    def front(self):
        # Devuelve el elemento al frente de la cola sin eliminarlo
        if not self.esta_vacia():
            return self.items[0]
        else:
            return "La cola está vacía"

    def esta_vacia(self):
        return len(self.items) == 0

# Función para simular el proceso de atención en una fila
def simular_atencion(fila):
    while not fila.esta_vacia():
        # Mientras la cola no esté vacía, atiende a la persona al frente de la fila
        print("\nAtendiendo a:", fila.dequeue())
        print("Elementos restantes en la fila:", len(fila.items))

# Crear una cola y agregar elementos a ella ingresados por el usuario
fila = Cola()  
print("\n****************BIENVENIDO USUARIO************\n")
num_p = int(input("Ingrese el número de personas en la fila: "))
for i in range(num_p):
    # Solicitar y agregar el nombre de cada persona a la cola
    persona = input(f"Ingrese el nombre de la persona {i+1}: ")
    fila.enqueue(persona)

# Mostrar los elementos de la fila de forma ordenada
print("\nFila de espera:")
for i, persona in enumerate(fila.items, 1):
    print(f"{i}. {persona}")

print("\nProceso de atención:")
simular_atencion(fila)

print("\nMUCHAS GRACIAS POR ESPERAR")

print("\n***********************************************")