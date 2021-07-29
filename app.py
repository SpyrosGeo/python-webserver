from flask import Flask,jsonify
from flask_cors import CORS
from yeelight import Bulb
ylight = Bulb('192.168.8.23')
app = Flask(__name__)
CORS(app)

@app.route('/')
def get_json_data():
    data = Bulb.get_properties(ylight)
    power = data['power']
    return jsonify({"power":power,"color":data['rgb']}) 

if __name__ == '__main__':
    app.run
