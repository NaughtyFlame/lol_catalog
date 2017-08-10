from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask import flash
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
    regions = session.query(Region)
    return render_template('regions.html', regions=regions)


# Create a new region
@app.route('/region/new/', methods=['GET', 'POST'])
def newRegion():
    if request.method == 'POST':
        region_name = request.form['name']
        region_slug = '-'.join(region_name.lower().split(' '))
        newRegion = Region(
            name=region_name,
            slug=region_slug,
            description=request.form['description']
        )
        session.add(newRegion)
        session.commit()
        return redirect(url_for('showRegions'))
    else:
        return render_template('newRegion.html')


# Edit a region
@app.route('/region/<string:region_slug>/edit/', methods=['GET', 'POST'])
def editRegion(region_slug):
    editedRegion = session.query(Region).filter_by(slug=region_slug).one()
    if request.method == 'POST':
        if request.form['name']:
            editedRegion.name = request.form['name']
            editedRegion.slug = '-'.join(request.form['name'].lower().split(' '))
            editedRegion.description = request.form['description']
            # flash
            return redirect(url_for('showRegions'))
    else:
        return render_template('editRegion.html', region = editedRegion)


# Delete a region
@app.route('/region/<string:region_slug>/delete/', methods=['GET', 'POST'])
def deleteRegion(region_slug):
    regionToDelete = session.query(Region).filter_by(slug=region_slug).one()
    if request.method == 'POST':
        session.delete(regionToDelete)
        #flash
        session.commit()
        return redirect(url_for('showRegions'))
    else:
        return render_template('deleteRegion.html', region=regionToDelete)


# Show champion in the chosen region
@app.route('/region/<string:region_slug>/')
def showChampionsInRegion(region_slug):
    region = session.query(Region).filter_by(slug=region_slug).one()
    champions = session.query(Champion).filter_by(region_id=region.id).all()
    return render_template('championList.html', region=region,
        champions=champions)


@app.route('/region/<string:region_slug>/champion/<string:champion_slug>/')
def showChampion(region_slug, champion_slug):
    return "show champions {} in {} region".format(champion_slug, region_slug)


# Create a new champion
@app.route('/region/<string:region_slug>/champion/new/')
def createNewChampion(region_slug):
    return "create new champion in {} region".format(region_slug)


# Edit the chosen champion
@app.route(
    '/region/<string:region_slug>/champion/<string:champion_slug>/edit/'
)
def editChampion(region_slug, champion_slug):
    return "edit #{} champion in {} region".format(champion_slug, region_slug)


# Delete the choson champion
@app.route(
    '/region/<string:region_slug>/champion/<string:champion_slug>/delete/'
)
def deleteChampion(region_slug, champion_slug):
    return "delete {} champion in {} region".format(champion_slug, region_slug)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
