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


@app.get("/computer/{computer_id}", response_model=schemas.Computer)
def read_user(computer_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_computer(db, computer_id=computer_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Computer not found")
    return db_user

@app.post("/computer/create", response_model=schemas.ComputerCreate)
def create_computer(computer_create: schemas.ComputerCreate, db: Session = Depends(get_db)):
    db_computer = crud.create_computer(db=db, computer=computer_create)
    return db_computer