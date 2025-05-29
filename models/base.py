import logging

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(level=logging.WARNING)
logging.getLogger('sqlalchemy.engine').setLevel(logging.WARNING)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeMeta
from abc import ABCMeta

class BaseMeta(DeclarativeMeta, ABCMeta):
    pass

Base = declarative_base(metaclass=BaseMeta)

engine = create_engine("sqlite:///academia.db", echo=True)

Session = sessionmaker(bind=engine)


