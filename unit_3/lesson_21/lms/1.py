# Create a double linked list class, i.e., a list where each element has an attribute previous and an attribute next,
# and of course previous and next are also instances of the same class.

class Node:

    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        current_node = self.head
        while current_node is not None \
                and current_node.data is not None:
            print(current_node.data)
            current_node = current_node.next

    def push(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node


if __name__ == '__main__':

    dll = DoublyLinkedList()
    dll.push(1)
    dll.push(2)
    dll.push(3)
    dll.print_list()
