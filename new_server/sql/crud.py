from sqlalchemy.orm import Session

from . import models, schemas


def get_computer(db: Session, computer_id: int):
    return db.query(models.Computer).filter(models.Computer.id == computer_id).first()

def get_computer_by_ip(db: Session, ip: str):
    return db.query(models.Computer).filter(models.Computer.ip == ip).first()


def get_computers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_computer(db: Session, computer: schemas.ComputerCreate):
    db_computer = models.Computer(computer_name=computer.computer_name)  # Use computer.name here
    db.add(db_computer)
    db.commit()
    db.refresh(db_computer)
    return db_computer



def get_command(db: Session, command_id: int):
    return db.query(models.Command).filter(models.Command.id == command_id).first()

def get_commands(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Command).offset(skip).limit(limit).all()

def create_command(db: Session, command: schemas.CommandCreate, computer_id: int):
    db_command = models.Command(name=command.name, target_id=computer_id)
    db.add(db_command)
    db.commit()
    db.refresh(db_command)
    return db_command

def delete_command(db: Session, command_id: int):
    db_command = db.query(models.Command).filter(models.Command.id == command_id).first()
    db.delete(db_command)
    db.commit()
    return None