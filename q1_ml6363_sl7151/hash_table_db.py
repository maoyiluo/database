import sys
import time
from database import *

class database:
    def __init__(self):
        self.data = []
        self.dict = {}
        self.index = -1 #index of the last element in the list
    
    def insert(self,key,value):
        if key in self.dict:
            index = self.dict.get(key)
            self.data[index] = value
        else:
            self.data.append(value)
            self.index = self.index + 1
            index = self.index
            self.dict[key] = index

    def search(self,key):
        if key in self.dict:
            return self.data[self.dict.get(key)]
        return "NOT PRESENT"

    def delete(self,key):
        self.dict.pop(key)

if __name__ == "__main__":
    db = database()
    print("HASH TABLE:")
    print_result(db, sys.argv[1])
    