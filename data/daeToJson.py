import xmltodict
import os
import json
import re

directory = "export_data"

for root, dirs, files in os.walk(directory):
    # print(root, dirs, files)
    for filename in files:
        if filename.lower().endswith(".dae"):
            print("Processing: " + filename)
            fn = os.path.splitext(os.path.basename(filename))[0]
# Concat the json data
            with open("export_data/data" + fn + ".json") as fs:
                dt = fs.read()
                dt = re.sub(r"[\n\s]+", "", dt)
                descript = {"GENERATED_DESCRIPTION" : dt}
                descript = str(descript).replace("'", "\"")
                descript = descript.replace("{", "[")
                descript = descript.replace("}", "]")

            with open("export_data/" + filename) as fs:
# Convert the .dae data
                doc = xmltodict.parse(fs.read())
                data = {"GENERATED_DATA" : doc}
                data = str(data).replace("'", "\"")
                data = data.replace("{", "[")
                data = data.replace("}", "]")
            with open("./export_data2/" + fn + ".json", "w") as outfile:
                towrite = str([descript, data])
                towrite = "{" + towrite[1:len(towrite)-1] + "}"
                outfile.write(towrite.replace("'", ''))

"""
For exporting back as .dae file, for checking's sake
with open('0_a.dae', "w") as outfile:
    outfile.write(xmltodict.unparse(doc, pretty=True))
"""
