import json
import glob

result = []
for f in glob.glob("export_data2/*.json"):
    with open(f) as infile:
        result.append(str(infile.readline()))

with open("mergedJson.jsonl", "w") as outfile:
    for item in result:
        outfile.write(item + "\n")
