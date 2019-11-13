# database
A simple, in-memory database.

# Dependencis
* Hash table: built-in dictionary
* B-trees: https://pypi.org/project/BTrees/
# How to use it
First we have to install B-trees,
```
pip3 install BTrees
```
Then run this script to test it.
```
from hash_table_db import database as database1
from b_tree_db import database2 as database2
x = database1()
y = database2()

x.insert(1,2)
y.insert(1,2)

x.search(1)
x.search(2)

x.delete(1)
x.delete(2)
```