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


@app.get("/computer/{computer_id}")
def read_user(computer_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_computer(db, computer_id=computer_id)
    commands = crud.get_commands_by(db=db,target_id=computer_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Computer not found")
    return {'name':db_user.computer_name, 'commands':commands}

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


