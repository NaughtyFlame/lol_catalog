from flask import Flask, render_template, request, redirect, jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Region, Champion
from flask import session as login_session
import random
import string
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

# Connect to Database and create database session
engine = create_engine('sqlite:///regionchampion.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# Show all regions
@app.route('/')
@app.route('/region/')
def showRegions():
    return "this page is main page"

# Create a new region
@app.route('/region/new/')
def newRegion():
    return "create a new region"

# Edit a region
@app.route('/region/<string:region_slug>/edit/')
def editRegion(region_slug):
    return "now edit {} region".format(region_slug)

# Delete a region
@app.route('/region/<string:region_slug>/delete/')
def deleteRegion(region_slug):
    return "now delete {} region".format(region_slug)

# Show champion in the chosen region
@app.route('/region/<string:region_slug>/')
def showAllChampion(region_slug):
    return "show champions in {} region".format(region_slug)
@app.route('/region/<string:region_slug>/champion/<string:champion_slug>/')
def showChampion(region_slug, champion_slug):
    return "show champions {} in {} region".format(champion_slug, region_slug)
# Create a new champion
@app.route('/region/<string:region_slug>/champion/new/')
def createNewChampion(region_slug):
    return "create new champion in {} region".format(region_slug)

# Edit the chosen champion
@app.route('/region/<string:region_slug>/champion/<string:champion_slug>/edit/')
def editChampion(region_slug, champion_slug):
    return "edit #{} champion in {} region".format(champion_slug, region_slug)

# Delete the choson champion
@app.route('/region/<string:region_slug>/champion/<string:champion_slug>/delete/')
def deleteChampion(region_slug, champion_slug):
    return "delete #{} champion in {} region".format(champion_slug, region_slug)




if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
