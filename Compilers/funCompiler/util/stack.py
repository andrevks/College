class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.__top = None
        self.__elem = 0

    def isEmpty(self):
        return self.__top == None

    def peek(self):
        return self.__top.data

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.__top
        self.__top = new_node
        self.__elem += 1

    def pop(self):
        if self.isEmpty():
            return None
        deleted_node = self.__top
        self.__top = deleted_node.next
        deleted_node.next = None
        self.__elem -= 1
        return deleted_node.data
