

import json
import pandas as pd
# the data.json is the schema file 
data = json.loads(open("data.json").read())

buildSchemaList = []

def addToMap(prefix,definitions,buildSchemaMap:list) -> None:
    for definition in definitions:
        map_name = definition["name"]
        if prefix != "":
            map_name = f"{prefix}.{definition['name']}"
        
        buildSchemaMap.append({
            "name": map_name,
            "description" : definition["description"],
            "type" : definition["type"],
            "mode" : definition["mode"]
        })
        if definition["type"] == "RECORD":
            addToMap(map_name, definition["fields"],buildSchemaMap)


addToMap("", data, buildSchemaList)

df = pd.DataFrame(buildSchemaList)
df.to_csv("test.csv")
