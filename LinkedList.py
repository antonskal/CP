class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    def insert(self, value):
        if self.next is None:
            self.next = LinkedListNode(value)
        else:
            self.next.insert(value)
    def get_size(self):
        if self.next is None:
            return 1
        else:
            return 1 + self.next.get_size()
    def get_values(self):
        if self.next is None:
            return [self.value]
        else:
            return [self.value] + self.next.get_values()
    def delete(self, value):
        '''ToDo'''
        return None
    def delete_at_middle(self):
        '''ToDo
        Delete the middle node of a linked list'''

        return None
ell = LinkedListNode(1)
ell.insert(2)
ell.insert(3)
ell.delete(1)
print(ell.get_values())
