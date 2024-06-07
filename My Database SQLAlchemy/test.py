import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Integer, Float, String, Column
import os

DIR = os.path.join(os.getcwd(), "My Database SQLAlchemy")
os.chdir(DIR)

# Connecting to the Database
FILE_NAME = 'test.db'
DATABASE_FILENAME = 'sqlite:///test.db'
engine = sqlalchemy.create_engine(DATABASE_FILENAME, echo=True)

# Maping Declaration
Base = declarative_base()

class User(Base):
    __tablename__ = 'users' # Obrigatory
    id = Column(Integer, primary_key=True) # Obrigatory
    name = Column(String(50))
    fullname = Column(String(50))
    age = Column(Integer)

# Create the table in the my_database database
## Check if the database exists

db_exists = os.path.exists(os.path.join(DIR, FILE_NAME))
print(db_exists)
if not db_exists:
    print("NAO EXISTE!!!")
    Base.metadata.create_all(engine)

# Create class instance
user = User(name='Rosbiff', fullname='The Devil', age=666)

# Create database session
Session = sessionmaker(bind=engine)
session = Session()

# Add object (INSERT command)
session.add(user)
session.commit()

user1 = User(name='Odin', fullname='The Father', age=1000)
user2 = User(name='Enzo', fullname='The Weird', age=1)
# Adding objects (INSERT command)
session.add_all([user1, user2])
session.commit()

class Newuser:
    def __init__(self, name, fullname, age):
        self.name = name
        self.fullname = fullname
        self.age = age
    #def __repr__(self):
        #return f"User(name={self.name}, fullname={self.fullname}, age={self.age})"
    
users = []
while(True):
    flag = int(input("1. To register new user. \n2. To commit registration. \n3. To check the database.\n\n"))

    if flag == 1:
        # Create a list of users
        name = input("Name: ")
        fullname = input("Full name: ")
        age = int(input("Age: "))
        users.append(User(name=name, fullname=fullname, age=age))

    elif flag == 2:
        session.add_all(users)
        session.commit()

    elif flag == 3:
        # Query the database
        users_db = session.query(User).all()
        for user in users_db:
            print(f'ID: {user.id}, Name: {user.name}, Fullname: {user.fullname}, Age: {user.age}')

