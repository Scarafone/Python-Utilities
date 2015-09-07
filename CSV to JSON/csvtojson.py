# CSV To Json Converter
# Written by Brent Scarafone
# Sep, 7 2015
# 
# The MIT License

import sys
import csv
import json

# 
# Arguments expected are:
# First:
#   CSV File To Convert
#   Currently I am only supporting a basic CSV with data organized
#   horizontally along the top
# 
# Second:
#   Max number of coloumns
# 
# Third:
#   Name of file to output.
#   Format will be JSON
# 

def main():
    # My Code

    if len(sys.argv) <= 1:
        print 'Missing file to read. Please provide the file to be reads location as the first argument.'
        return
    
    fileName = sys.argv[1]

    if len(sys.argv) > 2:
        outputName = sys.argv[2];
    else:
        outputName = fileName.split('.')[0]

    
    masterList = convertCSVToJson(fileName)
    writeJSONFile(masterList, outputName)


def convertCSVToJson(filePath):
    keyList = []
    masterList = []
    index = 0

    with open(filePath, 'rb') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:

            rowJson = {}
            jindex = 0
            for col in row:
                # Collect Key information
                if index == 0:
                    keyList.append(col)
                else: 
                    rowJson[keyList[jindex]] = col

                jindex += 1

            if rowJson:
                masterList.append(rowJson)

            # Iterate loop index last step
            index += 1

    return masterList

    

def writeJSONFile(data, fileName):
    print 'Writing output file... %s.json' % fileName
    with open("%s.json" % fileName, "w") as text_file:
        text_file.write(json.dumps(data, sort_keys = True,
                        indent=4, separators=(',', ': ')))
        print 'Write complete'


if __name__ =="__main__":
    main()