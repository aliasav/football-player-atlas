from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import csv

_URL = "http://www.futhead.com/16/players/?page=?&bin_platform=ps"

N = list(range(1,200))

players_list = []
players_dict = {}

for n in N:
	# fetch url
	url = "http://www.futhead.com/16/players/?page=" + str(n) +"&bin_platform=ps"		
	req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
	
	# parse page
	page = urlopen(req).read()	
	soup = BeautifulSoup(page, "lxml")
	players_html_elements = soup.find_all('div', class_='name')	
	players_dict_t = {}; names = [];
	
	# generate players from page
	if (len(players_html_elements)>0):
		for p in players_html_elements:
			try:
				
				html_value = p.text
				clean_str = html_value.strip().splitlines()[0]
				player_name = clean_str.splitlines()[0]
				
				if (player_name not in players_dict_t):
					players_dict_t[player_name] = 1

			except Exception as e:
				print(e)
	
	for key in players_dict_t:
		names.append(key)

	players_list = players_list + names
	print("Pages scrapped: %s\t\tTotal elements: %s" %(str(n), len(players_list)))

file_path = file_path = "/Users/saurabh/Projects/scripts/players_db.csv"

with open(file_path, 'w') as csvfile:
	
	writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

	for p in players_list:
		words = p.split(' ')
		#print(words)
		writer.writerow(words)










