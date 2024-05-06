# Assuming folder structure == data/v2/[dae && json] folders
# ---
# Training dataset format:
#   GENERATED_DESCRIPTION   |   GENERATED_DATA
#   <json location/size>    |   <library_geometries>
#   <room><location/size>   |   <geometry>
#   <obj><location/size>    |   <geometry>
# ---

import xml.etree.ElementTree as ET
import os, io, json

dae_dir = "data/v2/dae"
json_dir = "data/v2/json"
training_dir = "data/v2/training"

def remove_namespace(tree):
    for elem in tree.iter():
        # Remove namespace prefix from COLLADA dae elements
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]


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
            jsonData = json.load(f)
            for item in jsonData:
                get_generated_desc.append(str(jsonData[item]))

generated_data = {"GENERATED_DESCRIPTION": get_generated_desc, "GENERATED_DATA": get_generated_data}
with open("data/v2/training/mergedJson.json", "w") as f:
    json.dump(generated_data, f, indent=4)
