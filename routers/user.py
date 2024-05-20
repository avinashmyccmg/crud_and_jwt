from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas.schema import ShowUser, User
from service.user import UserService


router = APIRouter(
prefix="/user",
  tags=["Users"]
)

@router.post('/', response_model=ShowUser)
def create_user(request: User, db:Session = Depends(get_db)):
  return UserService.create(request,db)


@router.get("/", response_model=list[ShowUser])
def all(db:Session = Depends(get_db)):
  return UserService.get_all(db)


@router.get("/{id}", status_code=200, response_model=ShowUser)
def get_user(id:int, db: Session = Depends(get_db)):
  return UserService.show(id, db)