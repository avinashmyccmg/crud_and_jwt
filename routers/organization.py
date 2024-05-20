from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from database import get_db
from schemas.schema import ShowOrganization, Organization, User
from service.organization import OrganizationService
import oauth2


router = APIRouter(
  prefix="/organization",
  tags=["Organizations"]
)


@router.get("/", response_model=list[ShowOrganization])
def all(db:Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
  return OrganizationService.get_all(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: Organization, db:Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
  return OrganizationService.create(request,db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session= Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):

  return OrganizationService.destroy(id, db)


@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
def update(id,request: Organization, db:Session= Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
  return OrganizationService.update(id, request, db)


@router.get("/{id}", status_code=200, response_model=Organization)
def show(id: int, response: Response, db: Session = Depends(get_db), current_user: User = Depends(oauth2.get_current_user)):
  return OrganizationService.show(id, db)
