from pymongo import MongoClient
import csv


client = MongoClient('localhost', 27017)
db = client['ca2sean_brennan']

csvfile = open('C:\\Users\\Sean\\Documents\\3rdYearCollege\\BigDataSystems\\Ca2_Sean_Brennan\\FinalProjectData.csv', 'r')
reader = csv.DictReader( csvfile )

reader = csv.DictReader(csvfile, delimiter=';')
for row in reader:
	db.grades.insert_one(row)
