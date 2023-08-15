from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql import crud, models, schemas
from sql.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/computer/{computer_id}")
def get_computer_post(computer_id: int, ping: schemas.PingBase, db: Session = Depends(get_db)):
    computer = crud.get_computer(db, computer_id=computer_id)
    commands = crud.get_commands_by(db=db,target_id=computer_id)
    crud.set_ping(db,computer_id, ping)
    if computer is None:
        raise HTTPException(status_code=404, detail="Computer not found")
    return {'name':computer.computer_name,'ping':computer.ping, 'commands':commands}

@app.get("/computer/{computer_id}", response_model=schemas.Computer)
def get_computer(computer_id: int,db: Session = Depends(get_db)):
    computer = crud.get_computer(db, computer_id=computer_id)
    return computer


@app.get("/computer/name/{computer_name}")
def get_computer_by_name(computer_name: str, db: Session = Depends(get_db)):
    computer = crud.get_computer_by_name(db,computer_name)
    if computer is None:
        raise HTTPException(status_code=404, detail="Computer not found")
    return computer


@app.post("/computer/create", response_model=schemas.ComputerCreate)
def create_computer(computer_create: schemas.ComputerCreate, db: Session = Depends(get_db)):
    db_computer = crud.create_computer(db=db, computer=computer_create)
    return db_computer

@app.get("/computers/", response_model=schemas.Computer)
def read_computers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    computers = crud.get_computers(db, skip=skip, limit=limit)
    return computers

@app.get("/command/{command_id}", response_model=schemas.Command)
def read_command(command_id: int, db: Session = Depends(get_db)):
    db_command = crud.get_command(db, command_id=command_id)
    if db_command is None:
        raise HTTPException(status_code=404, detail="Command not found")
    return db_command

@app.post("/computer/command/", response_model=schemas.CommandCreate)
def create_command(command_create: schemas.CommandCreate,db: Session = Depends(get_db)):
    db_command = crud.create_command(db=db, command=command_create)
    return db_command

@app.delete("/command/{command_id}/delete", response_model=schemas.Command)
def delete_command(command_id: int, db: Session = Depends(get_db)):
    db_command = crud.delete_command(db=db, command_id=command_id)
    if db_command is None:
        raise HTTPException(status_code=404, detail="Command not found")
    return db_command

@app.put("/computer/{computer_id}/output/")
def create_command_output(computer_id:int, output: schemas.OuptutBase,db: Session = Depends(get_db)):
    db_computer = crud.output(db=db, computer_id=computer_id, command_output=output)
    return {'status':'yes'}