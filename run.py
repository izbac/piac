from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')