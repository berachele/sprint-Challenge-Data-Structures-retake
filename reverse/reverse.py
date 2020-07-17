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
        # if self.head is None:
        #     return None
        # if self.head.get_next() is None:
        #     return self.head.value
        # else:
        #     currentNode = self.head
        #     prevNode = None
        #     nextNode = currentNode.get_next()

        #     while currentNode:
        #         currentNode.set_next(prevNode)
        #         prevNode = currentNode
        #         currentNode = nextNode
        #         if nextNode:
        #             nextNode = nextNode.get_next()
        #     self.head = prevNode
        if node is None:
            return None
        if node.get_next() is None:
            return node
        
        recNode = reverse_list(node.next_node)
        node.next_node.next_node = node
        node.next_node = None
        return recNode
