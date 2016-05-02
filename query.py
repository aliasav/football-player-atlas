import csv
import sys

c = None

def main(c):
	if not c:
		c = str(input("Enter character:"))
	file_path = "/Users/saurabh/Projects/scripts/players_db.csv"
	players = {}
	with open(file_path, 'rt') as csvfile:
		rows = csv.reader(csvfile)
		for r in rows:
			flag = False
			full_name = ""
			for name in r:			
				full_name = full_name + " " + name
				if(len(name)>0 and name[0].lower()==c):
					flag = True
			if flag:
				if (full_name not in players):
					players[full_name] = True

	for p in players:
		print(p)

if __name__== "__main__":
	
	args = sys.argv	
	
	if(len(args)>0):
		c = str(args[1])
	else:
		c = None
	
	main(c)