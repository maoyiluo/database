from Connection import db,engine,connection,metadata,emp,emp_with_index
import random, time

# initialization: drop all the table
metadata.drop_all(engine)
# initialization: create all the table
metadata.create_all(engine)

# generate ramdon index
numbers = list(range(0, 99999))
random.shuffle(numbers)

# read data
file = open('emp.txt','r')
lines = file.readlines()

def insertion(table, table_type):
    start = time.time()
    for number in numbers:
        # get a random line
        line = lines[number]
        [ID, Name, Salary, Manager, Department] = line.split('|')
        insert = db.insert(table).values(ID=ID, Name=Name, Salary=Salary, Manager=Manager,Department=Department)
        connection.execute(insert)
    end = time.time()
    print("{} RUNNING TIME: {:.2f}s".format(table_type,end-start))

insertion(emp, "WITHOUT INDEX")
insertion(emp_with_index, "WITH INDEX")