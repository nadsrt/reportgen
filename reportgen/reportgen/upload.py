# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 09:56:47 2018

@author: Nadia Desratri Enmayani
"""

import functools
import pandas as pd
import numpy as np

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from reportgen.db import get_db

from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('upload', __name__, url_prefix='/upload')

@bp.route('/up', methods=('GET', 'POST'))
def upload_file():
    if request.method == 'POST':
        print(request.files['file'])
        f =request.files['file']
        df = pd.read_excel(f, 'Sheet1')
        error = None
               
        if not f:
            error ='File is required.'
        
        if error is None:
            return results(df)
        
        flash(error)
        
    return render_template('upload/upload_file.html')

@bp.route('/results')
def results(df):


    # change the appointment date from string into date
    df['Appointment Date'] = pd.to_datetime(df['Appointment Date'], dayfirst=True)
    
    # separate the first two digits of the zip code
    df['Postal Code'] = df['Postal Code'].astype('str')
    df['2Digit'] = df['Postal Code'].str[:2]
    
    # grouping by 2 digits postal code
    twozip = df.groupby(['2Digit']).size()
    twozip = twozip.reset_index()
    twozip = twozip.reset_index()
    twozip = twozip.sort_values(by=[0], ascending=False).head(10)
    lbl1 = twozip['2Digit'].tolist()
    val1 = twozip[0].tolist()

    # grouping by month
    countMth = df.groupby(pd.Grouper(key='Appointment Date', freq='M')).size()
    val2 = countMth.tolist()
    lbl2 = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    
    # stats
    mean = countMth.mean()
    stdev = countMth.std()
    stat = {
            "mean": mean,
            "stdev": stdev
     }
    
    return render_template('upload/results.html', lbl1=lbl1,val1=val1,val2=val2,lbl2=lbl2, stat=stat)
