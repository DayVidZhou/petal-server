from app import app
from flask import request, jsonify, redirect, url_for

@app.route('/', methods = ["GET","POST"])
@app.route('/index', methods = ["GET","POST"])
def measurement():
	try:
		if request.method == "POST":

			print(request.data)
			return request.data
			if request.is_json:
				json = request.get_json()
				formattedTime = dt.datetime.utcfromtimestamp(json['time']).strftime("%Y-%m-%d %H:%M:%S.%f")
				measurement = Measurement(time=formattedTime, current=json['current']\
					, voltage=json['voltage'], realp=json['realp'])
				db.session.add(measurement)
				db.session.commit()
				return jsonify(json)
		if request.method == "GET":
			return "OH YOU JUST TRYNA READDDD!!!!"
	except:
		return "SOMETHING WENT WRONG"


@app.route('/testing', methods = ["GET","POST"])
def test():
	if request.get_json():
		json = request.get_json()
		test = Test(tests=json['tests'], testf=json['testf'])
		db.session.add(test)
		db.session.commit()
		return jsonify(json)
	else:
		return "OH YOU wanna read TESTSTSS!!!!"

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