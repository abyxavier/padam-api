from sqlalchemy.orm import declarative_base 
from sqlalchemy import Column,String,Integer,Text

Base = declarative_base()

class MovieTable(Base):
    __tablename__ ="movies"
    id = Column(Integer,primary_key=True,index=True)
    title = Column(String,nullable=False,unique=True)
    descrption = Column(Text,nullable=False)
    genre=Column(String)
    language=Column(String)
    embedding=Column(Text)  
    
    