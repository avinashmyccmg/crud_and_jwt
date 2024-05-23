from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from database import get_db
from schemas.schema import ShowOrganization, Organization, User
from service.organization import OrganizationService
import oauth2
from typing import List


router = APIRouter(
  prefix="/organization",
  tags=["Organizations"]
)


@router.get("/", response_model=list[ShowOrganization])
def all(db: Session = Depends(get_db),current_user: User = Depends(oauth2.get_current_user)) -> List[Organization]:
  return OrganizationService.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Organization, db:Session = Depends(get_db),
           current_user: User = Depends(oauth2.get_current_user)) -> Organization:
  return OrganizationService.create(request,db)
