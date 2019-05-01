# Import dependencies

import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

# Copied the following code from a solved instructor file (titanic)
# Update the path for sqlite file
# Update reference tables

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return precipitation results from last year"""

    # Calculate the date 1 year ago from last date in database
    last_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Query precipitation results last year
    precip_results = session.query(Measurement.date, Measurement.prcp). \
        filter(Measurement.date >= last_year).all()

    # Create a dictionary and jsonify results to read
    # Attempted to use list comprehension
    precipitation = {date: prcp for date, prcp in precip_results}
    return jsonify(precipitation)

    # Using ravel instead of dictionary and list comprehension
    # all_measurements = list(np.ravel(precip_results))
    # return jsonify(all_measurements)

@app.route("/api/v1.0/stations")
def stations():
    """Return station list"""
    stat_results = session.query(Station.station).all()

    # Use 'ravel' from numpy to list the stations
    stations = list(np.ravel(stat_results))
    return jsonify(stations)

















if __name__ == '__main__':
    app.run(debug=True)