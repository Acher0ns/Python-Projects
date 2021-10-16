import node

class Stack:
    __slots__ = ['__top', '__size']


    def __init__(self):
        self.__top = None
        self.__size = 0


    def __repr__(self):
        result = '['
        node = self.__top
        if node != None:
            result += str(node.get_value())
            node = node.get_next()
            while node != None:
                result += ', ' + str(node.get_value())
                node = node.get_next()
        result += ']'
        return result


    def size(self):
        return self.__size

    
    def is_empty(self):
        return self.__size == 0


    def pop(self):
        if self.__top is None:
            raise IndexError('pop from an empty stack')
        top = self.__top
        value = top.get_value()
        self.__top = top.get_next()
        self.__size -= 1
        return value
    

    def push(self, value):
        new_node = node.Node(value, self.__top)
        self.__top = new_node
        self.__size += 1


    def peek(self):
        if self.__top != None:
            return self.__top.get_value()