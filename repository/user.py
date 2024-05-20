from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List

from models.model import User
from schemas import schema
from hashing import Hash


class UserRepository:

  @staticmethod
  def create(request: schema.User, db:Session) -> User:
    new_user = User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

  @staticmethod
  def show(id: int, db: Session) -> User:
    user = db.query(User).filter(User.id == id).first()
    if not user:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f"user with the id {id} is not avilable")
    return user

  @staticmethod
  def get_all(db: Session) -> List[User]:
    users = db.query(User).all()
    return users