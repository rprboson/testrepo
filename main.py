import requests
from bs4 import BeautifulSoup
from googlesearch import search
import xml.etree.ElementTree as ET
"""
query="imoveis humaira"
for url in search(query, sleep_interval=5, num_results=200):
    print(url)
"""
file='RJS739-NW3_BlackOil.mr2'
tree=ET.parse(file)
root=tree.getroot()

