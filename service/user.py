from sqlalchemy.orm import Session
from schemas import schema
from models import model
from repository.user import UserRepository
from typing import List, Optional, Any


class UserService:

  @staticmethod
  def create(request: schema.User, db: Session) -> model.User:
    return UserRepository.create(request, db)

  @staticmethod
  def get_all(db: Session) -> List[model.User]:
    return UserRepository.get_all(db)