from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List, Any, Optional

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
  def get_all(db: Session) -> List[User]:
    users = db.query(User).all()
    return users

