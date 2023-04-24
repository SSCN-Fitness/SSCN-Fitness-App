from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///payments.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)