#!/usr/bin/python3
"""index.py to connect to API"""
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from models import storage

@app_views.route('/status', strict_slashes=False)
    def hbnbStatus():
        """returns a JSON status : OK"""
        return jsonify({"status: "OK"})

if __name__ == "__main__":
    pass