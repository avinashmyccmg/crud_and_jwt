from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.schema import ShowUser, User
from service.user import UserService
from models import model
from typing import List


router = APIRouter(
prefix="/user",
  tags=["Users"]
)


@router.post('/', response_model=ShowUser)
def create_user(request: User, db: Session = Depends(get_db)) -> User:
  return UserService.create(request, db)


@router.get("/", response_model=list[ShowUser])
def all(db:Session = Depends(get_db)) -> List[model.User]:
  return UserService.get_all(db)

