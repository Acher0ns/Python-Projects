'''
Author: Kamron Cole
Originally created for assignment 13.3
Asks the user for a number of imposters and prints a journey based on that
'''
import random
from among_us import *
from among_us_crewmate import *
from node_queue import *

class Ship:
    __slots__ = ['__locations', '__tasks']

    def __init__(self, tasks):
        self.__tasks = tasks
        self.__locations = set()
        for task in tasks:
            self.__locations.add(task.get_location())


    def journey(self, imposters: int):
        '''
        Symulates a journey. Each journey a ship goes on gets a new team of imposters.
        All crewmates start in the cafeteria. Imposters can not enter the cafeteria and crewmates are safe in there.
        Each round one crewmate leaves to complete a task, if an imposter is where their task is, they die, else they return to the cafeteria until all their tasks are complete.
        At which point there are safe for the rest of the game

        Imposter locations change each round.
        '''
        # Setup
        crewmates = []
        if imposters > 4 or imposters < 1:
            raise ValueError('Can only have 1-4 imposters per journey.')

        colors = ['Black', 'Blue', 'Brown', 'Cyan', 'Green', 'Pink', 'Purple', 'Red', 'White', 'Yellow']
        num_of_crew = (10 - imposters)
        for _ in range(num_of_crew):
            crew_color = colors[random.randint(0, len(colors) - 1)]
            crewmate = Crewmate(crew_color)
            colors.remove(crew_color)
            num_of_tasks = random.randint(3, 6)
            for _ in range(num_of_tasks):
                crewmate.assign_task(self.__tasks[random.randint(0, len(self.__tasks) - 1)])
            crewmates.append(crewmate)

        # Create a dict to keep track of imposters and their location
        imposters_dict = {}

        # All crew members start in the cafeteria
        cafeteria = Queue()
        for crewmate in crewmates:
            cafeteria.enqueue(crewmate)

        # One condition used to check if the journey has ended
        all_tasks_complete = False

        # Beginning of journey
        print('The journey begins! There are', imposters, 'imposters on board!')
        while cafeteria.size() > 0 and not all_tasks_complete:
            # Change imposter location each round
            for i in range(imposters):
                imposters_dict[i] = random.sample(self.__locations, 1)

            # Choose crewmate whose turn it is to go do tasks
            crewmate = cafeteria.dequeue()
            task = crewmate.get_task()
            print(crewmate, 'begins', task)

            # Check if crewmate dies this round (imposter is same location as their task)
            dead = False
            for key in imposters_dict:
                if imposters_dict[key][0] == task.get_location():
                    dead = True
                    break

            if dead:
                print('  Oh no! An imposter is waiting in ambush!', crewmate, 'is murdered!')
                crewmate.kill()
            else:
                print(' ', task, 'Complete!')
                if not crewmate.done_with_tasks():
                    print(' ', crewmate, 'heads back to the cafeteria.')
                    cafeteria.enqueue(crewmate)
                else:
                    print(' ', crewmate,'has finished all of their tasks!')

            # Checks if all crewmates are done with tasks to mark end of journey
            all_tasks_complete = True
            for crewmate in crewmates:
                if not crewmate.done_with_tasks():
                    all_tasks_complete = False
                    break

        # End of journey
        print('The journey has ended!')
        
        num_alive = 0
        for crewmate in crewmates:
            if crewmate.is_alive():
                num_alive += 1
        
        # If a signle crewmate is alive, they win, else, imposters win.
        if num_alive == 0:
            print('The imposters wiped out the crew!')
            for crewmate in crewmates:
                print(' ', crewmate)
        else:
            print('The crew made it!')
            for crewmate in crewmates:
                print(' ', crewmate)
        

    def get_locations(self):
        '''
        returns all of the ship's locations
        '''
        return self.__locations


    def get_tasks(self):
        '''
        returns all of the ship's tasks
        '''
        return self.__tasks

