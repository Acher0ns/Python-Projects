class Node:
    __slots__ = ['__value', '__next']


    def __init__(self, value, next = None):
        self.__value = value
        self.__next = next


    def get_value(self):
        return self.__value


    def get_next(self):
        return self.__next


def print_node(node_seq):
    if node_seq.get_next() == None:
        print(node_seq.get_value())
        return

    print(node_seq.get_value(), ', ', sep = '', end = '')
    print_node(node_seq.get_next())


# a = Node(1)
# b = Node(2, a)
# c = Node(3, b)

# print_node(c)