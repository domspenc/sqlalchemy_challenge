########################
# Dependencies setup
########################

import datetime as dt
import numpy as np

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

########################
# Database setup
########################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(autoload_with=engine)

measurement = Base.classes.measurement
station = Base.classes.station

session = Session(engine)

########################
# Flask setup
########################

app = Flask(__name__)

########################
# Create routes
########################

# Homepage route
@app.route("/")
def home():
    return (
        f"Hawaii Climate Analysis API<br/>"
        f"Available Routes:<br/>"
        f"Precipitation: <a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a><br/>"
        f"Stations: <a href ='/api/v1.0/stations'>/api/v1.0/stations</a><br/>"
        f"Temperature Observation Data: <a href='/api/v1.0/tobs'>/api/v1.0/tobs</a><br/>"
        f"Start Year Data: <a href='/api/v1.0/temp/yyyy-mm-dd'>/api/v1.0/yyyy-mm-dd</a><br/>"
        f"Start and End Year Data: <a href='/api/v1.0/temp/yyyy-mm-dd/yyyy-mm-dd'>/api/v1.0/temp/yyyy-mm-dd/yyyy-mm-dd</a><br/>"
    )

# Precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    sel = [measurement.date, measurement.prcp]

    twelve_months = session.query(*sel).\
    filter(measurement.date > '2016-08-23').\
    order_by(measurement.date).all()

    print(twelve_months)

    precip = {date: prcp for date, prcp in twelve_months}
    return jsonify(precip)

# Stations route
@app.route("/api/v1.0/stations")
def stations():
   results = session.query(station.station).all()

   print(results)

   stations = list(np.ravel(results))
   #print(stations)
   return jsonify(stations=stations)

# Temperature Observation Data route
@app.route("/api/v1.0/tobs")
def tobs():
    most_active_stats = session.query(measurement.tobs).\
    filter(measurement.station == 'USC00519281').\
    filter(measurement.date > '2016-08-23').all()

    temp = list(np.ravel(most_active_stats))
    return jsonify(temp=temp)

# Start Date route
# Start and End Date route
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

def date(start=None, end=None):
    sel = [func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)]

    if not end:
        active_station_twelve_months = session.query(*sel).\
        filter(measurement.date > start).all()
       
        temp = list(np.ravel(active_station_twelve_months))
        return jsonify(temp=temp)
    
    else:
        active_station_twelve_months = session.query(*sel).\
        filter(measurement.date > start).\
        filter(measurement.date < end).all()

        temp = list(np.ravel(active_station_twelve_months))
        return jsonify(temp=temp)


if __name__ == '__main__':
    app.run(debug=True)

