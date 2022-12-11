#!/usr/bin/env python

import datetime
import glob
import json
import pathlib

path = pathlib.PurePath("setlists")
files = glob.glob("**/*.json", recursive=True)

new_file = "shows.json"

data = {}

for file in files:
    with open(file, "r") as fh:
        content = json.load(fh)
        date = datetime.datetime.strptime(content["date"], "%B %d, %Y")
        key = date.strftime("%Y%m%d")
        data[key] = content

with open(new_file,"w") as fh:
    json.dump(dict(sorted(data.items())),fh,indent=4)
