"""App.py - Flask App"""

from os import getenv
# import dotenv
from flask import Flask  # , render_template
from flask_sqlalchemy import SQLAlchemy


def create_app():
    """

    :return:
    """
    app = Flask(__name__)


    #
    # # Create a DB Object
    # DB = SQLAlchemy()




    # # Instantiate SQLAlchemy database connection
    # APP.config['DATABASE_URL'] = getenv('DATABASE_URL')
    # DB = SQLAlchemy(APP)
    #
    #
    # """ *** MODELS *** """
    #
    #
    # class Kickstarters(DB.Model):
    #     """
    #     Defines the "Kickstarters" table with SQLAlchemy
    #     """
    #     id = DB.Column(DB.BigInteger, primary_key=True)
    #     name = DB.Column(DB.String)
    #     blurb = DB.Column(DB.String)
    #     goal = DB.Column(DB.Float)
    #     campaign_duration = DB.Column(DB.Float)
    #     current_currency = DB.Column(DB.String)
    #     fx_rate = DB.Column(DB.Float)
    #     static_usd_rate = DB.Column(DB.Float)
    #     outcome = DB.Column(DB.Boolean)
    #     days_to_success = DB.Column(DB.Float)
    #     city = DB.Column(DB.String)
    #     state = DB.Column(DB.String)
    #     country = DB.Column(DB.String)
    #     category = DB.Column(DB.String)
    #     subcategory = DB.Column(DB.String)
    #     location = DB.Column(DB.String)
    #     latitude = DB.Column(DB.Float)
    #     longitude = DB.Column(DB.Float)
    #

    # *** ROUTES ***

    @app.route('/')
    def root():
        """Base view.
        # Retrieve the data from the database when the main route is called"""
        return 'Here we are!'

    @app.route('/foox')
    def foo():
        return 'Foo Foof!'


    # @app.route('/refresh')
    # def refresh():
    #     """Pull fresh data from Open AQ and replace existing data."""
    #     DB.drop_all()
    #     DB.create_all()

    return app


if __name__ == "__main__":
    create_app().run()
