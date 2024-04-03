import xmltodict
import os
import json
import re
import glob

directory = "export_data"

for root, dirs, files in os.walk(directory):
    # print(root, dirs, files)
    for filename in files:
        if filename.lower().endswith(".dae"):
            print("Processing: " + filename)
            fn = os.path.splitext(os.path.basename(filename))[0]
# Concat the json data
            with open("export_data/data" + fn + ".json") as fs:
                dt = json.load(fs)
                #descript = {"GENERATED_DESCRIPTION" : dt}
                descript = dt;
                descript = str(descript).replace("'", "\"")
                #descript = descript.replace("{", "[")
                #descript = descript.replace("}", "]")

            with open("export_data/" + filename) as fs:
# Convert the .dae data
                doc = xmltodict.parse(fs.read())
                #data = {"GENERATED_DATA" : doc}
                data = doc
                data = str(data).replace("'", "\"")
                data = data.replace("None", "\"None\"")
                #data = data.replace("{", "[")
                #data = data.replace("}", "]")
            with open("./export_data2/" + fn + ".json", "w") as outfile:
                combinedData = [descript, data]
                #combinedData = {"\"objectData\"" : combinedData}

                towrite = str(combinedData).replace("'", "")
                outfile.write(towrite)


result = []
for f in glob.glob("export_data2/*.json"):
    print("Processing: " + str(f))
    with open(f) as infile:
        result.append(str(infile.readline()))

with open("mergedJson.jsonl", "w") as outfile:
    for item in result:
        outfile.write(item + "\n")

"""
For exporting back as .dae file, for checking's sake
with open('0_a.dae', "w") as outfile:
    outfile.write(xmltodict.unparse(doc, pretty=True))
"""
