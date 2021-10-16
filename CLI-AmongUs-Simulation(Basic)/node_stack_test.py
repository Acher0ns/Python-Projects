from node_stack import *


def test_node_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)

    assert stack.size() == 2
    assert stack.is_empty() == False
    assert stack.peek() == 2

    value1 = stack.pop()

    assert stack.size() == 1
    assert stack.is_empty() == False
    assert value1 == 2

    value2 = stack.pop()
    assert stack.size() == 0
    assert stack.is_empty() == True
    assert value2 == 1

    print(stack)


test_node_stack()