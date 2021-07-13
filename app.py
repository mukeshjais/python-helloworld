from flask import Flask
import json
import logging
from datetime import datetime

app = Flask(__name__)

@app.route("/status", methods=['GET'])
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - healthy"}),
            status=200,
            mimetype='application/json'
    )
    ## log line
    app.logger.info('{0}, Status End point was reached.'.format(datetime.now().strftime("%b-%d-%Y %H:%M:%S")))
    return response
    
@app.route("/metrics", methods=['GET'])
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )
    app.logger.info('{0}, metrics End point was reached.'.format(datetime.now().strftime("%b-%d-%Y %H:%M:%S")))
    return response

@app.route("/")
def hello():
    app.logger.info('{0}, Main End point was reached.'.format(datetime.now().strftime("%b-%d-%Y %H:%M:%S")))
    return "Hello My World!"

if __name__ == "__main__":
    logging.basicConfig(filename='app.log',level=logging.DEBUG)
    app.run(host='0.0.0.0')