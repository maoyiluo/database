import sqlalchemy as db

# set up the connection
engine = db.create_engine('mysql+pymysql://root:passw0rd@localhost:3306/hw')
connection = engine.connect()
metadata = db.MetaData()

# set up table schema
emp = db.Table('emp', metadata,
      db.Column('ID', db.Integer),
      db.Column('Name', db.String(20)),
      db.Column('Salary', db.Integer),
      db.Column('Manager', db.Integer),
      db.Column('Department', db.String(20)),
     )

emp_with_index = db.Table('emp_index', metadata,
      db.Column('ID', db.Integer, index=True),
      db.Column('Name', db.String(20)),
      db.Column('Salary', db.Integer),
      db.Column('Manager', db.Integer),
      db.Column('Department', db.String(20)),
     )




