rom bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import requests

url = 'https://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
queryParams = '?' + urlencode({quote_plus('serviceKey'): '서비스키'
		, quote_plus('returnType'): 'xml'
		, quote_plus('numOfRows'): '10'
		, quote_plus('pageNo'): '1'
		, quote_plus('stationName'): '서창'
		, quote_plus('ver'): '1.0'})
res = requests.get(url + queryParams)
print(res)
soup = BeautifulSoup(res.content, 'xml')
data = soup.find_all('item')
print(data)
print(res.status_code)
print(res.text)
