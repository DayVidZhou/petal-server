import os
from flask import Flask, request, jsonify, redirect, url_for
from models import Base, Measurement
from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "petal.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)

@app.route('/', methods = ["GET","POST"])
def measurement():
	if request.get_json():
		json = request.get_json()
		measurement = Measurement(time=json['time'], current=json['current']\
			, voltage=json['voltage'], realp=json['realp'])
		db.session.add(measurement)
		db.session.commit()
		return jsonify({'messages':"IT WORKED"})
	return "OH YOU JUST TRYNA READDDD!!!!"

@app.route('/measurements', methods = ["GET"])
def getMeasurements():
	measurements = Measurements.query.all()
	measure_list = {}
	i = 1
	for x in measurements:
		measure_list[i] = x.realp
		i += 1
		print(measure_list)
	return jsonify(measure_list)

if __name__ == '__main__':
	app.run(debug=True)