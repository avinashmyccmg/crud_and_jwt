from sqlalchemy.orm import Session
from schemas import schema
from repository.organization import OrganizationRepository
from typing import List
from models.model import Organization


class OrganizationService:

  @staticmethod
  def get_all(db: Session) -> List[Organization]:
    return OrganizationRepository.get_all(db)

  @staticmethod
  def create(request: schema.Organization, db: Session) -> Organization:
    return OrganizationRepository.create(request=request, db=db)

  @staticmethod
  def destroy(id: int, db: Session) -> str:
    return OrganizationRepository.destroy(id,db)

  @staticmethod
  def update(id: int, request: schema.Organization, db: Session) -> str:
    return OrganizationRepository.update(id,request,db)

  @staticmethod
  def show(id: int, db: Session) -> Organization:
    return OrganizationRepository.show(id,db)