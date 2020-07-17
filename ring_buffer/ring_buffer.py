class RingBuffer:
    def __init__(self, capacity):
        self.size = 0
        self.storage = []
        self.capacity = capacity
        self.oldest = len(self.storage)-len(self.storage)

    def append(self, item):
        pass

    def get(self):
        pass