__author__ = 'Ingrid Marie'
""" helope
esdmsnfdsndmn """
import calendar;
import time;  # This is required to include time module.

ticks = time.asctime(time.localtime(time.time()))
print ("Number of ticks since 12:00am, January 1, 1970:", ticks)
cal = calendar.month(1987,1)
print(cal)

nat = calendar.month(2014,3)

print(nat)