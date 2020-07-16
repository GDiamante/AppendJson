import json
import sys
from os import listdir
from os.path import isfile, join

#Enter directory where JSON exists
jsonFolder = ""
fileSelection = 0

#Gets list of files in directory
fileList = [f for f in listdir(jsonFolder) if isfile(join(jsonFolder, f))]

#Display files in directory
for i, file in enumerate(fileList):
    print("%d)" % (i + 1), file)

#Select a number within the limit
while (fileSelection <= 0 or fileSelection > len(fileList)):
    fileSelection = int(input("Please select the file you wish to modify: "))

fileToModify = jsonFolder + fileList[fileSelection - 1]

#If no argument passed in, prompt to enter
if len(sys.argv) <= 1:
    newString = input("Please enter the string you wish to add:\n")
else:
    newString = sys.argv[1]

#Write to file
def write_json(data, filename=fileToModify):
    with open (filename, "w") as f:
        json.dump(data, f, indent=2)

#Get existing JSON and append string
with open (fileToModify) as jsonFile:
    data = json.load(jsonFile)
    data.update({newString: newString})

write_json(data)
