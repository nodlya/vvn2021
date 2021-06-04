from app import app

# -*- coding: utf-8 -*-
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('main_page.html')
