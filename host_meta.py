from __main__ import app
# from flask import current_app as app
import sys
import io
import random
import logging
import json
from flask import Flask, flash, Response, redirect, request, render_template, url_for

metadata = open('static/sean_meta.json')
metadata = json.load(metadata)
# metadata = "Metadata!"


@app.route("/meta/",defaults={'path': ''},methods=["POST","GET"])
@app.route("/meta/<path:path>",methods=["POST","GET"])
def meta_route(path):
    if(request.method == "GET"): return metadata


    return render_template("meta.html", meta=metadata)
