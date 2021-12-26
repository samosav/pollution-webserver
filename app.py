from datetime import datetime

from flask import Flask, request

app = Flask(__name__)


app.route('/')
def index():
    return 'OK'

@app.route('/update')
def update_data():
    val = request.args.get('d')
    timestamp = datetime.utcnow()
    with open("results2.csv","a") as outputfile:
        outputfile.write(f"{timestamp},{val}\n")
    return str(val)

# We only need this for local development.
if __name__ == '__main__':
   app.run(host='0.0.0.0')

