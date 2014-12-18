#!/usr/bin/env python
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
from scapy.layers.dns import DNS, DNSQR, DNSRR
from scapy.layers.inet import IP, UDP, TCP

__author__ = 'michael salerno'
#id: 108512298

if not os.geteuid() == 0:
    sys.exit('Script must be run as root')

pkt = IP(dst="www.slashdot.org")/TCP()/"GET /index.html HTTP/1.0 \n\n"

ans, unans = sr(pkt, multi=2, timeout=1, verbose=1)