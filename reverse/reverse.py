class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        pass
        #if head is none
        if self.head == None:
            return None
            #return None
        #head.get_next is None
        if self.head.get_next() == None:
            return self.head.value
            #return the value of head
        #otherwise
        else:
            #variables
            currentNode = self.head
            prevNode = None
            nextNode = currentNode.get_next()

            #while current:
            while currentNode:
                #next to prev
                currentNode.set_next(prevNode)
                #prev = current
                prev = currentNode
                #current = next
                currentNode = nextNode
                #if next:
                if nextNode:
                    #nex = nex get_nex
                    nextNode = nextNode.get_next()
            #head = prev
            self.head = prevNode
