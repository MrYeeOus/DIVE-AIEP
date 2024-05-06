# Assuming folder structure == data/v2/[dae && json] folders
# ---
# Training dataset format:
#   GENERATED_DESCRIPTION   |   GENERATED_DATA
#   <json location/size>    |   <library_geometries>
# ---

import xml.etree.ElementTree as ET
import os, io, json, base64, re

dae_dir = "data/v2/dae"
json_dir = "data/v2/json"
training_dir = "data/v2/training"

def remove_namespace(tree):
    for elem in tree.iter():
        # Remove namespace prefix from COLLADA dae elements
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]

#getDae = ET.parse('thing.dae')
#root = getDae.getroot()

# Get library_geometries
#remove_namespace(root)
#lg = root.find("library_geometries")
#toExport = ET.ElementTree(lg)
#toExport.write("export.xml")

# Clean & combine .dae files
get_generated_data = []
for root, dirs, files in os.walk(dae_dir):
    for file in files:
        with open(os.path.join(root, file), "rb") as f:
            tmpio = io.BytesIO()
            print("Processing: " + file)
            dt = ET.parse(f).getroot()
            remove_namespace(dt)
            dtlg = dt.find("library_geometries")
            dtlg = ET.ElementTree(dtlg)
            dtlg.write(tmpio)
            get_generated_data.append(str(tmpio.getvalue()))
            

# Process json files
get_generated_desc = []
for root, dirs, files in os.walk(json_dir):
    for file in files:
        print("Processing: " + file)
        with open(os.path.join(root, file), "rb") as f:
            jsonData = f.read()
            get_generated_desc.append(str(jsonData))


generated_data = {"GENERATED_DESCRIPTION": get_generated_desc, "GENERATED_DATA": get_generated_data}
with open("data/v2/training/gen_data.txt", "w") as f:
    json.dump(generated_data, f, indent=4)
