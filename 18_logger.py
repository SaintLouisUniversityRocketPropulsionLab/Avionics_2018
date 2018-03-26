from Adafruit_BME280 import *
from time import *
from adxl345 import ADXL345
import datetime
import gps
from math import *

t = gmtime(time()-18000)
fileName = str(t[0]) + "-" + str(t[1]) + "-" + str(t[2]) + "__" + str(t[3]) + "-" + str(t[4]) + "-" + str(t[5]) + ".csv"
f = file(fileName, 'w')
f.write("Time,Temp,Pressure,Humidity, Ax,Ay,Az,Anet, Longitue, Latitude, Altitude\n")
f.close()
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
adxl345 = ADXL345()

longitude = 0.0
latitude = 0.0
altitude = 0.0
'''restart = False
restart_attempted = False
tryAgain = True'''

while True:
    t = gmtime(time()-18000)
    timestamp = strftime(" %d %b %Y %H:%M:%S")
    '''if restart and tryAgain and not restart_attempted:
        try:
            adxl345 = ADXL345()
            restart_attempted = True
            restart = False
        except:
            tryAgain = False'''
    try:
        axes = adxl345.getAxes(True)
        x = float("%.3f" % ( axes['x'] ))*9.81
        y = float("%.3f" % ( axes['y'] ))*9.81
        z = float("%.3f" % ( axes['z'] ))*9.81
        a = sqrt(x**2+y**2+z**2)
        #if(x+y+z == 0):
        #   restart = True
    except IOError:
        #restart_attempted = False
        x = 'X'
        y = 'X'
        z = 'X'
        a = 'X'
    try:
        sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)
        #does not require error checking because read temp will wait for new value internally
        #other values will return the last read if no new val reported
        degrees = sensor.read_temperature()
        pascals = sensor.read_pressure()
        hectopascals = pascals / 100
        humidity = sensor.read_humidity()
    except IOError:
        degrees = 'X'
        pascals = 'X'
        hectopascals = 'X'
        humidity = 'X'

    #If a value is missing will write an 'X' as value in csv file
    
    try:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'lon'):
                longitude = report.lon
            else:
                longitude = 'X'
            if hasattr(report, 'lat'):
                latitude = report.lat
            else:
                latitude = 'X'
            if hasattr(report, 'alt'):
                altitude = report.alt
            else:
                altitude = 'X'
    except KeyError:
        pass
    except StopIteration:
        session = none
        print "GPSD HAS ENDED"
        
    outString = str(timestamp)+","+str(degrees)+","+str(hectopascals)+","+str(humidity)+","+str(x)+"," + str(y)+","+str(z)+"," + str(a) +"," +str(longitude)+","+str(latitude)+","+str(altitude) + "\n"
    f = file(fileName, 'a')
    f.write(outString)
    f.close()
    print "Reading Recorded"
