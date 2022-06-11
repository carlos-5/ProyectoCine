from Nodo import Nodo


class Pila:

    def __init__(self) -> None:
        self.top = None
        self.size = 0
    
    def apilar(self, client):

        if self.top is None:
            self.top = Nodo(client) 
        else:
            nuevo = Nodo(client)
            nuevo.next = self.top
            self.top = nuevo
        self.size += 1


    def imprimir(self):
        aux = self.top
        while aux != None:
            print(aux.client.age)
            aux = aux.next
    


    


