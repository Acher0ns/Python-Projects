'''
Author: Kamron Cole
Originally created for assignment 13.2
Contains the tests for queue class and the methods there-in
'''
import node_queue

def test_node_queue_class():
    '''
    Tests that queue is initialized empty w/ default values
    '''
    a_queue = node_queue.Queue()
    assert a_queue.size() == 0
    assert a_queue.is_empty()
    assert a_queue.front() == None
    assert a_queue.back() == None


def test_node_queue_enqueue():
    '''
    Test that enqueue properly adds values to the end of a queue
    '''
    a_queue = node_queue.Queue()
    a_queue.enqueue(1)
    a_queue.enqueue(2)
    assert a_queue.size() == 2
    assert not a_queue.is_empty()
    assert a_queue.back() == 2
    assert a_queue.front() == 1


def test_node_queue_dequeue():
    '''
    Tests that dequeue properly removes values from the front of a queue
    '''
    a_queue = node_queue.Queue()
    a_queue.enqueue(1)
    a_queue.enqueue(2)
    a_queue.enqueue(3)
    a_queue.enqueue(4)
    val = a_queue.dequeue()
    assert a_queue.size() == 3
    assert not a_queue.is_empty()
    assert a_queue.back() == 4
    assert a_queue.front() == 2
    assert val == 1

    try:
        a_queue.dequeue()
        a_queue.dequeue()
        a_queue.dequeue()
        a_queue.dequeue()
        a_queue.dequeue()
        assert False
    except IndexError:
        assert True
    else:
        assert False   


def test_node_queue_repr(capsys):
    '''
    Uses capsys to test that the returned string from repr is properly representing the values in a queue
    '''
    a_queue = node_queue.Queue()
    a_queue.enqueue(1)
    a_queue.enqueue(2)
    a_queue.enqueue(3)
    a_queue.enqueue(4)
    val = a_queue.dequeue()
    assert a_queue.size() == 3
    assert not a_queue.is_empty()
    assert a_queue.back() == 4
    assert a_queue.front() == 2
    assert val == 1
    print(a_queue)
    out = capsys.readouterr().out
    assert '[2, 3, 4]\n' == out
