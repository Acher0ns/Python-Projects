'''
Author: Kamron Cole
Originally created for assignment 13.1
Contains tests for methods within the Stack class
'''
from list_stack import *

def test_list_stack():
    '''
    Tests that the constructor creates an empty stack
    '''
    stack = Stack()
    assert stack.size() == 0
    assert stack.is_empty() == True


def test_peek_stack():
    '''
    Tests that peek properly returns the top node's value
    '''
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(10)
    assert stack.peek() == 10


def test_push_stack():
    '''
    Tests that push pushes the proper value to the top of the stack
    '''
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
    assert stack.is_empty() == False
    assert stack.peek() == 2


def test_pull_stack():
    '''
    Test that pull pops the proper value from the top of a stack
    '''
    stack = Stack()
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2
    assert stack.is_empty() == False
    assert stack.pull() == 2
    assert stack.peek() == 1


def test_repr_stack(capsys):
    '''
    Tests that the string representation of the stack is a string in list notation of all the values in the stack
    Left(Bottom) -> Right(Top)
    '''
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack)
    out = capsys.readouterr().out
    assert '[4, 3, 2, 1]' in out
