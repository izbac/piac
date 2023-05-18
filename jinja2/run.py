from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def szablon():
    return render_template('index.html', name="Stan", surname="Nats", email="stan@nats.eu")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')