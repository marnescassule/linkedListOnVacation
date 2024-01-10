class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None
    
    def insertElementAtStart(self, data):
        new_element = Node(data)
        if self.head == None:
            self.head = new_element
            return 
        else:
             new_element.next = self.head
             self.head = new_element
    
    def printAllElements(self):
        startElement = self.head
        while(startElement):
            print(startElement.data)
            startElement = startElement.next

    
    #criar um método que adiciona o nó em um determinado index [0]
    def insertAtIndex(self, data, index):
        new_node = Node(data)  
        current_node = self.head
        position = 0

        if position == index:
            self.insertElementAtStart(data)
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = new_node.next

            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else: 
                print("Index not present")   

    #criar um método que insere o valor no final[]
    def insertAtEnd(self, data):
        new_node = Node(data)  
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        
        current_node.next =  new_node

    #criar um método que atualiza o valor de um nó
    def updateNode(self, val, index):
        current_node = self.head
        position = 0

        if position == index:
            current_node.data = val
        else:
            while(current_node != None and position != index):
                partition = partition + 1
                current_node = current_node.next
            
            if current_node != None:
                current_node.data = val
            else:
                print("Index not present")   

    #criar um metódo que remove o primeiro nó
    def remove_first_node(self):
        if(self.head == None):
            return
        
        self.head = self.head.next
    
    #criar um metódo que remove o ultimo nó
    def remove_last_node(self):
        if(self.head is None):
            return   
        
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next

        current_node.next = None
    
    #criar um metódo que remove o nó com o index
    def remove_at_index(self, index):
        if(self.head == None):
            return  

        current_node = self.head
        position = 0

        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position + 1
                current_node = current_node.next

            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")
    
    #criar um método que imprime a quantidade de elemento no seu nó
    def sizeofLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
        
        return size



lista = LinkedList()
lista.insertElementAtStart(9)
lista.insertElementAtStart(8)
lista.printAllElements()
lista.insertAtIndex(5, 6)
lista.printAllElements()
print(lista.sizeofLL())

