Ok so here are all the things you need to know on working the pi for the rocket

	use sudo for all commands

  All crucial files are stored on the folder Avionics_2018, things that are in it are:
        av_launch.sh,  this is the launch script, make sure to edit this and that all the programs in it are things
that you want to launch at boot


	if needed use "sudo nano /etc/rc.local" this edits the boot to tell it what scripts to launch

	to detect if i2c connections are up use "sudo i2cdetect -y 1"

	to detect if gps is working use "sudo cgps -s"
	
	to test individual sensors go into the Avionics_2018 folder then LSM9DS1 folder then to example to find individual sensor librarbies and examples of code

	IMPORTANT in Avionics_2018 go to the LSM9DS1 folder then example folder to find all the logger programs that start at boot 


	new_logger.py, this is the logging file and what send the radio transmission, stores data locally in folder with time stamp

	accel_logger2.py, this is the acceleration logger program which localy stores acceleration data stores locally in time stamp

	video_logger.py, this is the video logger program, you will need to disable it in the av_launch.sh easy way to do that is to delete the function that calls it or comment it out


	after the flight the avionics package needs to be turned off, once turned off it will need to attached to a monitor and turned on again in order to kill the script, use "ps aux" this lists all processes. Find the process runnning the loggers and the ID number. use the command "sudo kill -9 ID". Replace ID with the ID number you found for the processes you want to kill. Then edit the boot script av_launch and comment out all the logger programs, this will disable the scripts at boot. 
	

	Ground Station,

xdfz	go into the Avionics Folder and find the rocketread.py, this is the program to read incoming radio signals, I made it not only write to local file but also output what it is recieving
