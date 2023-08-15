from typing import Union

from pydantic import BaseModel


class ComputerBase(BaseModel):
    computer_name: str
    ping: str



class ComputerCreate(BaseModel):
    computer_name: str

class Computer(ComputerBase):
    computer_name: str

    class Config:
        orm_mode = True

class OuptutBase(BaseModel):
    output: str

class PingBase(BaseModel):
    ping: str

class CommandBase(BaseModel):
    name: str


class CommandCreate(CommandBase):
    name: str
    target_id: int


class Command(CommandBase):
    id: int
    class Config:
        orm_mode = True
