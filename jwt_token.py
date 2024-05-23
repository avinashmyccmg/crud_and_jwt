from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from typing import Union, List, Dict, Any, Optional
from schemas.schema import TokenData


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict[str, Any]) -> str:
  to_encode: Dict[str, Any] = data.copy()
  expire: datetime = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp": expire})
  encoded_jwt: str = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt


def verify_token(token: str, credentials_exception: BaseException) -> None:
  try:
    payload: Dict[str, Any] = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    email: Optional[str] = payload.get('sub')
    if email is None:
      raise credentials_exception
    token_data = TokenData(email=email)
  except JWTError:
    raise credentials_exception