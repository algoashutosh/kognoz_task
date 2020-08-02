
import csv 
import requests 
import xml.etree.ElementTree as ET 


def parseXML(xmlfile): 
	tree = ET.parse(xmlfile) 
	root = tree.getroot()
	newsitems = [] 
	
	for item in root.findall('./channel/item'):
		news = {} 
		for child in item: 
			news[child.tag] = child.text
		
		newsitems.append(news) 
	
	return newsitems 


def savetoCSV(newsitems, filename):

	fields = ['title', 'link', 'description', 'pubDate', 'articleid', 'website','issue','type','showcase'] 
 
	with open(filename, 'w') as csvfile: 
		writer = csv.DictWriter(csvfile, fieldnames = fields) 
		writer.writeheader() 
		writer.writerows(newsitems) 

	
def main(): 
	newsitems = parseXML('Sample-XML.xml') 
	savetoCSV(newsitems, 'task.csv') 
	
	
if __name__ == "__main__": 
	main() 
