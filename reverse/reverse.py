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

    def reverse_list(self, node, prev=None):
        # are there any nodes in the list?
        if node is None:
            return
        # set a to current node    
        a = node
        # set b to next node
        b = a.next_node

        if b is None:
            # set the last node to head
            self.head = a
            return
        # if b is not none, then iterate
        b = self.reverse_list(b)

        a.next_node.next_node = a
        a.next_node = None