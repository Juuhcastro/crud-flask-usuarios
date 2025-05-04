class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Fila vazia")
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        return removed_data

    def peek(self):
        if self.is_empty():
            print("Fila vazia")
            return None
        return self.front.data

    def display_queue(self):
        if self.is_empty():
            print("Fila vazia")
            return
        current = self.front
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Código de teste
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Fila atual:")
q.display_queue()
# Adicionando mais elementos à fila
q.enqueue(4)
q.enqueue(5)
q.enqueue(6)

# Exibindo a fila após novos enfileiramentos
print("\nFila após adicionar 4, 5 e 6:")
q.display_queue()
# Removendo dois elementos da fila
q.dequeue()
q.dequeue()

# Exibindo a fila após as remoções
print("\nFila após remover dois elementos:")
q.display_queue()
# Mostrando o primeiro elemento da fila
print("\nPrimeiro elemento da fila (peek):", q.peek())
# Verificando se a fila está vazia
if q.is_empty():
    print("Fila está vazia")
else:
    print("Fila não está vazia")
