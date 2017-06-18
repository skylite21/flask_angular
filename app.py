from flask import Flask, redirect, request, url_for, jsonify
import os
from flask import render_template
from flask import send_from_directory
import json
# import logging
# from logging.handlers import RotatingFileHandler

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist')
assets_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dist/assets')

app = Flask(__name__, template_folder=tmpl_dir)
app.debug = True

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/<filename>')
def send_static(filename):
    print("getting filename {}".format(filename))
    return send_from_directory(tmpl_dir, filename)

@app.route('/assets/<filename>')
def send_assets(filename):
    print("getting asset:  {}".format(filename))
    return send_from_directory(assets_dir, filename)


@app.route("/")
def hello():
    print("hello")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', use_debugger=False)
