
from sqlalchemy import Table
from sqlalchemy import create_engine,String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy.exc import InvalidRequestError

from config import DATABASE_URL

Base = declarative_base()
engine = create_engine(DATABASE_URL)

if  not engine.dialect.has_table(engine,'words'):
    metadata = MetaData(engine)
    Table('words',metadata,
          Column('word',String,primary_key=True),
          Column('anagram',String))
    metadata.create_all()

Session = sessionmaker(bind=engine)
session = Session()



def save(object):
    try:
        session.add(object)
        session.commit()
    except InvalidRequestError:
        raise
class Word(Base):
    __tablename__ = 'words'
    word = Column(String(collation='utf8'),primary_key=True)
    anagram = Column(String)

    def __repr__(self):
        return '<Word(name={0}, anagram={1})>'.format(self.word,self.anagram)

    def save(self):
        save(self)

def get_word(anagram):
    print(anagram)
    return session.query(Word).filter(Word.anagram == anagram)
