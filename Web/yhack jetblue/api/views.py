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
	'RKS':'Rock Springs Wyoming'
	}

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def query(request, airports=None):
	airport_list = airports.split('&')
	gl = Getaway.objects.filter(flight_origin__in=airport_list)
	flights = []

	# api_key = 'd9c544f1c97ae823440f871289adbfe1'
	# api_secret = '5172eba0b3d63d4f'
	# flickr = flickrapi.FlickrAPI(api_key, api_secret)

	nrand = min(gl.count(), 3)
	rand = random.sample(range(0, gl.count()), nrand)

	# service = build("customsearch", "v1",
 #               developerKey="AIzaSyB6d0vUqwi5_geOPwcaY_FTfFkhLM97UmA")

	# service = build("customsearch", "v1",
 #               developerKey="AIzaSyAkrWrt0p8wWqil7lue7oVrzI-r8XDXW60")


	for r in rand:
		g = gl[r]
		city = airport_dict.get(g.flight_origin)
		# photo = flickr.walk(tag_mode='all', tags=city).next()
		service = build("customsearch", "v1",
               developerKey="AIzaSyAwHjNitnvZDlGjz66mXJsD4GUEd4BUgEs")
		
		res = service.cse().list(
		    q=city,
		    cx='016020790551409342918:ga4yedydubk',
		    searchType='image',
		    num=1,
		    imgType='photo',
		    fileType='jpg',
		    imgSize="large"
		).execute()

		url = res['items'][0]['link']

		flight_dict = {'img_url':url, 'city':city, 'price':g.jetblue_price, 'date': g.check_in.strftime('%m/%d/%Y'), 'savings':g.savings}
		flights.append(flight_dict)
	response = HttpResponse(json.dumps(flights, cls=DecimalEncoder), content_type="application/json")
	return response
