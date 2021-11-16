


# *** IMPORTS ***
from flask_sqlalchemy import SQLAlchemy


# Create a DB Object
DB = SQLAlchemy()


# *** Table Definitions ***


"""
Col    DType
0          Unnamed: 0    int64
1                name   object
2               blurb   object
3                goal  float64
4   campaign_duration  float64
5    current_currency   object
6             fx_rate  float64
7     static_usd_rate  float64
8             outcome  float64
9     days_to_success  float64
10               city   object
11              state   object
12            country   object
13           category   object
14        subcategory   object
15           location   object
16           latitude  float64
17          longitude  float64

"""

class Kickstarters(DB.Model):
    """
    Defines the "Kickstarters" table with SQLAlchemy
    """
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String)
    blurb = DB.Column(DB.String)
    goal = DB.Column(DB.Float)
    campaign_duration = DB.Column(DB.Float)
    current_currency = DB.Column(DB.String)
    fx_rate = DB.Column(DB.Float)
    static_usd_rate = DB.Column(DB.Float)
    outcome = DB.Column(DB.Boolean)
    days_to_success = DB.Column(DB.Float)
    city = DB.Column(DB.String)
    state = DB.Column(DB.String)
    country = DB.Column(DB.String)
    category = DB.Column(DB.String)
    subcategory = DB.Column(DB.String)
    location = DB.Column(DB.String)
    latitude = DB.Column(DB.Float)
    longitude = DB.Column(DB.Float)