import os
import urllib2
import simplejson


def CheckTime():
  js = "http://date.jsontest.com/"
  request = urllib2.Request(js)
  response = urllib2.urlopen(request)
  results = simplejson.load(response)
  theresponse = results['time']
  return theresponse

  
keyword = raw_input('                  Enter a keyword to get those headlines!\n')
url = ('https://ajax.googleapis.com/ajax/services/search/news?v=1.0&q='+ keyword) # Url to extract json data from
request = urllib2.Request(url)
response = urllib2.urlopen(request)
results = simplejson.load(response)

print ('\n')
print ('\n')
print ('Time is now :')
print (CheckTime())

# Crawl each object in the list then display some values in each one of them
for idx,item in enumerate(results['responseData']['results']):
	print '\n'
	print (results['responseData']['results'][idx]['titleNoFormatting'])
	print (results['responseData']['results'][idx]['publisher'] )
	print '\n'
	
raw_input()
