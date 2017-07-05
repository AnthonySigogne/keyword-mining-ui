#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
API - extract keywords from a text.

The algorithm extracts the main nominal groups (relevant keyword candidates) from the text
and, for each one, attributes a score based on multiple parameters including the number of occurrences.

See https://github.com/AnthonySigogne/keyword-mining for more information.
"""

__author__ = "Anthony Sigogne"
__copyright__ = "Copyright 2017, Byprog"
__email__ = "anthony@byprog.com"
__license__ = "MIT"
__version__ = "1.0"

import os
import requests
from flask import Flask, request, jsonify, render_template

# init flask app and env variables
app = Flask(__name__)
host = os.getenv("HOST")
port = os.getenv("PORT")

@app.route("/", methods=['GET'])
def keywords_from_url():
    """
    URL : /
    Extract keywords from an URL.
    Method : POST or GET (no url)
    Form data :
        - url : url to analyze
    Return the list of relevant keywords.
    """
    # GET data
    url = request.args.get("url", None)

    if url :
        # get keywords
        try :
            r = requests.post('http://%s:%s/keywords_from_url'%(host, port), data = {'url':url, 'hits':50})
        except :
            return "Error, check your installation"

        # show the list of keywords
        data = r.json()
        return render_template('layout.html',
            url=url,
            total=data["total"],
            response_time=r.elapsed.total_seconds(),
            keywords=data["keywords"])

    # return homepage (no query)
    return render_template('layout-empty.html')
