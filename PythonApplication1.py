#Imports
import requests
import re
from robobrowser import RoboBrowser
import urllib.request
import urllib.parse
#Getting the HTML
s = requests.Session()
s.headers['User-Agent'] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36" 
br = RoboBrowser(session = s, history =True)
br.open("http://rdominguez.pythonanywhere.com/")

print(br.parsed)


#Suppose to give me the average
"""start = '>'
end = "<"
result = re.search('%s(.*)%s' % (start,end), src).group(1) 
print(result)"""

