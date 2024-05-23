from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm

from database import get_db
from models.model import User
from hashing import Hash
from jwt_token import create_access_token
from typing import Dict


router = APIRouter(
  prefix="/login",
  tags=["Login"]
)


@router.post("/")
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)) -> Dict[str,str]:
  user = db.query(User).filter(User.email == request.username).first()
  if not user:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Invalid Credentials")
  if not Hash.verify(user.password,request.password):
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                        detail=f"Incorrect password")

  access_token = create_access_token(
    data={"sub": user.email},
  )
  return {"access_token": access_token, "token_type": "bearer"}