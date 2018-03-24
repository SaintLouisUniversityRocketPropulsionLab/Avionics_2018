import gps
session = gps.gps("localhost", "2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
  try:
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
