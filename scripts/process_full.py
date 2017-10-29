import xmltodict
import pprint
import string
import glob
import xml.etree.ElementTree
from bs4 import BeautifulSoup
import time
import os, re
import sys
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import *


def getClaimsAndClasses(inFile):

	e = xml.etree.ElementTree.parse(inFile).getroot()

	split = inFile.split('/')
	inF = split[len(split) - 1]

	f = open(inFile, 'r')
	soup = BeautifulSoup(f, 'xml')
	if soup:
		section = soup.find('section')
		# cs = soup.find('class')
		if section:# and cs and cs is not '':
			section = section.text
			if section == 'H' or section == 'G':
				claims = soup.find_all('claim-text')
				w1 = open(sys.path[0]+'/claims-full/'+inF+'_.txt', 'w')
				# w2 = open(sys.path[0]+'/'+inF+'_.txt', 'w')

				for claim in claims:
					# text = [stem(regex.sub(' ', word)) for word in claim.text.lower().split() if word not in cached]
					# text = [stem(word) for word in text if ''.join(word.split()) not in cached]
					# text = " ".join(text)
					w1.write(claim.text)
					# w1.write(claim.text)

			# w2.write(section.text + " " + cs.text)

			# if not os.path.exists('search/'+section.text+cs.text):
			# 	os.makedirs('search/'+section.text+cs.text)
			# w3 = open(sys.path[0]+'/search/'+section.text+cs.text+'/'+inF+'.txt', 'w')
			# for claim in claims:
			# 	w3.write(claim.text)

				w1.close()
			# w2.close()
			# w3.close()


# getClaimsAndClasses('iptest.xml')

files = glob.glob(sys.path[0]+"/xml-appa/*.xml")
i = 0
for fil in files:
	split = fil.split('/')
	last = split[len(split) - 1]
	getClaimsAndClasses(fil)
	if i % 500 == 0:
		print('finished', i)
	i += 1
