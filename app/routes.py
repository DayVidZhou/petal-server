from app import app, db
from flask import request, jsonify, redirect, url_for
from app.models import Measurement, Test
import datetime as dt

@app.route('/', methods = ["GET","POST"])
@app.route('/index', methods = ["GET","POST"])
def measurement():
	try:
		if request.method == "POST":
			formattedTime = dt.datetime.utcfromtimestamp(float(request.form.get('time')))
			measurement = Measurement(time = formattedTime, user = int(request.form.get('user')), current1 = float(request.form.get('current1')), \
				voltage = float(request.form.get('voltage')), current2 = float(request.form.get('current2')), \
				realP1 = float(request.form.get('realP1')), realP2 = float(request.form.get('realP2')))
			db.session.add(measurement)
			db.session.commit()
			return 'thanks for measurments at ' + formattedTime.strftime("%Y-%m-%d %H:%M:%S.%f")
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
			start = dt.datetime.strptime(request.args['start'],'%m-%d-%Y-%H')
			end = dt.datetime.strptime(request.args['end'],'%m-%d-%Y-%H')
			print("Start time is ", start, " the end time is ", end)
			measurements = Measurement.query.filter(Measurement.time <= end).filter(Measurement.time >= start)
			for x in measurements:
				temp = {}
				temp['time'] = x.time.strftime("%m-%d-%Y-%H")
				temp['power'] = x.realP1 + x.realP2
				measurelist.append(temp)
			print("THE LIST IS ", jsonify(measurelist))
		if len(request.args) == 0:
			print("Getting all measurements")
			measurements = Measurement.query.all()
			for x in measurements:
				temp = {}
				time = x.time
				temp['time'] = str(x.time)
				temp['voltage'] = x.voltage
				temp['current1'] = x.current1
				temp['current2'] = x.current2
				temp['power'] = x.realP1 + x.realP2
				measurelist.append(temp)
		return (jsonify(measurelist))
	except Exception as e:
		print(str(e))
		return str(e), 400

@app.route('/lastmeasurement', methods = ["GET"])
def getLastMeasurements():
	try:
		lastRow = db.session.query(Measurement).order_by(Measurement.time.desc()).first()
		ans = {}
		ans['time'] = lastRow.time.strftime("%m-%d-%Y-%H")
		ans['power'] = lastRow.realP1 + lastRow.realP2
		return jsonify(ans)
	except Exception as e:
		print(str(e))
		return str(e), 400

@app.route('/delete_all_measurements', methods = ["GET"])
def deletingMeasurements():
	try:
		deleted = db.session.query(Measurement).delete()
		db.session.commit()
		return "Deleted " + str(deleted) + " rows"
	except Exception as e:
		print(str(e))
		return str(e), 400