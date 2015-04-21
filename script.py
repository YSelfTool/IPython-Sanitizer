import json
from sys import argv
ffn = argv[1] if len(argv) > 1 else "*.ipynb"
fwn = argv[2] if len(argv) > 2 else "output.py"
with open(ffn, "r") as nbf, open(fwn, "w") as wrf:
    data = json.load(nbf)
    cells = data["cells"]
    for key in cells:
        if key["cell_type"] == "code":
            for line in key["source"]:
                wrf.write(line)
            wrf.write("\n")
