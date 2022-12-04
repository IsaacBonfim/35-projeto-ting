class Queue:
    def __init__(self):
        self._data= list()

    def __len__(self):
        return len(self._data)

    def enqueue(self, value):
        self._data.append(value)

    def dequeue(self):
        removed_item = self._data[0]
        
        self._data.pop(0)
        
        return removed_item

    def search(self, index):
        if index < 0 or index >= len(self._data):
            raise IndexError()
        
        return self._data[index]
