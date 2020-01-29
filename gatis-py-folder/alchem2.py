from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite://')
DBsession = sessionmaker(bind=engine)
session = DBsession()

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column('id', Integer, primary_key=True)
    name = Column('name', String(40))
    age = Column('age', Integer)
    lastname = Column('lastname', String(60))


Base.metadata.create_all(engine)

new_person = Person(name='Mary', lastname='Lundkvist', age=30)
session.add(new_person)

new_person = Person(name='John', lastname='Dear', age=42)
session.add(new_person)

new_person = Person(name='Vasja', lastname='Pupkin', age=55)
session.add(new_person)

session.commit()

for row in session.query(Person).all():
    print('{} with lastname {} is {} years old'.format(row.name, row.lastname, row.age))
