import unittest
from ParseApache import *
from datetime import datetime
import doctest
import os.path

class ApacheParserTestCase(unittest.TestCase):

    def test_simple(self):
        parser = ParseApache()
        sample = '127.0.0.1 - - [03/Dec/2011:05:22:38 -0500] "GET / HTTP/1.0" 200 9826 "-" "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.19; aggregator:Spinn3r (Spinn3r 3.1); http://spinn3r.com/robot) Gecko/2010040121 Firefox/3.0.19"'
        log_parse = parser.match_regex(sample)
        log_data = parser.parse_data(log_parse)
        self.assertNotEqual(log_data, None)
        self.assertEqual(log_data['host'], '127.0.0.1')
        self.assertEqual(str(log_data['status']), '200')
        self.assertEqual(log_data['identity'], '-')
        self.assertEqual(log_data['request_name'], 'GET')
        self.assertEqual(log_data['user_agent_name'], 'Mozilla/5.0')
        self.assertTrue(datetime.strptime(str(log_data['time']), "%Y-%m-%d %H:%M:%S"))



if __name__ == "__main__":
    unittest.main()       
