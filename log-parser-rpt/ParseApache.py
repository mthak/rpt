
import re
import json
import pandas as pd
from collections import defaultdict, Counter, namedtuple
from datetime import datetime
from itertools import chain
import user_agents

format_pat = re.compile(
    r"(?P<host>[\d\.]+)\s"
    r"(?P<identity>\S*)\s"
    r"(?P<user>\S*)\s"
    r"\[(?P<time>.*?)\]\s"
    r'"(?P<request>.*?)"\s'
    r"(?P<status>\d+)\s"
    r"(?P<size>\S*)\s"
    r'"(?P<referer>.*?)"\s'
    r'"(?P<user_agent>.*)"'
)

class ParseApache():

    def __init__(self):
        self.pattern = format_pat
    
    def match_regex(self,line):
        self.line = line
        match = self.pattern.match(self.line)
        if match:
           return match.groupdict()


    def parse_data(self,data):
        # Get User agent details and parse it
        ua = user_agents.parse(data['user_agent'])
        data['browser'] = ua.browser.family + ua.browser.version_string
        data['os'] = ua.os.family
        data['user_agent_name'] = data['user_agent'].split()[0]
        # Get Request name separately from the request
        data['request_name'] = data['request'].split()[0]
        # Convert time in to datettime
        time = data['time'].split()[0]
        try:
            date = datetime.strptime(time, "%d/%b/%Y:%H:%M:%S")
        except ValueError:
            date = "NULL"
        data['time'] = date
        if data["user"] == "-":
            data["user"] = None
        data["status"] = int(data["status"])
        if data["size"] == "-":
            data["size"] = 0
        else:
            data["size"] = int(data["size"])
        if data["referer"] == "-":
            data["referer"] = None
        return data

