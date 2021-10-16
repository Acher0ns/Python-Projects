'''
Author: Kamron Cole
Originally created for assignment 13.3
Contains the outline for a Task
'''
class Task():
    __slots__ = ['__name', '__location']

    def __init__(self, name, location):
        self.__name = name
        self.__location = location


    def __str__(self):
        '''
        Returns simple string of the task and its location
        '''
        return self.__name + ' in ' + self.__location


    def get_location(self):
        '''
        returns the location this task is in
        '''
        return self.__location
