#!/usr/bin/env python

from flask import Flask, request
app = Flask(__name__)

#@app.route('/', methods=['GET', 'POST'], defaults={'path': ''})
#@app.route('/<path:path>', methods=['GET', 'POST'])
@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def black_hole(path):
    print request.get_data()
    return '<html>stuff goes here</html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
