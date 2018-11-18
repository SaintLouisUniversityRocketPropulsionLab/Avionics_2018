import time
from Adafruit_BME280 import *
from time import time
#from adxl345 import ADXL345
import datetime
import gps
from math import *
import smbus
import serial
import datetime


radio = serial.Serial(
    port = '/dev/ttyUSB0',
    baudrate = 57600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1/20
    )


#t = gmtime(time()-18000)
FORMAT = '%d%H%M%S'
path = 'Rocketlog.csv'
fileName ='%s_%s' % (datetime.datetime.now().strftime(FORMAT), path)
f = file(fileName, 'w')
f.write("Time,Temp,Pressure,Humidity,GYROx,GYROy,GYROz,ACCELx,ACCELy,ACCELz,MAGx,MAGy,MAGz,Longitue,Latitude,Altitude\n")
f.close()
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
#adxl345 = ADXL345()

longitude = 0.0
latitude = 0.0
altitude = 0.0
'''restart = False
restart_attempted = False
tryAgain = True'''

from ctypes import *

path = "../lib/liblsm9ds1cwrapper.so"
lib = cdll.LoadLibrary(path)

lib.lsm9ds1_create.argtypes = []
lib.lsm9ds1_create.restype = c_void_p

lib.lsm9ds1_begin.argtypes = [c_void_p]
lib.lsm9ds1_begin.restype = None

lib.lsm9ds1_calibrate.argtypes = [c_void_p]
lib.lsm9ds1_calibrate.restype = None

lib.lsm9ds1_gyroAvailable.argtypes = [c_void_p]
lib.lsm9ds1_gyroAvailable.restype = c_int
lib.lsm9ds1_accelAvailable.argtypes = [c_void_p]
lib.lsm9ds1_accelAvailable.restype = c_int
lib.lsm9ds1_magAvailable.argtypes = [c_void_p]
lib.lsm9ds1_magAvailable.restype = c_int

lib.lsm9ds1_readGyro.argtypes = [c_void_p]
lib.lsm9ds1_readGyro.restype = c_int
lib.lsm9ds1_readAccel.argtypes = [c_void_p]
lib.lsm9ds1_readAccel.restype = c_int
lib.lsm9ds1_readMag.argtypes = [c_void_p]
lib.lsm9ds1_readMag.restype = c_int

lib.lsm9ds1_getGyroX.argtypes = [c_void_p]
lib.lsm9ds1_getGyroX.restype = c_float
lib.lsm9ds1_getGyroY.argtypes = [c_void_p]
lib.lsm9ds1_getGyroY.restype = c_float
lib.lsm9ds1_getGyroZ.argtypes = [c_void_p]
lib.lsm9ds1_getGyroZ.restype = c_float

lib.lsm9ds1_getAccelX.argtypes = [c_void_p]
lib.lsm9ds1_getAccelX.restype = c_float
lib.lsm9ds1_getAccelY.argtypes = [c_void_p]
lib.lsm9ds1_getAccelY.restype = c_float
lib.lsm9ds1_getAccelZ.argtypes = [c_void_p]
lib.lsm9ds1_getAccelZ.restype = c_float

lib.lsm9ds1_getMagX.argtypes = [c_void_p]
lib.lsm9ds1_getMagX.restype = c_float
lib.lsm9ds1_getMagY.argtypes = [c_void_p]
lib.lsm9ds1_getMagY.restype = c_float
lib.lsm9ds1_getMagZ.argtypes = [c_void_p]
lib.lsm9ds1_getMagZ.restype = c_float

lib.lsm9ds1_calcGyro.argtypes = [c_void_p, c_float]
lib.lsm9ds1_calcGyro.restype = c_float
lib.lsm9ds1_calcAccel.argtypes = [c_void_p, c_float]
lib.lsm9ds1_calcAccel.restype = c_float
lib.lsm9ds1_calcMag.argtypes = [c_void_p, c_float]
lib.lsm9ds1_calcMag.restype = c_float

imu = lib.lsm9ds1_create()
lib.lsm9ds1_begin(imu)
if lib.lsm9ds1_begin(imu) == 0:
	print("Failed to communicate with LSM9DS1.")
        quit()
lib.lsm9ds1_calibrate(imu)



while True:
#    t = gmtime(time()-18000)
    now=datetime.datetime.now()
    timestamp=now.strftime("%H:%M:%S")
#    timestamp = strftime(" %d %b %Y %H:%M:%S")
    '''if restart and tryAgain and not restart_attempted:
        try:
            adxl345 = ADXL345()
            restart_attempted = True
            restart = False
        except:
            tryAgain = False'''
#    try:
#        axes = adxl345.getAxes(True)
#        x = float("%.3f" % ( axes['x'] ))*9.81
#        y = float("%.3f" % ( axes['y'] ))*9.81
#        z = float("%.3f" % ( axes['z'] ))*9.81
    #    a = sqrt(x**2+y**2+z**2)
        #if(x+y+z == 0):
        #   restart = True
#    except IOError:
        #restart_attempted = False
#        x = 'X'
#        y = 'X'
#        z = 'X'
#        a = 'X'

    try:
        while lib.lsm9ds1_gyroAvailable(imu) == 0:
            pass
        lib.lsm9ds1_readGyro(imu)
        while lib.lsm9ds1_accelAvailable(imu) == 0:
            pass
        lib.lsm9ds1_readAccel(imu)
        while lib.lsm9ds1_magAvailable(imu) == 0:
            pass
        lib.lsm9ds1_readMag(imu)

        gx = lib.lsm9ds1_getGyroX(imu)
        gy = lib.lsm9ds1_getGyroY(imu)
        gz = lib.lsm9ds1_getGyroZ(imu)

        ax = lib.lsm9ds1_getAccelX(imu)
        ay = lib.lsm9ds1_getAccelY(imu)
        az = lib.lsm9ds1_getAccelZ(imu)

        mx = lib.lsm9ds1_getMagX(imu)
        my = lib.lsm9ds1_getMagY(imu)
        mz = lib.lsm9ds1_getMagZ(imu)

        cgx = lib.lsm9ds1_calcGyro(imu, gx)
        cgy = lib.lsm9ds1_calcGyro(imu, gy)
        cgz = lib.lsm9ds1_calcGyro(imu, gz)

        cax = lib.lsm9ds1_calcAccel(imu, ax)
        cay = lib.lsm9ds1_calcAccel(imu, ay)
        caz = lib.lsm9ds1_calcAccel(imu, az)

        cmx = lib.lsm9ds1_calcMag(imu, mx)
        cmy = lib.lsm9ds1_calcMag(imu, my)
        cmz = lib.lsm9ds1_calcMag(imu, mz)


    except IOError:
        cgx = 'X'
        cgy = 'X'
        cgz = 'X'

        cax = 'X'
        cay = 'X'
        caz = 'X'

        cmx = 'X'
        cmy = 'X'
        cmz = 'X'

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
     #   print "GPSD HAS ENDED"
        
    outString = str(timestamp)+","+str(degrees)+","+str(hectopascals)+","+str(humidity)+","+str(cgx)+","+str(cgy)+","+str(cgz)+","+str(cax)+","+","+str(cay)+","+","+str(caz)+","+","+str(cmx)+","+","+str(cmz)+","+","+str(cmy)+","+str(longitude)+","+str(latitude)+","+str(altitude)+"\n"
    f = file(fileName, 'a')
    f.write(outString)
    f.close()
    radio.write(outString)
    #print "Reading Recorded"
