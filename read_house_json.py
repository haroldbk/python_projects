#read_house_json
import json,string
jfile="D:/PythonTestSamples/nearby.json"

with open(jfile,'r') as jsonfile:
    nearby_from_file = json.load(jsonfile)

    for k1,v1 in nearby_from_file.items():
        print(repr(k1))
        for k2, v2 in v1.items():
            print(f"{k2!r}: {v2!r}")




