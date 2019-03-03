from app import app, db
from flask import request, jsonify, redirect, url_for
from app.models import Measurement, Test
import datetime as dt

@app.route('/', methods = ["GET","POST"])
@app.route('/index', methods = ["GET","POST"])
def measurement():
	try:
		if request.method == "POST":
			print(request.form)
			formattedTime = dt.datetime.utcfromtimestamp(float(request.form.get('time'))).strftime("%Y-%m-%d %H:%M:%S.%f")
			measurement = Measurement(time = formattedTime, current1 = float(request.form.get('current1')), \
				voltage = float(request.form.get('voltage')), current2 = float(request.form.get('current2')), \
				realP1 = float(request.form.get('realP1')), realP2 = float(request.form.get('realP2')))
			# if request.is_json:
			# 	json = request.get_json()
			# 	formattedTime = dt.datetime.utcfromtimestamp(json['time']).strftime("%Y-%m-%d %H:%M:%S.%f")
			# 	measurement = Measurement(time=formattedTime, current=json['current']\
			# 		, voltage=json['voltage'], realp=json['realp'])
			db.session.add(measurement)
			db.session.commit()
			return 'thanks for measurments'
		if request.method == "GET":
			return "OH YOU JUST TRYNA READDDD!!!!"
	except Exception as e:
		print(str(e))
		return str(e), 400


@app.route('/testing', methods = ["GET","POST"])
def test():
	try:
		if request.get_json():
			json = request.get_json()
			test = Test(tests=json['tests'], testf=json['testf'])
			db.session.add(test)
			db.session.commit()
			return jsonify(json)
		else:
			return "OH YOU wanna read TESTSTSS!!!!"
	except Exception as e:
		print(str(e))
		return str(e), 400

@app.route('/measurements', methods = ["GET"])
def getMeasurements():
	measurements = Measurement.query.all()
	measure_list = {}
	i = 1
	for x in measurements:
		measure_list[i] = x.time
		i += 1
		print(measure_list)
	return jsonify(measure_list)