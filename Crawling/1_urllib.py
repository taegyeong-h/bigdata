#!/usr/bin/env python3
import sys
import urllib.request as res
import urllib.parse as parse

if len(sys.argv) <= 1:
    print("usege: download-forecast-argv <rigion number>")
    sys.exit()
    
regionNumber = sys.argv[1]

api_addr ="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
values = {
    'stnId' : regionNumber
}

params = parse.urlencode(values)
url = api_addr + "?" + params
print("url =", url)

data = res.urlopen(url).read()
text = data.decode("utf-8")
print(text)
