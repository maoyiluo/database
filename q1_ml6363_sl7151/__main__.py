from hash_table_db import database as ht_db
from b_tree_db import database as bt_db
from database import *
import sys

if __name__ == "__main__":
    db = ht_db()
    print_result(db, sys.argv[1],"hash_table")
    db = bt_db()
    print_result(db, sys.argv[1], "b_tree")
