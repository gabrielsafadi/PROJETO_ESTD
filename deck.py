class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None

# ------------------------------------ Implementação Deque para desfazer ações ----------------------------------

class deck:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self._size = 0

    def __len__(self):
        return self._size

    def empty(self):
        return len(self) == 0

    def __repr__(self) -> str:
        if self.empty():
            return 'Está Vazio'
        p = self.left
        s = 'left <<'

    def push_left(self,elemento):
        node = Node(elemento)
        if self.left is None:
            self.left = node
            self.right = node
        else:
            self.left.previous = node
            node.next = self.left
            self.left = node
        self._size +=1

    def pop_left(self):
        if self.empty():
            return 'Está Vazio'
        elemento = self.left.data
        self.left = self.left.next
        self.left.previous = None
        self._size -= 1
        return elemento

    def pop_right(self):
        
        if self.empty():
            return 'Está Vazio'
        # elemento = self.right.data
        self.right.next = None
        self.right = self.right.previous
        self._size -= 1
        return self.right.data


    def peek_left(self):
        if self.empty():
            return 'Está Vazio'
        return self.left.data
    

    def peek_right(self):
        if self.empty():
            return 'Está Vazio'
        return self.right.data

# ------------------- Função recursiva para adicionar as ações limitada em 10 -----------------------------------------

    def push_right(self,elemento):
        if self._size <= 10:
            node = Node(elemento)
            if self.right is None:
                self.right = node
                self.left = node
            else:
                node.previous = self.right
                self.right.next = node
                self.right = node
            self._size +=1
        else: self.pop_left();self.push_right(elemento)
    
    