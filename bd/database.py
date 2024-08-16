import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Nombre del archivo de la base de datos
sqlalchemy_name = "movies.sqlite"

# Directorio base del archivo actual
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construcción correcta de la URL para SQLite
SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(base_dir, sqlalchemy_name)}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
