from django.shortcuts import render
from django.http import HttpResponse
from api.models import Getaway
import json
import decimal
from decimal import Decimal
import random
from apiclient.discovery import build

# Create your views here.
airport_dict = {
	'BHM':'Birmingham',
	'DHM':'Dothan',
	'HSV':'Huntsville',
	'MOB':'Mobile',
	'MGM':'Montgomery Alabama',
	'ANC':'Anchorage Alaska',
	'FAI':'Fairbanks Alaska',
	'JNU':'Juneau Alaska',
	'FLG':'Flagstaff Arizona',
	'PHX':'Phoenix Arizona',
	'TUS':'Tucson Arizona',
	'YUM':'Yuma Arizona',
	'FYV':'Fayetteville',
	'LIT':'Little Rock',
	'BUR':'Burbank',
	'FAT':'Fresno',
	'LGB':'Long Beach',
	'LAX':'Los Angeles',
	'OAK':'Oakland',
	'ONT':'Ontario',
	'PSP':'Palm Springs',
	'SMF':'Sacramento',
	'SAN':'San Diego',
	'SFO':'San Francisco',
	'SJC':'San Jose',
	'SNA':'Santa Ana',
	'ASE':'Aspen',
	'COS':'Colorado Springs',
	'DEN':'Denver',
	'GJT':'Grand Junction Colorado',
	'PUB':'Pueblo Colorado',
	'BDL':'Hartford Connecticut',
	'IAD':'Washinton',
	'DCA':'Washington',
	'DAB':'Daytona Beach',
	'FLL':'Fort Lauderdale',
	'RSW':'Fort Meyers',
	'JAX':'Jacksonville',
	'EYW':'Key West',
	'MIA':'Miami',
	'MCO':'Orlando',
	'PNS':'Pansacola',
	'PIE':'St. Petersburg Florida',
	'SRQ':'Sarasota',
	'TPA':'Tampa',
	'PBI':'West Palm Beach',
	'PFN':'Panama City',
	'ATL':'Atlanta',
	'AGS':'Augusta',
	'SAV':'Savannah',
	'ITO':'Hilo',
	'HNL':'Honolulu',
	'OGG':'Kahului',
	'KOA':'Kailua',
	'LIH':'Lihue',
	'BOI':'Boise',
	'MDW':'Chicago',
	'ORD':'Chicago',
	'MLI':'Moline',
	'PIA':'Peoria',
	'EVV':'Evansville',
	'FWA':'Fort Wayne',
	'IND':'Indianapolis',
	'SBN':'South Bend',
	'CID':'Cedar Rapids',
	'DSM':'Des Moines',
	'ICT':'Wichita',
	'LEX':'Lexington',
	'SDF':'Louisville',
	'BTR':'Baton Rouge',
	'MSY':'New Orleans',
	'SHV':'Shreveport',
	'AUG':'Augusta',
	'BGR':'Bangor',
	'PWM':'Portland',
	'BWI':'Baltimore',
	'BOS':'Boston',
	'HYA':'Hyannis',
	'ACK':'Nantucket',
	'ORH':'Worcester',
	'BTL':'Battlecreek Michigan',
	'DTW':'Detroit',
	'DET':'Detroit',
	'FNT':'Flint',
	'GRR':'Grand Rapids',
	'AZO':'Kalamazoo',
	'LAN':'Lansing',
	'MBS':'Saginaw',
	'DLH':'Duluth',
	'MSP':'Minneapolis/St.Paul',
	'RST':'Rochester',
	'GPT':'Gulfport',
	'JAN':'Jackson',
	'MCI':'Kansas City',
	'STL':'St Louis',
	'SGF':'Springfield',
	'BIL':'Billings',
	'LNK':'Lincoln',
	'OMA':'Omaha',
	'LAS':'Las Vegas',
	'RNO':'Reno-Tahoe',
	'MHT':'Manchester New Hampshire',
	'ACY':'Atlantic City',
	'EWR':'Neward',
	'TTN':'Trenton',
	'ABQ':'Albuquerque',
	'ALM':'Alamogordo',
	'ALB':'Albany',
	'BUF':'Buffalo',
	'ISP':'Islip',
	'JFK':'New York',
	'LGA':'New York',
	'SWF':'Newburgh',
	'ROC':'Rochester',
	'SYR':'Syracuse',
	'HPN':'Westchester',
	'AVL':'Asheville',
	'CLT':'Charlotte/Douglas',
	'FAY':'Fayetteville',
	'GSO':'Greensboro',
	'RDU':'Raleigh',
	'INT':'Winston-Salem',
	'BIS':'Bismark',
	'FAR':'Fargo',
	'CAK':'Akron',
	'CVG':'Cincinnati',
	'CLE':'Cleveland',
	'CMH':'Columbus',
	'DAY':'Daytona Beach',
	'TOL':'Toledo',
	'OKC':'Oklahoma City',
	'TUL':'Tulsa',
	'EUG':'Eugene Oregon',
	'PDX':'Portland',
	'HIO':'Portland',
	'SLE':'Salem Oregon',
	'ABE':'Allentown Pennsylvania',
	'ERI':'Erie',
	'MDT':'Harrisburg',
	'PHL':'Philadelphia',
	'PIT':'Pittsburgh',
	'AVP':'Scranton',
	'PVD':'Providence',
	'CHS':'Charleston',
	'CAE':'Columbia',
	'GSP':'Greenville',
	'MYR':'Myrtle Beach',
	'PIR':'Pierre South Dakota',
	'RAP':'Rapid City South Daktoa',
	'FSD':'Sioux Falls',
	'TRI':'Bristol',
	'CHA':'Chattanooga',
	'TYS':'Knoxville',
	'MEM':'Memphis',
	'BNA':'Nashville',
	'AMA':'Amarillo',
	'AUS':'Austin',
	'CRP':'Corpus Christi',
	'DAL':'Dallas',
	'DFW':'Dallas',
	'ELP':'El Paso',
	'HOU':'Houston',
	'IAH':'Houston',
	'LBB':'Luboock',
	'MAF':'Midland',
	'SAT':'San Antonio',
	'SLC':'Salt Lake City',
	'BTV':'Burlington',
	'MPV':'Montpelier',
	'RUT':'Rutland',
	'IAD':'Dulles',
	'PHF':'Newport',
	'ORF':'Norfolk Virginia',
	'RIC':'Richmond',
	'ROA':'Roanoke',
	'PSC':'Pasco Washington',
	'SEA':'Seattle Washington',
	'GEG':'Spokane',
	'CRW':'Charleston West Virginia',
	'CKB':'Clarksburg West Virginia',
	'GRB':'Green Bay Wisconsin',
	'MSN':'Madison Wisconsin',
	'MKE':'Milwaukee',
	'CPR':'Casper Wyoming',
	'CYS':'Cheyenne Wyoming',
	'JAC':'Jackson Hole Wyoming',
	'RKS':'Rock Springs Wyoming',
	'SJU':'Puerto Rico',
	'BGI':'Barbados',
	'SDQ':'Dominican Republic',
	'CUN':'Cancun',
	'SXM':'Saint Maarten',
	'AUA':'Aruba',
	'UVF':'Saint Lucia',
	'NAS':'Bahamas',
	'CUR':'Curacao',
	'PLS':'Providenciales',
	'MBJ':'Jamaica',
	'LIR':'Costa Rica',
	'BDA':'Bermuda',
	'GCM':'Cayman Islands',
	'GND':'Grenada',
	'POP':'Dominican Republic',
	'PUJ':'Dominican Republic',
	'AZS':'Dominican Republic',
	'LRM':'Dominican Republic'
	}

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def query(request, airports=None, option=0):
	airport_list = airports.split('&')
	if airports != None:
		gl = Getaway.objects.filter(flight_origin__in=airport_list)
	else:
		gl = Getaway.objects.all()
	flights = []
	getaways = []

	# random
	num = min(gl.count(), 3)
	if int(option) == 0:
		rand = random.sample(range(0, gl.count()), num)
		for r in rand:
			getaways.append(gl[r])
	# cheap
	elif int(option) == 1:
		getaways = list(gl.order_by('jetblue_price')[:num])
	# discounted
	else:
		getaways = list(gl.order_by('-savings')[:num])

	for g in getaways:
		city = airport_dict.get(g.flight_dest)
		# service = build("customsearch", "v1",
  #              developerKey="AIzaSyAwHjNitnvZDlGjz66mXJsD4GUEd4BUgEs")

		service = build("customsearch", "v1",
               developerKey="AIzaSyAwHjNitnvZDlGjz66mXJsD4GUEd4BUgEs")
		
		res = service.cse().list(
		    q=city,
		    cx='016020790551409342918:ga4yedydubk',
		    searchType='image',
		    num=5,
		    imgType='photo',
		    fileType='jpg',
		    imgSize="large"
		).execute()

		url = res['items'][random.randint(0,4)]['link']

		flight_dict = {'g_id':g.id, 'img_url':url, 'city':city, 'price':g.jetblue_price, 'date': g.check_in.strftime('%m/%d'), 'savings':g.savings}
		flights.append(flight_dict)
	response = HttpResponse(json.dumps(flights, cls=DecimalEncoder), content_type="application/json")
	return response

def details(request, id=None):
	g = Getaway.objects.get(id=id)
	expedia_price = str(g.expedia_price)
	if expedia_price.rfind('.') != -1:
		expedia_price = expedia_price[:expedia_price.rfind('.')]
	jetblue_price = str(g.jetblue_price)
	if jetblue_price.rfind('.') != -1:
		jetblue_price = jetblue_price[:jetblue_price.rfind('.')]
	return render(request, 'flight.html', {"flight_origin": g.flight_origin, "flight_dest": g.flight_dest, "hotel": g.hotel, "nights": g.nights, "check_in": g.check_in, "check_out": g.check_out, 'expedia_price': expedia_price, 'jetblue_price': jetblue_price, 'savings': g.savings, 'advance_weeks': g.advance_weeks})

