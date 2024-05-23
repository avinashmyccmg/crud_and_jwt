from sqlalchemy.orm import Session
from typing import List

from models.model import Organization
from schemas import schema


class OrganizationRepository:

  @staticmethod
  def get_all(db:Session) -> List[Organization]:
    new_org = db.query(Organization).all()
    return new_org

  @staticmethod
  def create(request: schema.Organization, db: Session) -> Organization:
    new_org = Organization(name=request.name, user_id=1)
    db.add(new_org)
    db.commit()
    db.refresh(new_org)
    return new_org
