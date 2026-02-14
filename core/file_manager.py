import json
import os

def append_json(file_path, new_data):
    if os.path.exists(file_path):
        with open(file_path,"r") as f:
            data=json.load(f)
    else:
        data=[]

    data.extend(new_data)

    with open(file_path,"w") as f:
        json.dump(data,f,indent=2)
