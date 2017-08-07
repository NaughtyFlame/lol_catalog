from flask import Flask, render_template, request, redirect, jsonify, url_for



app = Flask(__name__)


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
@app.route('/region/<int:region_id>/edit/')
def editRegion(region_id):
    return "now edit #{} region".format(region_id)

# Delete a region
@app.route('/region/<int:region_id>/delete/')
def deleteRegion(region_id):
    return "now delete #{} region".format(region_id)

# Show champion in the chosen region
@app.route('/region/<int:region_id>/')
@app.route('/region/<int:region_id>/champion/')
def showChampion(region_id):
    return "show champions in #{} region".format(region_id)
# Create a new champion
@app.route('/region/<int:region_id>/champion/new/')
def createNewChampion(region_id):
    return "create new champion in #{} region".format(region_id)

# Edit the chosen champion
@app.route('/region/<int:region_id>/champion/<int:champion_id>/edit/')
def editChampion(region_id, champion_id):
    return "edit #{} champion in #{} region".format(champion_id, region_id)

# Delete the choson champion
@app.route('/region/<int:region_id>/champion/<int:champion_id>/delete/')
def deleteChampion(region_id, champion_id):
    return "delete #{} champion in #{} region".format(champion_id, region_id)




if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
