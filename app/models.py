from app import db

class Measurement(db.Model):
	__tablename__ = 'measurements'

	time = db.Column(db.DateTime, primary_key=True, unique=True, nullable=False)
	user = db.Column(db.Integer, default=0)
	current1 = db.Column(db.Float, nullable=False)
	current2 = db.Column(db.Float, nullable=False)
	voltage = db.Column(db.Float, nullable=False)
	realP1 = db.Column(db.Float, nullable=False)
	realP2 = db.Column(db.Float, nullable=False)

	def __repr__(self):
		return "<Time: {}>".format(self.time)

class Test(db.Model):
	__tablename__ = 'tests'

	tests = db.Column(db.String(120), primary_key=True, unique=True)
	testf = db.Column(db.Float, nullable=False)

	def __repr__(self):
		return "<test string: {}>".format(self.tests)

class Appliance(db.Model):
	__tablename__ = 'appliances'

	name = db.Column(db.String(120), primary_key=True, unique=True)
	duration = db.Column(db.Integer, default=0)
	power = db.Column(db.Float, default=0.0)

	def __repr__(self):
		return "<Device is : {}>".format(self.name)