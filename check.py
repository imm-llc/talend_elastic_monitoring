#!/usr/bin/env python3
import json
import sys
import requests
from os import environ

elastic_json = ""

ignored_loggers = ["org.talend.administrator.remoterepositorymgt.business.LoginHandler"]

for line in sys.stdin:
    elastic_json += line

j = json.loads(elastic_json)

if len(j['hits']['hits']) < 1:
    print("No results retrieved")
    sys.exit(0)
else:
    print(f"Analyzing {len(j['hits']['hits'])} events")

for i in j['hits']['hits']:

    stamp = i['_source']['@timestamp']
    level = i['_source']['priority']
    message = i['_source']['message']
    logger_name = i['_source']['logger_name']
    if level == "TEST":
        print(f"Event from {logger_name} is level {level}")
        print(f"Event message: {message}")
        pass
    else:
        
        if logger_name in ignored_loggers:
            pass
        else:
            slack_alert(logger_name, level, message)
            """

            print(
                    f"Timestamp: {stamp}\
                    Level: {level}\
                    Message: {message}\
                    Logger: {logger_name}"
                
            )
            """

def slack_alert(logger_name, level, message):

    m = f"""
    Level: {level}
    Error Message: {message}
    Check out the error here: http://talend.imm.com:5601
    """
    t = f"Talend Error: {logger_name}"

    icon = environ.get("slack_icon") if environ.get("slack_icon") is not None else ":fred_zoom:"
    channel = environ.get("slack_channel") if environ.get("slack_channel") is not None else "#alerts"
    j = {
        "title": t,
        "color": "danger",
        "channel": channel,
        "username": "TalendElasticBot",
        "icon": icon,
        "message": m
    }
    
    requests.post(environ.get('slack_url'), json=j)
