from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
)
from database import (
    Base,
    engine,
)
from sqlalchemy.orm import relationship
from user.models import User



class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))


    creator = relationship("User", back_populates="blogs")


Base.metadata.create_all(engine)
