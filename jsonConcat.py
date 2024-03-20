import json
import glob

result = []
for f in glob.glob("export_data2/*.json"):
    with open(f) as infile:
        result.append(json.load(infile))

with open("mergedJson.jsonl", "w") as outfile:
    for item in result:
        json.dump(item, outfile)
        outfile.write("\n")
