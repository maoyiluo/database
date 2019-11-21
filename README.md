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
Then run these scripts to test it.
```
python3 q1_ml6363_sl7151 operations.txt
```
# Format of the operations.txt
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
The timing of each data structure will be stored in seperate `txt` file, named `q1_ml6363_sl7151_b_tree_timing.txt` and `q1_ml6363_sl7151_hash_table_timing.txt`  
Here is an example of the output:
```
OPERATION: search, TIME: 8.34e-06s, RESULT: 19730
OPERATION: insert, TIME: 4.05e-06s
OPERATION: search, TIME: 2.15e-06s, RESULT: 1
OPERATION: delete, TIME: 3.10e-06s
OPERATION: search, TIME: 1.19e-06s, RESULT: NOT PRESENT
TOTAL TIME: 1.64e-04s
```
