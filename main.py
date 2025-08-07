from database import Base, engine
from models import Client, Order, Payment 

Base.metadata.create_all(bind=engine)