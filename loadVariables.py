#! python3

# loadVariables.py - this subroutine will handle the user info both saving and loading that data. 

import json

def loadJson(filename):
    f = open(filename)
    data = json.load(f)
    return data

def saveJson(filename, output):
    with open(filename, "w") as outfile:
        json.dump(output, outfile)
    return

# TODO add the load and save logic in the right place of main to maintain the latest updates made to userInfo.json
 
# output = loadJson("databases/userInfo.json")

# for i in output['maxes']:
#     print(i, output['maxes'][i])