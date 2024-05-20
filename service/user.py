from sqlalchemy.orm import Session
from schemas import schema
from repository.user import UserRepository
from models.model import User
from typing import List


class UserService:

  @staticmethod
  def create(request: schema.User, db:Session) -> User:
    return UserRepository.create(request, db)

  @staticmethod
  def show(id: int, db: Session) -> User:
    return UserRepository.show(id,db)

  @staticmethod
  def get_all(db: Session) -> List[User]:
    return UserRepository.get_all(db)