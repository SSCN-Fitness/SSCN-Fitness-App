from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Payment(Base):
    __tablename__ = 'payments'

    id = Column(Integer, primary_key=True)
    amount = Column(Float, nullable=False)
    currency = Column(String(3), nullable=False)
    description = Column(String(255), nullable=False)
    return_url = Column(String(255), nullable=False)
    cancel_url = Column(String(255), nullable=False)

    def get_json(self):
        return{
        'id': self.id,
        'amount': self.amount,
        'currency': self.currency,
        'description': self.description,
        'return_url': self.return_url,
        'cancel_url': self.cancel_url
    }


    
