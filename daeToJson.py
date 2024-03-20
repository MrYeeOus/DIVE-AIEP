import xmltodict
import os
import json

directory = "export_data"

for root, dirs, files in os.walk(directory):
    # print(root, dirs, files)
    for filename in files:
        if filename.lower().endswith(".dae"):
            fn = os.path.splitext(os.path.basename(filename))[0]
            # Concat the json data
            with open("export_data/data" + fn + ".json") as fs:
                dt = fs.read()
                descript = {'GENERATED_DESCRIPTION' : dt}

            with open("export_data/" + filename) as fs:
                doc = xmltodict.parse(fs.read())
                dta = {'GENERATED_DATA': doc}
            with open("./export_data2/" + fn + ".json", "w") as outfile:
                json.dump([descript, dta], outfile, indent=4)

"""
For exporting back as .dae file, for checking's sake
with open('0_a.dae', "w") as outfile:
    outfile.write(xmltodict.unparse(doc, pretty=True))
"""
