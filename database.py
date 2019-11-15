import time
import sys

def insert(db):
    file = open("myindex.txt",'r')
    data = file.readlines()
    firstline = True
    for entry in data:
        entry = entry.strip('\n')
        [key, value] = entry.split('|')
        try:
            key = int(key)
            value = int(value)
        except ValueError:
            if firstline :
                firstLine = False
            else:
                print("key or value is not a number.")
                print("The input line is:"," ",key," ",value)
            continue
        db.insert(key,value)

def operation(db,file):
    file = open(file,'r')
    data = file.readlines()
    for entry in data:
        entry = entry.strip('\n')
        [operate, arguement] = entry.split("(")
        arguement = arguement.strip(')')
        if operate == "search":
            try:
                arguement = int(arguement)
            except ValueError:
                print("fail to parse the input",operate, arguement,seq=" ")
            start = time.time()
            value = db.search(arguement)
            end = time.time()
            print("OPERATION: {}, TIME: {:.2e}s, RESULT: {}".format(operate, float(end-start), value))
        elif operate == "insert":
            [key, value] = arguement.split(",")
            try:
                key = int(key)
                value = int(value)
            except ValueError:
                print("failt to parse the input",operate,key,value,seq=" ")
            start = time.time()
            db.insert(key,value)
            end = time.time()
            print("OPERATION: {}, TIME: {:.2e}s".format(operate, float(end-start)))
        elif operate == "delete":
            try:
                arguement = int(arguement)
            except ValueError:
                print("fail to parse the input",operate, arguement,seq=" ")
            start = time.time()
            db.delete(arguement)
            end = time.time()
            print("OPERATION: {}, TIME: {:.2e}s".format(operate, float(end-start)))
        else:
            print("fail to parse the operation",operate, arguement,seq=" ")

def print_result(db,file_name):
    insert(db)
    start = time.time()
    operation(db,file_name)
    end = time.time()
    print("TOTAL TIME: {:.2e}s".format(float(end-start)))