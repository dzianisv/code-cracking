# import requests
# import mysql.connector
# import pandas as pd

# Space: N
# Time: M, N. N + N * M
def interleave(data):
    if len(data) < 1:
        return []
        
    result = []
    max_length = max(len(lst) for lst in data)
    
    for column_i in range(max_length):
        for row in data:
            if len(row) > column_i:
                result.append(row[column_i])
            
            
    return result

assert(interleave([[1,2,3],[4,5],[6],[],[7,8,9]]) == [1,4,6,7,2,5,8,3,9])
assert(interleave([]) == [])
assert(interleave([[], []]) == [])

class ListIterator:
    def __init__(self, data):
        self.i = 0
        self.data = data
    
    def hasNext(self) -> bool:
        return len(self.data) > self.i
    
    def getNext(self) -> int:
        assert(self.hasNext())
        self.i += 1
        return self.data[self.i-1]

iter1 = ListIterator([1,2,3])
assert(iter1.hasNext())
assert(iter1.getNext() == 1)
assert(iter1.getNext() == 2)
assert(iter1.getNext() == 3)
assert(not iter1.hasNext())

listIter2 = ListIterator([])
assert(not listIter2.hasNext())

class RangeIterator:
    def __init__(self, start, end, step=1):
        self.step = step
        self.next = start
        self.end = end
    
    def hasNext(self) -> bool:
        return self.next < self.end if self.step >= 0 else self.next > self.end 
    
    def getNext(self) -> int:
        if not self.hasNext():
            raise StopIteration()
        
        r = self.next
        self.next += self.step
        return r

iter2 = RangeIterator(10, 20, 2)
assert(iter2.hasNext())
for i in range(10, 20, 2):
    assert(iter2.hasNext())
    assert(iter2.getNext() == i)

try: 
    iter2.getNext()
    assert(False)
except StopIteration:
    pass
    
iter3 = RangeIterator(10, 10, 1)
assert(not iter3.hasNext())

iter3 = RangeIterator(-3, 3, 2)
for i in range(-3, 3, 2):
    assert(iter3.hasNext())
    assert(iter3.getNext() == i)

iter3 = RangeIterator(-3, 3, -1)
for i in range(-3, 3, -1):
    assert(iter3.hasNext())
    assert(iter3.getNext() == i)


try: 
    iter3.getNext()
    assert(False)
except StopIteration:
    pass
    

class InterleaveIterator:
    def __init__(self, iterators):
        self.iterators = iterators
        self.i = 0
        self.i = self.findNextNonEmptyIterator()
        
    def findNextNonEmptyIterator(self):
        for j in range(len(self.iterators)):
            i = (self.i + j) % len(self.iterators)
            nextIterator = self.iterators[i]
            if nextIterator.hasNext():
                return i
            
        return None

    def hasNext(self) -> bool:
        return self.i is not None
        
    def getNext(self) -> int:
        if not self.hasNext():
            raise StopIteration()
        
        nextIterator = self.iterators[self.i]
        r = nextIterator.getNext()
        self.i += 1
        self.i = self.findNextNonEmptyIterator()
        return r

iter0 = InterleaveIterator([
    ListIterator([1,2]),
    ListIterator([4,5])
])
assert(iter0.hasNext())
assert(iter0.getNext() == 1)
assert(iter0.getNext() == 4)
assert(iter0.getNext() == 2)
assert(iter0.getNext() == 5)
assert(not iter0.hasNext())

iter0 = InterleaveIterator([
    RangeIterator(-999, 999, 1),
    RangeIterator(-999, 999, 2)
])

assert(iter0.hasNext())
assert(iter0.getNext() == -999)
assert(iter0.getNext() == -999)

assert(iter0.getNext() == -998)
assert(iter0.getNext() == -997)

assert(iter0.getNext() == -997)
assert(iter0.getNext() == -995)