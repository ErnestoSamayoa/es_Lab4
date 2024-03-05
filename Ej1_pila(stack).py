#1. Implementación de una Pila (Stack)

class Pila:
    def __init__(self):
        self.items = []

    def push(self, elemento):
        self.items.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            raise IndexError("La pila está vacía")

    def peek(self):
        if not self.esta_vacia():
            return self.items[-1]
        else:
            raise IndexError("La pila está vacía")
              
    def esta_vacia(self):
        return len(self.items) == 0

# Función para revertir el orden de una lista dada utilizando una pila
def revertir_lista(lista):
    pila = Pila()
    # Agregar todos los elementos de la lista a la pila
    for elemento in lista:
        pila.push(elemento)
    lista_revertida = []
    # Sacar los elementos de la pila y agregarlos a la lista revertida
    while not pila.esta_vacia():
        lista_revertida.append(pila.pop())
    return lista_revertida

lista_original = [1, 2, 3, 4, 5]
lista_revertida = revertir_lista(lista_original)

print("\n****************BIENVENIDO USUARIO************\n")
print("Lista Original:", lista_original)
print("Lista Revertida:", lista_revertida)
print("\n***********************************************")
