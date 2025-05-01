# track_utils.py

import sqlite3
import pytz
from datetime import datetime

conn = sqlite3.connect('./data/data.db', check_same_thread=False)
c = conn.cursor()
IST = pytz.timezone('Asia/Kolkata')

def create_page_visited_table():
    c.execute('CREATE TABLE IF NOT EXISTS pageTrackTable(pagename TEXT, timeOfvisit TIMESTAMP)')

def add_page_visited_details(pagename, timeOfvisit=None):
    if timeOfvisit is None:
        timeOfvisit = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S")
    c.execute('INSERT INTO pageTrackTable(pagename, timeOfvisit) VALUES (?, ?)', (pagename, timeOfvisit))
    conn.commit()

def view_all_page_visited_details():
    c.execute('SELECT * FROM pageTrackTable')
    return c.fetchall()

def create_prediction_table():
    c.execute('CREATE TABLE IF NOT EXISTS yieldPredictionTable(temperature REAL, rainfall REAL, soil_type INT, fertilizer REAL, prediction REAL, timeOfvisit TIMESTAMP)')

def add_prediction_details(temperature, rainfall, soil_type, fertilizer, prediction, timeOfvisit=None):
    if timeOfvisit is None:
        timeOfvisit = datetime.now(IST).strftime("%Y-%m-%d %H:%M:%S")
    c.execute('INSERT INTO yieldPredictionTable(temperature, rainfall, soil_type, fertilizer, prediction, timeOfvisit) VALUES (?, ?, ?, ?, ?, ?)',
              (temperature, rainfall, soil_type, fertilizer, prediction, timeOfvisit))
    conn.commit()

def view_all_prediction_details():
    c.execute('SELECT * FROM yieldPredictionTable')
    return c.fetchall()
