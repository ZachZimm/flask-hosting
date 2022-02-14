from __main__ import app
# from flask import current_app as app
import sys
import io
import random
import logging
from PIL import Image
from flask import Flask, flash, Response, redirect, request, render_template, send_from_directory, url_for
sean = Image.open('static/sean.jpg')

@app.route("/sean/",methods=["POST","GET"])
def sean_route():
    # if(request.method == "GET"): return sean

    # return render_template("img.html", img=sean)
    return send_from_directory('static','sean.jpg')

@app.route("/blackswan/",methods=["POST","GET"])
def sean_route():
    # if(request.method == "GET"): return sean

    # return render_template("img.html", img=sean)
    return send_from_directory('static','black-swan.jpg')
