import re
import xmltodict
import json

with open("export_data/0.dae") as fn, open("export_data/data0.json") as fm, open("tester.json", "w") as outfile:
    doc =  xmltodict.parse(fn.read())
    jt = fm.read()
    jt = re.sub("\n", "", jt)
    jt = re.sub(r"\s+", "", jt)
    jt = {'sdfsdf': jt}
    # ot = json.dumps([doc, jt], separators=(",",":"))
    print(jt)
    ot = json.dumps(doc, separators=(",", ":"))
    outfile.write(str([jt, ot]))
    # for line in fn.readlines():
        # cl = line.replace("\\n", "")
        # cl = cl.replace("\\", "")
        # outfile.write(cl)
