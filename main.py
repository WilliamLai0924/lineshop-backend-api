import google_drive as gd
import os
import configparser

from flask import Flask, abort, jsonify, request

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')

FID = os.environ.get('FiD', None)

if FID is None:
    FID = config['googledirve']['fid']

@app.route('/hi', methods=['Get'])
def hi():
    return 'nice'

@app.route('/gdrive/products', methods=['Get'])
def query_products():    
    service = gd.get_drive_service2()
    return gd.fetch_product_data(service, FID)

@app.route('/cc', methods=['Get'])
def cc():
    return os.environ.get('GDCLIENT', None)

if __name__ == '__main__':
    app.run(debug=True)