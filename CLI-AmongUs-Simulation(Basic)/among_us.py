'''
Author: Kamron Cole
Originally created for assignment 13.3
Asks the user for a number of imposters and prints a journey based on that
'''
import csv
from among_us_task import *
from among_us_ship import *

PATH_TO_DATA = 'data/'

def build_tasks(filename):
    '''
    Gets a list of available tasks from a csv file
    '''
    tasks = []
    with open(filename) as f:
        c = csv.reader(f)
        next(c)
        for task in c:
            task = Task(task[0], task[1])
            tasks.append(task)
    return tasks


def main():
    '''
    If the user enters a blank line, quit.
    If the user enters an invalid number of imposters, print a message and prompt them again.
    Otherwise, uses ship to simulate a journey with the specified number of imposters.
    '''
    tasks = build_tasks(PATH_TO_DATA + 'tasks_01.csv')
    ship = Ship(tasks)
    while True:
        num_of_imposters = input('How many imposters: ')
        if not num_of_imposters:
            break

        try:
            ship.journey(int(num_of_imposters))
            break
        except ValueError:
            print('Invalid number of imposters:', num_of_imposters)


if __name__ == "__main__":
    main()
