from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Parent(Base):
    __tablename__ = "parents"
    id   = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    children = relationship("Child", back_populates="parent", cascade="all, delete")

    def __repr__(self):
        return f"<Parent id={self.id} name={self.name!r}>"


class Child(Base):
    __tablename__ = "children"
    id        = Column(Integer, primary_key=True)
    name      = Column(String, nullable=False)
    parent_id = Column(Integer, ForeignKey("parents.id"), nullable=False)

    parent = relationship("Parent", back_populates="children")

    def __repr__(self):
        return f"<Child id={self.id} name={self.name!r} parent_id={self.parent_id}>"
