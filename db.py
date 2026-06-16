from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker, declarative_base


DATABASE_URL = "sqlite:///documents.db"


engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(
    bind=engine
)


Base = declarative_base()


class Document(Base):

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)

    extracted_text = Column(Text)

    analysis = Column(Text)


Base.metadata.create_all(bind=engine)