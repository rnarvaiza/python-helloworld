from flask import Flask
from flask import json
import logging

app = Flask(__name__)

@app.route('/status')
def status():
    response = app.response_class(
            response=json.dumps({"result":"OK - hHHealthy"}),
            status=200,
            mimetype='application/json'
    )

    ## log line
    app.logger.info('Status request succesful')
    return response

@app.route('/metrics')
def metrics():
    response = app.response_class(
            response=json.dumps({"status":"success","code":0,"data":{"UserCount":140,"UserCountActive":23}}),
            status=200,
            mimetype='application/json'
    )

        ## log line
    app.logger.info('Metrics request succesful')
    return response

@app.route("/")
def hello():

    ## log line
    app.logger.info('Main request succesful')
    return "Hello World!"

if __name__ == "__main__":

    ##Stream logs to myapp.log file
    
    logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
    app.run(host='0.0.0.0', port=8080)
