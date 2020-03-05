# Sam Cole
# this is the Queue class First in First out
from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.myList = LinkedList()

    def push(self, data):
        self.myList.add_to_end()

    def pop(self, data):
        self.myList.remove_head()
