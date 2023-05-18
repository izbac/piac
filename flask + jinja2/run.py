from flask import Flask, render_template, redirect, url_for, request
from flask_mail import  Mail, Message
import smtplib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return app.send_static_file('aboutme.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == "POST":
        return request.form["name"]+"+"+ request.form["surname"]+"+"+request.form["text"]
    else:
        return render_template('contact.html')
    
@app.route('/mail')
def mail():
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USERNAME'] = ''
    app.config['MAIL_PASSWORD'] = ''
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USE_SSL'] = True
    mail = Mail(app)

    msg = Message('Hello', sender = '', recipients = [''])
    msg.body = "Hello Flask message sent from Flask-Mail"
    mail.send(msg)
    return "Sent"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')