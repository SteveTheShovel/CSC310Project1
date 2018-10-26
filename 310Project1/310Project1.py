"""Basic example of an adapter class to provide a stack interface to Python's list."""

#from ..exceptions import Empty



class ArrayStack:
  """LIFO Stack implementation using a Python list as underlying storage."""

  def __init__(self):
    """Create an empty stack."""
    self._data = []                       # nonpublic list instance

  def __len__(self):
    """Return the number of elements in the stack."""
    return len(self._data)

  def is_empty(self):
    """Return True if the stack is empty."""
    return len(self._data) == 0

  def push(self, e):
    """Add element e to the top of the stack."""
    self._data.append(e)                  # new item stored at end of list

  def top(self):
    """Return (but do not remove) the element at the top of the stack.

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Exception('Stack is empty')
    return self._data[-1]                 # the last item in the list

  def pop(self):
    """Remove and return the element from the top of the stack (i.e., LIFO).

    Raise Empty exception if the stack is empty.
    """
    if self.is_empty():
      raise Exception('Stack is empty')
    return self._data.pop()               # remove last item from list

  def fromPostFix(self, s):
    Stak = ArrayStack()
    while (len(s) > 0):
      if (s[0] >= '1' and s[0] <= '9'):
        Stak.push(int(s[0]))
      elif (s[0] == '*'):
        Stak.push(Stak.pop()*Stak.pop())
      elif (s[0] == '/'):
        t = Stak.pop()
        Stak.push(Stak.pop()/t)
      elif (s[0] == '-'):
        t = Stak.pop()
        Stak.push(Stak.pop()-t)
      elif(s[0] == '+'):
        Stak.push(Stak.pop()+Stak.pop())
      else:
        print("Incorrectly Entered")
      s = s[1:len(s)]
    print(Stak.pop())

class ArrayQueue:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Exception('Queue is empty')
    return self._data[self._front]

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Exception('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None         # help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self.data))     # double the array size
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1

  def _resize(self, cap):                  # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                       # keep track of existing list
    self._data = [None] * cap              # allocate list with new capacity
    walk = self._front
    for k in range(self._size):            # only consider existing elements
      self._data[k] = old[walk]            # intentionally shift indices
      walk = (1 + walk) % len(old)         # use old size as modulus
    self._front = 0                        # front has been realigned


  def radixSort(self):
    tempQueue = ArrayQueue()

    for i in range(0, 10):
      for j in range (0, self.__len__()):
        if(self.first()%10 == i):
          tempQueue.enqueue(self.dequeue())
        else:
          self.enqueue(self.dequeue())

    for t in range(0, tempQueue.__len__()):
      self.enqueue(tempQueue.dequeue());

    for i in range(0, 10):
      for j in range (0, self.__len__()):
        if(self.first()//10 == i):
          tempQueue.enqueue(self.dequeue())
        else:
          self.enqueue(self.dequeue())

    for i in range (0, tempQueue.__len__()):
      print(tempQueue.dequeue())

if __name__ == '__main__':
  T = ArrayStack()
  T.fromPostFix("52+83-*4/")

  S = ArrayQueue()               # contents: [ ]
  S.enqueue(33)
  S.enqueue(35)
  S.enqueue(53)
  S.enqueue(55)
  S.enqueue(52)
  S.enqueue(32)
  S.enqueue(25)

  S.radixSort()