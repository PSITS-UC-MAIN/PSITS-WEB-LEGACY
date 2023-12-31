from concurrent.futures import thread
import os
import socket
#from time import sleep

import flask
from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
from flask_cors import CORS

from Database import getAnnouncements, getAccountByID,\
    databaseInit, databaseLog, GETAllEvent, GETAllPSITSOfficer, GETAllFacultyMember, CREATEFacultyMember, \
    UPDATEFacultyMember,  \
    SEARCHFacultyMember#, GETAllMerchandise, SEARCHMerchOrder, getAllAccounts
from Models import FacultyMember#, Merchandise, Account, MerchOrder
from Util import rankOfficers, CONFIGURATION, CONFIGURATION_DISPLAY
from Util import isAdmin, hashData#, GetReference
from waitress import serve
#import messages
#import threading

THREADS = []

UPLOAD_FOLDER = CONFIGURATION()['SERVER_FILES_PATH']
ALLOWED_EXTENSION = {'png', 'jpg'}
RUNNING = False

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'PSITS2022BYABEJAR'
CORS(app)
import routes.login_route
import routes.app_route_1_2
import webApp_utility
import routes.announcement_route
import routes.register_route
import routes.event_route
import routes.order_route
import routes.merchandise_route
import routes.app_route_1_3
import routes.app_route_1_3_api
import routes.app_route_1_4
import routes.app_route_1_4_api
from webApp_utility import save_redirection, checkImageExist, is_blocked_route

"""
      ____  ____ ___ _____ ____  
     |  _ \/ ___|_ _|_   _/ ___| 
     | |_) \___ \| |  | | \___ \ 
     |  __/ ___) | |  | |  ___) |
     |_|   |____/___| |_| |____/ 
    A web application that handles announcements and events
    for UC CCS Students developed by Jayharron Mar Abejar and 
    this private project is open for collaboration to students
    who are willing to collaborate.
    
    - Collaborators: [Please indicate your names below]
        - Rey Vincent de los Reyes
        - Harold Cuico
        - Nathaniel Tiempo
        - Ferrer Mariella
        - Pia Abellana
"""

# Globals
officers = GETAllPSITSOfficer()
officers = rankOfficers(officers)


@app.route("/")
def webpage():
    save_redirection('landing_page')
    return redirect(url_for("landing_page"))


@app.route("/PSITS")
def landing_page():
    save_redirection('landing_page')
    events: list = GETAllEvent()
    announcements: list = getAnnouncements()

    # Load the Photos if exist
    for announcement in announcements:
        if checkImageExist(str(announcement.uid) + announcement.title + ".png"):
            announcement.image_location = f"{str(announcement.uid) + announcement.title}.png"
        if checkImageExist(str(announcement.uid) + announcement.title + ".jpg"):
            announcement.image_location = f"{str(announcement.uid) + announcement.title}.jpg"
        for num in range(1,100):
            if checkImageExist(f"{str(announcement.uid) + announcement.title + str(num)}.png"):
                announcement.image_file_extras.append(f"{str(announcement.uid) + announcement.title + str(num)}.png")
        for num in range(1,100):
            if checkImageExist(f"{str(announcement.uid) + announcement.title + str(num)}.jpg"):
                    announcement.image_file_extras.append(f"{str(announcement.uid) + announcement.title + str(num)}.jpg")
    # show the latest 10 announcement
    temp = announcements.copy()
    if len(announcements) > 10:
        announcements: list = []
        for i in range(0, 10):
            announcements.append(temp[i])
        temp.clear()
    if "username" in session:
        if isAdmin(session['username']):
            return render_template("Homepage.html",
                                   title="PSITS ANNOUNCEMENTS",
                                   ANNOUNCEMENTS=announcements,
                                   login="none",
                                   logout="block",
                                   account=session['username'],
                                   admin="block",
                                   events=events,
                                   access_key = str("API_SECRET-"+hashData(str((int(session['username'])*250)))).strip(),
                                   account_data=getAccountByID(session['username']),
                                   version = 'v1.4')
        else:
            if is_blocked_route('landing_page'):
                return redirect(url_for('maintenance_page'))
            return render_template("Homepage.html",
                                   title="PSITS ANNOUNCEMENTS",
                                   ANNOUNCEMENTS=announcements,
                                   login="none", logout="block",
                                   account=session['username'],
                                   admin="none",
                                   events=events,
                                   account_data=getAccountByID(session['username']),
                                   version = 'v1.4')
    if is_blocked_route('landing_page'):
        return redirect(url_for('maintenance_page'))
    return render_template("Homepage.html",
                            title="PSITS ANNOUNCEMENTS",
                            ANNOUNCEMENTS=announcements,
                            login="block",
                            logout="none", admin="none", events=events,
                            version = 'v1.4')


@app.route("/PSITS@Faculty", methods=['GET', 'POST'])
def psits_faculty_members():
    if flask.request.method == 'GET':
        save_redirection('psits_faculty_members')
        if is_blocked_route('psits_faculty_members'):
            return redirect(url_for('maintenance_page'))
        if 'username' not in session:
            return render_template("Faculty.html",
                                   title="Faculty Members",
                                   MEMBERS=GETAllFacultyMember(),
                                   login="block",
                                   logout="none",
                                   admin="none",
                                   events=GETAllEvent())
        else:
            if isAdmin(session['username']):
                return render_template("Faculty.html",
                                       title="Faculty Members ADMIN",
                                       MEMBERS=GETAllFacultyMember(),
                                       login="none",
                                       logout="block",
                                       account=session['username'],
                                       admin="block",
                                       events=GETAllEvent(),
                                       account_data=getAccountByID(session['username']))
            else:
                return render_template("Faculty.html",
                                       title="Faculty Members",
                                       MEMBERS=GETAllFacultyMember(),
                                       login="none",
                                       logout="block",
                                       account=session['username'],
                                       admin="none",
                                       events=GETAllEvent(),
                                       account_data=getAccountByID(session['username']))
    else:
        # POST
        if 'username' not in session:
            return redirect(url_for('cant_find_link'))
        if isAdmin(session['username']):
            member = FacultyMember(
                None,
                request.form['name'],
                request.form['position'],
                request.form['description'],
                request.form['job']
            )
            CREATEFacultyMember(member)
            databaseLog(f"Added new faculty member [{member.name}]")
            member: FacultyMember = SEARCHFacultyMember(member.name)[0]
            if 'photo' in request.files:
                file = request.files['photo']
                if file is not None:
                    if file.filename != '':
                        ext = file.filename.split(".")[1]
                        if ext in ALLOWED_EXTENSION:
                            file.filename = "faculty" + str(member.uid) + "." + ext
                            member.image_src = "faculty" + str(member.uid) + "." + ext
                            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
                            file.save(path)
                            file.close()
                            databaseLog(f"Faculty member [{member.name}] comes with an image")
            UPDATEFacultyMember(member)
            return redirect(url_for('psits_faculty_members'))


@app.route("/PSITS@AboutUs")
def about_us():
    save_redirection('about_us')
    if is_blocked_route('about_us'):
        return redirect(url_for('maintenance_page'))
    
    if "username" in session:
        if isAdmin(session['username']):
            return render_template("aboutUs.html",
                                   title="About Us PSITS",
                                   login="none",
                                   logout="block",
                                   account=session['username'],
                                   admin="block",
                                   account_data=getAccountByID(session['username']),
                                   officers=officers)
        else:
            return render_template("aboutUs.html",
                                   title="About Us PSITS",
                                   login="none", logout="block",
                                   account=session['username'],
                                   admin="none",
                                   account_data=getAccountByID(session['username']),
                                   officers=officers)
    return render_template("aboutUs.html",
                           title="About Us PSITS",
                           login="block",
                           logout="none", admin="none",
                           officers=officers)




@app.route("/CannotFindLink")
def cant_find_link():
    return render_template("404Page.html", logout="none", login="none", title="PSITS I'm lost :<")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404Page.html", logout="none", login="none", title="PSITS I'm lost!", message=e), 404


@app.after_request
def after_request(response):
    response.headers.add('Cache-Control', 'no-store,no-cache,must-revalidate,post-check=0,pre-check=0')
    return response


@app.route('/uploads/<path:filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)



if __name__ == '__main__':
    CONFIGURATION_DISPLAY()
    hostname = socket.gethostname()
    IPAddress = socket.gethostbyname(hostname)
    if databaseInit():
        databaseLog(f"Server Initialized, configured to run on {IPAddress}:{CONFIGURATION()['PORT']}")
        # use this if you are debugging the app
        if CONFIGURATION()['PRODUCTION'].lower() == 'false':
            databaseLog(f"Server starting on DEBUG mode, will run on {IPAddress}:{CONFIGURATION()['PORT']}")
            # app.run(host=CONFIGURATION()['APP_HOST'], port=CONFIGURATION()['PORT'], debug=True, ssl_context=('cert.pem', 'key.pem'))
            app.run(host=CONFIGURATION()['APP_HOST'], port=CONFIGURATION()['PORT'], debug=True)
        elif CONFIGURATION()['PRODUCTION'].lower() == 'true':
            # Production
            databaseLog(f"Server starting on PRODUCTION mode, will run on {IPAddress}:{CONFIGURATION()['PORT']}")
            serve(app, host="0.0.0.0", port=CONFIGURATION()['PORT'], url_scheme='https')
        else:
            databaseLog(f"Failed to start web app, check `::PRODUCTION` setting at configuration.psits_config")

