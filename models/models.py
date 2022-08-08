from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String)
    age= Column(Integer)
    time_regist= Column(DateTime(timezone=True),server_default= func.now())
    status_id= Column(Integer, ForeignKey("Status.id"))

    status = relationship("Status")

class Status(Base):
    __tablename__="Status"
    id = Column(Integer, primary_key=True, index=True)
    name= Column(String)
    is_dangerous= Column(Boolean)
