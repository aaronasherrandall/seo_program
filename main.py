#urllip.req module defines functions and classes which help in opening URLs (mostly HTTP)
from urllib.request import urlopen
from bs4 import BeautifulSoup

url = input("Which page would you like to check? Enter Full URL: ")
keyword = input("What is your SEO keyword? ")

#urlopen(url); Open a network object denoted by a URL for reading.
#use url as an argument
try:
	html = urlopen(url)
except HTTPError as e:
	print(e)

data = BeautifulSoup(html, "html.parser")

#method?
#casefold removes any case designation in string
def seo_title(keyword, data):
	if keyword.casefold() in data.title.text.casefold():
		status = "Found"
	else:
		status = "Not Found"
	return status

print(seo_title(keyword, data))

