import json

log_dict = {}
def log(**kwargs):
    for key,val in kwargs.items():        
        log_dict.update({key:val})

def commit_log():
    with open("log.json", "w",  encoding="utf-8") as f:
        print(json.dumps(log_dict, indent=4), file=f)