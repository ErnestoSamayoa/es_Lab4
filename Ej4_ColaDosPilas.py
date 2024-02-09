#4. Implementación de una Cola con Dos Pilas
class ColaConPilas:
    def __init__(self):
#Dos pilas
        self.pila_entrada = []
        self.pila_salida = []

    def enqueue(self, elemento):
        while self.pila_salida:
            self.pila_entrada.append(self.pila_salida.pop())
        self.pila_entrada.append(elemento)

    def dequeue(self):
        if not self.pila_salida:
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())
        if not self.pila_salida:
            raise IndexError("La cola está vacía")
        return self.pila_salida.pop()

# Ejemplo de uso
cola = ColaConPilas()

cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)
cola.enqueue(5)

print("\n****************BIENVENIDO USUARIO************\n")

print(cola.dequeue())  
print(cola.dequeue())  
print(cola.dequeue())
print(cola.dequeue())  
print(cola.dequeue())  

print("\n************************************************")   
