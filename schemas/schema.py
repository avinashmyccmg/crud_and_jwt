from pydantic import BaseModel
from typing import List, Union


class OrganizationBase(BaseModel):
  name:str


class Organization(OrganizationBase):
  class Config():
    orm_mode = True


class User(BaseModel):
  name: str
  email: str
  password: str

class ShowUser(BaseModel):
  name: str
  email: str
  organizations: List[Organization]
  class Config():
    orm_mode = True


class ShowOrganization(BaseModel):
  name: str
  creator: ShowUser

  class Config():
    orm_mode = True


class Login(BaseModel):
  username: str
  password: str


class Token(BaseModel):
  access_token: str
  token_type: str


class TokenData(BaseModel):
  email: Union[str, None] = None