from __main__ import app
# from flask import current_app as app
import sys
import io
import random
import logging
import json
from flask import Flask, flash, Response, redirect, request, render_template, url_for

HEADS_TAILS = True

@app.route("/meta/",defaults={'path': ''},methods=["POST","GET"])
@app.route("/meta/<path:path>",methods=["POST","GET"])
def meta_route(path):
    filepath = 'static/sean_meta.json'

    if(HEADS_TAILS):
        if(path == ''):
            path = "0"
        if((int(path) + 2) % 2 == 0):
            path = "0"
        else:
            path = "1"

    if(path != ''):
        path = str(int(path))
        filepath = 'static/id'+path+'.json'
    else:
        filepath = 'static/sean_meta.json'
    metadata = open(filepath)
    metadata = json.load(metadata)
    # if(request.method == "GET"): return path
    if(request.method == "GET"): return metadata

    return render_template("meta.html", meta=metadata)
