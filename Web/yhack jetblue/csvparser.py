import csv
from datetime import datetime

with open('getaways.csv', 'rb') as csvfile:
	reader = csv.reader(csvfile)
	parse_list = list(reader)
	for r in parse_list[1:]:
		g = Getaway()
		g.flight_origin = r[0]
		g.flight_dest = r[1]
		g.hotel = r[2]
		g.nights = int(float(r[3]))
		g.check_in = datetime.strptime(r[4] , '%Y/%m/%d')
		g.check_out = datetime.strptime(r[5] , '%Y/%m/%d')
		g.expedia_price = r[6]
		g.jetblue_price = r[7]
		g.savings = r[8][:-1]
		if r[9] == 'within 1 wk':
			g.advance_weeks = 1
		elif r[9] == '1-2 wks':
			g.advance_weeks = 2
		else:
			g.advance_weeks = 3
		g.save()