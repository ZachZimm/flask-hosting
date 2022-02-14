import sys
import io
import random
import logging
from flask import Flask, flash, Response, redirect, request, render_template, url_for
# import riskribbon_strategy_reduced as strategy

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    import host_meta as host_meta
    import host_img as host_img

    app.run(debug=True, use_reloader=True, host='0.0.0.0',port=8081)
    app.debug = True
    app.secret_key = 'WX78654H'

    # TODO
    # Keep a CSV of executed trades
    # I wonder if I could pass variable = plot_svg(get_stat_df_from_csv(is_connected), "Server Uptime") to html and expect it retrun the right plot if I use {{variable}}