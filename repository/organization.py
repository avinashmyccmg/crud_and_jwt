from sqlalchemy.orm import Session
from fastapi import HTTPException, status
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

  @staticmethod
  def destroy(id:int,db:Session) -> str:
    org = db.query(Organization).filter(Organization.id == id)

    if not org.first():
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f"Blog with id {id} not found")
    org.delete(synchronize_session=False)
    db.commit()
    return "Done"

  @staticmethod
  def update(id:int, request: schema.Organization, db:Session) -> str:
    org = db.query(Organization).filter(Organization.id == id)
    if not org.first():
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f"Blog with the id {id} is not found")
    org.update(request.dict())
    db.commit()
    return "updated"

  @staticmethod
  def show(id:int, db:Session) -> Organization:
    org = db.query(Organization).filter(Organization.id == id).first()
    if not org:
      raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                          detail=f"Blog with the id {id} is not avilable")
    return org
