#!/usr/bin/env python3
# -*- coding: utf8 -*-
"""Simple flask app"""

from flask import Flask

app = Flask(__name__)  # __name__ is a dunder or magic variable


@app.route("/")
def about_me():     # view function
    me = {
        "first_name": "Andrew",
        "last_name": "Reynolds",
        "hobbies": "Video games"
    }
    return me
