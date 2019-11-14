# Description
A simple, in-memory database.

# Dependencis
* Hash table: built-in dictionary
* B-trees: https://pypi.org/project/BTrees/
# How to use it
Install B-trees,
```
pip3 install BTrees
```
Then run this script to test it.
```
python3 hash_table_db.py operations.txt
python3 b_tree_db.py operations.txt
```
# Format of the input
Each line of the `operations.txt` should be a operation, such as `insert`, `delete`, or `search`.  
* For `delete` and `search` the file should provide one parameter which is the key, arounded by bracket. For example
```
delete(1)
search(1)
```
* For insert the file should provide two parameter, the key and the value, separated by comma. For example
```
insert(1,2)
```
I attached the `operations.txt` as example.
# Data
Each database is initialized with the data in `myindex.txt`, if you are going to change the data, please replace this file and keep the format.
# Output
Here is an example of the output:
```
HASH TABLE:
OPERATION: search, TIME: 5.0067901611328125e-06s, RESULT: 19730, 
OPERATION: insert, TIME: 4.0531158447265625e-06s
OPERATION: search, TIME: 9.5367431640625e-07s, RESULT: 1, 
OPERATION: delete, TIME: 4.0531158447265625e-06s
OPERATION: search, TIME: 9.5367431640625e-07s, RESULT: NOT PRESENT, 
TOTAL TIME: 0.0002911090850830078s
```
The first line is which data structure we are using. After that it's the timing for each operation. At the end of the output is the total time for every operations.