from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Organization(Base):
  __tablename__ = "organizations"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  user_id = Column(Integer, ForeignKey("users.id"))

  creator = relationship("User", back_populates="organizations")


class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  email = Column(String)
  password = Column(String)

  organizations = relationship("Organization", back_populates="creator")
