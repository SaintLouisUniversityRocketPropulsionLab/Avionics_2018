!bin/sh
av_launch.sh
cd /
cd home/pi/Avionics_2018/LSM9DS1_RaspberryPi_Library/example
sudo python video_logger.py &
sudo python new_logger.py &
sudo python accel_logger2.py &
cd /
