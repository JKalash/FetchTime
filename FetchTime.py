import socket

server = "time.nist.gov"
port = 37
buffer_size = 4096		# 4kB

#create and connect the socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect((server,port))

#receive a raw string from server
raw = mysocket.recv(buffer_size)
mysocket.close

#convert the raw string into a string of binary
binary  =  ' '.join(format(ord(i),'b').zfill(8) for i in raw)
binary = ''.join(binary.split())

#convert the binary string to integer
seconds = int(binary, 2)
seconds += 2*3600 			#Add 2 hours to switch from GMT to GMT+2

SECS_PER_YEAR = 31556900
DAYS_PER_MONTH = 30.4238
SECS_PER_DAY = 3600*24
SECS_PER_MONTH = DAYS_PER_MONTH * SECS_PER_DAY

#Get year
year = seconds / SECS_PER_YEAR + 1900
seconds %= (SECS_PER_YEAR)

#Get Month
month = seconds/SECS_PER_MONTH
seconds %= (SECS_PER_MONTH)

#Get Day
day = seconds / SECS_PER_DAY
readable_day = int(day)
seconds %= (SECS_PER_DAY)

#Get Hour
hour = seconds / 3600
readable_hour = int(hour)
seconds %= 3600

#Get Minute
minute = seconds / 60
readable_minute = int(minute)
seconds %= 60

#Get month string from number
readableMonth = ""
if int(month) == 0:
	reareadableMonth = "Jan"
elif int(month) == 1:
	reareadableMonth = "Feb"
elif int(month) == 2:
	reareadableMonth = "Mar"
elif int(month) == 3:
	reareadableMonth = "Apr"
elif int(month) == 4:
	reareadableMonth = "May"
elif int(month) == 5:
	reareadableMonth = "Jun"
elif int(month) == 6:
	reareadableMonth = "Jul"
elif int(month) == 7:
	reareadableMonth = "Aug"
elif int(month) == 8:
	reareadableMonth = "Sep"
elif int(month) == 9:
	reareadableMonth = "Oct"
elif int(month) == 10:
	reareadableMonth = "Nov"
elif int(month) == 11:
	reareadableMonth = "Dec"

#Print everything in one line in the proper format
print "%02d %s %d %02d:%02d:%02d GMT+2" % (readable_day, reareadableMonth, year, readable_hour, readable_minute, seconds)