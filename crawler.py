#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
从网站爬取房源信息
"""

import urllib
import urllib2

page = 1
url = 'http://sz.58.com/chuzu/pn' + str(page) + '/'
 
try:
	request = urllib2.Request(url)
	response = urllib2.urlopen(request)
	print response.read()
except urllib2.URLError,e:
	if hasattr(e,'code'):
		print e.code
	if hasattr(e,'reason'):
		print e.reason