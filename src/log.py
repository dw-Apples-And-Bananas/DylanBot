# this only logs messages that start with "dylan, "

import json
from datetime import datetime



def message(msg):
    file = "log.json"
    now = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
    with open(file) as f:
        data = json.load(f)
    data[now] = {"user": str(msg.author), "message": str(msg.content)}
    with open(file, "w") as f:
        json.dump(data, f, indent=1)