from passlib.context import CryptContext
from typing import Any

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash():
  @staticmethod
  def bcrypt(password:str) -> Any:
    return pwd_cxt.hash(password)

  @staticmethod
  def verify(hashed_password: str, plain_password: str) -> bool:
    return bool(pwd_cxt.verify(plain_password,hashed_password))
