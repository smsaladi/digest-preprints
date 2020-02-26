"""

Resolves (biorxiv) dois into specific resources of that preprint

"""

import os
import sys

import flask
from flask import Flask, render_template, request, jsonify, url_for, redirect

app = Flask(__name__)

@app.route("/")
@app.route("/v1")
def register():
    return redirect('https://github.com/smsaladi/digest-preprints')

@app.route("/v1/<doi_prefix>/<doi_suffix_server_ver>/body/<paraN>")
def paragraphs(doi_prefix, doi_suffix_server_ver, paraN):
    return jsonify({
        'meta': {'license': ''},
        'data': ['']
    })
