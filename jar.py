class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        new_size = n + self.size
        if new_size > self.capacity:
            raise ValueError("Capacity exceeded")
        self.size = new_size

    def withdraw(self, n):
        if n > self.size:
            raise ValueError("Not enough cookies")
        remaining = self._size - n
        self.size = remaining

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size=0):
        self._size = size

