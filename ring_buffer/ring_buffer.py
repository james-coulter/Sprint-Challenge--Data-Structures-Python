class RingBuffer:
    def __init__(self, capacity):
        self.items = []  # stores buffer
        self.capacity = capacity
        self.latestIndex = 0  # tracks oldest index

    def append(self, item):
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            self.items[self.latestIndex] = item
            self.latestIndex += 1
        if self.latestIndex == self.capacity:
            self.latestIndex = 0

    def get(self):
        return self.items
