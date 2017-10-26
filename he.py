#!/usr/bin/env python

import urllib
import json
import os
import sys

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))
    
    res = processRequest(req)
    print("Request processed")
    
    res = json.dumps(res, indent=4)
    print(res)
    
    r = make_response(res)
    print(r)
    
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") == "hello":
            result=req.get('resolvedQuery')
            print(result)
       
    return 





def makeWebhookResult(data):
    print("MakeWebhook method")
    query = data.get('d')
    print("Query1:")
    print(query)
    if query is None:
        return {}

    result = query.get('WORKITEM_ID')
    if result is None:
        return {}

    channel = query.get('DESCRIPTION')
    if channel is None:
        return {}

  
	

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
