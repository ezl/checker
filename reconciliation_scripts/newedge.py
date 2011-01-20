import urllib
import urllib2
from lxml import etree
from newedgeutils import *


class NewEdgeWebsite(object):
    def __init__(self, userid="ERICLIU", password="Ctc12345"):
        self.userid = userid
        self.password = password

        # build opener with HTTPCookieProcessor
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())
        urllib2.install_opener(self.opener)

        self.credentials = urllib.urlencode(dict(userid=self.userid, password=self.password))

    def _curl(self, url, referer=None):
        if referer is None:
            referer = "http://python.org"
        user_agent = "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7"
        self.request_headers = {"User-Agent": user_agent, "Referer": referer}
        request = urllib2.Request(url, headers=self.request_headers)
        f = self.opener.open(request, self.credentials)
        page = f.read()
        f.close()
        return page

    def connect(self):
        """Not sure why, but newedge seems to complain if I don't hit the main page and the report landing page"""

        print "Logging in to DataPort..."
        url = "https://pulse.newedgegroup.com/wps/myportal"
        self._curl(url)

        #WTF? I have no idea why i need to hit this page
        print "Accessing report landing page..."
        url = "https://pulsedataport.newedgegroup.com/wps/myportal/reports"
        self._curl(url)

    def retrieve_trades(self):
        print "Retrieving real time trades..."
        url = "https://pulsedataport.newedgegroup.com/wps/PA_dataport-report-na/crystalExport.jsp?exportFormat=CSV&repid=31934186&archid=31934561"
        page = self._curl(url)
        return page

    def retrieve_positions(self):
        print "Retrieving open position..."
        url = "https://pulsedataport.newedgegroup.com/wps/PA_dataport-report-na/crystalExport.jsp?exportFormat=CSV&repid=31934370&archid=33260099"
        page =self._curl(url)
        return page

userid = "ERICLIU"
password = "Ctc12345"

ne = NewEdgeWebsite(userid=userid, password=password)
ne.connect()
p = ne.retrieve_positions()
t = ne.retrieve_trades()

positions = parse_positions(p)
trades = parse_trades(t)

