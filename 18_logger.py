from Adafruit_BME280 import *
import time
from adxl345 import ADXL345
import datetime
import gps


adxl345 = ADXL345()

axes = adxl345.getAxes(True)

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100
humidity = sensor.read_humidity()



print 'Temp      = {0:0.3f} deg C'.format(degrees)
print 'Pressure  = {0:0.2f} hPa'.format(hectopascals)
print 'Humidity  = {0:0.2f} %'.format(humidity)

print "   x = %.3fG" % ( axes['x'] )
print "   y = %.3fG" % ( axes['y'] )
print "   z = %.3fG" % ( axes['z'] )


report = session.next()
#print report
if report['class'] == 'TPV':
    if hasattr(report, 'time'):
        print report.time
    if hasattr(report, 'lon'):
        print "longitude:"+str(report.lon)
    if hasattr(report, 'lat'):
        print "latitude:"+str(report.lat)
    if hasattr(report, 'alt'):
        print "altitude:"+st(report.alt)
  except KeyError:
    pass
  except KeyboardInterrupt:
    quit()
  except StopIteration:
    session = None
    print "GPSD has terminated"







