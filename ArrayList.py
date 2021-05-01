class ArrayList:
    
    def __init__ (self):
        self.list = []

    def add(self, item):
        self.list.append(item)
    
    def pop(self):
        return self.list.pop()

    def size(self):
        return len(self.list)

    def print(self):
        print(self.list)
    
    def remove(self, i):
        try:
            del self.list[i]
        except:
            print("Index out of bounds")