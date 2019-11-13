from BTrees.IIBTree import IIBTree

class database:
    def __init__(self):
        self.data = []
        self.dict = IIBTree()
        self.index = -1 #index of the last element in the list
    
    def insert(self,key,value):
        if self.dict.has_key(key):
            index = self.dict.get(key)
            self.data[index] = value
        else:
            self.data.append(value)
            self.index = self.index + 1
            index = self.index
            self.dict.update({key:index})

    def search(self,key):
        if self.dict.has_key(key):
            value = self.data[self.dict.get(key)]
            return value
        return "Not found"

    def delete(self,key):
        self.dict.pop(key)
    

if __name__ == "__main__":
    x = database()
    x.insert(1,1)
    print(x.search(1))
    x.insert(1,2)
    print(x.search(1))
    x.delete(1)
    print(x.search(1))