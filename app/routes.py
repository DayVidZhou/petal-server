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
	try:
		measurelist = []
		if request.args:
			start = dt.datetime.strptime(request.args['start'],'%m-%d-%Y')
			end = dt.datetime.strptime(request.args['end'],'%m-%d-%Y')
			print("Start time is ", start, " the end time is ", end)
			measurements = Measurement.query.filter(Measurement.time <= end).filter(Measurement.time >= start)
			for x in measurements:
				temp = {}
				temp['time'] = x.time.strftime("%m-%d-%Y")
				temp['power'] = x.realP1 + x.realP2
				measurelist.append(temp)
			print("THE LIST IS ", jsonify(measurelist))
		if len(request.args) == 0:
			measurements = Measurement.query.all()
			for x in measurements:
				temp = {}
				time = x.time
				temp['time'] = str(x.time)
				temp['voltage'] = x.voltage
				temp['current1'] = x.current1
				temp['current2'] = x.current2
				measurelist.append(temp)
		return (jsonify(measurelist))
	except Exception as e:
		print(str(e))
		return str(e), 400