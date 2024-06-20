class ArrayQueue:
    '''
    FIFO queue implementation using a Python list as underlying storage.
    '''
    DEFAULT_CAPACITY = 5 # moderate capacity for all new queues
    def __init__(self):
        '''
        Create an empty queue.
        '''
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front =0
    #def
    def __len__(self):
        '''
        Return the number of elements in the queue.
        '''
        return self._size
    #def
    def is_empty(self):
        '''
        Return True if the queue is empty.
        '''
        return self._size == 0
    #def
    def first(self):
        '''
        Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise ArrayQueue('Queue is Empty')
        return self._data[self._front]
    #def
    def dequeue(self):
        '''
        Remove and return the first element of the queue (i.e., FIFO).
        Raise Empty exception if the queue is empty.
        '''
        if self.is_empty():
            raise ArrayQueue('Queue is Empty')
        answer = self._data[self._front]
        self._data[self._front] = None #help garbage collection
        self._front = (self._front+1)%len(self._data)#circular indexing
        self._size -=1 #reduce the queue size
        return answer
    #def
    def enqueue(self,e):
        '''
        Add an element to the back of queue.
        '''
        if self._size == len(self._data):
            self.resize(2*len(self._data)) #double the array size
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
    #def
    def resize(self,cap):
        '''
        Resize to a new list of capacity >= len(self).
        '''
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size): #only consider existing elements
            self._data[k] = old[walk] #intentionally shift indices
            walk = (1+walk)%len(old) #use old size as modulus
        self._front = 0 
    #def
    def __str__(self):
        #String representation of the queue
        return '<'+''.join(str(self._data))+'<'

#Class:
class main:
    if __name__ == '__main__':
        print('===========Demo Queue============')
        q = ArrayQueue()
        q.enqueue(5)
        q.enqueue(3)
        q.enqueue(9)
        q.enqueue(7)
        q.enqueue(2)
        q.enqueue(4)
        q.enqueue(1)
        q.enqueue(0)
        print('===============DEMO================')
        print('Q: ',q)
        print('Queue length: ',len(q))
        print('Remove last item: ',q.dequeue())
        print('Remove last item: ',q.dequeue())
        print('Q: ',q)
        print('Queue length: ',len(q))
        

        