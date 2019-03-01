from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Measurement(Base):
	__tablename__ = 'measurements'

	time = Column(DateTime(), primary_key=True, unique=True, nullable=False)
	current = Column(Integer, nullable=False)
	voltage = Column(Integer, nullable=False)
	realP = Column(Integer, nullable=False)

	def __repr__(self):
		return "<Time: {}>".format(self.time)