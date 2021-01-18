#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

url = input("Enter URL to crawl here --> ")
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
dataSite = soup.find_all('a', href=True)

for data in dataSite:
	if "http" not in data['href']:
		print(">> " + url + data['href'])

	else:
		print(">> " + data['href'])
