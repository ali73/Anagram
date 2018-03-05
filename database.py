
from    openpyxl import Workbook
from sqlalchemy import Table
from sqlalchemy import create_engine,String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy.exc import InvalidRequestError
Base = declarative_base()
engine = create_engine("postgresql://nlp:123456@localhost/persianwords")

if  not engine.dialect.has_table(engine,'words'):
    metadata = MetaData(engine)
    Table('words',metadata,
          Column('word',String,primary_key=True),
          Column('anagram',String))
    metadata.create_all()

Session = sessionmaker(bind=engine)
session = Session()
class Word(Base):
    __tablename__ = 'words'
    word = Column(String(collation='utf8'),primary_key=True)
    anagram = Column(String)

    def __repr__(self):
        return '<Word(name={0}, anagram={1})>'.format(self.word,self.anagram)

    def save(self):
        try:
            if self.word is None :
                raise ValueError('word can\'t be None')
            if self.anagram is None:
                raise ValueError('anagram can\'t be None')
            session.add(self)
            session.commit()
        except InvalidRequestError as e:
            print(e)
            pass

def get_word(anagram):
    print(anagram)
    return session.query(Word).filter(Word.anagram == anagram)
