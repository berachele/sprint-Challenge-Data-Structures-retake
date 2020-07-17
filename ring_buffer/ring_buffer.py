class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = []
        self.oldest = len(self.storage)-len(self.storage)

    def append(self, item):
        if self.size == self.capacity:
            print('IF')
            #need to pop the oldest index
            self.storage.pop(self.oldest)
            self.storage.insert(self.oldest, item)
            self.oldest += 1
            # self.storage.append(item)
        #otherwise
        else:
            #we add it to the end
            self.storage.append(item)
            self.size += 1
            print(f'ELSE--adding size: {self.size}')

    def get(self):
        return self.storage