# JSON Relationship Mapper
# Written by Brent Scarafone
# Sep, 7 2015
#
# The MIT License

# Goal is to take in a json file, a key and then create a 
# relationship between them. 

import sys
import json
import os
from pprint import pprint


def main():

	# Greet
	print "Hello I'm JRM (JSON Relationship Mapper)"

	# Check for file
	try:
		inputFile = sys.argv[1]
	except IndexError, e:
		print 'No file path included'
		return;

	except Exception, e:
		print 'Gotta Catch em All!'
		raise e
		return;

	# Check for key
	try:
		masterKey = sys.argv[2]
	except Exception, e:
		masterKey = None
		print 'No Master Key'


	# Check valid inputFile
	if not os.path.exists(inputFile):
		print 'File not found'
		return

	data_list = readFile(inputFile)
	print("%d objects in file" % len(data_list))

	

	if masterKey:
		print 'Using masterKey',masterKey 
		sorted_list = sortByKey(data_list,masterKey)

		writeJSONFile(sorted_list, inputFile)
	else:	
		printKeys(data_list)



def sortByKey(data,key):
	print 'Sorting by key %s ...' % key
	# Takes in a json object and master key
	# Then sorts each object with same value for key

	returnJsonList = []
	returnJsonObject = {}

	valueHold = None
	for obj in data:

		if not valueHold:
			valueHold = obj[key]

		if valueHold != obj[key]:
			returnJsonList = []
			valueHold = obj[key]

		returnJsonList.append(obj)
		returnJsonObject[valueHold] = returnJsonList

	print 'Sort complete.'
	return returnJsonObject


def writeJSONFile(data, fileName):
	outputName = fileName.split('/')[1].split('.')[0]
	print "Writing file... %s_sorted.json" % outputName
	with open("%s_sorted.json" % outputName, "w") as text_file:
		text_file.write(json.dumps(data, sort_keys = True,
                        indent=4, separators=(',', ': ')))
		print 'Write complete'


def readFile(file):
	print "Reading file...", file
	with open(file) as data_file:
		data = json.load(data_file)
	return data;

def printKeys(data):
	print "\nAvailable Keys:"
	for key in data[0]:
		print key

if __name__ == "__main__":
	main()