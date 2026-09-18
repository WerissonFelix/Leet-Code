'''   
Inversão de Lista Simplesmente Encadeada

Dada uma lista simplesmente encadeada representada por objetos Node, implemente uma
função inverter_linked_list(head) que inverta a ordem dos nós da lista.

A função deve receber o primeiro nó (head) e retornar o novo head após a inversão.

Exemplo:

Antes:
10 → 20 → 30 → 40 → None

Depois:
40 → 30 → 20 → 10 → None

Requisitos:

Não crie novos nós.
Apenas altere as referências next dos nós existentes.
Percorra a lista iterativamente.
Retorne o novo primeiro nó da lista.
Proibido recursão.


'''

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

node4 = Node(40, None)
node3 = Node(30, node4)
node2 = Node(20, node3)
node1 = Node(10, node2)

head = node1

def inverter_linked_list(head: Node):
    anterior = None 
    atual = head
    while atual is not None:      
        proximo = atual.next
        atual.next = anterior    
        anterior = atual
        atual = proximo
        
    return anterior 

head_invertido = inverter_linked_list(head)
while head_invertido is not None:
    print(f"{head_invertido.value} => ", end="")
    head_invertido = head_invertido.next
        