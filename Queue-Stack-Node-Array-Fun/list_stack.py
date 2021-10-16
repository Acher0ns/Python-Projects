'''
Author: Kamron Cole
Originally created for assignment 13.1
Contains blueprint for a stack using lists
'''
class Stack:
    __slots__ = ['__top', '__size']


    def __init__(self):
        '''
        Creates an empty stack
        '''
        self.__top = []
        self.__size = 0

    
    def __repr__(self):
        '''
        Represents the stack as a string of all the values in the stack in list notation
        '''
        result = '['
        node = self.__top
        if node != []:
            result += str(node[1])
            node = node[0]
            while node != []:
                result += ', ' + str(node[1])
                node = node[0]
        result += ']'
        return result


    def push(self, value):
        '''
        Pushes a value to the top of the stack
        [next, value]
        '''
        self.__top = [self.__top, value]
        self.__size += 1


    def pull(self):
        '''
        Pops the top node off the stack and returns the value of the node that was removed
        '''
        if self.__top is []:
            raise IndexError('pop from an empty stack')
        value = self.__top.pop()
        self.__top = self.__top[0]
        self.__size -= 1
        return value


    def peek(self):
        '''
        Returns the value of the top node in the stack
        '''
        if self.__top != []:
            return self.__top[1]
    

    def size(self):
        '''
        Returns how many nodes are in the stack
        '''
        return self.__size

    
    def is_empty(self):
        '''
        Returnes whether the stack is empty or not
        '''
        return self.__size == 0
