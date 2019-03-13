from app import app, db
from flask import request, jsonify, redirect, url_for
from app.models import Measurement, Test, Appliance
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

@app.route('/appliancesData', methods = ["GET", "POST"])
def processApplianceData():
	try:
		if request.method == "POST":
			if request.is_json:
				json = request.get_json()
				if Appliance.query.filter_by(name = 'toaster').first() == None:
					print("no toaster")
					toaster = Appliance(name = "toaster", duration = 0, power = 0.0)
					db.session.add(toaster)
					db.session.commit()
				if Appliance.query.filter_by(name = 'hair dryer').first() == None:
					print("no dryer")
					hairdryer = Appliance(name = "hair dryer", duration = 0, power = 0.0)
					db.session.add(hairdryer)
					db.session.commit()
				if Appliance.query.filter_by(name = 'hair iron').first() == None:
					print("no iron")
					hairiron = Appliance(name = "hair iron", duration = 0, power = 0.0)
					db.session.add(hairiron)
					db.session.commit()

				toasterquery = Appliance.query.filter_by(name = 'toaster').first()
				dryerquery = Appliance.query.filter_by(name = 'hair dryer').first()
				ironquery = Appliance.query.filter_by(name = 'hair iron').first()
				toasterlist = json['toaster']
				dryerlist = json['hair dryer']
				ironlist = json['hair iron']

				counter = 0
				power = 0
				for i in toasterlist:
					if i != 0:
						counter += 1
					power += i
				toasterquery.duration = toasterquery.duration + counter
				toasterquery.power = toasterquery.power + float(power)
				db.session.commit()

				counter = 0
				power = 0
				for j in dryerlist:
					if j != 0:
						counter += 1
					power += i
				dryerquery.duration = dryerquery.duration + counter
				dryerquery.power = dryerquery.power + float(power)
				db.session.commit()

				counter = 0
				power = 0
				for k in ironlist:
					if k != 0:
						counter += 1
					power += i
				ironquery.duration = ironquery.duration + counter
				ironquery.power = ironquery.power + float(power)
				db.session.commit()

				return "got the lists"
			else:
				return "send a json man"
		else:
			print(" its a get")
			if Appliance.query.filter_by(name = 'toaster').first() == None:
					print("no toaster")
					toaster = Appliance(name = "toaster", duration = 0, power = 0.0)
					db.session.add(toaster)
					db.session.commit()
			if Appliance.query.filter_by(name = 'hair dryer').first() == None:
				print("no dryer")
				hairdryer = Appliance(name = "hair dryer", duration = 0, power = 0.0)
				db.session.add(hairdryer)
				db.session.commit()
			if Appliance.query.filter_by(name = 'hair iron').first() == None:
				print("no iron")
				hairiron = Appliance(name = "hair iron", duration = 0, power = 0.0)
				db.session.add(hairiron)
				db.session.commit()
			appliancelist = []
			allappliance = Appliance.query.all()
			for i in allappliance:
				appliance = {}
				appliance['name'] = i.name
				appliance['duration'] = i.duration
				appliance['power'] = i.power
				appliancelist.append(appliance)
			return jsonify(appliancelist)
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