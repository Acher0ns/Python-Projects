'''
Author: Kamron Cole
Originally created for assignment 13.3
Contains all tests used to create the 'Who Goes There,' an 'Among Us' like game
'''
from among_us import *
from among_us_ship import *
from among_us_task import *
from among_us_crewmate import *

def test_task_class(capsys):
    '''
    tests that the Task class proper sets its values
    '''
    task = Task('Wires', 'Electrical')
    assert task.get_location() == 'Electrical'
    print(task)
    assert 'Wires in Electrical' in capsys.readouterr().out


def test_build_tasks(capsys):
    '''
    tests that build_tasks properly returns a list of tasks from the file and test that their indices are correct
    '''
    tasks = build_tasks(PATH_TO_DATA + 'tasks_01.csv')
    print(tasks[0])
    assert 'Align Engine Output in Upper Engine' in capsys.readouterr().out
    print(tasks[10])
    assert 'Divert Power in O2' in capsys.readouterr().out
    print(tasks[-1])
    assert 'Upload Data in Weapons' in capsys.readouterr().out


def test_crewmate_class(capsys):
    '''
    tests that the crewmate class sets variables properly and that the methods within the Crewmate class work properly
    '''
    crewmate = Crewmate('Red')
    crewmate.assign_task(Task('Wires', 'Electrical'))
    print(crewmate)
    print([crewmate])
    out = capsys.readouterr().out
    assert 'Red Crewmate' in out
    assert 'color=Red' in out
    assert 'alive=True' in out
    assert 'tasks: [Wires in Electrical]' in out
    task = crewmate.get_task()
    assert str(task) == 'Wires in Electrical'
    print([crewmate])
    out = capsys.readouterr().out
    assert 'tasks: []' in out
    crewmate.kill()
    print([crewmate])
    print(crewmate)
    out = capsys.readouterr().out
    assert 'alive=False' in out
    assert 'Red Crewmate (deceased)' in out


def test_ship_class():
    '''
    tests that the ship class properly sets its values
    '''
    ship = Ship([Task('Wires', 'Electrical'), Task('Wires', 'O2')])
    assert 'Electrical' in str(ship.get_locations())
    assert 'O2' in str(ship.get_locations())
