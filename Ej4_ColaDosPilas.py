#4. Implementación de una Cola con Dos Pilas
class ColaConPilas:
    def __init__(self):
        # Inicialización de dos pilas: una para la entrada y otra para la salida
        self.pila_entrada = []
        self.pila_salida = []

    def enqueue(self, elemento):
        # Método para agregar un elemento a la cola
        # Si hay elementos en la pila de salida, se transfieren a la pila de entrada
        while self.pila_salida:
            self.pila_entrada.append(self.pila_salida.pop())
        # El nuevo elemento se agrega a la pila de entrada
        self.pila_entrada.append(elemento)

    def dequeue(self):
        # Método para eliminar y devolver el primer elemento de la cola
        # Si la pila de salida está vacía, se transfieren todos los elementos de la pila de entrada a la pila de salida
        if not self.pila_salida:
            while self.pila_entrada:
                self.pila_salida.append(self.pila_entrada.pop())
        # Si la pila de salida aún está vacía después de la transferencia, la cola está vacía
        if not self.pila_salida:
            raise IndexError("La cola está vacía")
        # Se devuelve el primer elemento de la pila de salida, que es el primer elemento de la cola
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