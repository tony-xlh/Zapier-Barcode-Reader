from flask import Flask, request, send_file, Response
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__, static_url_path='/', static_folder='./')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

data = {}

@app.route('/code', methods=['POST','GET'])
@cross_origin()
def code():
    global data
    response = {}
    if request.method == 'POST':
        uuid = request.args.get('uuid')
        barcode = request.args.get('barcode')
        barcodes = [];
        if uuid in data:
            barcodes = data[uuid]
        else:
            data[uuid] = barcodes
        barcodes.append(barcode)    
    else:
        uuid = request.args.get('uuid')
        if uuid in data:
            barcodes = data[uuid]
            new_list = []
            for barcode in barcodes:
                new_list.append(barcode)
            response["barcodes"] = new_list
            barcodes.clear()
        else:
            response["barcodes"] = []
    print(data)
    response["success"] = True
    json_string = json.dumps(response)
    resp = Response(json_string)
    resp.headers['Content-Type'] = 'application/json'
    return resp

if __name__ == '__main__':
   app.run(host = "0.0.0.0", port = 8888) #, ssl_context='adhoc'