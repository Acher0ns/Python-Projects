'''
Author: Kamron Cole
Originally created for assignment 13.2
Contains the outline of a queue object using nodes (linked-list)
'''
import node

class Queue():
    __slots__ = ['__front', '__back', '__size']

    def __init__(self):
        '''
        Creates an empty queue
        '''
        self.__front = None
        self.__back = None
        self.__size = 0


    def __repr__(self):
        '''
        Returns string of all values in the queue in list notation
        '''
        result = '['
        node = self.__front
        if node != None:
            result += str(node.get_value())
            node = node.get_next()
            while node != None:
                result += ', ' + str(node.get_value())
                node = node.get_next()
        result += ']'
        return result


    def enqueue(self, value):
        '''
        Adds a value to the back of the queue
        If queue is empty, front is new node
        Else, set back's next to the node and the back to the new node
        '''
        new_node = node.Node(value)
        if self.is_empty():
            self.__front = new_node
        else:
            self.__back.set_next(new_node)
        self.__back = new_node
        self.__size += 1


    def dequeue(self):
        '''
        Removes value from the front of the queue returns that value
        If queue is empty, raise and index error
        '''
        if self.is_empty():
            raise IndexError('Trying to dequeue from an empty queue.')
        value = self.__front.get_value()
        self.__front = self.__front.get_next()
        self.__size -= 1
        if self.is_empty():
            self.__back = None
        return value


    def size(self):
        '''
        Returns how many values are in the queue
        '''
        return self.__size


    def is_empty(self):
        '''
        Returns true if the queue is empty
        '''
        return self.__size == 0


    def front(self):
        '''
        Returns the value of the front node in the queue
        '''
        if self.__front != None:
            return self.__front.get_value()
    

    def back(self):
        '''
        Returns the value of the front node in the queue
        '''
        if self.__back != None:
            return self.__back.get_value()
