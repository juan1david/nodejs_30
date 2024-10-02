from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_DB="mysql+mysqlconnector://root:0000@localhost:3306/banco"
crear=create_engine(URL_DB)
Sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=crear)
Base=declarative_base()

def get_db():
    db = Sessionlocal()
    try:
        yield db
    finally:
        db.close()