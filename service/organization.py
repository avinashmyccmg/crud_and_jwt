from sqlalchemy.orm import Session
from schemas import schema
from repository.organization import OrganizationRepository
from typing import List, Any
from models.model import Organization


class OrganizationService:

  @staticmethod
  def get_all(db: Session) -> List[Organization]:
    return OrganizationRepository.get_all(db)

  @staticmethod
  def create(request: schema.Organization, db: Session) -> Organization:
    return OrganizationRepository.create(request=request, db=db)