'''
Author: Kamron Cole
Originally created for assignment 13.3
Contains the outline for a Crewmate
'''
from node_stack import *

class Crewmate():
    __slots___ = ['__color', '__tasks', '__alive']

    def __init__(self, color):
        self.__color = color
        self.__tasks = Stack()
        self.__alive = True

    
    def __repr__(self):
        '''
        Returns a detailed string of crewmates variables
        '''
        return 'Crewmate: \n' + \
            '  color=' + self.__color + '\n' + \
            '  alive=' + str(self.__alive) + ' \n' + \
            '  tasks: ' + str(self.__tasks) + '\n'

    
    def __str__(self):
        '''
        Returns a simplified string of the crewmates color and whether it is dead of alive
        '''
        result = self.__color + ' Crewmate'
        if not self.__alive:
            result += ' (deceased)'
        return result


    def kill(self):
        '''
        kills the crewmate making them dead
        '''
        self.__alive = False

    
    def assign_task(self, task):
        '''
        adds a task to a crewmates tasks stack
        '''
        self.__tasks.push(task)


    def get_task(self):
        '''
        returns next task to do an removes it from the task list
        '''
        return self.__tasks.pop()


    def is_alive(self):
        '''
        returns whether the crewmate is alive or not
        '''
        return self.__alive


    def done_with_tasks(self):
        '''
        returns whether the crewmate is done with tasks or not
        '''
        return self.__tasks.is_empty()