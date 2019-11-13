from hash_table_db import database as ht_database
from b_tree_db import database as bt_database

def insert(bt, ht):
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
        ht.insert(key,value)
        bt.insert(key,value)

def operation(ht,bt):
    file = open("operations.txt",'r')
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
            print(ht.search(arguement))
            print(bt.search(arguement))
        elif operate == "insert":
            [key, value] = arguement.split(",")
            try:
                key = int(key)
                value = int(value)
            except ValueError:
                print("failt to parse the input",operate,key,value,seq=" ")
            ht.insert(key,value)
            bt.insert(key,value)
        elif operate == "delete":
            try:
                arguement = int(arguement)
            except ValueError:
                print("fail to parse the input",operate, arguement,seq=" ")
            ht.delete(arguement)
            bt.delete(arguement)
        else:
            print("fail to parse the operation",operate, arguement,seq=" ")


if __name__ == "__main__":
    ht = ht_database()
    bt = bt_database()
    insert(bt,ht)
    operation(bt,ht)