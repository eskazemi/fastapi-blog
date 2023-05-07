from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from db.base_class import Base
from sqlalchemy.orm import relationship



class Blog(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    owner_id = Column(Integer, ForeignKey('user.id'))
    creator = relationship("User", back_populates="blogs")

