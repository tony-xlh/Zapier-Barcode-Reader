from flask import Flask, request, send_file, Response
from flask_cors import CORS, cross_origin
import json
import time

app = Flask(__name__, static_url_path='/', static_folder='./')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

data = {}

@app.route('/auth', methods=['POST','GET'])
@cross_origin()
def auth():
    response = {}
    response["success"] = True
    json_string = json.dumps(response)
    resp = Response(json_string)
    resp.headers['Content-Type'] = 'application/json'
    return resp

@app.route('/code', methods=['POST','GET'])
@cross_origin()
def code():
    global data
    new_barcode_items = []
    if request.method == 'POST':
        uuid = request.args.get('uuid')
        barcode = request.args.get('barcode')
        barcodes = [];
        if uuid in data:
            barcodes = data[uuid]
        else:
            data[uuid] = barcodes
        item = {}
        item["id"] = int(time.time()*1000)
        item["barcode"] = barcode
        barcodes.append(item)    
    else:
        uuid = request.args.get('uuid')
        if uuid in data:
            barcodes = data[uuid]
            for item in barcodes:
                new_barcode_items.append(item)
            clear = request.args.get('clear')
            print(clear)
            if clear != None:
                barcodes.clear()
    print(data)
    print(new_barcode_items)
    json_string = json.dumps(new_barcode_items)
    resp = Response(json_string)
    resp.headers['Content-Type'] = 'application/json'
    return resp

if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 8888) #, ssl_context='adhoc'