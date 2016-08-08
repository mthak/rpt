Parses log lines from an apache log file in  format possible


Installation
============

    pip install log-parser-rpt

Requirements
===========
    This module uses pandas and user_agent  to format access logs


Usage
======
     python parse.py -l <logfile> -d <date_to_search> -v <verbose on>
     logfile name is optional by default the logfile is sample.log
     date to search is optional by default it will search and groupby on all dates individually
     -v will turn the logging to debug
      pyhton parse.py -h will show the help message

Example
======
        python parse.py -l data.log -d 03-Dec-2011
        python parse.py
        python parse.py -v 
        python parse.py -d 02-Dec-2011
        output from <python parse.py>
        [07/Aug/2016 22:51:18 +0000] Number of requests on day 2011-12-03 is 
 604
[07/Aug/2016 22:51:18 +0000] Top 3 user agents  on day 2011-12-03 is 
 user_agent_name
Mozilla/5.0         390
Mozilla/4.0         101
WordPress/3.2.1;     23
dtype: int64
[07/Aug/2016 22:51:18 +0000] Requests on a day is 2011-12-03 is 
 request_name  os           
GET           Android          100.000000
              Linux            100.000000
              Mac OS X         100.000000
              Other             93.112245
              Ubuntu            66.666667
              Windows           70.000000
              Windows 2000      71.428571
              Windows 3.1       75.000000
              Windows 7         83.333333
              Windows 95        66.666667
              Windows 98        66.666667
              Windows CE        66.666667
              Windows Vista     75.000000
              Windows XP        75.555556
              iOS              100.000000
HEAD          Other              0.510204
POST          Other              6.377551
              Ubuntu            33.333333
              Windows           30.000000
              Windows 2000      28.571429
              Windows 3.1       25.000000
              Windows 7         16.666667
              Windows 95        33.333333
              Windows 98        33.333333
              Windows CE        33.333333
              Windows Vista     25.000000
              Windows XP        24.444444
dtype: float64
[07/Aug/2016 22:51:18 +0000] Number of requests on day 2011-12-02 is 
 2572
[07/Aug/2016 22:51:18 +0000] Top 3 user agents  on day 2011-12-02 is 
 user_agent_name
Mozilla/5.0         1409
Mozilla/4.0          541
WordPress/3.2.1;     102
dtype: int64
[07/Aug/2016 22:51:18 +0000] Requests on a day is 2011-12-02 is 
 request_name  os            
GET           Android           100.000000
              FreeBSD           100.000000
              Linux              99.137931
              Mac OS X          100.000000
              Other              92.875481
              Symbian OS        100.000000
              Ubuntu             50.000000
              Windows            69.047619
              Windows 2000       75.268817
              Windows 7          75.000000
              Windows 95         72.727273
              Windows 98         70.000000
              Windows CE         71.428571
              Windows ME         75.757576
              Windows NT 4.0     68.421053
              Windows Vista      75.000000
              Windows XP         78.406709
              iOS               100.000000
HEAD          Linux               0.862069
              Other               0.449294
POST          Other               6.675225
              Ubuntu             50.000000
              Windows            30.952381
              Windows 2000       24.731183
              Windows 7          25.000000
              Windows 95         27.272727
              Windows 98         30.000000
              Windows CE         28.571429
              Windows ME         24.242424
              Windows NT 4.0     31.578947
              Windows Vista      25.000000
              Windows XP         21.593291
dtype: float64
[07/Aug/2016 22:51:18 +0000] Number of requests on day 2011-12-01 is 
 2822
[07/Aug/2016 22:51:18 +0000] Top 3 user agents  on day 2011-12-01 is 
 user_agent_name
Mozilla/5.0         1604
Mozilla/4.0          569
WordPress/3.2.1;     106
dtype: int64
[07/Aug/2016 22:51:18 +0000] Requests on a day is 2011-12-01 is 
 request_name  os            
GET           Fedora            100.000000
              FreeBSD           100.000000
              Linux             100.000000
              Mac OS X          100.000000
              Other              93.929174
              Symbian OS        100.000000
              Ubuntu             66.666667
              Windows            91.304348
              Windows 2000       73.493976
              Windows 3.1        85.714286
              Windows 7          96.721311
              Windows 95         72.727273
              Windows 98         77.777778
              Windows CE         75.000000
              Windows ME         82.352941
              Windows NT 4.0     75.000000
              Windows Phone     100.000000
              Windows Vista      91.304348
              Windows XP         76.651982
              iOS               100.000000
HEAD          Windows XP          0.220264
POST          Other               6.070826
              Ubuntu             33.333333
              Windows             8.695652
              Windows 2000       26.506024
              Windows 3.1        14.285714
              Windows 7           3.278689
              Windows 95         27.272727
              Windows 98         22.222222
              Windows CE         25.000000
              Windows ME         17.647059
              Windows NT 4.0     25.000000
              Windows Vista       8.695652
              Windows XP         23.127753

