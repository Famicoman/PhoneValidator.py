#!/usr/bin/python
# PhoneValidator 0.1
# Mike Dank 2013
# Given a file of phone numbers, determine if each is a landline or cell.
import re
import urllib2
import sys
import time

# Take input file of phone numbers as cmdline arg, numbers separated by newline.
ins = open( sys.argv[1], "r" )

# Set up our outfile
f = open("workfile.txt", 'a')

# For each line in your input file
for line in ins:
	# Take out all non-numerical characters
	strip = re.sub("[^0-9]", "", line)
	# Check validity of phone number based on length
	if len(strip)==10:
		# Craft our URL to check the number, using intelius' service
		url = 'http://www.intelius.com/results.php?ReportType=33&qnpa='+strip[:3]+'&qnxx='+strip[3:6]+'&qstation='+strip[6:]+'&focusfirst=1'
		# Let's open the url, and scrape the html
		response = urllib2.urlopen(url)
		html = response.read()
		# If it finds 'Land Line' write it to the outfile
		if 'Land Line' in html:
			f.write('Land line')
		# If it finds 'Cellular' write it to the outfile
		elif 'Cellular' in html:
			f.write('Cellular')
	# If out number is invalid, write that to the outfile
	else:
		f.write('Invalid number')
	f.write('\n')
	# Sleep for 2 seconds, don't hammer the server too hard
	time.sleep(2)
