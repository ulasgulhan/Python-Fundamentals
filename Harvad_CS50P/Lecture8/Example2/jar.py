class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Wrong capacity')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError('Jar capacity at maksimum')
        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError('There are less cookies in jar')
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    
jar = Jar()
jar.deposit(10)
jar.withdraw(9)
print(jar)


