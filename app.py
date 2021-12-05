 # app.py

from flask import Flask, request
app = Flask(__name__)

app.DATA=None

@app.route('/')
def show_data():
    return f'<h1>Test Server Data</h1>{app.DATA}'

@app.route('/update')
def update_data():
    app.DATA = request.args.get('d')
    print(app.DATA)
    return f'<h1>Test Server Data</h1>{app.DATA}'

# We only need this for local development.
if __name__ == '__main__':
    app.run(host='0.0.0.0')

