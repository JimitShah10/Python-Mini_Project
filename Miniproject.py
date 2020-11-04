import winsound
import datetime
import os
import time

def check_alarm_input(alarm_time):
	"""Checks to see if the user has entered in a valid alarm time"""
	if len(alarm_time) == 1: # [Hour] Format
		if alarm_time[0] < 24 and alarm_time[0] >= 0:
			return True
	if len(alarm_time) == 2: # [Hour:Minute] Format
		if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
		   alarm_time[1] < 60 and alarm_time[1] >= 0:
			return True
	elif len(alarm_time) == 3: # [Hour:Minute:Second] Format
		if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
		   alarm_time[1] < 60 and alarm_time[1] >= 0 and \
		   alarm_time[2] < 60 and alarm_time[2] >= 0:
			return True
	return False

# Get user input for the alarm time
print("Set a time for the alarm (Ex. 06:30 or 18:30:00)")
while True:
	alarm_input = input(">> ")
	try:
		alarm_time = [int(n) for n in alarm_input.split(":")]
		if check_alarm_input(alarm_time):
			break
		else:
			raise ValueError
	except ValueError:
		print("ERROR: Enter time in HH:MM or HH:MM:SS format")

# Convert the alarm time from [H:M] or [H:M:S] to seconds
seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second
alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_time)], alarm_time)])

# Get the current time of day in seconds
now = datetime.datetime.now()
current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])

# Calculate the number of seconds until alarm goes off
time_diff_seconds = alarm_seconds - current_time_seconds

# If time difference is negative, set alarm for next day
if time_diff_seconds < 0:
	time_diff_seconds += 86400 # number of seconds in a day

# Display the amount of time until the alarm goes off
print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))

# Sleep until the alarm goes off
time.sleep(time_diff_seconds)

# Time for the alarm to go off
duration = 1000  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)
print("Now time for Submission!")


if os.path.isfile("C:\\Users\\DELL\\TODO.txt"):
    file = "C:\\Users\\DELL\\TODO.txt"
    log_file = open("TODO.txt", 'w')
    log_file.write('Write results')
    log_file.close()
    os.startfile("C:\\Users\\DELL\\TODO.txt")
