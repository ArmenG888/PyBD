from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class Computer(Base):
    __tablename__ = "computers"

    id = Column(Integer, primary_key=True, index=True)
    computer_name = Column(String, index=True)
    computer_ip = Column(String, index=True)
    output_text = Column(String, index=True)
    ping = Column(Boolean, index=True)


    commands = relationship("Command", back_populates="target")

class Command(Base):
    __tablename__ = "commands"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    target_id = Column(Integer, ForeignKey("computers.id"))
    target = relationship("Computer", back_populates="commands")
