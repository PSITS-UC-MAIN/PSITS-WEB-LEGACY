from __main__ import app

from flask import session, redirect, url_for, render_template, request

from Database import getAnnouncements, databaseLog, getAccountByID, GETAllEvent, getAccount
from Util import hashData
from webApp_utility import has_redirection, get_redirection, get_redirection_extra, is_blocked_route


@app.route("/PSITS@Login")
def login_page():
    if is_blocked_route('landing_page'):
        return redirect(url_for('maintenance_page'))
    if 'username' in session:
        return redirect(url_for("landing_page"))
    return render_template("Login.html",
                           title="PSITS login",
                           ANNOUNCEMENTS=getAnnouncements(),
                           login="none",
                           logout="none")


@app.route("/PSITS@Logout")
def logout():
    if 'username' not in session:
        return redirect(url_for("landing_page"))
    databaseLog(f"Account ID [{session['username']}] has logged out")
    session.clear()
    return redirect(url_for("landing_page"))


# Entry point
@app.route("/PSITSLogin", methods=['POST'])
def login():
    if is_blocked_route('landing_page'):
        return redirect(url_for('maintenance_page'))
    account_id: str = request.form['id_number']
    password: str = request.form['password']
    account = getAccount(int(account_id), hashData(password))
    if account.uid is not None:
        session['username'] = account.uid
        databaseLog(f"Account [{account.lastname}, {account.firstname} - ID: {account.uid}] has logged in")
        if has_redirection():
            REDIRECTION = get_redirection()
            if 'psits_merchandise_product' in REDIRECTION or 'psits_receipt_generator' in REDIRECTION:
                return redirect(url_for(REDIRECTION,uid=get_redirection_extra()))
            elif REDIRECTION != '':
                return redirect(url_for(REDIRECTION))
        return redirect(url_for("landing_page"))

    account = getAccountByID(int(account_id))
    message = "Account not found!"
    if account.uid is not None:
        if getAccount(int(account_id),hashData('@password_reset')).uid is not None:
            session['username'] = account.uid
            return redirect(url_for('reset_account_password',uid=account.uid))
        message = "Invalid password"

    return render_template("Login.html",
                           title="Login PSITS",
                           ANNOUNCEMENTS=getAnnouncements(),
                           login="none",
                           logout="none",
                           message=message)





