from database import Base
from sqlalchemy import Column, Integer, String


class Memo(Base):
    __tablename__ = 'memos'

    memo_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    content = Column(String, index=True)
