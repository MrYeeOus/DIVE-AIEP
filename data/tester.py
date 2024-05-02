import xmltodict
import os
import json
import re

directory = "export_data"

for root, dirs, files in os.walk(directory):
    # print(root, dirs, files)
    for filename in files:
        if filename == "0.dae":
            print("Processing: " + filename)
            fn = os.path.splitext(os.path.basename(filename))[0]
# Concat the json data
            with open("export_data/data" + fn + ".json") as fs:
                dt = json.load(fs)
                descript = {"GENERATED_DESCRIPTION" : dt}
                descript = str(descript).replace("'", "\"")
                descript = descript[1:len(descript) - 1]

            with open("export_data/" + filename) as fs:
# Convert the .dae data
                doc = xmltodict.parse(fs.read())
                data = {"GENERATED_DATA" : doc}
                data = str(data).replace("'", "\"")
                data.replace("None", "\"None\"")
            with open("tester.json", "w") as outfile:
                combinedData = [descript, data]
                combinedData = {"\"objectData\"" : combinedData}

                towrite = str(combinedData).replace("'", "")
                outfile.write(towrite)

"""
For exporting back as .dae file, for checking's sake
with open('0_a.dae', "w") as outfile:
    outfile.write(xmltodict.unparse(doc, pretty=True))
"""
