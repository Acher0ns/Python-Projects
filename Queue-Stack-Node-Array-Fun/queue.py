import arrays

class Queue():
    __slots__ = ['__front', '__back', '__size', '__array']


    def __init__(self, capacity = 10):
        self.__front = 0
        self.__back = 0
        self.__size = 0
        self.__array = arrays.Array(capacity)


    def __repr__(self):
        result = '['
        if not self.is_empty():
            start = self.__front
            end = self.__back
            while start != end:
                result += str(self.__array[start]) + ', '
                start += 1
                if start == len(self.__array):
                    start = 0
        result += ']'
        return result


    def __resize(self):
        print('Resizing Queue!')
        new_array = arrays.Array(len(self.__array) * 2)
        for i in range(len(self.__array)):
            new_array[i] = self.__array[i]
        self.__array = new_array

    
    def enqueue(self, value):
        self.__array[self.__back] = value
        self.__back += 1
        old_back = self.__back
        self.__size += 1
        if self.__back == len(self.__array):
            self.__back = 0
        if self.__back == self.__front:
            self.__resize()
            self.__back = old_back


    def dequeue(self):
        if self.__size == 0:
            raise IndexError('Trying to dequeue an empty queue.')
        value = self.__array[self.__front]
        self.__front += 1
        if self.__front == len(self.__array):
            self.__front = 0
        self.__size -= 1
        return value


    def size(self):
        return self.__size


    def is_empty(self):
        return self.__size == 0


    def front(self):
        if self.__size > 0:
            return self.__array[self.__front]


    def back(self):
        if self.__size > 0:
            index = self.__back - 1
            if index < 0:
                index = len(self.__array) -1
            return self.__array[index]
