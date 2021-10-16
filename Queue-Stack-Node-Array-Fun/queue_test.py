import queue

def test_queue_class():
    a_queue = queue.Queue(10)
    assert a_queue.size() == 0
    assert a_queue.is_empty()
    assert a_queue.front() == None
    assert a_queue.back() == None

    assert str(a_queue) == '[]'

    print(a_queue)
    a_queue.enqueue(1)
    print(a_queue)
    a_queue.enqueue(2)
    print(a_queue)

    assert a_queue.size() == 2
    assert not a_queue.is_empty()
    assert a_queue.front() == 1
    assert a_queue.back() == 2

    val = a_queue.dequeue()
    assert not a_queue.is_empty()
    assert a_queue.size() == 1
    assert a_queue.back() == 2
    assert a_queue.front() == 2
    assert val == 1
    print(a_queue)

    val = a_queue.dequeue()
    assert a_queue.is_empty()
    assert a_queue.size() == 0
    assert a_queue.back() == None
    assert a_queue.front() == None
    assert val == 2
    print(a_queue)

    a_queue = queue.Queue(1)
    for i in range(10):
        a_queue.enqueue(i)

    for i in range(10, 30):
        a_queue.enqueue(i)
        print(a_queue.dequeue())

    assert a_queue.size() == 10
    assert a_queue.back() == 29
    assert a_queue.front() == 20


    print(a_queue)


test_queue_class()
