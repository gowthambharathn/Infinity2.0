#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Infinity2.0! 🚀"




