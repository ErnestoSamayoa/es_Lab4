#5. Revertir la Mitad de una Cola:

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
def reverse_half_queue(queue):
    stack = []

    # Mover la mitad de los elementos a la pila
    half_size = queue.size() // 2
    for _ in range(half_size):
        stack.append(queue.dequeue())

    # Poner de nuevo los elementos en la cola en orden inverso
    while stack:
        queue.enqueue(stack.pop())

    # Mover los elementos restantes en la cola a la pila
    for _ in range(queue.size() - half_size):
        stack.append(queue.dequeue())

    # Poner de nuevo los elementos en la cola
    while stack:
        queue.enqueue(stack.pop())

# Ejemplo de uso
my_queue = Queue()
for i in range(1, 11):
    my_queue.enqueue(i)
print("\n****************BIENVENIDO USUARIO************\n")
print("Cola original:", my_queue.items)

reverse_half_queue(my_queue)
print("Cola con la mitad invertida:", my_queue.items)

print("\n************************************************")   
