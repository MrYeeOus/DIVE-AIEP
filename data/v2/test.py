import xml.etree.ElementTree as ET
import io

def remove_namespace(tree):
    for elem in tree.iter():
        # Remove namespace prefix from COLLADA dae elements
        if '}' in elem.tag:
            elem.tag = elem.tag.split('}', 1)[1]
tmpio = io.BytesIO()
with open("0_0.dae", "rb") as f:
    dt = ET.parse(f)
    remove_namespace(dt)
    # output = str(ET.tostring(dt, method='xml'))
    # output = output.replace("\\n", "")
    # output = output.replace("b'", "")
    # with open("out.dae", "w") as n:
    #     n.write(output)

    dt.write(tmpio)

with open("output.dae", "wb") as f:
    f.write(tmpio.getvalue())
