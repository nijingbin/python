# -*- coding=utf-8 -*-
# https://www.yahoo.com/news/weather/china/yidu/yidu-2168403
from xml.parsers.expat import ParserCreate
from contextlib import contextmanager,closing
from urllib.request import urlopen
# '''lin21
# line2
#  line3'''用'''....'''表示多行的字符串
xmlStr = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
	<yweather:location city="Beijing" region="" country="China"/>
</ol>
'''

class WeatherSaxHandler(object):
	#固定类的变量只有这些,变量名字需要用''包裹
	__slots__ = ('city','country')
	
	#用@property和@getcity.setter表示类变量的条件赋值与输出
	#property装饰器中，函数名字不能与__slots__ 中的变量名字相同
	@property
	def getcity(self):
		return self._city
	@getcity.setter
	def getcity(self,value):
		self._city = value
		
	def start_element(self, name, attrs):
		dir(attrs)
		if name == 'yweather:location':
			print('sa:start_element:%s,attrs:%s'%(name, str(attrs)))
		elif name == 'yweather:forecast':
			pass
		else:
			pass
	def end_element(self, name):
		print('sax:end_element:%s'%name)
	def char_data(self, text):
		print('self:%s,sax:char_data:%s'%(self,text))
	
	
def writeTXT(strCity):
	with closing(urlopen('https://www.yahoo.com/news/weather/china/yidu/yidu-2168403')) as page:
		with open('httpcontext.txt','wb+') as f:
			for line in page:
				if isinstance(line,bytes):
					f.write(line)
	
def readWeather(strCity):
	handler = WeatherSaxHandler()
	parser = ParserCreate()
	parser.StartElementHandler = handler.start_element
	parser.EndElementHandler = handler.end_element
	parser.CharacterDataHandler = handler.char_data
	parser.Parse(strCity)
	return strCity
	
def parse_weather(xml):
    return {
        'city': 'Beijing',
        'country': 'China',
        'today': {
            'text': 'Partly Cloudy',
            'low': 20,
            'high': 33
        },
        'tomorrow': {
            'text': 'Sunny',
            'low': 21,
            'high': 34
        }
    }

if __name__=='__main__':
	readWeather(xmlStr)
	# 测试:
	data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
	<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
		<channel>
			<title>Yahoo! Weather - Beijing, CN</title>
			<lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
			<yweather:location city="Beijing" region="" country="China"/>
			<yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
			<yweather:wind chill="28" direction="180" speed="14.48" />
			<yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
			<yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
			<item>
				<geo:lat>39.91</geo:lat>
				<geo:long>116.39</geo:long>
				<pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
				<yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
				<yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
				<yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
				<yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
				<yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
				<yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
			</item>
		</channel>
	</rss>
	'''
	weather = parse_weather(data)
	assert weather['city'] == 'Beijing', weather['city']
	assert weather['country'] == 'China', weather['country']
	assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
	assert weather['today']['low'] == 20, weather['today']['low']
	assert weather['today']['high'] == 33, weather['today']['high']
	assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
	assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
	assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
	print('Weather:', str(weather))
