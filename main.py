import requests
from bs4 import BeautifulSoup
from googlesearch import search
import xml.etree.ElementTree as ET

file='RJS739-NW3_BlackOil.mr2'
tree=ET.parse(file)
root=tree.getroot()

