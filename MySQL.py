__author__ = 'Ingrid Marie'
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

def tableCreate():
    c.execute('CREATE TABLE love (ID INT, name TEXT)')

def enterData():
    c.execute("INSERT INTO love VALUES (6,' peter')")

enterData()

