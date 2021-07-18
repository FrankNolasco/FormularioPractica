from flask import render_template, Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/submit')
def submit_form():
    return "HOLA"


if __name__ == '__main__':
    app.run()
