class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = []
        self.oldest = len(self.storage)-len(self.storage)

    def __str__(self):
        return f'{self.storage}'

    def append(self, item):
        if self.size == self.capacity:
            print('IF')
            self.storage.pop(self.oldest)
            self.storage.insert(self.oldest, item)
            self.oldest += 1
            if self.oldest == self.capacity:
                self.oldest = len(self.storage)-len(self.storage)
        else:
            self.storage.append(item)
            self.size += 1
            print(f'ELSE--adding size: {self.size}')

    def get(self):
        return self.storage

