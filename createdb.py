from database import Base, engine
from tabelas import *

print("Creating database...")

Base.metadata.create_all(engine)

print("Database created...")