#!/usr/bin/python
# (c) Copyright 2016 Talent, Inc
#
# Parse the access log file to generate the following analysis
# number of requests per day
# Most used user agents on a given day
# GET/POST ratio by OS per day
#
# Requirements:
#   python 2.7
#   pandas
#   user_agents
# To satisfy on RH6, do: 
#   yum install -y python-virtualenv
#   virtualenv env
#   env/bin/easy_install pandas user_agents;

# TODO : 
#     Better Error Handling and test cases to to check fields like status,date etc.
#     Enable more usecases by providing pandas grammer as commandline arguments e.g.#     groupby ip etc.


import logging
import pandas as pd
from ParseApache import *
from optparse import OptionParser

def get_day_requests(dataframe):
    return len(dataframe.index)

def get_top_user_agent(dataframe):
    return dataframe.groupby('user_agent_name').size(
        ).sort_values(ascending=False).head(3)

def get_hit_ratio(dataframe):
    os = dataframe.groupby('os').size()
    #logging.info("%s  Logger by a day information %s", key, os)
    request = dataframe.groupby(['request_name', 'os']).size()
    ratio = request.div(os, level='os') * 100
    return ratio

if __name__ == "__main__":
    # Using optionParser to parse arguments we can also use argparse for python >2.7

    parser = OptionParser()
    #parser.set_defaults(verbose=True)
    parser.add_option("-l", "--logfile", action="store", dest="logfile", default='sample.log',
                      help="absolute path of the log file to parse default it ./sample.log")
    parser.add_option("-d", "--date", action="store", dest = "ddate", default="*",
                      help="date for which we want to parse logs. should be like %d/%b/%Y e.g. 03/Dec/2015")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose",
                       help="enable verbose")
    (options, args) = parser.parse_args()
    logfile = options.logfile
    ddate = options.ddate
    verbose = options.verbose
    print "verbose is " , verbose
    if ddate != '*':
       try:
          ddate = str(datetime.strptime(ddate, "%d/%b/%Y").date())
       except:
          raise ("Date is not in correct format should be like 04/Jul/2015")
    
    LOG_FORMAT = '[%(asctime)s] %(message)s'
    DATE_FORMAT = '%d/%b/%Y %H:%M:%S %z'
    if verbose: 
       logging.basicConfig(level=logging.DEBUG,
                        format=LOG_FORMAT, datefmt=DATE_FORMAT)
    else:
       logging.basicConfig(level=logging.INFO,
                        format=LOG_FORMAT, datefmt=DATE_FORMAT)

    dict = {}
    # Read log file to parse
    fh = open(logfile, 'r')
    apachelog = ParseApache()
    # Read log file line by line and match for pattern
    for line in fh:
        dline = apachelog.match_regex(line)
        logging.debug( "dictionary created is %s", dline)
        # Create a formatted and parsed dictionary after parsing the log file
        data = apachelog.parse_data(dline)
        # Check if date specified in logfile is correct
        if data['time'] != 'NULL':
            date = str(data['time'].date())
            # Pick the user specified date (if specified)
            if ddate != '*':
               if ddate == date:
                  if not dict.has_key(date):
                     dict[date] = []
                  dict[date].append(data)
            else:
               if not dict.has_key(date):
                     dict[date] = []
               dict[date].append(data)

    for key, value in dict.iteritems():
        # Use pandas to create a Dataframe from the dictionary created above
        df = pd.DataFrame.from_records(value)
        # Get total number of requests in a given day
        totalrequest = get_day_requests(df)
        # Get top3 user agent by day 
        topuseragent = get_top_user_agent(df)
        # Get GET/POST ratio by OS on a given day
        requestratio = get_hit_ratio(df)
        logging.info( "Number of requests on day %s is \n %s", key, totalrequest)
        logging.info( "Top 3 user agents  on day %s is \n %s", key, topuseragent)
        logging.info( "Requests on a day is %s is \n %s", key, requestratio)
