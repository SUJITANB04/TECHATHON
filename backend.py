# backend/db.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "learning_tool.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class ChildProgress(Base):
    __tablename__ = "child_progress"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    age = Column(Integer, nullable=True)
    condition = Column(String, nullable=False)
    recommendation = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

def init_db():
    Base.metadata.create_all(bind=engine)

def save_progress(name, age, condition, recommendation):
    session = SessionLocal()
    try:
        record = ChildProgress(
            name=name,
            age=age,
            condition=condition,
            recommendation=recommendation
        )
        session.add(record)
        session.commit()
        session.refresh(record)
        return record
    finally:
        session.close()
