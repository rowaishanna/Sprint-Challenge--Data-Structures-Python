class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.index = 0

    def append(self, item):
        # if the list is not at capacity
        if len(self.storage) < self.capacity:
            # add items to the end of the list
            self.storage.append(item)
            return
        # if the list is at capacity
        if len(self.storage) == self.capacity:
            # is self.index going beyond the limit?
            if self.index > (len(self.storage)-1):
                # if it is, then set the index to 0
                self.index = 0
                # remove the value at index off of the array
                self.storage.pop(self.index)
                # add the value at the specified index
                self.storage.insert(self.index, item)
                # increment the index
                self.index += 1
            # if the index is within limits
            else:
                # remove value at index off of the array
                self.storage.pop(self.index)
                # add value at the index of the list
                self.storage.insert(self.index, item)
                # increment index
                self.index += 1


         

    def get(self):
        return self.storage