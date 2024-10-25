from typing import List

import crud
import model
import schema
from database import SessionLocal, engine
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/memos", response_model=List[schema.MemoSchema])
async def read_memos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    memos = crud.get_memos(db, skip=skip, limit=limit)
    return memos

@app.post("/memos", response_model=schema.MemoSchema)
async def create_memo(memo: schema.MemoCreatingSchema, db: Session = Depends(get_db)):
    return crud.create_memo(db=db, memo=memo)

