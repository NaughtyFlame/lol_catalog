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
    region = session.query(Region).filter_by(slug=region_slug).one()
    champion = session.query(Champion).filter_by(region_id=region.id, slug =champion_slug).one()
    return render_template('showChampion.html',champion=champion,region=region)


# Create a new champion
@app.route('/region/<string:region_slug>/champion/new/', methods=['GET', 'POST'])
def createNewChampion(region_slug):
    region = session.query(Region).filter_by(slug=region_slug).one()
    if request.method == 'POST':
        name = request.form['name']
        slug = '-'.join(name.split(' '))
        newChampion = Champion(
            name = name,
            slug = slug,
            role = request.form['role'],
            description = request.form['description'],
            pic_url = request.form['pic_url'],
            info_url = request.form['info_url'],
            region_id =region.id
        )
        session.add(newChampion)
        session.commit()
        #flash
        return redirect(url_for('showChampionsInRegion', region_slug=region_slug))
    else:
        return render_template('newChampion.html',region=region)

# Edit the chosen champion
@app.route(
    '/region/<string:region_slug>/champion/<string:champion_slug>/edit/',
    methods=['GET', 'POST']
)
def editChampion(region_slug, champion_slug):
    region = session.query(Region).filter_by(slug=region_slug).one()
    editedchampion = session.query(Champion).filter_by(slug=champion_slug, region_id=region.id).one()

    print request.method
    if request.method == 'POST':

        if request.form['name']:
            champion_name = request.form['name']
            editedchampion.name =champion_name
            editedchampion.slug = '-'.join(champion_name.split(' '))
        if request.form['role']:
            editedchampion.role =request.form['role']
        if request.form['description']:
            editedchampion.description =request.form['description']
        if request.form['pic_url']:
            editedchampion.pic_url =request.form['pic_url']
        if request.form['info_url']:
            editedchampion.info_url =request.form['info_url']
        session.add(editedchampion)
        session.commit()
        # flash
        return redirect(url_for('showChampion', region_slug=region.slug, champion_slug=editedchampion.slug))

    if request.method == 'GET':
        return render_template('editChampion.html',champion=editedchampion,region=region)

# Delete the choson champion
@app.route(
    '/region/<string:region_slug>/champion/<string:champion_slug>/delete/',
    methods=['GET', 'POST']
)
def deleteChampion(region_slug, champion_slug):
    region = session.query(Region).filter_by(slug=region_slug).one()
    championToDelete = session.query(Champion).filter_by(slug=champion_slug, region_id=region.id).one()
    if request.method == 'POST':
        session.delete(championToDelete)
        session.commit()
        # flash
        return redirect(url_for('showChampionsInRegion',region_slug=region.slug))
    else:
        return render_template('deleteChampion.html',champion=championToDelete,region=region)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
